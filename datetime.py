#date time related all things

import datetime
today=datetime.datetime.today()


print(today.strftime("%a")) #day in short
print(today.strftime("%A"))  #day

print(today.strftime("%b"))  #month in short
print(today.strftime("%B"))  #month

print(today.strftime("%c"))  #day date time year
print(today.strftime("%C"))  #20

print(today.strftime("%d"))  #day of month
print(today.strftime("%D"))  #date: 09/22/19

print(today.strftime("%e"))  #day of month

print(today.strftime("%f"))  #ip address
print(today.strftime("%F"))  #date: 2019-09-22

print(today.strftime("%G"))  #year
print(today.strftime("%g"))  #year in short

print(today.strftime("%h"))  #month
print(today.strftime("%H"))  #hour

print(today.strftime("%I"))  #hour number after 12 pm: 16->4

print(today.strftime("%j")) #day of year

print(today.strftime("%m"))  #month no
print(today.strftime("%M"))  #minute

print(today.strftime("%n")) #space of 2 line


print(today.strftime("%p")) #pm/am


print(today.strftime("%r")) # total time
print(today.strftime("%R")) #hour & minute

print(today.strftime("%S")) #second

print(today.strftime("%t")) #one line space
print(today.strftime("%T")) # hour min & sec

print(today.strftime("%u")) #7
print(today.strftime("%U")) #week no of year

print(today.strftime("%V")) #week no of year

print(today.strftime("%w")) #0
print(today.strftime("%W")) #37

print(today.strftime("%x")) #total date: 09/22/19

print(today.strftime("%y")) #year in short
print(today.strftime("%Y")) #year

print(today.strftime("%z")) #one line space
print(today.strftime("%Z")) #one line space



