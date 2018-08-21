import xlsxwriter
class WriteExcel2:

    def __init__(self, fileName):
        self.workbook = xlsxwriter.Workbook(fileName)
        self.worksheet = self.workbook.add_worksheet("TestSummary")
        self.worksheet3 = self.workbook.add_worksheet("TestSuite")
        self.worksheet2 = self.workbook.add_worksheet("TestDetail")

    def init(self):
        self.worksheet.set_column("A:A", 15)
        self.worksheet.set_column("B:B", 20)
        self.worksheet.set_column("C:C", 20)
        self.worksheet.set_column("D:D", 20)
        self.worksheet.set_column("E:E", 20)
        self.worksheet.set_column("F:F", 20)
        self.worksheet.set_column("G:G", 30)

        self.worksheet.set_row(1, 30)
        self.worksheet.set_row(2, 30)
        self.worksheet.set_row(3, 30)
        self.worksheet.set_row(4, 30)
        self.worksheet.set_row(5, 30)
        self.worksheet.set_row(6, 30)

        define_format_H1 = self.get_format(self.workbook, {'bold': True, 'font_size': 18})
        define_format_H2 = self.get_format(self.workbook, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        self.worksheet.merge_range('B1:G1', 'Test Summary', define_format_H1)
        self.worksheet.merge_range('B2:G2', 'Test Summary', define_format_H2)

    def test_detail(self,testcaseList):
        self.worksheet2.set_column("A:A", 20)
        self.worksheet2.set_column("B:B", 30)
        self.worksheet2.set_column("C:C", 20)
        self.worksheet2.set_column("D:D", 30)
        self.worksheet2.set_column("E:E", 30)
        self.worksheet2.set_column("F:F", 20)
        self.worksheet2.set_column("G:G", 20)
        self.worksheet2.set_column("H:H", 30)
        self.worksheet2.set_column("I:I", 30)
        self.worksheet2.set_column("J:J", 30)

        self.worksheet2.merge_range('A1:L1', 'Test Detail', self.get_format(self.workbook,
                                                                 {'bold': True, 'font_size': 18, 'align': 'center',
                                                                  'valign': 'vcenter', 'bg_color': 'blue',
                                                                  'font_color': '#ffffff'}))
        self._write_center(self.worksheet2, "A2", 'User Story', self.workbook)
        self._write_center(self.worksheet2, "B2", 'Test Case', self.workbook)
        self._write_center(self.worksheet2, "C2", 'Test Result', self.workbook)
        self._write_center(self.worksheet2, "D2", 'Start Time', self.workbook)
        self._write_center(self.worksheet2, "E2", 'End Time', self.workbook)
        self._write_center(self.worksheet2, "F2", 'Time Spand', self.workbook)
        self._write_center(self.worksheet2, "G2", 'Error Type', self.workbook)
        self._write_center(self.worksheet2, "H2", 'Test Detail', self.workbook)
        self._write_center(self.worksheet2, "I2", 'Memo', self.workbook)
        self._write_center(self.worksheet2, "J2", 'Screen', self.workbook)
        self._write_center(self.worksheet2, "K2", 'TestTotal', self.workbook)
        self._write_center(self.worksheet2, "L2", 'TestFailed', self.workbook)

        temp = 3
        for item in testcaseList:
            self._write_left(self.worksheet2, "A" + str(temp), item.user_story, self.workbook)
            self._write_left(self.worksheet2, "B" + str(temp), item.test_case, self.workbook)
            self._write_center(self.worksheet2, "C" + str(temp), self._test_result(item.result), self.workbook)
            self._write_center(self.worksheet2, "D" + str(temp), item.start, self.workbook)
            self._write_center(self.worksheet2, "E" + str(temp), item.end, self.workbook)
            self._write_date(self.worksheet2, "F" + str(temp), '=E'+str(temp)+'-D'+str(temp), self.workbook)
            self._write_date(self.worksheet2, "G" + str(temp), '', self.workbook)
            self._write_left(self.worksheet2, "H" + str(temp), item.log, self.workbook)
            self._write_center(self.worksheet2, "I" + str(temp), 'Blank', self.workbook)
            self._write_url(self.worksheet2, "J" + str(temp), item.screen)
            self._write_center(self.worksheet2, "K" + str(temp), 1, self.workbook)
            self._write_center(self.worksheet2, "L" + str(temp), int(item.result), self.workbook)
            temp = temp + 1
        self._write_date(self.worksheet2, "F" + str(temp), '=SUM(F2:F' + str(temp - 1) + ')', self.workbook)
        self._write_center(self.worksheet2, "K" + str(temp),'=SUM(K2:K'+str(temp-1)+')' , self.workbook)
        self.testcase_total = '=TestDetail!$K$' + str(temp)
        self._write_center(self.worksheet2, "L" + str(temp),  '=SUM(L2:L' + str(temp - 1) + ')', self.workbook)
        self.testcase_failed = '=TestDetail!$L$' + str(temp)

    def test_suite(self,testsuiteList):
        #sheet 3
        self.worksheet3.set_column("A:A", 20)
        self.worksheet3.set_column("B:B", 30)
        self.worksheet3.set_column("C:C", 20)
        self.worksheet3.set_column("D:D", 30)
        self.worksheet3.set_column("E:E", 30)
        self.worksheet3.set_column("F:F", 20)

        self.worksheet3.merge_range('A1:G1', 'Test Suite Summary', self.get_format(self.workbook,
                                                                            {'bold': True, 'font_size': 18,
                                                                             'align': 'center',
                                                                             'valign': 'vcenter', 'bg_color': 'blue',
                                                                             'font_color': '#ffffff'}))
        self._write_center(self.worksheet3, "A2", 'User Story', self.workbook)
        self._write_center(self.worksheet3, "B2", 'Start Time', self.workbook)
        self._write_center(self.worksheet3, "C2", 'End Time', self.workbook)
        self._write_center(self.worksheet3, "D2", 'Time Spand', self.workbook)
        self._write_center(self.worksheet3, "E2", 'Test Total', self.workbook)
        self._write_center(self.worksheet3, "F2", 'Test Failed', self.workbook)
        self._write_center(self.worksheet3, "G2", 'Suite Total', self.workbook)

        temp = 3
        for item in testsuiteList:
            self._write_left(self.worksheet3, "A" + str(temp), item.user_story, self.workbook)
            self._write_center(self.worksheet3, "B" + str(temp), item.start, self.workbook)
            self._write_center(self.worksheet3, "C" + str(temp), item.end, self.workbook)
            self._write_date(self.worksheet3, "D" + str(temp), '=C' + str(temp) + '-B' + str(temp), self.workbook)
            self._write_center(self.worksheet3, "E" + str(temp), item.total, self.workbook)
            self._write_center(self.worksheet3, "F" + str(temp), item.failed, self.workbook)
            self._write_center(self.worksheet3, "G" + str(temp), 1, self.workbook)
            temp = temp + 1
        self._write_center(self.worksheet3, "G" + str(temp), '=SUM(G2:G' + str(temp - 1) + ')', self.workbook)
        self.testsuite_total='=TestSuite!$G$'+str(temp)

    def pie(self):
        chart1 = self.workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name': 'Summary Total',
            'categories': '=TestSummary!$D$4:$D$5',
            'values': '=TestSummary!$E$4:$E$5',
        })
        chart1.set_title({'name': 'Summary Total'})
        chart1.set_style(10)
        self.worksheet.insert_chart('A10', chart1, {'x_offset': 25, 'y_offset': 10})

    def get_format(self,wd, option={}):
        return wd.add_format(option)

    def get_format_center(self,wd, num=1):
            return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})

    def set_border_(self,wd, num=1):
            return wd.add_format({}).set_border(num)

    def _write_center(self,worksheet, cl, data, wd):
            return worksheet.write(cl, data, self.get_format_center(wd))

    def _write_left(self,worksheet, cl, data, wd):
            return worksheet.write(cl, data, wd.add_format({'align': 'left', 'valign': 'vcenter', 'border': 1}))

    def _write_url(self,worksheet, cl, data):
        #worksheet.write_url('C6', 'D:\P01.png', string='Screen Short')
        if data.strip()!='':
            return worksheet.write_url(cl, data, string='Screen Short')

    def _write_date(self,worksheet, cl, data, wd):
        format7 = wd.add_format({'num_format': 'hh:mm:ss','border': '1'})
        return worksheet.write(cl, data, format7)

    def _test_result(self,num):
        if num=='0':
            return 'Pass'
        else:
            return 'Failed'

    def test_summary(self,testappList):
        self._write_center(self.worksheet, "B3", 'Project', self.workbook)
        self._write_center(self.worksheet, "B4", 'Test Suite', self.workbook)
        self._write_center(self.worksheet, "B5", 'Language', self.workbook)
        self._write_center(self.worksheet, "B6", 'Server', self.workbook)
        self._write_center(self.worksheet, "B7", '', self.workbook)

        self._write_center(self.worksheet, "C3", 'Novauts', self.workbook)
        self._write_center(self.worksheet, "C4", self.testsuite_total, self.workbook)
        self._write_center(self.worksheet, "C5", 'C#', self.workbook)
        self._write_center(self.worksheet, "C6",  testappList['Server'], self.workbook)
        self._write_center(self.worksheet, "C7", '', self.workbook)

        self._write_center(self.worksheet, "D3", "Total", self.workbook)
        self._write_center(self.worksheet, "D4", "Pass", self.workbook)
        self._write_center(self.worksheet, "D5", "Failed", self.workbook)
        self._write_center(self.worksheet, "D6", "Profile", self.workbook)
        self._write_center(self.worksheet, "D7", '', self.workbook)

        self._write_center(self.worksheet, "E3", self.testcase_total, self.workbook)
        self._write_center(self.worksheet, "E4", '=E3-E5', self.workbook)
        self._write_center(self.worksheet, "E5", self.testcase_failed, self.workbook)
        self._write_center(self.worksheet, "E6", testappList['Profile'], self.workbook)
        self._write_center(self.worksheet, "E7", '', self.workbook)

        self._write_center(self.worksheet, "F3", 'Order Entry', self.workbook)
        self._write_center(self.worksheet, "F4", 'Office', self.workbook)
        self._write_center(self.worksheet, "F5", 'Prepress', self.workbook)
        #self._write_center(self.worksheet, "F6", 'Item Mait', self.workbook)
        self._write_center(self.worksheet, "F6", '', self.workbook)
        self._write_center(self.worksheet, "F7", '', self.workbook)

        self._write_left(self.worksheet, "G3",testappList['OrderEntry'], self.workbook)
        self._write_left(self.worksheet, "G4",testappList['Office'], self.workbook)
        self._write_left(self.worksheet, "G5",testappList['Prepress'], self.workbook)
        #self._write_left(self.worksheet, "G6", testappList['ItemMait'], self.workbook)
        self._write_left(self.worksheet, "G6", '', self.workbook)
        self._write_left(self.worksheet, "G7", '', self.workbook)

        self.pie()

    def close(self):
        self.workbook.close()

