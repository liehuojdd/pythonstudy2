from Common.ReadXml import ReadXml
from Common.WriteExcel import WriteExcel
from Common.WriteExcel2 import WriteExcel2
from Common.Feed import Feed
import time

if __name__ == '__main__':
    timestr = time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
    reportname='report'+timestr+'.xlsx'

    readXml=ReadXml('testresult.xml')
    testcaseList=readXml.ReadTestCase()
    testsuiteList=readXml.TestSuiteList()
    testappList = readXml.TestAppList()

    writeExcel2=WriteExcel2(reportname)
    writeExcel2.init()
    writeExcel2.test_suite(testsuiteList)
    writeExcel2.test_detail(testcaseList)
    writeExcel2.test_summary(testappList)
    writeExcel2.close()

    b=1