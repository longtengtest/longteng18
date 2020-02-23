

if "%lf%"=="true" C:\Users\Secoo\AppData\Local\Programs\Python\Python37-32\python.exe -m pytest %path% --html=reports/report.html --self-contained-html --lf -m=%mark% else C:\Users\Secoo\AppData\Local\Programs\Python\Python37-32\python.exe -m pytest %path% --html=reports/report.html --self-contained-html -m=%mark%