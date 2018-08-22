'''
splinter: https://splinter.readthedocs.io/en/latest/

'''
from splinter import Browser

class site:

    def __init__(self):
        chromeDriverpath = 'C:\Program Files\Java\webdriver\chromedriver.exe'  # Web driver path
        executable_path = {'executable_path': chromeDriverpath}  # DO NOT change it
        self.browser = Browser('chrome', **executable_path)

    def start_browser(self,url):
        self.browser.visit(url)
        a=1

    def click(self, xpath):
        button=self.browser.find_by_xpath(xpath)
        button.click()

    def getcontent(self,xpath):
        return self.browser.find_by_xpath(xpath)[0].html

    def filter(self,filters,content):
        newcontent=content
        for filter in filters:
            newcontent=newcontent.replace(filter,'')
        return newcontent
