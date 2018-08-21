import xlsxwriter
class WriteExcel:

    def __init__(self, fileName):
        self.workbook = xlsxwriter.Workbook('report2.xlsx')
        self.worksheet1 = self.workbook.add_worksheet("TestSummary")
        self.worksheet2 = self.workbook.add_worksheet("TestDetail")

        self.worksheet1.set_column("A:A", 15)
        self.worksheet1.set_column("B:B", 20)
        self.worksheet1.set_column("C:C", 20)
        self.worksheet1.set_column("D:D", 20)
        self.worksheet1.set_column("E:E", 20)
        self.worksheet1.set_column("F:F", 20)

        self.worksheet1.set_row(1, 30)
        self.worksheet1.set_row(2, 30)
        self.worksheet1.set_row(3, 30)
        self.worksheet1.set_row(4, 30)
        self.worksheet1.set_row(5, 30)

        define_format_H1 = self.set_format({'bold': True, 'font_size': 18})
        define_format_H2 = self.set_format({'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        self.worksheet1.merge_range('B1:G1', 'Test Summary', define_format_H1)
        self.worksheet1.merge_range('B2:G2', 'Test Summary', define_format_H2)
        '''
       self.write_center(self, "B3", 'Project', workbook)
       self.write_center(self, "B4", '', workbook)
       self.write_center(self, "B5", 'Language', workbook)
       self.write_center(self, "B6", 'Test Suite', workbook)
       '''

    def set_border_(self, num=1):
        self.workbook.add_format({}).set_border(num)

    def set_format(self,option={}):
        return self.workbook.add_format(option)

    def set_format_center(self, num=1):
        return self.workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})

    def write_center(self,worksheet, cl, data):
        return worksheet.write(cl, data,self.set_format_center())

    def write_url(self, cl, data, name):
        return self.worksheet1.write_url(cl, data, name)

    def pie(workbook, worksheet):
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name': 'Summary Total',
            'categories': '=TestSummary!$D$4:$D$5',
            'values': '=TestSummary!$E$4:$E$5',
        })
        chart1.set_title({'name': 'Summary Total'})
        chart1.set_style(10)
        worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

    def test_detail(self,worksheet,workbook):
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)
        worksheet.set_column("I:I", 20)
        worksheet.set_column("J:J", 20)
        '''
        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)
        worksheet.set_row(8, 30)
        worksheet.set_row(9, 30)
        '''

        worksheet.merge_range('A1:M1', 'Test Detail', self.set_format(workbook,
                                                                 {'bold': True, 'font_size': 18, 'align': 'center',
                                                                  'valign': 'vcenter', 'bg_color': 'blue',
                                                                  'font_color': '#ffffff'}))
        self.write_center(worksheet, "A2", 'User Story', workbook)
        self.write_center(worksheet, "B2", 'Test Case', workbook)
        self.write_center(worksheet, "C2", 'Test Result', workbook)
        self.write_center(worksheet, "D2", 'Start Time', workbook)
        self.write_center(worksheet, "E2", 'End Time', workbook)
        self.write_center(worksheet, "F2", 'Time Spand', workbook)
        self.write_center(worksheet, "G2", 'Error Type', workbook)
        self.write_center(worksheet, "H2", 'Test Detail', workbook)
        self.write_center(worksheet, "I2", 'Memo', workbook)
        self.write_center(worksheet, "J2", 'USTotal', workbook)
        self.write_center(worksheet, "K2", 'USFailed', workbook)
        self.write_center(worksheet, "L2", 'TestTotal', workbook)
        self.write_center(worksheet, "M2", 'TestFailed', workbook)

    def WriteByTab(self,tabIndex,line,data):
        if tabIndex==1:
            self.WriteDetail(line,data)

        self.workbook.close()

    def WriteDetail(self,line,data):
        self.write_center(self.worksheet2, "A" + str(line), data["user_story"])
        self.write_center(self.worksheet2, "B" + str(line), data["test_case"])
        self.write_center(self.worksheet2, "C" + str(line), data["result"])
        self.write_center(self.worksheet2, "D" + str(line), data["start"])
        self.write_center(self.worksheet2, "E" + str(line), data["end"])
        self.write_center(self.worksheet2, "F" + str(line), "")
        self.write_center(self.worksheet2, "G" + str(line), "")
        self.write_center(self.worksheet2, "H" + str(line), "")
        self.write_center(self.worksheet2, "I" + str(line), "")
