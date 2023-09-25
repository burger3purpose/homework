class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"

class Dog(Pet):
    def bark(self, n):
        for _ in range(n):
            print("bark!")

    def human_age(self):
        return self.age * 4

class Cat(Pet):
    def meow(self, n):
        for _ in range(n):
            print("meow~")

    def human_age(self):
        return self.age * 4


dog = Dog("popo", 10)
dog.bark(3) 
print(dog)
print(f"사람의 나이로 환산: {dog.human_age()}")

cat = Cat("pipi", 5)
cat.meow(4)
print(cat)
print(f"사람의 나이로 환산: {cat.human_age()}") 