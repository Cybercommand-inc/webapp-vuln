# 11-ディレクトリリスティング
### 環境構築
1. 好みをwebサーバを構築。

2. 例　Debian系のlinuxにApacheウェブサーバーをインストールする手順
  ```
ステップ 1: システムを更新する
ターミナルを開き、次のコマンドを実行してシステムパッケージを更新します。
sudo apt update
sudo apt upgrade

ステップ 2: Apacheをインストールする
次に、Apacheをインストールします。以下のコマンドを実行してください。
sudo apt install apache2

ステップ 3: Apacheのサービスを起動する
インストールが完了したら、Apacheサービスを起動します。
sudo systemctl start apache2

ステップ 4: Apacheの自動起動を設定する
サーバーの再起動時にApacheが自動的に起動するように設定します。
sudo systemctl enable apache2

ステップ 5: ファイアウォールの設定
UFW（Uncomplicated Firewall）を使用している場合、Apacheのトラフィックを許可します。
sudo ufw allow 'Apache'

ステップ 6: Apacheが正常に動作しているか確認する
ブラウザを開き、次のURLにアクセスします。
http://localhost/
「Apache2 Debian Default Page」が表示されれば、インストールは成功しています。

ステップ 7: Apacheの設定ファイルを確認する
Apacheの設定ファイルは /etc/apache2/apache2.conf にあります。必要に応じて編集できます。
sudo nano /etc/apache2/apache2.conf

ステップ 8: Apacheの再起動
設定を変更した場合は、Apacheを再起動します。
sudo systemctl restart apache2

ステップ 9: サイトをホストする
デフォルトのウェブサイトのルートは /var/www/html です。ここにHTMLファイルを配置して、サイトをホストできます。
sudo nano /var/www/html/index.html
```

3.サーバのステータスを確認。
```
 $ sudo systemctl status apache2   
```

4. ディレクトリを作成
```
sudo mkdir listing1
sudo mkdir listing2
```

5. ディレクトリ構成を確認
```
$ pwd
/var/www/html

$ ls -aslrth lis*      
   
listing1:
合計 12K
4.0K -rw-r--r-- 1 root root    7    secret1.txt
4.0K drwxr-xr-x 2 root root 4.0K    .
4.0K drwxr-xr-x 6 root root 4.0K   ..

listing2:
合計 12K
4.0K -rw-r--r-- 1 root root    7    secret2.txt
4.0K drwxr-xr-x 2 root root 4.0K    .
4.0K drwxr-xr-x 6 root root 4.0K    ..
```  
