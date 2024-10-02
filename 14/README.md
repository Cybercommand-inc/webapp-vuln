# 14-HTTPヘッダインジェクション

# 06-OSコマンドインジェクション

### 環境構築
1. プロジェクトディレクトリに移動
```
$ cd $HOME/projects/webapp-vuln
```

2. pythonとpipのバージョン確認
```
$ python --version
$ pip --version
```

3. Damn Small Vulnerable Web (DSVW) (脆弱性のあるwebapp)のダウンロード
```
$ git clone https://github.com/stamparm/DSVW.git
```

4. 必要なライブラリのインストール
```
$ pip install -r requirements.txt
```

5. サービスの起動
```
$ python3 dsvw.py
```

6. ブラウザからアクセスして確認
```
http://localhost:65412
```
