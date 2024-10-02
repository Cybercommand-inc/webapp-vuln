# 20-アクセス制御の不備、欠落

### 環境構築

1. 必要なパッケージ
```
$ pip3 install Flask Flask-CORS
```

2. ディレクトリ構造

```
/corsVulnerabilityApp
│
├── /static (オプショナル、JSやCSSなどの静的アセット用)
│
├── app.py                   # メインのFlaskアプリケーション
│
└── test.html                # CORS脆弱性をテストするための外部HTMLファイル
```

3. Linux PC1でコマンドを実行 
```
$ python3 app.py
```

4. Linux PC2でブラウザから
```
file:///path/to/test.html　へアクセス
```
