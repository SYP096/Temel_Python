from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()     # 可以查看现在的时间
simdi = datetime.today()   # 同 8 行

result = datetime.now()
print(result)    # 2023-08-19 17:10:33.044793
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)     # 和 now 有一点不太一样的是 顺序相反
print(result)    # Sat Aug 19 17:10:33 2023
result = datetime.strftime(simdi, '%Y')    # 查看simdi中的年份
result = datetime.strftime(simdi, '%X')
print(result)    # 17:11:17     时:分:秒
result = datetime.strftime(simdi, '%d')
print(result)      # 19 今天是19号
result = datetime.strftime(simdi, '%A')
result = datetime.strftime(simdi, '%B')
result = datetime.strftime(simdi, '%Y %B %A')     # 查看simdi中的年月日(其中日是周几的样式)
print(result)    # 2023 August Saturday
#  strftime 和 strptime 相反， 一个是查看日期中的某个元素， 一个是把一个字符串整合成日期
t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t,  '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983, 5, 9, 12, 30, 10)      # 使其整合成一个日期， 年月日时分秒
print(birthday)       # 1983-05-09 12:30:10
result = datetime.timestamp(birthday)  # saniye  时间截  返回的数据是秒
print(result)    # 421320610.0
result = datetime.fromtimestamp(result)  # saniye to datetime
print(result)    # 1983-05-09 12:30:10
result = datetime.fromtimestamp(0)   # 1970.01.01
print(result)      # 1970-01-01 03:00:00     最早的时间截就是这个日期

result = simdi - birthday  # timedelta   时间增减

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)
# 先导入datetime中的timedelta， 然后才能使用以下代码
# result = simdi + timedelta(days=10)    # 在simdi的时间基础上 加上十天
# result = simdi + timedelta(days=730,  minutes = 10)    # 加上730天10分钟

result = simdi - timedelta(days=10)

print(result)
