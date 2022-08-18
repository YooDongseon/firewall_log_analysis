import pymysql
import ipaddress
import macaddress
import os

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='mycompany', charset='utf8')
cur = conn.cursor()

sql1 = "SELECT DISTINCT Source_IP FROM firewall"
cur.execute(sql1)
result = cur.fetchall()

with open('Source_IP.txt', 'w', encoding='UTF-8') as f:
    for record in result:
        a = str(ipaddress.ip_address(record[0]))
        f.write(a+'\n')

sql2 = "SELECT DISTINCT Source_MAC FROM firewall"
cur.execute(sql2)
result = cur.fetchall()

with open('Source_MAC.txt', 'w', encoding='UTF-8') as f:
    for record in result:
        a = str(macaddress.MAC(record[0])).replace("-", ":")
        f.write(a.lower()+'\n')
    
sql3 = "SELECT DISTINCT Destination_IP FROM firewall"
cur.execute(sql3)
result = cur.fetchall()

with open('Destination_IP.txt', 'w', encoding='UTF-8') as f:
    for record in result:
        a = str(ipaddress.ip_address(record[0]))
        f.write(a+'\n')

sql4 = "SELECT DISTINCT Destination_MAC FROM firewall"
cur.execute(sql4)
result = cur.fetchall()

with open('Destination_MAC.txt', 'w', encoding='UTF-8') as f:
    for record in result:
        a = str(macaddress.MAC(record[0])).replace("-", ":")
        f.write(a+'\n')

sql5 = "SELECT DISTINCT Destination_PORT FROM firewall"
cur.execute(sql5)
result = cur.fetchall()

with open('Destination_PORT.txt', 'w', encoding='UTF-8') as f:
    for record in result:
        a = str(record[0])
        f.write(a+'\n')

conn.close()

os.system('grep -v -f EMPLOYEE_IP.txt Source_IP.txt > UNKNOWN_Src_IP.txt')
os.system('grep -v -f EMPLOYEE_MAC.txt Source_MAC.txt > UNKNOWN_Src_MAC.txt')
os.system('grep -v -f SERVER_IP.txt Destination_IP.txt > UNKNOWN_Dst_IP.txt')
os.system('grep -v -f SERVER_MAC.txt Destination_MAC.txt > UNKNOWN_Dst_MAC.txt')
os.system('grep -v -f SERVER_PORT.txt Destination_PORT.txt  > UNKNOWN_Dst_PORT.txt')