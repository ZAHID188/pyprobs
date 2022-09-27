name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mails={}
for line in handle:
    if line.startswith("From") :  # find the line what begins with from
        words=line.split()        # insert them in a list
        
        if words[1] not in mails and len(words)>3:  # insert into a dictionary
            mails[words[1]]=1
            # print(words)
   
            
        elif len(words)>3:
            mails[words[1]]+=1
            # print(words)
       
# print(mails)
largest=0
for mail in mails:
    if mails[mail]>largest:
        largest=mails[mail]
        x=mail,largest
    
    
#
print(x[0],x[1])
