lst = '127.0.0.1 www.javatpoint.com,127.0.0.1 www.facebook.com'
lst_temp = lst.split(',')
print(lst_temp)
fp = open('test.txt','r+')
lines = fp.readlines()
print(lines)
word = '127.0.0.1 www.facebook.com'
if word in lst_temp:
    print(word)
