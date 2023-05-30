import cx_Oracle

NDAS = cx_Oracle.connect('NDA', '123456', '122.112.235.69:8521/NDAS_BETA')
NDAM = cx_Oracle.connect('NDA', '123456', '122.112.235.69:8521/NDAM_BETA')
NDMC1 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC1_BETA')
NDMC2 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC2_BETA')
NDMC3 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC3_BETA')
NDMC4 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC4_BETA')

cur_NDAS = NDAS.cursor()
cur_NDAM = NDAM.cursor()
cur_NDMC1 = NDMC1.cursor()
cur_NDMC2 = NDMC2.cursor()
cur_NDMC3 = NDMC3.cursor()
cur_NDMC4 = NDMC4.cursor()

sql = "SELECT * FROM ISPACE_USER_INFO"

cur_NDAS.execute(sql)
result = cur_NDAS.fetchall()
for data in result:
    print(data)
NDAS.close()
# cur_NDAS.close()
