#coding=utf-8

from bs4 import BeautifulSoup
from novel.feisu1 import feisu
from novel.pinshu3 import pinshu
from novel.biqu import biqu
'''
change python version
File->Settings->project:your project->Project Interpreter
Select Porject Interpreter,and click Apply

str1='<div id="content"><!--div class="ads_cscript></div-->wmzhang'
strFind='-->'
strNow=str1[str1.find(strFind) + len(strFind):]
'''
#print strNow


#novel=feisu()
#novel.main()

pinshu=pinshu()
pinshu.main()

#biqu=biqu()
#biqu.main()