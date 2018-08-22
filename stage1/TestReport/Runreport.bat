set localpath=D:\bak\workspace\pythonstudy2\stage1\TestReport\

xcopy \\togdev02\c$\NewTestPass\Screenshot\testresult.xml %localpath%  /r /y
python %localpath%test.py
xcopy %localpath%*.xlsx D:\bak\email\  /r /y
::xcopy %folder1% %folder2% /e /r /y
::del %temp%
ECHO Finish Copy & PAUSE>nul

::Delete rush file
::cd C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE
::del RP*.png
::rd TestResults /s