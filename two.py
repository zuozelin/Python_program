# 记录生肖，根据年份来判断生肖

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

#print (chinese_zodiac[0:4])
#print (chinese_zodiac[-1])

year = 2019
a = year % 12
print(chinese_zodiac[a+8])

#print('狗' not in chinese_zodiac)

#print(chinese_zodiac + chinese_zodiac)

#print(chinese_zodiac * 3)

# 星座
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (2, 15)

zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
#print(zodiac_day)
zodiac_len= len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])



# 列表
a_list = ['abc', 'xyz']
a_list.append('X')
print(a_list)
a_list.remove('xyz')
print(a_list)
a_list.remove('X')
print(a_list)