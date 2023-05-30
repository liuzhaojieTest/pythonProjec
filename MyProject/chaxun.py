import cx_Oracle
NDMC1 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC1_BETA')
cur_NDMC1 = NDMC1.cursor()
sql1 = "SELECT mp.*,ROWNUM no FROM RCS_VIRDIR_MAP mp WHERE VIRDIRID='1A11mp0pc00245005'AND no<=10"
cur_NDMC1.execute(sql1)
result = cur_NDMC1.fetchall()
print(result)
