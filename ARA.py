import sys
import os
import time
import socket
import random
#kode dibawah jangan diubah
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#batas awal
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#batas akhir
#awal program
os.system("clear")
os.system("figlet Report Akun")
print
print "-----------------------------]"
print "Author    : Hans Hax"
print "Contact me: +6287850013150"
print "Thanks To : HansHaX"
print "-----------------------------]"
print "Peringatan! apapun yang terjadi, author tidak bertanggung jawab"
print
akun = raw_input("Akun Target                         : ")
report = input("Berapa Report Yang ingin  Dikirim   : ")
#proses
os.system("clear")
print "Sedang Mengunci Target"
time.sleep(2)
print "[                    ] 0% "
time.sleep(5)
print "[=                   ] 10% "
time.sleep(9)
print "[=====               ] 25%"
time.sleep(8)
print "[==========          ] 50%"
time.sleep(10)
print "[===============     ] 75%"
time.sleep(9)
print "[====================] 100%"
time.sleep(3)
print "Berhasil Mengunci Target"
time.sleep(2)
print "mengirim sms ke Target"
time.sleep(2)
#looping
sent = 0
while True:
     sent = sent + 1
     report = report + 1
     print "Mengirim  %s report ke %s dengan jumlah report:%s"%(sent,akun,report)                                          if report == 65534:
       report = 1
#selesai
