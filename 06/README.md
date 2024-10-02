# 06-OSコマンドインジェクション

### 環境構築
1. プロジェクトディレクトリに移動
```
$ cd $HOME/projects/webapp-vuln
```

3. pythonとpipのバージョン確認
```
$ python --version
$ pip --version
```

5. Damn Small Vulnerable Web (DSVW) (脆弱性のあるwebapp)のダウンロード
```
$ git clone https://github.com/stamparm/DSVW.git
```

7. 必要なライブラリのインストール
```
$ pip install -r requirements.txt
```

9. サービスの起動
```
$ python3 dsvw.py
```

10. ブラウザからアクセスして確認
```
http://localhost:65412
```
