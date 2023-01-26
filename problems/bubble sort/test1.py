'''
1.  all input from the users  ---- Done
2.  make a list of all the input -- Done
4.  find the ending position(EP) and the position before the ending position (BEP) .  --Done
5.  check the BEP is smaller then EP or not .
6.  if BEP is smaller then EP Go to 9--x=0 
7.  if BEP is not smaller then Ep Then go to 8  
8.  exchange position: EP value in BEP position value and BEP value in EP position x=1
9.  Go to before 1 postion for both EP and BEP.
10. go to 5-6   
11. if BEP pointer position is 0 then go to 4
12. 
'''

'''
BUGS:
1. If user input using ',' and ' ' together
2. if user input same number twice
'''

# from itertools import groupby
# def all_equal(iterable): 
#     g = groupby(iterable)
#     return next(g, True) and not next(g, False)

unsortedlist=['4','3','1','40','11','7','9']
# userIput=input("Insert the numbers with space : ")
# userIput=userIput.strip()
# unsortedlist=userIput.split(' ')
print(unsortedlist)
EP=unsortedlist[-1]
BEP=unsortedlist[-2]
if(BEP<EP):
    print('BEP is smaller')
else:
    print('EP is smaller')

