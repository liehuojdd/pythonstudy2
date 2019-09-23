Python Study Code
==================================================
- [Python](https://www.python.org/)
- [Chrome](https://chrome.en.softonic.com)
- [ChromeWebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Notepad++](https://notepad-plus-plus.org/)
- [Notepad plugins MarkdownViewer++](https://github.com/nea/MarkdownViewerPlusPlus/releases)
Download a release version and copy the included MarkdownViewerPlusPlus.dll to the plugins sub-folder at your Notepad++ 

Modules
--------------------------------------

### Modules(3.6.3)
- **pymssql** for connect sql server database
manual download from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql, then pip install
- _pycryptodomex_ encode and decode with AES
pip3 install -i https://pypi.douban.com/simple pycryptodomex
- splinter, autotest for website
https://splinter.readthedocs.io/en/latest/
- **BeautifulSoup** formate text
pip install beautifulsoup4
- **XlsxWriter** tool for excel
pip install XlsxWriter, http://xlsxwriter.readthedocs.io/

### Modules(2.7.13)
- Mechanize, collect html content, Only support Python 2.*



### More details:
**pymssql**
If account under domain, you can ignore user=,password=.
Default port 1433, you can ignore port=1433
server='ComputerName' is fine

To open local server port for testing:
1.MS Sql Server->Configuration tools->Sql Server Configuration Manager
2.SQL Server Network Configuration/Protocols for MSSQLSERVER/TCP/IP, right click-enabled
3.Restart SQL Server service


Errors
--------------------------------------
```bash
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": 
http://landinghub.visualstudio.com/visual-cpp-build-tools
```
maybe not match version for your localy

Notes
--------------------------------------

### From CMD
Create SSH Key
$ ssh-keygen -t rsa -C abc@test.com
(Help->Show SSH Key)

Add file:
1.$ git init
2.$ git clone https://github.com/liehuojdd/nv2.git
3.Copy file to nv2 folder.
4. git add.  then git commit -m 'write some common'
5.$ git push origin master
6.Remote branch:
$ git push origin --delete branch1
(or remote->delete branch)

### From GUI
1.Clone exitsting repository<br/>
Source location:https://github.com/liehuojdd/nv2.git<br/>
Target directory:D:\path\test2  (folder test2 not exits)<br/>
or<br/>
1. Add Remote, remote->add<br/>
  Name:origin<br/>
  Location:https://github.com/liehuojdd/nv2.git<br/>
2. Create branch, create localy, then push.<br/>
  branch->Create, enter name then create. then click push.<br/>
3. Delete branch<br/>
  remote->delete branch<br/>
Or<br/>
1.Get latest version and merge<br/>
Remote->Fatch from->Origin, then Merge->Local merge<br/>

### pychrame
Change python version
File->Settings->project:your project->Project Interpreter
Select Porject Interpreter,and click Apply

Projects
--------------------------------------
* stage1\laboratory_a,
New function test
* mssql
* stage1\Story
* stage1\TestReport,
change xml to xlsx report
* 2.7\20171109Python2.7

https://blog.csdn.net/woshisangsang/article/details/73230433

