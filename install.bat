pyi-makespec --onefile calibrationBot.py
pyinstaller --clean calibrationBot.spec
start python moveFiles.py
pause