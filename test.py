class Students:
    def __init__(self,name: str,age: int):
        self.name = name
        self.age = age

    def get(self):
        return f'Học sinh: {self.name}, Tuổi: {self.age}'
    
a = Students('nghia',1)
print(a.get())
print(Students().get())