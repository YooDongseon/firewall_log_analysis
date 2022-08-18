import pymysql
import time
import ipaddress
import macaddress

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='mycompany', charset='utf8')
cur = conn.cursor()

attacker_mac = int(macaddress.MAC('f8:ff:c2:32:68:d2'))

sql = "SELECT * FROM firewall WHERE Source_MAC=%s"
cur.execute(sql, [attacker_mac])
result = cur.fetchall()


with open('Attacker_Access_log.txt', 'w', encoding='UTF-8') as f:
    for record in result:

        parse = list(record) 

        epoch_time= parse[0]
        time_formatted = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(epoch_time))

        src_ip = str(ipaddress.ip_address(parse[1]))
        src_mac = str(macaddress.MAC(parse[2])).replace("-", ":")
        src_port = str(parse[3])
        dst_ip = str(ipaddress.ip_address(parse[4]))
        dst_mac = str(macaddress.MAC(parse[5])).replace("-", ":")
        dst_port = str(parse[6])
        size = str(parse[7])
        
        f.write(time_formatted + " " + src_ip + " " + src_mac.lower() + " " + src_port + " " + dst_ip + " " + dst_mac + " " + dst_port + " " + size + '\n')

conn.close()