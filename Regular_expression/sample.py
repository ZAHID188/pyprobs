
''' With regular expression 2
input::
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

output:
    uct.ac.za
'''

# import re 
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('^From .*@([^ ]*)',lin)
# print(y)




''' With regular expression 2
input::
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

output:
    uct.ac.za
'''

# import re 
# lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)',lin)
# print(y)



''' without regular expression 2
input::
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

output:
    uct.ac.za
'''
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# words = data.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])




''' without regular expression 1
input::
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

output:
    uct.ac.za
'''

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos)
# sppos = data.find(' ',atpos)
# print(sppos)

# host = data[atpos+1 : sppos]
# print(host)



'''
input::
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

output:
    ['From stephen.marquard@uct.ac.za']
    ['stephen.marquard@uct.ac.za']
'''

# import re
# x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y=re.findall('From \S+@\S+',x)   # string with non-blank charecter on both side 
# z=re.findall('From (\S+@\S+)',x)   # string with non-blank charecter on both side 
# print(y)
# print(z)



'''
input::
'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

output:
    ['stephen.marquard@uct.ac.za']
'''

# import re
# x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y=re.findall('\S+@\S+',x)   # string with non-blank charecter on both side 

# print(y)



'''
input::
'From: Using the : character'

output:
    ['From: Using the :']
    ['From:']
'''


# import re
# x='From: Using the : character'
# y=re.findall('^F.+:',x)  # greedy match
# z=re.findall('^F.+?:',x) # non-greedy match

# print(y)
# print(z)





'''
classic way
'''
# fhand = open('mbox-short.txt')

# for line in fhand:
#     words = line.rstrip()
#     if line.find('From')>=0:
#         print(words)


'''
using regular expression

'''
# import re 

# fhand = open('mbox-short.txt')

# for line in fhand:
#     words = line.rstrip()
#     if re.search('From:',words):
#         print(words)

#     # in classic we used line.startswith its same in RE as ^
#     elif re.search('^From',words):   
#         print("line starts with from")

    
'''

input::
'My 2 favourite numbers Are  19 and 42'

output:
    ['2', '1', '9', '4', '2']
    ['2', '19', '42']
    ['A']
'''

# import re
# x='My 2 favourite numbers Are  19 and 42'
# y=re.findall('[0-9]',x)
# z=re.findall('[0-9]+',x)

# st=re.findall('[AEIOU]+',x)


# print(y)
# print(z)
# print(st)


      

import re
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    # if re.search('^From:',line):
    # if re.search('^X.*:',line):
    if re.search('^X-\S+:',line):
        print(line)


