# 28-メールヘッダインジェクション
### 環境構築
1. Debian系のLinuxにpostfixを入れる

```
sudo apt update
sudo apt install postfix
```

2. メールアカウント作成など
mailuser1
mailuser2 

```
sudo adduser mailuser1
sudo adduser mailuser2
sudo mkdir -p /home/mailuser1/Maildir/{cur,new,tmp}
sudo chown -R mailuser1:mailuser1 /home/mailuser1/Maildir
sudo chmod -R 700 /home/mailuser1/Maildir

sudo mkdir -p /home/mailuser2/Maildir/{cur,new,tmp}
sudo chown -R mailuser2:mailuser2 /home/mailuser2/Maildir
sudo chmod -R 700 /home/mailuser2/Maildir
```


```
sudo nano /etc/postfix/main.cf
以下の設定を追加または変更
home_mailbox = Maildir/
```

sudo systemctl restart postfix

```
# See /usr/share/postfix/main.cf.dist for a commented, more complete version


# Debian specific:  Specifying a file name will cause the first
# line of that file to be used as the name.  The Debian default
# is /etc/mailname.
#myorigin = /etc/mailname


# Relax restrictions on recipient address syntax
smtpd_recipient_restrictions =
    permit_mynetworks,
    permit_sasl_authenticated,
    reject_non_fqdn_recipient,
    reject_unknown_recipient_domain,
    permit

header_checks = regexp:/etc/postfix/header_checks



smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
biff = no

# appending .domain is the MUA's job.
append_dot_mydomain = no

# Uncomment the next line to generate "delayed mail" warnings
#delay_warning_time = 4h

readme_directory = no

# See http://www.postfix.org/COMPATIBILITY_README.html -- default to 3.6 on
# fresh installs.
compatibility_level = 3.6

# Enable authentication for port 587
smtpd_tls_security_level = encrypt
smtpd_tls_cert_file = /etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file = /etc/ssl/private/ssl-cert-snakeoil.key
smtpd_tls_loglevel = 1
smtpd_tls_mandatory_protocols = !SSLv2, !SSLv3
smtpd_tls_mandatory_ciphers = medium
smtpd_tls_security_level = may
smtpd_tls_loglevel = 1
smtpd_tls_received_header = yes

# SASL authentication settings
smtpd_sasl_auth_enable = yes
smtpd_sasl_security_options = noanonymous
smtpd_sasl_tls_security_options = noanonymous
smtpd_sasl_authenticated_header = yes


# TLS parameters
#smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
#smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
#smtpd_tls_security_level=may

#smtp_tls_CApath=/etc/ssl/certs
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache


smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination


home_mailbox = Maildir/
myhostname = srt
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
#mydestination = $myhostname, srt, localhost.localdomain, , localhost
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain



mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all
inet_protocols = all

#myhostname = mail.local
mydomain = local
myorigin = $mydomain
#inet_interfaces = all
#inet_protocols = ipv4
#strict_rfc821_envelopes = no


#smtpd_recipient_restrictions =
 #   check_recipient_access hash:/etc/postfix/recipient_checks,
  #  permit


smtpd_helo_required = no
strict_rfc821_envelopes = no


```

3. 外部へのアクセスが必要 
burpスキャナーはburpCollaboratorで検出
ロカールでも可能ですがburpスキャナーが検出しませんでした。


```
sudo apt update
sudo apt install mailutils
```

メールテスト
echo "This is a test email" | mail -s "Test Subject" mailuser2@srt



send.phpを使用しているサンプルburpリクエスト
```
POST /send.php HTTP/1.1
Host: 192.168.7.246
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 49
Origin: http://192.168.7.246
DNT: 1
Sec-GPC: 1
Connection: keep-alive
Referer: http://192.168.7.246/
Cookie: connect.sid=2pvMuu55-TqLKiFWEgwyXVwnyQqO4lZE.oGMEDzXIkKptjFypMFsCPRNLup7BbRM%2BAZGb54H6PJc
Upgrade-Insecure-Requests: 1
Priority: u=0, i

email=mailuser1%40srt%0d%0acc:mailuser2@srt&text=
```
