@echo off
chcp 65001 >nul
echo [1/4] Pulling...
git pull || goto :fail
echo [2/4] Adding changes...
git add .
echo [3/4] Committing...
setlocal EnableDelayedExpansion
set MSG=
for /f "delims=" %%f in ('git diff --cached --name-only') do set MSG=!MSG! %%f
if defined MSG (
  set "GIT_EDITOR=true"
  git commit -m "Update%MSG%"
) else (
  echo No changes to commit, skip.
)
echo [4/4] Pushing...
git push && goto :done
:fail
echo Failed: pull or push did not succeed.
:done
pause
