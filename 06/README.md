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

5. レポジトリ内の”dsvw.py”のいれかえ
```
$cp dsvw.py dsvw1.py
``` 

6. サービスの起動。レポジトリ内の”dsvw.py”を使用
```
$ python3 dsvw.py
```

7. ブラウザからアクセスして確認
```
http://localhost:65412
```
