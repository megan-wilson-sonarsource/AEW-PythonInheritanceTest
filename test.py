class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relationship = self.relationship()
        self.saying = self.say()
    def say(self):
        return("Hello I am a " + self.relationship)
    def relationship(self):
        return "Parent"
    def display(self):
        print(self.name)
        print(self.age)
        print(self.say())

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
    def relationship(self):
        return "Child"

def compare_ages_of(a, b):
    if a.age > b.age:
        return(a.name)
    else:
        return(b.name)

def main():
    person1 = Parent("Mary", 63)
    person2 = Child("Megan", 35)
    person3 = Child("Amanda", 25)
    print("Hello, world!")
    print("---------------------")
    print("Name: " + person1.name)
    print("Age: " + str(person1.age))
    print("Relationship: " + person1.relationship)
    print(person1.saying)
    print("DISPLAY:")
    person1.display()
    print("---------------------")
    print("Name: " + person2.name)
    print("Age: " + str(person2.age))
    print("Relationship: " + person2.relationship)
    print(person2.saying)
    print("DISPLAY:")
    person2.display()
    print("---------------------")
    print("Name: " + person3.name)
    print("Age: " + str(person3.age))
    print("Relationship: " + person3.relationship)
    print(person3.saying)
    print("DISPLAY:")
    person3.display
    print("---------------------")
    print("Between " + person2.name + " and " + person3.name + ", " +compare_ages_of(person2, person3)+ " is the older")
    print("Between " + person1.name + " and " + person3.name + ", " +compare_ages_of(person1, person3)+ " is the older")




if __name__ == '__main__':
    main()