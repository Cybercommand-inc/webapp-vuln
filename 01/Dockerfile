FROM php:8.2-apache

# ApacheとSSLツールのインストール
RUN apt-get update && \
    apt-get install -y apache2 openssl && \
    apt-get clean

# SSLモジュールとデフォルトSSLサイトの有効化
RUN a2enmod ssl && \
    a2ensite default-ssl

# SSL証明書とApache設定ファイルのコピー
COPY ./certs /etc/ssl/private
COPY ./conf/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ./conf/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
COPY ./html /var/www/html

# HTTPおよびHTTPSポートの公開
EXPOSE 80 443

# Apacheをフォアグラウンドで起動
CMD ["apachectl", "-D", "FOREGROUND"]
