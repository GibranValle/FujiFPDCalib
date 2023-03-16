pyi-makespec --onefile calibrationBot.py
pyinstaller --clean calibrationBot.spec
start python ./shell/moveFiles.py
pause