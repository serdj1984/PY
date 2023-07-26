a="""
#1	Необходимо реализовать для класса Student атрибут id, который должен присваиваться случайным образом
#2	Сделать сортировку списка students по убыванию атрибута id (от 100 до 1 к примеру)
"""


from Student import Student
import random as r
students = []
names = ['Ivan Ivanov','Petr Petrov','Vanya Ivanov']
groups = ['p123','q24','q333','t96']

for i in range(10):
    student = Student(names[r.randint(0,2)],#random.randint(0,2) -выбирает случайный индекс
                      groups[r.randint(0,3)],
                      r.randint(0,100))
    students.append(student)


# for i in range(10):
#     students[i].show()#students[i] - это объект 1 студент
#     #print(students[i].group)   #print(students[i].getGroup())
#     #print(students[i].name())   

#---------------выяснили разницу сеттеров и геттеров--------------------#
# students[0].setGroup('123')
# print(students[0].getgroup)

# students[0].setGroup(123)
# students[0].setGroup(123)
# students[0].setGroup({123}



#------------------- показать всех студентов из одной группы, -> необхоимо реализовать геттер для группы
group_for_search = 'p123'
for student in students:
    if student.getgroup == group_for_search:
        student.show()

print("\n#--------------------#\n") 

for student in students:
        student.show()    
print("\n#--------------------#\n") 
#---------------------- отсортировать студентов по среднему баллу
for j in range(len(students)):# за повторный проход
    for i in range(len(students)-1):
        if students[i].getgpa < students[i+1].getgpa:
            students[i], students[i+1] = students[i+1], students[i]


for student in students:
        student.show()
