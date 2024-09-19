# 05-SQLインジェクション

### 環境構築
1. brokencrystals(脆弱性のあるwebapp)のダウンロード
```
$ git clone git@github.com:NeuraLegion/brokencrystals.git
```

2. イメージのビルド＆実行
```
$ docker compose --file=docker-compose.local.yml up -d --build
```

3. ブラウザからアクセスして確認
```
http://localhost:3000
```
