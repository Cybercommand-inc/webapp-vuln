# 01-セッション管理の不備

## 環境構築手順

1. dockerコンテナーを起動する

```
$ cd 01
$ docker build -t webapp-vuln-01 .
$ docker run -d -p 80:80 -p 443:443 --name webapp-vuln-01 webapp-vuln-01
```

2. ブラウザからアクセスして起動していることを確認する
```
https://localhost/client.html
```
