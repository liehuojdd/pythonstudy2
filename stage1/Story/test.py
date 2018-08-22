from study.ticket.ticket2 import Ticket
from website.site import site
from website.file import file

'''
change python version
File->Settings->project:your project->Project Interpreter
Select Porject Interpreter,and click Apply
'''

if __name__ == '__main__':
    try:
        url = b'2f8401fe7a0dd0e90e80021caa400d397d58dab4fa4d0f930b84fa2f3323a0296c309889d112f40bc3152d1d43de0716'
        file = file('a.txt')

        site = site()
        site.start_browser(url)
        for i in range(0, 520):
            title = site.getcontent("//div[@id='nr_title']")
            content = site.getcontent("//div[@id='nr']/div[@id='nr1']")
            filters = ['&nbsp;',
                       '<br>',
                       '<p>',
                       '</p>']
            content = site.filter(filters, content)
            file.write(title)
            file.write(content)
            print('end page of:' + str(i))
            site.click("//td[@class='next']/a[@id='pb_next']")
        file.close()
        b = 1
    except Exception as e:
        print(str(e))
