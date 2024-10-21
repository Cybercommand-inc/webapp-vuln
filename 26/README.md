# 26-DOMベースのサービス拒否

## 環境構築手順

1. dockerコンテナーを起動する

```
$ cd 26
$ docker build -t webapp-vuln-26 .
$ docker run -d -p 8080:80 --name webapp-vuln-26 webapp-vuln-26
```

2. ブラウザからアクセスして起動していることを確認する
```
http://127.0.0.1:8080/input.html
```
