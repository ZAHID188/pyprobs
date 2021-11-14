# Add sequence number 1, 2, 3, … to the strings in file
# companies.txt, and write into another file scompanies.txt  


# for example this xxx.txt has some text inside it 
# now i have to add 1,2,3,4 in the begining of every line
# and save it with a new file xxx_serial.txt 

with open("xxx.txt") as f:
    line=f.readlines()

for i in range(len(line)):
    line[i]=str(i+1)+'. '+line[i]
    print(line[i])
with open("xxx_serial.txt","w") as f2:
    f2.writelines(line)