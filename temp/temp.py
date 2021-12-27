# my changes3
'''
[['Roxane', 'Campain', 'Rapid Trading Intl', '1048 Main St', 'Fairbanks', 'Fairbanks North Star', 'AK', '99708', '907-231-4722', '907-335-6568', 'roxane@hotmail.com'], ['Lavera', 'Perin', 'Abc Enterprises Inc', '678 3rd Ave', 'Miami', 'Miami-Dade', 'FL', '33196', '305-606-7291', '305-995-2078', 'lperin@perin.org'], ['Erick', 'Ferencz', 'Cindy Turner Associates', '20 S Babcock St', 'Fairbanks', 'Fairbanks North Star', 'AK', '99712', '907-741-1044', '907-227-6777', 'erick.ferencz@aol.com'], ['Fatima', 'Saylors', 'Stanton, James D Esq', '2 Lighthouse Ave', 'Hopkins', 'Hennepin', 'MN', '55343', '952-768-2416', '952-479-2375', 'fsaylors@saylors.org'], ['Jina', 'Briddick', 'Grace Pastries Inc', '38938 Park Blvd', 'Boston',
'Suffolk', 'MA', '2128', '617-399-5124', '617-997-5771', 'jina_briddick@briddick.com'], ['Kanisha', 'Waycott', 'Schroer, Gene E Esq', '5 Tomahawk Dr', 'Los Angeles', 'Los Angeles', 'CA', '90006', '323-453-2780', '323-315-7314', 'kanisha_waycott@yahoo.com'], ['Emerson', 'Bowley', 'Knights Inn', '762 S Main St', 'Madison', 'Dane', 'WI', '53711', '608-336-7444', '608-658-7940', 'emerson.bowley@bowley.org'], ['Blair', 'Malet', 'Bollinger Mach Shp & Shipyard', '209 Decker Dr', 'Philadelphia', 'Philadelphia', 'PA', '19132', '215-907-9111', '215-794-4519', 'bmalet@yahoo.com']]


'''


# import csv
# filename = '50-contacts.csv'
# x=list()
# with open(filename, 'r') as data:
#     reader = csv.reader(data)
#     for item in reader:
#             x.append(item)
# print(x)
    








# my changes2
'''

output:
first_name Blair
last_name Malet
company_name Bollinger Mach Shp & Shipyar
address 209 Decker Dr
city Philadelphia
county Philadelphia
state PA
zip 19132
phone1 215-907-9111
phone 215-794-4519
email bmalet@yahoo.com

'''

# import csv 
# filename ="50-contacts.csv"
# x=list()
# with open(filename, 'r') as data:
      
#     for line in csv.DictReader(data):
#         print("\n")
#         for k,v in line.items():
#                 print("%s = %s"%(k,v))
            



# my changes

# import csv 
# filename ="50-contacts.csv"
# x=list()
# with open(filename, 'r') as data:
      
#     for line in csv.DictReader(data):
#         x.append(line['first_name'])
#         # print(line['first_name'])
#         # x={line}

# print(x)








#list
# import csv
# file="50-contacts.csv"

# with open(file, newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         # print(', '.join(row))
#         print(', ',row)

#list

# import csv, sys
# filename = '50-contacts.csv'
# with open(filename, newline='') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print(row)
#     except csv.Error as e:
#         sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))



#dictionary

# import csv 
# filename ="50-contacts.csv"
# # opening the file using "with" 
# # statement
# with open(filename, 'r') as data:
      
#     for line in csv.DictReader(data):
#         print(line)
        
        


   

# mak=['From', 'stephen.marquard@uct.ac.za', 'Fri', 'Jan', '4', '04:07:34', '2008']
# mak2=['From:', 'gopal.ramasammycook@gmail.com']
# print(len(mak2))

# stuff = dict()
# print(stuff.get('candy',4))



import pandas as pd
import matplotlib.pyplot as plt
scores = pd.read_excel('score.xlsx')
x=scores.boxplot(color="r")
# x=scores.iloc[1:2]
# x=scores.English
# print(x)
# plt.show()
