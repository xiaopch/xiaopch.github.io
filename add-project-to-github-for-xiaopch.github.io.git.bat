rmdir /S /Q .git
git init
git add .
git commit -m "chore: init zensical site"
git branch -M main
git remote add origin git@github.com:xiaopch/xiaopch.github.io.git
git push -f origin main
pause