# Python
## 仮想環境構築
* 仮想環境作成  
`python -m venv [仮想環境名]`  
* 仮想環境のアクティベート  
`source [仮想環境名]/bin/activate`
* インストールパッケージとバージョン書き出し  
`pip freeze > requirements.txt`
* 一括インストール  
`pip install -r requirements.txt`
* 仮想環境ディアクティベート  
`deactivate`