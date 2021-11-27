#here is a class for student
class stdclass():
    def __init__ (self,name,major,gpa, is_on_probation) :
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation

    def __repr__(self):
        return "stdclass(name='{}',major='{}',gpa='{}',is_on_probation='{}')".format(self.name,self.major,self.gpa,self.is_on_probation)

    def __str__(self):
        return self.__repr__()
zahid=stdclass("zahidul","SE","4.6","yes")
rofiq=stdclass("zahidul","SE","4.6","yes")
sofiq=stdclass("zahidul","SE","4.6","yes")
sadek=stdclass("zahidul","SE","4.6","yes")
ullash=stdclass("zahidul","SE","4.6","yes")

students=[zahid,rofiq,sofiq,sadek,ullash]
print(zahid)
print(students)




        
 