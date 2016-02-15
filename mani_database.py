import win32com.client   

conn = win32com.client.Dispatch(r'ADODB.Connection')   
DSN = r'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=F:\\Working Source\\tornado test\\my.mdb;'   
conn.Open(DSN)