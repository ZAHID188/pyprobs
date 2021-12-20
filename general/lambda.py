people =[
    {"name": "harry","house": " lowa"},
    {"name": " zahid", "house": "kishoreganj"},
    {"name": "rayhan", "house": "lokkhipur"}
]
#



#def f(person):
  # return person["house"]

#people.sort(key=f)


#we can only do the one line code // or we can do three line code 
people.sort(key=lambda person:person["name"])
print(people)