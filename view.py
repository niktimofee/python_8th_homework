def get_operation():
    operation = int(input(
        " 1 - добавить ученика \n 2 - добавить учебный предмет \n 3 - добавить оценку ученику по предмету \n 4 - показать список учеников \n 5 - показать оценки конкретного ученика \n 6 - выход \n"))
    return operation

def add_student():
    name = input("✏️  Введите имя и фамилию ученика: ")
    return name
    # print(" 💾 Сохранено")

def add_study_subject():
    subject = input("✏️  Введите название учебного предмета: ")
    return subject
        # print("Учебный предмет добавлен")

def add_grade():
    name = input("✏️  Введите имя и фамилию ученика которому желаете поставить оценку: ")
    subject = input("✏️  Введите предмет по которому будет оценка: ")
    grade = input("✏️  Введите оценку: ")
    return name, subject, grade

def print_student():
    name = input("✏️  Введите имя и фамилию ученика: ")
    return name