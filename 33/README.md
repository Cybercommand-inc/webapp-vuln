# 33-クローラへの耐性

### 環境構築

1. アプリケーションの概要 

公開エリア：すべてのユーザーがアクセス可能です。
制限エリア：保護されることを意図していますが、robots.txt のみを使用して不適切に守られています。

プロジェクトディレクトリを作成する

新しいディレクトリをプロジェクト用に作成します。例えば、webapp という名前にします。
```
mkdir webapp
cd webapp
```

2. アプリケーションの構造を作成する

以下のファイル構造を作成します：
```
webapp/
├── public/
│   └── index.html
├── restricted/
│   └── secret.html
├── robots.txt
└── server.py


index.html を作成する
secret.htmlを作成する
robots.txtを作成する
server.pyを作成する
```

3. 必要なパッケージを入れる
```
$ pip install Flask
```

4. アプリケーションをスタート
```
$ python3 server.py
```
