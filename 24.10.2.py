#storage
class Storage:
    storage=[]
    def __init__(self,capacity):
        self.capacity=capacity
    def add_product(self,product:str):
        if len(Storage.storage)<self.capacity:
            Storage.storage.append(product)
    def get_products(self):
        return Storage.storage

#weapon
class Weapon:
    def __init__(self,bullets=0):
        self.bullets = bullets
    def shoot(self):
        if self.bullets>0:
            self.bullets-=1
            return 'shooting...'
        else:
            return "no bullets left"
    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

#Catalogue
class Catalogue:
    products = []
    def __init__(self,name):
        self.name = name
    def add_product(self,product_name:str):
        Catalogue.products.append(product_name)
    def get_by_letter(self,first_letter:str):
        return [p for p in self.products if p.lower().startswith(first_letter.lower())]
    def __repr__(self):
       self.products.sort()
       return f"Items in the {self.name} catalogue:\n"+"\n".join(x for x in self.products)

#Town
class Town:
    def __init__(self,name:str):
        self.name = name
        self.latitude = "0N"
        self.longitude = "0E"
    def set_latitude(self,latitude):
        self.latitude = latitude
    def set_longitude(self,longitude):
        self.longitude=longitude
    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

#Class
class Class:
    __students_count = 22
    def __init__(self,name):
        self.name = name
        self.grades = []
        self.students = []
    def add_student(self,name:str,grade:float):
        if len(self.students)<Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self):
        return sum(self.grades)/len(self.grades)
    def __repr__(self):
        return f"The students in {self.name}: "+", ".join(x for x in self.students)+f". Average grade: {self.get_average_grade():.2f}"

#Inventory
class Inventory:
    def __init__(self,capacity:int):
        self.__capacity = capacity
        self.items = []
    def add_item(self,item:str):
        if len(self.items)<self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in inventory"
    def get_capacity(self):
        return self.__capacity
    def __repr__(self):
        return f"Items: "+", ".join(x for x in self.items)+".\n"+f"Capacity left: {self.__capacity-len(self.items)}"

#Articles
class Article:
    def __init__(self,title:str,content:str, author:str):
        self.title = title
        self.content = content
        self.author = author
    def edit(self,new_content:str):
        self.content=new_content
    def change_author(self,new_author:str):
        self.author=new_author
    def rename(self,new_title:str):
        self.title=new_title
    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"
