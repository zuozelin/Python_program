#

x = 'abc'
if x == 'abc' :
    print('x的值与abc相等')
else:
    print('x的值与abc不相等')

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# year = int(input('请用户输入出生年份'))

# print(chinese_zodiac[(year % 12)-4])

# if(chinese_zodiac[(year % 12)-4]) == '狗' :
#    print('狗年运势...')

#for cz in chinese_zodiac:
#    print(cz)

#for i in range(13):
#    print(i)

#for year in range(2000, 2020):
#    print('%s年的生肖是 %s' %(year, chinese_zodiac[(year % 12)-4]))

#num = 5
#while True:
#    print('a')
#    num = num + 1
#    if num >= 10:
#        break

import time
num = 5
while True:
    num = num + 1


    print(num)
    time.sleep(1)