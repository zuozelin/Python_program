
# f = open('file')
# data = f.read()
# print(data.split('|'))

# f2 = open('file2')
## data2 = f2.read()
# i = 1
# for line in f2.readlines():
#     if i %2 == 1:
##   line.strip('\n') 为删除行的换行符
#         print(line.strip('\n'))
#     i += 1

# file3 = open('file3', encoding='GB18030')
## replace('\n','') 把换行符替换成空格
# print(f3.read().replace('\n',''))


# def func(filename):
#     print(open('filename').read())
#     print('test func')

# func('file')



import re
def find_item( hero ):
    with open('file',encoding='GB18030') as f:
        data = f.read().replace('\n','')
        name_num = re.findall(hero,data)
        print('主角 %s 出现 %s 次' %(hero, len(name_num)))
    return name_num

name_dict = {}
with open('file') as f:
    for line in f:
        names = line.split('|')
        for n in names:
#            print(n)
            name_num = find_item(n)
            name_dict[n] = name_num

name_sorted = sorted(name_dict.item(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])