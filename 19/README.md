# 19-認証

### 環境構築


1. アプリケーションのディレクトリ構造:

```
あなたのプロジェクトフォルダー/ │ 
├── app.py # Flaskサーバーサイドコード
 ├── templates/ # このフォルダーにはHTMLファイルが保存されます
 │ └── index.html # フロントエンドフォーム（HTML）
 └── static/ # 静的ファイル（例: CSS、JavaScriptなど）


主なポイント:

app.py: FlaskサーバーサイドアプリケーションがJWTの脆弱性を処理します。
templates/index.html: このHTMLファイルは、脆弱性をテストするためのフロントエンドフォームを作成するために使用されます。Flaskは自動的にtemplates/ディレクトリ内のindex.htmlファイルを検索します。
静的ファイル（任意）: CSSやJavaScriptファイルを追加する必要がある場合は、それらをstatic/フォルダーに保存できます。


```

2.アプリケーションスタート

```
$ python3 app.py
```


3. テスト用のURL

```
http://192.168.7.246:5000/no-signature-verification?token=eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.invalidsignature

http://192.168.7.246:5000/weak-hmac-secret?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o
```
