# 05-クリックジャッキング

### 環境構築
以下を参照してください。

https://github.com/Cybercommand-inc/webapp-vuln#user-content-broken-crystalsの環境構築

### PoC1
1. 罠サーバーを立ち上げる
```
$ cd $PROJECT_DIR/05
$ python -m http.server
```

2. Proxyの設定
Burpを立ち上げて、FireFoxのFoxyProxyで、Burpを設定します。

3. 罠ページにブラウザからアクセス
```
http://<PCのIP>:8000/clickjacking.html
```

4. `クリック`をクリックして、BurpのHTTP histroyを確認。

### PoC2
1. 罠サーバーを立ち上げる
```
$ cd $PROJECT_DIR/05/demo
$ python -m http.server
```

2. Proxyの設定
Burpを立ち上げて、FireFoxのFoxyProxyで、Burpを設定します。

3. 罠ページにブラウザからアクセス
```
http://<PCのIP>:8000/click.html
```

4. `クリック`をクリックして、BurpのHTTP historyを確認。

### PoC3
```
$ cd $PROJECT_DIR/05/PoC3

1. npm 関係コマンドを実行
$ sudo npm init -y
$ sudo npm install express

2. "node"でサーバーを立ち上げる。
$ node server.js
node server.js 
サーバーが http://localhost:3000 で実行中

3. index.htmlとattack.htmlを別のサーバにいれる。nginx,apache
/var/www/html

4. Proxyの設定
Burpを立ち上げて、FireFoxのFoxyProxyで、Burpを設定します。

5. 罠ページにブラウザからアクセス
http://<PCのIP>/attack.html

6. `ここをクリックして賞品を獲得！`をクリックして、BurpのHTTP historyを確認。
```
