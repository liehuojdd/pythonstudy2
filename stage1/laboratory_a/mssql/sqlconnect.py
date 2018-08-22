'''

If account under domain, you can ignore user=,password=.
Default port 1433, you can ignore port=1433
server='ComputerName' is fine

To open local server port for testing:
1.MS Sql Server->Configuration tools->Sql Server Configuration Manager
2.SQL Server Network Configuration/Protocols for MSSQLSERVER/TCP/IP, right click-enabled
3.Restart SQL Server service

'''
import pymssql

class sqlconnect:
    def __init__(self,server,database):
        user=''
        password=''
        port=''
        self.conn = pymssql.connect(server=server,database= database)
        self.cursor = self.conn.cursor()

    def execute(self,str):
        self.cursor.execute(str)
        '''
        cursor.executemany(
            "INSERT INTO persons VALUES (%d, %s, %s)",
            [(1, 'John Smith', 'John Doe'),
             (2, 'Jane Doe', 'Joe Dog'),
             (3, 'Mike T.', 'Sarah H.')])
        conn.commit()
        '''
        self.conn.commit()

    def select(self,str):
        self.cursor.execute(str)
        row = self.cursor.fetchone()
        while row:
            print("ID=%d, Name=%s" % (row[0], row[1]))
            row = self.cursor.fetchone()

        # for row in cursor:
        #     print("ID=%d, Name=%s" % (row[0], row[1]))

    def close(self):
        self.conn.close()
