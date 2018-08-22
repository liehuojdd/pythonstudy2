from splinter.browser import Browser
import time

def GetElementIndex():
    lines=browser.find_by_xpath('//tbody[@id="queryLeftTable"]/tr')
    i=0
    for line in lines:
        if line.text.find('K1023') != -1:
            #Because always get two rows of one line.
            #Index such as: 0, 2, 4, 6
            return int(i/2)
        else:
            i=i+1

    return -1

#executable_path = {'executable_path':'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}
executable_path = {'executable_path':'C:\Program Files\Java\webdriver\chromedriver.exe'}
browser = Browser('chrome', **executable_path)
#browser = Browser('chrome')

#Login
browser.visit('https://kyfw.12306.cn/otn/login/init')

loginBtn=browser.find_by_id('loginSub')
browser.fill('loginUserDTO.user_name','username')
browser.fill('userDTO.password','password')
loginBtn.click()


#Search ticket
#browser.visit('https://kyfw.12306.cn/otn/leftTicket/init')
time.sleep(4)
browser.find_by_xpath('//li[@id="selectYuding"]/a').click()
browser.evaluate_script('document.getElementById("fromStation").setAttribute("type","visiable")')
browser.evaluate_script('document.getElementById("toStation").setAttribute("type","visiable")')
browser.evaluate_script('document.getElementById("train_date").readOnly=false')
browser.fill('leftTicketDTO.from_station','TJP')
browser.fill('leftTicketDTO.to_station','MHL')
browser.fill('leftTicketDTO.train_date','2017-11-30')
browser.evaluate_script('document.getElementsByClassName("cal-wrap")[0].style.display="none"')
#browser.find_by_text('查询').click()
time.sleep(2)
browser.find_by_text('查询').click()
#browser.reload()
#browser.find_by_text('预订')[3].click()
time.sleep(2)

links=browser.find_by_text('预订')

#Select K1023
elementIndex=GetElementIndex()
links[elementIndex].click()

#Select contact
#1 is first index
contactIndex=2
browser.find_by_xpath('//ul[@id="normal_passenger_id"]/li['+str(contactIndex)+']/input').click()
#Add kid ticket
#browser.find_link_by_partial_text('添加儿童票')

#Select type
#If second contact, seatType_2
#Value: 3 硬卧, 1 硬座, 4 软卧
browser.find_by_xpath('//select[@id="%s"]//option[@value="%s"]' % ('seatType_1', '3')).first._element.click()

#Submit
browser.find_link_by_partial_text('提交订单').click()

browser.quit()



