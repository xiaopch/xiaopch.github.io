<<<<<<< HEAD
::cmd  /k  E:\virtualenv\cuda\Scripts\activate
::pip install -r requirements.txt
::pip install pysoundfile
::cmd  /k  E:\virtualenv\cpu\Scripts\pyinstaller -F resize-image.py  --noconsole
cmd  /c  mkdocs gh-deploy
cmd  /c start https://xiaopch.github.io/
cmd /k cd .
=======
::cmd  /k  E:\virtualenv\cuda\Scripts\activate
::pip install -r requirements.txt
::pip install pysoundfile
::cmd  /k  E:\virtualenv\cpu\Scripts\pyinstaller -F resize-image.py  --noconsole
cmd  /c  mkdocs gh-deploy
cmd  /c start https://xiaopch.github.io/
cmd /k cd .
>>>>>>> ee0de038a932e9888ffa0b60c04e3c6a89d7d464
::sleep 80