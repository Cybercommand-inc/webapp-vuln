# 11-XPathインジェクション

### 環境構築


1. virtualenvのインストール
Pythonのパッケージ管理ツールであるpipを使ってインストールします。

```
pip3 install virtualenv
```

2. 仮想環境の作成
仮想環境を作成します。仮想環境のディレクトリを指定することで、指定した場所に仮想環境が作成されます。ここで、webapp-vulnは仮想環境の名前で、任意の名前をつけることができます。

```
$ virtualenv webapp-vuln
```

3. 仮想環境のアクティベート
仮想環境をアクティベートすると、その環境内でのPythonコマンドやパッケージの操作が可能になります。仮想環境がアクティベートされると、プロンプトが変わり、環境の名前が表示されます。

Windowsの場合:
```
myenv\Scripts\activate
```

macOSやLinuxの場合:
```
source myenv/bin/activate
```


4. パッケージのインストール
仮想環境がアクティベートされている状態で、pipを使ってパッケージをインストールします。これにより、仮想環境内にのみパッケージがインストールされます。
``` 
$ pip3 install flask lxml
```

5. ディレクトリ構成
```
$ cd xpath
$ ls
app.py
index.html
```

6. アプリケーションスタート
```
[~/xpath]
$ python3 app.py
```
