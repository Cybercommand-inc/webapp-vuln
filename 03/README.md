# 03-クロスサイトリクエストフォージェリー

### 環境構築
1. webapp-vulnのフォルダに移動する
```
$ cd $PROJECT_DIR/webapp-vuln
```

2. brokencrystals(脆弱性のあるwebapp)のダウンロード
```
$ git clone git@github.com:NeuraLegion/brokencrystals.git
```

3. イメージのビルド＆実行
```
$ cd brokencrystals
$ docker compose --file=docker-compose.local.yml up -d --build
```

4. ラウザからアクセスして確認
```
http://localhost:3000
```
