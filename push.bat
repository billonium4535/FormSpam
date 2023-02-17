@echo off

:choice
set /P c=Have you updated the version in setup.py? [Y/N]
if /I "%c%" EQU "Y" goto :push
if /I "%c%" EQU "N" goto :changeVersion
goto choice

:push
cd base-GoogleFormSpam
rmdir build
rmdir dist
rmdir GoogleFormSpam.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*
pause
exit

:changeVersion
cd base-GoogleFormSpam
notepad setup.py
goto choice