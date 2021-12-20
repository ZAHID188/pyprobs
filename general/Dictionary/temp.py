def menu():
    def rtclick(x, y):
        if x==12:
            return True
    return rtclick(12,15)
    
       
 
while True:
    menu()
    if menu() == True:
            print("It is true!")
    else:
        print("not true")
    break