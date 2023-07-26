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
                      r.randint(0,100),
                      r.randint(100,999)) # атрибут id, который присваиваться случайным образом
    students.append(student)


print("\n#---------- показать всех студентов ----------#\n")
for student in students:
        student.show()
print("\n\n") 

# --- показать всех студентов из одной группы, -> необхоимо реализовать геттер для группы --- #
print("\n#---------- показать всех студентов из одной группы ----------#\n")
group_for_search = 'p123'
for student in students:
    if student.getgroup == group_for_search:
        student.show()
print("\n\n") 
   

# ---------------------- отсортировать студентов по среднему баллу -------------------------- #
for j in range(len(students)):# за повторный проход
    for i in range(len(students)-1):
        if students[i].getgpa < students[i+1].getgpa:
            students[i], students[i+1] = students[i+1], students[i]
            
print("\n#---------- отсортировать студентов по среднему баллу ----------#\n") 
for student in students:
        student.show()
print("\n\n") 

#-------------------------- отсортировать студентов по убыванию id -------------------------- #
for j in range(len(students)):# за повторный проход
    for i in range(len(students)-1):
        if students[i].getid < students[i+1].getid:
            students[i], students[i+1] = students[i+1], students[i]

print("\n#---------- отсортировать студентов по убыванию id ----------#\n")            
for student in students:
        student.show()
