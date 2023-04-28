#-*- coding: utf-8 -*-
# Creation Date : 2023-04-21
import requests

class Person():
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("Hi my name is " + self.name)

class Student(Person): # class
    def __init__(self, name): 
        Person.__init__(self, name)

        grade = 60
        self.grade = grade  #attribute / property

    def say_name(self):
        print(self.grade)
        print("Hi my name is " + self.name + " my grade is " + str(self.grade))

class Pokemon():
    def __init__(self):
        self.weight = None
        self.HP = None

    def set_weight(self, weight):
        self.weight = weight

    def say_weight(self):
        print(self.weight)

# student1 is the instance
student1 = Student("Arnold")
student2 = Student("Judith")
student1.say_name()
student2.say_name()
print(student2.grade)

requests.get("http://www.google.com")
