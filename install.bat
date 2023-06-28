pyi-makespec --onefile calibrationBot.py
pyinstaller --clean calibrationBot.spec
start python ./shell/moveFiles.py
set DIR=C:\Users\gibra\Documents\Programming\Python\FujiFPDCalib
xcopy %DIR%\img %DIR%\dist\img /R /S /Y /Q
pause