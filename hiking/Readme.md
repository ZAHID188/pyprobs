```

'''The program shall provide a terminal where the user can input the 
        (i) name of a trip/mountain, 
        (ii) the length of the trip in kilometers, and 
        (iii) the vertical climb of the trip in total. 
The program must accept multiple hikes to be registered.

The program shall provide a report upon the input “END” that prints all the
trips, as well as the combined length and height of the trips.'''


# Dictionary for the temporary storage
temporaryDictMemory=dict()
while(True):
    tripName=input('name of a trip/mountain: \t')
    if tripName =='END':
        print('Program Ended')
        break
    try:
        length=float(input('length of the trip in kilometers: \t'))
        VerticalLength=float(input('vertical climb of the trip in kilometers: \t'))
        if(type(length)==float and type(VerticalLength)==float):
            temporaryDictMemory[tripName]=[length,VerticalLength]

    except:
        print("length in kilometer should be in decimal(Ex: 14.4)")
    
print("----------------------------------------------------------------------------------------")
print("{1:<30}{0:^20}{2:>30}".format('length', 'Trip Name', 'Vertical climb'))

print("----------------------------------------------------------------------------------------")
totalength=0
totalVerticalLength=0
# From the temporary memory key values are iterated
# using index we grab the value from the list 
for tripName,dataValues in temporaryDictMemory.items():
    print("{1:<30}{0:^20}{2:>30}".format(str(dataValues[0])+'km',tripName, str(dataValues[1])+'km'))
    totalength=totalength+dataValues[0]
    totalVerticalLength=totalVerticalLength+dataValues[1]
print("-----------------------------------------------------------------------------------------")
print("{1:<30}{0:^20}{2:>30}".format(str(totalength)+'km', 'Total-', str(totalVerticalLength)+'km'))

print("----------------------------------------------------------------------------------------")
print('Combined length and height of the trips:\t'+str(totalength+totalVerticalLength)+'km')



```