rmdir  /S /Q site
git add .github/workflows/docs.yml
git add .
git commit -m "chore: add github pages workflow"
git push -f origin main
pause