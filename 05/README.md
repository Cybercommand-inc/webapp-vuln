# 05-クリックジャッキング

### 環境構築
こちらのREADMEを参照

https://github.com/Cybercommand-inc/webapp-vuln/tree/main/02

### PoC
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
