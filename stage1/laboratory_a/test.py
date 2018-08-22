from mssql.sqlconnect import sqlconnect

if __name__=='__main__':

    sql = """
    IF OBJECT_ID('persons', 'U') IS NOT NULL
        DROP TABLE persons
    CREATE TABLE persons (
        id INT NOT NULL,
        name VARCHAR(100),
        salesrep VARCHAR(100),
        PRIMARY KEY(id)
    )
    """
    conn = sqlconnect('ComputerName','DBName')
    conn.execute(sql)
    conn.select('SELECT * FROM dbo.LoadTestCase')
    conn.close()
