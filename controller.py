import view

main_dct = {}
students_list = []
study_subjects_list = []

def start():
    while True:
        op = view.get_operation()
        if op == 1:
            student = view.add_student()
            if student not in students_list:
                students_list.append(student)    
                main_dct[student] = {}
                for subject in study_subjects_list:
                    main_dct[student][subject] = []

        if op == 2:
            subject = view.add_study_subject()
            if subject not in study_subjects_list:
                study_subjects_list.append(subject)
                for student in students_list:
                    main_dct[student][subject] = []

        if op == 3:
            name, subject, grade = view.add_grade()
            main_dct[name][subject].append(grade)

        if op == 4:
            print(main_dct)

        if op == 5:
            name = view.print_student()
            print(main_dct[name])
            
        elif op == 6:
            break