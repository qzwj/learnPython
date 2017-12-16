#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
from datetime import datetime

# 获取当前日期
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2016, 8, 28, 12, 30, 25)
print(dt)
print(type(dt))


# datetime转timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

print('timestamp =',dt.timestamp())
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

# timestamp转datetime
a = dt.timestamp()
print(datetime.fromtimestamp(a)) #本地时间
print(datetime.utcfromtimestamp(a)) #UTC时间, 标准时间


#str 转datetime
cday = datetime.strptime('2015-6-1 18:19:48', '%Y-%m-%d %H:%M:%S')
print(cday)


#datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import timedelta
print(now + timedelta(hours = 10)) #在now时间 加10个小时
print(now - timedelta(days = 1)) # 在now时间 减少1天
print(now + timedelta(days = 2, hours = 12)) #同时进行


# 本地时间转UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours = 8)) #创建市区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) #强制设置为UTC+8:00
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
time1 = datetime(2015,5,18,17,2,10,871012, tzinfo=timezone(timedelta(0,28800)))
print(time1)


# 时区转换 utcnow()
# 拿到UTC时间, 并且强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
print(type(utc_dt))
# astimezone() 转换时区为北京时间UTC+8:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
print(type(bj_dt))
# 东京时间UTC+9:00
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 将北京时间转为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。


# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。


