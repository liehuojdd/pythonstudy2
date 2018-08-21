import xml.dom.minidom

from Common.Feed import Feed
from Common.Feed import TestSuite
'''
Replace "  []   ()   <>  & /
'''
class ReadXml:
    dom=None
    def __init__(self,fileName):
        self.dom=xml.dom.minidom.parse(fileName)
        self.appversion = {'OrderEntry': '', 'Office': '', 'Prepress': '', 'ItemMait': '', 'Server': '', 'Profile': ''}

    def ReadFirstNode1(self):
        root=self.dom.documentElement
        itemlist = root.getElementsByTagName('login')
        item = itemlist[0]
        un = item.getAttribute("username")

        cc = self.dom.getElementsByTagName('caption')
        c1 = cc[0]
        c1.firstChild.data

        return root.getElementsByTagName('maxid')

    def ReadTestCase(self):
        userstorys=self.dom.getElementsByTagName('userstory')
        list=[]
        self.testsuiteList=[]
        self.userstory_count=0;
        for userstory in userstorys:
            testsuite=TestSuite()
            userstoryName=userstory.getAttribute("name")
            testapps=userstory.getElementsByTagName('testapp')
            testsuite.user_story=userstoryName
            for testapp in testapps:
                testappName=testapp.getAttribute("name")
                testappVersion=self.ReadData(testapp.getElementsByTagName('version')[0])
                testServer=self.ReadData(testapp.getElementsByTagName('server')[0])
                testProfile = self.ReadData(testapp.getElementsByTagName('profile')[0])
                self.WriteVersion(testappName,testappVersion,testServer,testProfile)

            self.testcase_count=0
            self.testcase_failed=0
            testcases = userstory.getElementsByTagName('testcase')
            for testcase in testcases:
                feed=Feed()
                feed.user_story=userstoryName
                feed.test_case=testcase.getAttribute("name")
                feed.result = self.ReadData(testcase.getElementsByTagName('result')[0])
                feed.start = self.ReadData(testcase.getElementsByTagName('start')[0])
                feed.end = self.ReadData(testcase.getElementsByTagName('end')[0])
                feed.log = self.ReadData(testcase.getElementsByTagName('log')[0])
                feed.screen = self.ReadData(testcase.getElementsByTagName('screen')[0])
                feed.oe=self.ReadVersion('OrderEntry')
                feed.office = self.ReadVersion('Office')
                feed.prepress = self.ReadVersion('Prepress')
                feed.itemmait = self.ReadVersion('ItemMait')
                if (feed.result == '1'):
                    self.testcase_failed = self.testcase_failed + 1
                testsuite.end=feed.end
                list.append(feed)
                self.testcase_count=self.testcase_count+1
                if self.testcase_count==1:
                    testsuite.start=feed.start
                testsuite.failed = self.testcase_failed
                testsuite.total=self.testcase_count
            self.userstory_count=self.userstory_count+1
            self.testsuiteList.append(testsuite)
        return list

    def ReadData(self,element):
        try:
            return element.firstChild.data
        except BaseException:
            return ""

    def ReadVersion(self,element):
        return self.appversion.get(element)

    def WriteVersion(self,name,version,testServer,testProfile):
        try:
            if(name=='OrderEntry' and version.strip()!=''):
                self.appversion['OrderEntry']=version
            if (name == 'Office' and version.strip()!=''):
                self.appversion['Office'] = version
            if (name == 'Prepress' and version.strip()!=''):
                self.appversion['Prepress'] = version
            if (name == 'ItemMait' and version.strip()!=''):
                self.appversion['ItemMait'] = version
            if (testServer.strip()!=''):
                self.appversion['Server'] = testServer
            if (testProfile.strip()!=''):
                self.appversion['Profile'] = testProfile
        except BaseException:
            return

    def TestSuiteList(self):
        return self.testsuiteList;

    def TestAppList(self):
        return self.appversion
