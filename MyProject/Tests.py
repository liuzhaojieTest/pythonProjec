import pymysql
import cx_Oracle
import time

NDMC1 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC1_BETA')
NDMC2 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC2_BETA')
NDMC3 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC3_BETA')
NDMC4 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC4_BETA')
tidb = pymysql.connect(host='192.168.1.51', user='root', password='123456', database='yun_personal_kd_db',
                       port=4000)

cur_NDMC1 = NDMC1.cursor()
cur_tidb2 = tidb.cursor()
cur_NDMC1_2 = NDMC1.cursor()
cur_NDMC1_3 = NDMC1.cursor()
cur_tidb = tidb.cursor()
cur_tidb3 = tidb.cursor()

sql1 = "SELECT COUNT(*) FROM RCS_VIRDIR_MAP WHERE VIRDIRID='1A11mp0pc00245005'"
sql2 = "SELECT COUNT(*) FROM recyclebin_record WHERE file_id like'%1A11mp0pc00245005'"
sql3 = "SELECT trashed FROM recyclebin_record WHERE file_id like'%1A11mp0pc00245005'"
sql4 = "SELECT UPDATETIME FROM RCS_VIRDIR_MAP WHERE VIRDIRID='1A11mp0pc00245005'"
sql5 = "SELECT expire_time FROM recyclebin_record WHERE file_id like'%1A11mp0pc00245005'"
sql6 = "SELECT HOLDTIME FROM RCS_VIRDIR_MAP WHERE VIRDIRID='1A11mp0pc00245005'"

cur_NDMC1.execute(sql1)
cur_tidb.execute(sql2)
cur_tidb2.execute(sql3)
cur_tidb3.execute(sql5)
cur_NDMC1_2.execute(sql4)
cur_NDMC1_3.execute(sql6)
result = cur_NDMC1.fetchall()
res = cur_tidb.fetchall()
result2 = cur_tidb2.fetchall()
result4 = cur_tidb3.fetchall()
result3 = cur_NDMC1_2.fetchall()
result5 = cur_NDMC1_3.fetchall()

a = res[0]
b = result[0]
c = result2[0]
d = result3[0]
e = str(d[0])
f = result4[0]
print(f)
time_str = e
stuct_time = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
print(stuct_time)
timestap = time.mktime(stuct_time) * 1000
print(timestap, c[0])
g = c[0] + result5[0][0] * 24 * 3600 * 1000
print(g)
if a.__eq__(b):
    print('数据条数一致')
else:
    print("数据条数不一致")
if timestap == c[0]:
    print("时间戳转换一致")
else:
    print("时间戳转换有误")
if f[0] == g:
    print("expire_time字段正确")
else:
    print("expire_time字段计算错误")
time.sleep(10)
tidb.close()
