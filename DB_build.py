import pymysql
import ipaddress
import macaddress
from datetime import datetime
from datetime import timedelta
import time

conn = pymysql.connect(host='127.0.0.1', user='....', password='....', db='mycompany', charset='utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE firewall(Access_Time BIGINT, Source_IP BIGINT, Source_MAC BIGINT, Source_PORT INT,\
Destination_IP BIGINT, Destination_MAC BIGINT, Destination_PORT INT, Size BIGINT)") # DB TABLE 최초 생성

sql = "insert into firewall(Access_Time, Source_IP, Source_MAC, Source_PORT, Destination_IP, Destination_MAC, Destination_PORT, Size)\
    values (%s, %s, %s, %s, %s, %s, %s, %s)"

logfile_path = '01.txt' # 01.txt ~ 20.txt 차례로 DB에 삽입

count = 0
count2 = 0
db_list = []
with open(logfile_path, 'r') as f:
    for line in f:

        count += 1
   
        log_parse = line.split(' ')

        date = log_parse[0] + " " + log_parse[1] + " " + log_parse[2] + " " + log_parse[3] + " " + log_parse[4]
        epoch_time = (time.mktime((datetime.strptime(date, '%a %b %d %H:%M:%S %Y') + timedelta(hours=9)).timetuple())) # Timestamp -> epochtime / UTC(+09:00)
        epoch_time = int(epoch_time)
        src_ip = int(ipaddress.IPv4Address(log_parse[5])) # IP-> INT
        src_mac = int(macaddress.MAC(log_parse[6])) # MAC -> INT
        src_port = int(log_parse[7])
        dst_ip = int(ipaddress.IPv4Address(log_parse[8])) # IP -> INT
        dst_mac = int(macaddress.MAC(log_parse[9])) # MAC -> INT
        dst_port = int(log_parse[10])
        size = int(log_parse[11])

        # for executemany
        db_list.append([])
        db_list[count-1].append(epoch_time)
        db_list[count-1].append(src_ip)
        db_list[count-1].append(src_mac)
        db_list[count-1].append(src_port)
        db_list[count-1].append(dst_ip)
        db_list[count-1].append(dst_mac)
        db_list[count-1].append(dst_port)
        db_list[count-1].append(size)
        
        if count % 1000000 == 0:
            count2 += 1
            print(count2)
            cur.executemany(sql, db_list)
            conn.commit()
            print(count)
            db_list = []
            count = 0
            
conn.close()
f.close()