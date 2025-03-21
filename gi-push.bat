rmdir /s /q site
git status
git add -A
git status
git commit -m commit_%random% 
::git pull
cmd /k git push
pause