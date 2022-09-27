# xfile=open('info.txt')
# txt=xfile.read()

# print("Total text:",len(txt))
# print("Text: \n", txt)

# hi=txt.find("Date")
# print("\n after ICT::",txt[hi+4:])



#search throgh file





# #with newline
# print("with newline")
# xfile=open('info.txt')
# for line in xfile:
#     if line.startswith('From:'):
#         print(line)


# # without newline
# print("without newline")
# xfile=open('info.txt')
# for line in xfile:
#     line=line.rstrip()  # now this line variable is no longer has the newline(\n) at the end of it.
#     if line.startswith('From:'):
#         print(line)


# #skipping with the continue
# xfile=open('info.txt')
# for line in xfile:
#     line=line.rstrip() 
#     if not line.startswith('From:'):   # Skip 'uninteresting lines'
#         continue
#     print(line)    # Process our 'interesting' line



#using in to select the lines
xfile=open('info.txt')
for line in xfile:
    line=line.rstrip() 
    if not 'uct.ac.za' in line: 
        continue
    print(line)




