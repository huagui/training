#-*-coding:utf-8-*- 
import MySQLdb
import socket

HOST = 'localhost'
USER = 'root'
PASSWD = '' #4c1fadc64b
if socket.gethostname()=='iZ94zoeilgyZ':
    PASSWD = '4c1fadc64b' #4c1fadc64b
PORT = 3306
DBNAME = 'training'
# DBNAME = 'test'


socket = "/tmp/mysql.sock"
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def connect_mysql():
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWD,port=PORT,unix_socket=socket, charset="utf8")
        conn.select_db(DBNAME)
        return conn
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
     
def get_id_list(id):
    bin_str = bin(id).replace('0b','')
    id_list = []
    for i, item in enumerate(reversed(bin_str)):
        if item == '1':
            id_list.append(i)
    return id_list


if __name__ == "__main__":
    pass
    # update(1, "192.168.255.255", 1234)
    #delete(5)

    #send_to_device("d0:10:00:0","start")
    #create(5,"huagui","falkdjf", '192.168.121.215', 55552,time.strftime(TIMEFORMAT, time.localtime()))
    #update(5,'192.168.121.220', 12354,time.strftime(TIMEFORMAT, time.localtime()))
