for i in range(5):
     print("good morning ")
def greet():
      print("Sanjay")
      print("Sanjay")
greet()
        
def add(a,b):
    result= a + b
    print(result)
add(10,20)
add(50,30)
students=["sanjay","tejas","nibbi","nibba"]
students.append("durga")
students.remove("nibbi")
print(students[3])
print(students)


student={
     "name":"nibba",
     "age":23,
     "marks" : 85.5 ,
     "passed":True
}
student["course"]= "python programming"
student["marks"] = 90
print(student["course"])
print(student["marks"])

class stundent:
     def display(self):
         print("hello stundents")
         print("welcome to python programming")
                
s1=stundent()
s1.display()

########constructor######
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age = age
        self.marks = marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
        
s1=student("nibba",23,85.5)
s2=student("nibbi",67,90.0)
s1.display()
s2.display()
        
        