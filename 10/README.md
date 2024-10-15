# 10-XMLインジェクション

### 環境構築
1. コマンドでwebサーバ開始
```
 $ php -S 127.0.0.1:5000
```

2. ブラウザからhttp://127.0.0.1:5000/scanxxe.php?xml=   　
へアクセス。

phpバージョン
```
$ php -v
PHP 8.1.2-1ubuntu2.18 (cli) (built: Jun 14 2024 15:52:55) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.2, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.2-1ubuntu2.18, Copyright (c), by Zend Technologies
```

PoC実行時にPHPアプリ側で９行目でエラーが出る場合は、`php-xml`をインストールする必要があります。
```
sudo apt-get install php-xml
```
