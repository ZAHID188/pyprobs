# finding a data 
# from zahidprantakg@yangzhou.com  he is a really good guy.

data="from zahidprantakg@yangzhou.com  he is a really good guy."
atpos=data.find('@')
print(atpos)
second_pos=data.find(' ',atpos) #it will search a space after the @
print(second_pos)
host=data[atpos:second_pos]
host1=data[atpos+1:second_pos]

print(host)
print(host1)




