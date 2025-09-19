class Person():
    def __init__(self, date_of_birth: str ,name: str, gender: str, status:str):
        self.date_of_birth = date_of_birth
        self.name = name
        self.gender = gender
        self.status = status

    def speak(self):
            print(f"hello my name is {self.name}")

    def walk(self):
        print("Hi I am walking ")

        
person1 = Person("4th Oct ", "Philipa" , "Female" ,"single for now")        
print(person1.name)
person1.speak()