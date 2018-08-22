'''
Author: Mark Zhang
Email: zwm_8086@163.com
Update date: 11/29/2017
Version: V1

Enviroment required:
1.Python 3.6  https://www.python.org/
2.Splinter 0.7.7 http://splinter.readthedocs.io/en/latest/
3.Chrome 59.0  https://chrome.en.softonic.com
4.Chrome webdriver https://sites.google.com/a/chromium.org/chromedriver/downloads

Note:
Please define all variables at the beginning of the class first.
Any suggestion please contact me. thanks!

'''
from splinter.browser import Browser
import time
import os

class Ticket:
    loginUsername='username' # Your login name
    loginPassword='password' # Your login password
    chromeDriverpath='C:\Program Files\Java\webdriver\chromedriver.exe'# Web driver path
    fromStation='TJP' # From station value, you can find it by chrome developer tool. ex: TJP  天津
    toStation='THL' # To station value, you can find it by chrome developer tool. ex: MHL 梅河口, THL  通化
    startDate='2017-02-03' # The date you want
    trainNumber='K971' # The train number you wanted
    #trainNumber='ABCD'
    contactList = {3} # Add contact list from your contact list,start with 1
    seatType=3 # Select seat type 3 硬卧, 1 硬座, 4 软卧

    #searchInterval=5
    searchInterval=3 # Set refresh interval, unit for second
    mp3='D:\KuGou\CD1\simple1.mp3' # If success, play the music you want

    executable_path = {'executable_path': chromeDriverpath} # DO NOT change it
    browser = Browser('chrome', **executable_path) # DO NOT change it

    def __init__(self):
        self.browser.visit('https://kyfw.12306.cn/otn/login/init')

    def __login(self):
        self.browser.fill('loginUserDTO.user_name', self.loginUsername)
        self.browser.fill('userDTO.password', self.loginPassword)

    def login(self):
        self.__login()
        print('Step 1,Login. select picture then press "ENTER" to continue')
        input()
        loginBtn = self.browser.find_by_id('loginSub')
        loginBtn.click()

        print('Please press "ENTER" to continue, or press "r" to retry:')
        letter = input()
        if letter == 'r':
            self.login()
        else:
            return

    def __searchTicket(self):

        time.sleep(4)
        self.browser.find_by_xpath('//li[@id="selectYuding"]/a').click()
        self.browser.evaluate_script('document.getElementById("fromStation").setAttribute("type","visiable")')
        self.browser.evaluate_script('document.getElementById("toStation").setAttribute("type","visiable")')
        self.browser.evaluate_script('document.getElementById("train_date").readOnly=false')
        self.browser.fill('leftTicketDTO.from_station', self.fromStation)
        self.browser.fill('leftTicketDTO.to_station', self.toStation)
        self.browser.fill('leftTicketDTO.train_date', self.startDate)
        self.browser.evaluate_script('document.getElementsByClassName("cal-wrap")[0].style.display="none"')
        # browser.find_by_text('查询').click()
        # browser.reload()
        # browser.find_by_text('预订')[3].click()


    def searchTicket(self):
        print('Step 2,Search ticket, press CTRL+C to break')
        self.__searchTicket()
        while True:
            time.sleep(self.searchInterval)
            self.browser.find_by_text('查询').click()
            elementIndex = self.getElementIndex(self.trainNumber)
            try: # If not find the link
                if (elementIndex != -1):
                    time.sleep(2)
                    links = self.browser.find_by_text('预订')
                    links[elementIndex].click()
                    return
            except Exception:
                a=1

    def addContact(self):
        print('Step 3,Add contact')
        # Select contact
        # 1 is first index
        i=1
        for contact in self.contactList:
            self.browser.find_by_xpath('//ul[@id="normal_passenger_id"]/li[' + str(contact) + ']/input').click()
            # Select type
            # If second contact, seatType_2
            # Value: 3 硬卧, 1 硬座, 4 软卧
            time.sleep(2)
            self.browser.find_by_xpath(
            '//select[@id="%s"]//option[@value="%s"]' % ('seatType_'+str(i), str(self.seatType))).first._element.click()
            i=i+1

        # Add kid ticket
        # browser.find_link_by_partial_text('添加儿童票')

        # Submit
        self.browser.find_link_by_partial_text('提交订单').click()

    def getElementIndex(self,text):
        lines = self.browser.find_by_xpath('//tbody[@id="queryLeftTable"]/tr')
        i = 0
        for line in lines:
            if line.text.find(text) != -1:
                # Because always get two rows of one line.
                # Index such as: 0, 2, 4, 6
                return int(i / 2)
            else:
                i = i + 1

        return -1

    def playSound(self):
        os.system(self.mp3)

    def run(self):
        self.login()
        self.searchTicket()
        self.addContact()
        self.playSound()