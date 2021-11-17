>''' input :   cheseses= ['Cheddar', 'Edam', 'Gouda']
>              numbers = [123,23,34,343,234,234,123]
>
>    Output::
>               ['Cheddar', 'Edam', 'Gouda','[123,23,34,343,234,234,123]']
>               []
>               [['zahid', 123, 455, '123123zahid', 12.33]]
>
>            
> '''


<br>cheseses= ['Cheddar', 'Edam', 'Gouda']   
<br>numbers = [123,23,34,343,234,234,123]
<br>
<br>
<br>for i in range(len(cheseses)):
<br>    if cheseses[i]=="Edam":
<br>        cheseses.append(numbers)
<br>
<br>print(cheseses)
<br>del cheseses[0:]
<br>print(cheseses)
<br>num=["zahid",123,455,"123123zahid",12.33]
<br>cheseses.append(num)
<br>print(cheseses)









''' input :   cheseses= ['Cheddar', 'Edam', 'Gouda']
              numbers = [123,23,34,343,234,234,123]
Output::
               ['Cheddar', 'Edam', 'Gouda','[123,23,34,343,234,234,123]']

            
 '''
# cheseses= ['Cheddar', 'Edam', 'Gouda']
# numbers = [123,23,34,343,234,234,123]


# for i in range(len(cheseses)):
#     if cheseses[i]=="Edam":
#         cheseses.extend(numbers)

# print(cheseses)
        








''' input :   cheseses= ['Cheddar', 'Edam', 'Gouda']
              numbers = [123,23,34,343,234,234,123]
Output::
               ['Cheddar', '[123,23,34,343,234,234,123]', 'Gouda']

            
 '''
# cheseses= ['Cheddar', 'Edam', 'Gouda']
# numbers = [123,23,34,343,234,234,123]


# for i in range(len(cheseses)):
#     if cheseses[i]=="Edam":
#         cheseses[i]=numbers

# print(cheseses)
        






''' input : cheseses= []
Output::
            
 '''
# cheeses = []
# for i in cheeses:
#     print(i)




''' input : cheseses= ['Cheddar', 'Edam', 'Gouda']
Output::
            CheddarCheddarCheddarCheddar 
            EdamEdamEdamEdam 
             GoudaGoudaGoudaGouda

 '''
# cheeses = ['Cheddar', 'Edam', 'Gouda']

# for word in range(len(cheeses)):
#     cheeses[word]=cheeses[word]*4

# for i in cheeses:
#     print(i)






''' input : cheseses= ['Cheddar', 'Edam', 'Gouda']
Output::
            ['CheddarCheddarCheddarCheddar', 'EdamEdamEdamEdam', 'GoudaGoudaGoudaGouda']
 '''
# cheeses = ['Cheddar', 'Edam', 'Gouda']

# for word in range(len(cheeses)):
#     cheeses[word]=cheeses[word]*4

# print(cheeses)





''' input : cheseses= ['Cheddar', 'Edam', 'Gouda']
Output::
            cheddar
            Edam
          gounda
 '''
# cheeses = ['Cheddar', 'Edam', 'Gouda']

# for word in cheeses:
#      print(word)