# webapp-vuln

### 全体の環境構築
以下ので順でprojectsフォルダを作成し、教材をcloneしましょう。
```
$ cd $HOME
$ mkdir projects
$ cd projects
$ git clone git@github.com:Cybercommand-inc/webapp-vuln.git
$ ls # webapp-vulnフォルダが作成されている。

# 以降の教材はすべて、$HOME/projects/webapp-vulnフォルダ内で進めます。
$ cd webapp-vuln
```

### BROKEN CRYSTALSの環境構築
```
$ cd $HOME/projects/webapp-vuln
$ git clone git@github.com:NeuraLegion/brokencrystals.git
$ cd brokencrystals
$ docker compose --file=docker-compose.local.yml up -d --build
```

- ブラウザからアクセスして確認します。
```
http://<PCのIP>:3000
```

### DSVWの環境構築
```
$ cd $HOME/projects/webapp-vuln
$ python --version # pythonのバージョンが3以上であることの確認
$ pip --version # pipのバージョン確認
$ git clone https://github.com/stamparm/DSVW.git
$ cd DSVW
$ pip install -r requirements.txt
$ python dsvw.py

```

- ブラウザからアクセスして確認します。
```
http://<PCのIP>:65412
```
