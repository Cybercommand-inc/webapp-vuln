# 20-ユーザーID等の調査

### 環境構築
1. vulnerableAppディレクトリを作成

```
 $ mkdir vulnerableApp 
```

2. データ作成
```
index.html
login.php
dashboard.php
style.css
```
を作成

3. サーバ開始
```
vulnerableApp$ php -S 192.168.7.246:5000
```

4. ウェブブラウザを開き、次のURLにアクセスしてログインページを表示します:
http://192.168.7.246:5000/ へアクセス

5. ユーザー名”user”とパスワード”password”を使ってログインします。ログイン後、URL内のセッショントークン　”dashboard.php?token=...”を確認してください。
