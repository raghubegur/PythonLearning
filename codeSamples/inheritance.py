class Person:
    def __init__(self, name):
        #print('Inside Person Constructor')
        self.name = name
    def sayHello(self):
        print('Hello, ' + self.name)


class Student(Person):
    def __init__(self, name, school):
        #print('Inside Student Constructor')
        super().__init__(name)
        self.school = school
    def singSchoolSong(self):
        print('Ode to ' + self.school)


student = Student('Raghu', 'National College')
student.sayHello()
student.singSchoolSong()

# What are you
print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))

