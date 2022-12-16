#计算机的时间从1970-1-1 的 00:00:00开始 以千分之一秒计算。我们吧1970这个时刻称为“unix时间点”
import time


t =  time.time()
print(t)

#打印出目前的日期
#计算距离1970/1/1一共有多少天
total_days= t/(60*60*24)
print(total_days)

#假定一年365天，查询假定年份
y_suppose =  1970+t/(60*60*24*365)
print(y_suppose)

#计算从假定年份的前一年开始到1970年一共又多少闰年
leap_count = 0
for i in range(1970,int(y_suppose)):
    if(i%100 == 0):
        if(i%400 == 0):
           # print(i)
            leap_count += 1
    else:
        if i % 4 == 0:
            #print(i)
            leap_count += 1
print(leap_count)#该值为在今年前一年到1970年有多了多少天
#每有一个闰年从假定年份中减去1/365
year = y_suppose - (leap_count/365)
#打印出年份
print(int(year))

#打印出现在离开今年的1月1日 0点0分过了多少天
#但是我们要的是号数 所以要加1
days_in_this_year =  total_days - ((int(year)-1970)*365+leap_count) + 1
print(days_in_this_year)

dayf= 28
if(int(year)%100 == 0):
        if(int(year)%400 == 0):
            dayf  = 29
else:
        if int(year) % 4 == 0:
            dayf = 29


m_days=[31,dayf,31,30,31,30,31,31,30,31,30,31]

int_day = int(days_in_this_year)
print(int_day)
mouth_count = 1
#for i in range(12):
 #   print(m_days[i])

for i in range(12):
    if int_day - m_days[i] > 0:
        int_day -= m_days[i]
        mouth_count +=1

print(mouth_count)

duplicate_days = days_in_this_year
for i in range (mouth_count-1):
    days_in_this_year -= m_days[i]

print(days_in_this_year)

day = int(days_in_this_year)
print(day)
today_passed = days_in_this_year-int(days_in_this_year)
print(today_passed)
hours = today_passed*24
print(hours)
minutes = (hours-int(hours))*60
print(minutes)
seconds = (minutes-int(minutes))*60
print(seconds)

report = '现在是{0}时间时{1}年{2}月{3}日{4}时{5}分{6}秒'
report_utc = report.format('utc',int(year),mouth_count,int(day),int(hours),(int(minutes)),int(seconds))
report_cn = report.format('中国',int(year),mouth_count,int(day),int(hours)+8,(int(minutes)),int(seconds))
report_jp = report.format('日本',int(year),mouth_count,int(day),int(hours)+9,(int(minutes)),int(seconds))

print(report_utc)
print(report_cn)
print(report_jp)


