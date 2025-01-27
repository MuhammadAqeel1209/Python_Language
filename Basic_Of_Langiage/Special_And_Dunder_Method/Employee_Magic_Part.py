class Employee:
    name = "Aqeel"
    def __len__(self): #-->Name of Method 
        return len(self.name)
    def __str__(self):
        return F"Name is {self.name}"  
    def __repr__(self):
        return F"Name is ('{self.name}')"  
    def __call__(self):
        print("Hello Man")         

e1 = Employee()
print(e1.name)
print(len(e1)) # --> calling at time 
#That Why Called Magic Method

