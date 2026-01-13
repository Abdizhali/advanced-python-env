class Person:
    def say(self):
        print("I am Aset")

class Student(Person):
    def say(self):
        print("I am a student")

p = Person()
s = Student()

p.say()
s.say()
