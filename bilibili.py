# # Get the name of the file and open it
# name = input('Enter file:')
# handle = open(name, 'r')

# # Count word frequency 
# counts = dict()
# for line in handle:
#   words = line.split()
#   for word in words:
#     counts[word] = counts.get(word,0)+1

# # Find the most common word
# bigcount = None
# bigword = None
# for word,count in counts.item():
#   if bigcount is None or count > bigcount:
#     bigword = word
#     bigcount = count

# # All done
# print(bigword, bigcount)

# print('hello')

# nzt = input('Enter your name: ')
# print('Hello',nzt)

# xh = input("Enter Hours: ")
# xr = input("Enter Rate: ")
# xp = float(xh) * float(xr)
# print("pay:",xp)

# x=5
# if x == 5:
#   print('Is 5')
#   print('Is still 5')
#   print('Third 5')
# print('Afterwards 5')
# print('Before 6')
# if x == 6:
#   print('Is 6')
#   print('Is still 6')
#   print('Third 6')
# print('Afterwards 6')

# x = 5
# if x > 2:
#   print('Bigger than 2')
#   print('Still bigger')
# print('Done with 2')

# for i in range(5):
#   print(i)
#   if i > 2:
#     print('Bigger than 2')
#   print('Done with i', i)
# print('All done')

# x = 42
# if x > 1:
#   print('More than one')
#   if x < 100:
#     print('Less than 100')
# print('All done')

# x = 4
# if x < 2:
#   print('Bigger')
# else:
#   print('Smaller')
# print('All done')


# for x in range(12):
#   print(x)
#   if x < 2:
#     print('Small')
#   elif x < 10:
#     print('Medium')
#   else :
#     print('Large')
# print('All done')

# astr = 'Hello Bob'
# try:
#   istr = int(astr)
# except:
#   istr = -1
# print('First', istr)
# astr = '123'
# try:
#   istr = int(astr)
# except:
#   istr = -1
# print('Second', istr)

# astr = 'Bob'
# try:
#   print('Hello')
#   istr = int(astr)
#   print('There')
# except:
#   istr = -1
# print('Done', istr)

# rawstr = input('Enter a number')
# try:
#   ival = int(rawstr)
# except:
#   ival = -1
# if ival > 0:
#   print('Nice work')
# else:
#   print('Not a number')

# sh = input('Enter Hours: ')
# sr = input('Enter Rate: ')
# fh = float(sh)
# fr = float(sr)
# print(fh, fr)
# xp = fh * fr
# print("pay:",xp)

# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# fh = float(sh)
# fr = float(sr)
# if fh > 40:
#   print("Overtime")
#   reg = fr * fh
#   otp = (fh - 40) * (fr * 1.5)
#   xp = reg + otp
# else:
#   print("Regular")
#   xp = fh + fr
# print("Pay:",xp)

# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# try:
#   fh = float(sh)
#   fr = float(sr)
# except:
#   print("Error, please enter numeric input")
#   quit()
# print(fh, fr)
# if fh > 40:
#   reg = fr * fh
#   otp = (fh - 40.0) * (fr * 1.5)
#   xp = reg + otp
# else:
#   xp = fh * fr
# print("Pay:", xp)

# def thing():
#   print('Hello')
#   print('Fun')
# thing()
# print('Zip')
# thing()

# big = max('Hello world')
# print(big)
# tiny = min('Hello world')
# print(tiny)

# def print_lyrics():
#   print("I'm a lumberjack, and I'm okay.")
#   print("I sleep all night and I work all day.")
# print_lyrics()

# def greet(lang):
#   if lang == 'es':
#     print('Hola')
#   elif lang == 'fr':
#     print('Bonjour')
#   else :
#     print('Hello')
# greet('en')
# greet('es')
# greet('fr')

# def greet():
#   return "Hello"
# print(greet(), "Glenn")
# print(greet(), "Sally")

# def greet(lang):
#   if lang == 'es':
#     return 'Hola'
#   elif lang == 'fr':
#     return 'Bonjour'
#   else:
#     return 'Hello'
# print(greet('en'), "Glenn")
# print(greet('fr'), "Sally")
# print(greet('es'), "Michael")

# def addtwo(a,b):
#   added = a + b
#   return added
# x = addtwo(3,5)
# print(x)

# def computepay(hours, rate):
#   print("In computepay", hours, rate)
# sh = input("Enter Hours:")
# sr = input("Enter Rate:")
# fh = float(sh)
# fr = float(sr)
# computepay(fh,fr)
# if fh > 40:
#   reg = fr * fh
#   otp = (fh - 40.0)*(fr * 0.5)
#   xp = reg + otp
# else:
#   xp = fh * fr
# print("Pay:",xp)

# def computepay(hours, rate):
#   print("In computepay", hours, rate)
#   if hours > 40:
#     reg = rate * hours
#     otp = (hours - 40.0)*(rate * 0.5)
#     pay = reg + otp
#   else :
#     pay = reg + otp
#   print("Returing",pay)
#   return pay
# sh = input("Enter Hours:")
# sr = input("Enter Rate:")
# fh = float(sh)
# fr = float(sr)
# xp = computepay(fh,fr)
# print("Pay:",xp)

# n=5
# while n >0:
#   print(n)
#   n = n-1
# print('Blastoff!')
# print(n)

# while True:
#   line = input('>')
#   if line == 'done':
#     break
#   print(line)
# print('Done!')

# while True:
#   line = input('>')
#   if line[0] == '#':
#     continue
#   if line =='done':
#     break
#   print(line)
# print('Done!')

# for i in [5,4,3,2,1]:
#   print(i)
# print('Blastoff!')

# friends = ['Joseph','Glenn','Sally']
# for friend in friends:
#   print('Happy New Year:',friend)
# print('Done!')

# print('Before')
# for thing in [9,41,12,3,74,15]:
#   print(thing)
# print('After')

# largest_so_far = -1
# print('Before',largest_so_far)
# for the_num in [9,41,12,3,74,15]:
#   if the_num > largest_so_far:
#     largest_so_far = the_num
#   print(largest_so_far, the_num)
# print('After', largest_so_far)

# zork = 0
# print('Before', zork)
# for thing in [9,41,12,3,74,15]:
#   zork = zork + 1
#   print(zork, thing)
# print('After', zork)

# zork = 0
# print('Before', zork)
# for thing in [9,41,12,3,74,15]:
#   zork = zork + thing
#   print(zork, thing)
# print('After', zork)

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [9,41,12,3,74,15]:
#   count = count+1
#   sum = sum + value
#   print(count, sum, value)
# print('After', count, sum, sum/count)

# print('Before')
# for value in [9,41,12,3,74,15]:
#   if value > 20:
#     print('Large number',value)
# print('After')

# found = False
# print('Before', found)
# for value in [9,41,12,3,74,15]:
#   if value == 3:
#     found = True
#   print(found, value)
# print('After',found)

# smallest_so_far = -1
# print('Before', smallest_so_far)
# for the_num in [9,41,12,3,74,15]:
#   if the_num < smallest_so_far:
#     smallest_so_far = the_num
#   print(smallest_so_far, the_num)
# print('After', smallest_so_far)

# smallest = None
# print('Before')
# for value in [9,41,12,3,74,15]:
#   if smallest is None:
#     smallest = value
#   elif value < smallest:
#     smallest = value
#   print(smallest,value)
# print('After', smallest)

# num = 0
# tot = 0
# while True :
#   sval = input('Enter a number:')
#   if sval == 'done' :
#     break
#   try:
#     fval = float(sval)
#   except:
#     print('Invalid input')
#     quit()
#   fval = float(sval)
#   print(fval)
#   num = num +1
#   tot = tot +fval
# print('ALL DONE')
# print(tot,num,tot/num)

# a = '10'
# print(int(a))

# fruit = 'banana'
# letter = fruit[1]
# print(letter)

# fruit = 'banana'
# x = 3
# w = fruit[x - 1]
# print(w)

# fruit = 'banana'
# print(len(fruit))

# fruit = 'banana'
# index = 0
# while index < len(fruit):
#   letter = fruit[index]
#   print(index, letter)
#   index = index + 1

# fruit = 'banana'
# for letter in fruit:
#   print(letter)

# word = 'banana'
# count = 0
# for letter in word:
#   if letter == 'a':
#     count = count + 1
# print(count)

# s = 'Monty Python'
# print(s[0:4])
# print(s[6:7])
# print(s[7:7])
# print(s[6:20])

# s = 'Monty Python'
# print(s[:2])
# print(s[8:])
# print(s[:])

# a = 'Hello'
# b = a + 'There'
# print(b)
# c = a + ' ' + 'There'
# print(c)

# fruit = 'banana'
# a = 'n' in fruit
# print(a)
# b = "m" in fruit
# print(b)

# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)
# print(greet)
# print('Hi There'.lower())

# fruit = 'banana'
# pos = fruit.find('na')
# print(pos)
# aa = fruit.find('z')
# print(aa)

# greet = 'Hello Bob'
# nnn = greet.upper()
# print(nnn)
# www = greet.lower()
# print(www)

# greet = 'Hello Bob'
# nstr = greet.replace('Bob','Jane')
# print(nstr)
# nstr = greet.replace('o','X')
# print(nstr)

# greet = '  Hello Bob  '
# a = greet.lstrip()
# print(a)
# b = greet.rstrip()
# print(b)
# c = greet.strip()
# print(c)

# line = 'Please have a nice day'
# a = line.startswith('Please')
# print(a)
# b = line.startswith('p')
# print(b)

# line = 'Please have a nice day'
# a = line.startswith('P')
# print(a)

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos)
# sppos = data.find(' ',atpos)
# print(sppos)
# host = data[atpos+1 : sppos]
# print(host)

