::cmd  /k  E:\virtualenv\cuda\Scripts\activate
::pip install -r requirements.txt
::pip install pysoundfile
::cmd  /k  E:\virtualenv\cpu\Scripts\pyinstaller -F resize-image.py  --noconsole
cmd  /c  mkdocs gh-deploy
cmd  /c start https://xiaopch.github.io/ 
cmd /k cd .
::sleep 80