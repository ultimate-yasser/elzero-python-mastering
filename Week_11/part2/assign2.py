import datetime

ctime = datetime.datetime(2004, 5, 30)

format1 = ctime.strftime('%Y-%m-%d')
format2 = ctime.strftime('%b %d, %Y')
format3 = ctime.strftime('%d - %b - %Y')
format4 = ctime.strftime('%d / %b / %y')
format5 = ctime.strftime('%d / %b / %Y')
format6 = ctime.strftime('%a, %d %B %Y')

print(format1, format2, format3, format4, format5, format6, sep='\n')