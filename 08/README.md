# 08-XMLインジェクション

### 環境構築
1. "scanxxe.php"を作成
2. $ php -S 192.168.7.246:5000
コマンドでwebサーバ開始
3. ブラウザからhttp://192.168.7.246:5000/scanxxe.php?xml=   　
へアクセス。

phpバージョン
$ php -v
PHP 8.1.2-1ubuntu2.18 (cli) (built: Jun 14 2024 15:52:55) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.2, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.2-1ubuntu2.18, Copyright (c), by Zend Technologies
