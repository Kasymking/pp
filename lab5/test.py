class My_class:
    pass
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f" {self.surname}"  
    def my_func(asd):
        print("Hello my name is",asd.name)
        
p1 = My_class("John","Brother")
p1.my_func() 

class student(My_class):
    pass
x = student("Kasym","Akhali")
x.my_func()