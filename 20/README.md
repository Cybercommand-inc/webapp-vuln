# 20-ユーザーID等の調査

### 環境構築
1. サーバーを起動
```
$ cd vulnerableApp 
$ php -S 127.0.0.1:5000
```

2. ブラウザからアクセス
```
http://127.0.0.1:5000/
```

3. ログイン
ユーザー名: `user` パスワード: `password`を使ってログインします。
ログイン後、URL内のセッショントークン `dashboard.php?token=...` を確認してください。
