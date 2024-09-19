# OSコマンドインジェクション

### 環境構築
1. Damn Small Vulnerable Web (DSVW) (脆弱性のあるwebapp)のダウンロード
```
$ git clone [git@github.com:NeuraLegion/brokencrystals.git](https://github.com/stamparm/DSVW.git)](https://github.com/stamparm/DSVW.git)
```

2. このプログラムを実行するには、Python (3.x) が必要です。アイテム XML 外部エンティティ (ローカル)、XML 外部エンティティ (リモート)、およびブラインド XPath インジェクション (ブール) は、python-lxml のインストールが必要です (例: apt-get install python-lxml)。そうしないと、それらは無効になります。

lxml を pip でインストールするには、以下のコマンドを実行してください。
```
$ pip install -r requirements.txt
```

3. 実行
```
$ python3 dsvw.py 
```

4. ブラウザからアクセスして確認
```
http://localhost:65412
```
