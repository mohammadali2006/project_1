from os import system
from time import sleep
system('cls')

continue_ = True
student_list = [
    ['helen', 'jackson', 'female', '0044', '1207', '60', '40'],
    ['masood', 'habibi', 'male', '0055', '1208', '70', '70'],
    ['narmin', 'sheikhl', 'female', '0066', '1209', '80', '30'],
    ['behnam', 'karami', 'male', '0077', '1210', '90', '50']
]


while continue_:
    print('\n\n1. [A]dd student')
    print('2. [S]how All students')
    print('3. [R]emove student')
    print('4. [E]dit student')
    print('5. [SE]arch student')
    print('6. best [PHP] Score')
    print('7. best [PYTHON] Score')
    print('8. best [AV]erage')
    print('9. [Exit]')

    menu = input('\n Select Menu :')
    system('cls')


    if menu in ['1', 'A']:

        temp = True


        while temp:
            system('cls')
            # region get name
            flag = True


            while flag:
                name = input('Please Enter Name :')
                system('cls')


                if name != '':
                    flag = False
                else:
                    print('ERROR !!!!\nPlease Try Again')
                    sleep(2)
                    system('cls')
            # endregion

            # region get family
            flag = True


            while flag:
                family = input('Please Enter Family :')
                system('cls')


                if family != '':
                    flag = False
                else:
                    print('ERROR !!!!\nPlease Try Again')
                    sleep(2)
                    system('cls')
            # endregion

            # region get gender
            flag = True


            while flag:
                gender = input('Enter Gender (male, female, other) :')
                system('cls')


                if gender in ['male', 'female', 'other'] and gender != '':
                    flag = False
                else:
                    print('ERROR !!!!\nPlease Try Again', end='')
                    sleep(2)
                    system('cls')
            # endregion

            # region get nationalcode
            flag = True


            while flag:
                national_code = input('Please Enter National Code :')
                system('cls')


                if national_code == '':
                    print('ERROR !!!!\nPlease Try Again')
                    sleep(2)
                    system('cls')
                else:
                    check_exist = False


                    for student in student_list:
                        if student[3] == national_code:
                            check_exist = True


                    if check_exist:
                        print('ERROR !!!!', national_code, 'exists')
                        sleep(5)
                        system('cls')
                    else:
                        flag = False
            # endregion

            # region get stdcode
            flag = True

            while flag:
                student_code = input('Please Enter Student Code :')
                system('cls')

                if student_code == '':
                    print('ERROR !!!!\nPlease Try Again')
                    sleep(2)
                    system('cls')
                else:
                    check_exist = False

                    for student in student_list:
                        if student[4] == student_code:
                            check_exist = True

                    if check_exist:
                        print('ERROR !!!!', student_code, 'exists')
                        sleep(5)
                        system('cls')
                    else:
                        flag = False
            # endregion

            # region get score php score
            flag = True

            while flag:
                php_score = float(input('Please Enter php_score Score (0 - 100) :'))
                system('cls')

                if 0 <= php_score <= 100:
                    flag = False
                else:
                    print('ERROR !!!!\nThe Entered Number Is Not Within The Range (Please try again)')
                    sleep(3)
                    system('cls')
            # endregion

            # region get score python score
            flag = True


            while flag:
                python_score = float(input('Please Enter PYTHON Score (0 - 100) :'))
                system('cls')


                if 0 <= python_score <= 100:
                    flag = False
                else:
                    print('ERROR !!!!\nThe Entered Number Is Not Within The Range (Please Try Again)')
                    sleep(3)
                    system('cls')
            # endregion

            # region get continue
            if input('\n\nDo You Want To Add Another Student (yes - no) : ') == ['yes']:
                sleep(2)
                system('cls')
            else:
                system('cls')
                temp = False
            # endregion

        student = [name, family, gender, student_code, national_code, student_code, php_score, python_score]
        student_list.append(student)

    elif menu in ['2', 'S']:


        if input('Do You Want See All Student Profile (yes - no) :') == 'yes':
            system('cls')
            display_index = [0, 1, 2, 3, 4, 5, 6]
        else:
            system('cls')
            columns = ['Name', 'Family', 'Gender', 'National', 'Student', 'Score PHP', 'Score PYTHON']
            display_index = []


            for index in range(len(columns)):
                print('Do You Want To Display', columns[index], ' : ', end='')
                if input() == 'yes':
                    display_index.append(index)
                system('cls')

        print('\nName - Family - Gender - National - Student Code - Score PHP - Score PYTHON')
        print('----------------------------------------------------------------------------')


        for student in student_list:


            for index in display_index:
                print(student[index], end="\t")
            print()
        print('------------------------------------------------------------------------------')
        sleep(3)

    elif menu in ['3', 'R']:

        temp = True


        while temp:
            # region show students
            print('\nName - Family - Gender - National - Student Code - Score PHP - Score PYTHON')
            print('----------------------------------------------------------------------------')

            for student in student_list:
                for item in student:
                    print(item, end='\t')
                print()
            print('----------------------------------------------------------------------------')
            # endregion
            search = int(input('\n\nWhich One Do You Want To Search With ? \n1. National Code\n2. Student Code\n3. Exit\nSelect Number :'))
            select = search
            system('cls')


            if select == 1:
                # region search with national code
                select = input('\n\nNational Code (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                        if student[3] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'Does Not Exist')
                    else:
                        print('Name :', find_student[0], 'Family', find_student[1], 'National Code :', find_student[3], 'Student Code :', find_student[4])


                        if input('Are You Sure Delete This Student ? (yes - no) : ') == 'yes':
                            student_list.remove(find_student)
                            system('cls')
                        print('Done !!!')
                        sleep(2)
                        system('cls')
                # endregion
            elif select == 2:
                # region search with student code
                select = input('\n\nStudent Code (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                
                        
                        if student[4] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'does not exist')
                    else:
                        print('Name :', find_student[0], 'Family', find_student[1], 'National Code :', find_student[3], 'Student Code :', find_student[4])


                        if input('Are You Sure Delete This Student ? (yes - no) : ') == 'yes':
                            student_list.remove(find_student)
                            system('cls')
                        print('Done !!!')
                        sleep(2)
                        system('cls')
                # endregion
            elif select == 3:
                    temp = False

    elif menu in ['4', 'E']:
        # region show students
        print('\n\nName - Family - Gender - Natonal - Student Code - PHP Score - PYTHON Score')
        print("------------------------------------------------------------------")

        for student in student_list:
            for item in student:
                print(item, end="\t")
            print()
        print("------------------------------------------------------------------")
        # endregion
        search = int(input('\n\nWhich One Do You Want To Search With ?\n1. National Code\n2. Student Code\n3. Exit\nSelect Number :'))
        select = search
        system('cls')

        if select == 1:
            # region search with national code
            select = input('\n\nNational Code (exit) :')
            system('cls')


            if select == 'exit':
                temp = False
            else:
                find_student = None

                for student in student_list:
                    if student[3] == select:
                        find_student = student


                if find_student == None:
                    print(select, 'Does Not Exist')
                else:

                    edit_continue = True

                    while edit_continue:
                        print("Name :", find_student[0])
                        print("Family :", find_student[1])
                        print("Gender :", find_student[2])                        
                        print("National Code :", find_student[3])
                        print("Student Code :", find_student[4])
                        print("PHP Score :", find_student[5])
                        print("PYTHON Score :", find_student[6])
                        edit_menu = int(input("\n1. Name\n2. Family\n3. Gender\n4. National Code\n5. Student Code\n6. PHP Score\n7. PYTHON Score\n8. Exit : "))
                        system("cls")

                        if edit_menu == 1:
                            # region get new name
                            flag = True

                            while flag:
                                new_name = input('New Name : ')
                                system("cls")

                                if new_name != '':
                                    flag = False
                                else:
                                    print('Error!!!!')
                            # endregion
                            find_student[0] = new_name
                            
                        elif edit_menu == 2:
                            # region get new family
                            flag = True

                            while flag:
                                new_family = input('New Family : ')
                                system("cls")

                                if new_family != '':
                                    flag = False
                                else:
                                    print('Error!!!!')
                            # endregion
                            find_student[1] = new_family

                        elif edit_menu == 3:
                            # region get new gender
                            flag = True

                            while flag:
                                new_gender = input('New Gender : ')
                                system("cls")

                                if new_gender != '':
                                    flag = False
                                else:
                                    print('Error!!!')
                            # endregion
                            find_student[2] = new_gender     
                            
                        elif edit_menu == 4:
                            # region get new national code
                            flag = True

                            while flag:
                                new_national_code = input('New National Code : ')
                                system("cls")
                                
                                temp = True
                                
                                while temp:
                                    
                                    if new_national_code != '':
                                        temp = False
                                    # region unique national code
                                    if new_national_code :
                                        check_exist = False

                                        for student in student_list:
                                            if student[3] == new_national_code:
                                                check_exist = True

                                        if check_exist:
                                            print('ERROR!!!!!!', new_national_code, 'exists', '\nPlease Try Again')
                                            sleep(5)
                                            system('cls')
                                            temp = False
                                        else:
                                            flag = False
                                    # endregion
                            # endregion
                            find_student[3] = new_national_code 
                            
                        elif edit_menu == 5:
                            # region get new student code
                            flag = True

                            while flag:
                                new_student_code = input('New Student Code : ')
                                system("cls")

                                if new_student_code != '':
                                    flag = False
                                    # region unique student code
                                    if new_student_code :
                                        check_exist = False

                                        for student in student_list:
                                            if student[3] == new_student_code:
                                                check_exist = True

                                        if check_exist:
                                            print('ERROR!!!!!!', new_student_code, 'exists', '\nPlease Try Again')
                                            sleep(5)
                                            system('cls')
                                            temp = False
                                        else:
                                            flag = False
                                    # endregion
                            # endregion
                            find_student[4] = new_student_code
                            
                        elif edit_menu == 6:
                            # region get new php score
                            flag = True

                            while flag:
                                new_php_score = input('New PHP Score : ')
                                system("cls")

                                if new_php_score != '':
                                    flag = False
                                else:
                                    print('Error!!!!')
                            # endregion
                            find_student[5] = new_php_score 
                             
                        elif edit_menu == 7:
                            # region get new python score
                            flag = True

                            while flag:
                                new_pythone_score = input('New PYTHON Score : ')
                                system("cls")

                                if new_pythone_score != '':
                                    flag = False
                                else:
                                    print('Error!!!')
                            # endregion
                            find_student[6] = new_pythone_score
                            
                        elif edit_menu == 8:
                            edit_continue = False

                        else:
                            print('ERROR !!!!', end='')
                            sleep(2)
                            system('cls')
            # endregion
        elif select == 2:
            # region search with student code
            select = input('\n\nStudent Code (exit) :')
            system('cls')


            if select == 'exit':
                temp = False
            else:
                find_student = None

                for student in student_list:
                    if student[4] == select:
                        find_student = student


                if find_student == None:
                    print(select, 'does not exist')
                else:
                    edit_continue = True


                    while edit_continue:
                        print("Name :", find_student[0])
                        print("Family :", find_student[1])
                        print("Gender :", find_student[2])                        
                        print("National Code :", find_student[3])
                        print("Student Code :", find_student[4])
                        print("PHP Score :", find_student[5])
                        print("PYTHON Score :", find_student[6])
                        edit_menu = int(input("\n1. Name  2. Family  3. Gender  4. National Code  5. Student Code  6. PHP Score  7. PYTHON Score  8. Exit : "))
                        system("cls")
            
                        if edit_menu == 1:
                            # region get new name
                            flag = True

                            while flag:
                                new_name = input('New Name : ')
                                system("cls")

                                if new_name != '':
                                    flag = False
                                else:
                                    print('Error!!!!')
                            # endregion
                            student[0] = new_name
                            
                        elif edit_menu == 2:
                            # region get new family
                            flag = True

                            while flag:
                                new_family = input('New Family : ')
                                system("cls")

                                if new_family != '':
                                    flag = False
                                else:
                                    print('Error!!!!')
                            # endregion
                            student[1] = new_family

                        elif edit_menu == 3:
                            # region get new gender
                            flag = True

                            while flag:
                                new_gender = input('New Gender : ')
                                system("cls")

                                if new_gender != '':
                                    flag = False
                                else:
                                    print('Error!!!')
                            # endregion
                            student[2] = new_gender     
                            
                        elif edit_menu == 4:
                            # region get new national code
                            flag = True

                            while flag:
                                new_national_code = input('New National Code : ')
                                system("cls")

                                temp = True
                                
                                while temp:
                                    
                                    if new_national_code != '':
                                        temp = False
                                    # region unique national code
                                    if new_national_code :
                                        check_exist = False

                                        for student in student_list:
                                            if student[3] == new_national_code:
                                                check_exist = True

                                        if check_exist:
                                            print('ERROR!!!!!!', new_national_code, 'exists', '\nPlease Try Again')
                                            sleep(5)
                                            system('cls')
                                            temp = False
                                        else:
                                            flag = False
                                    # endregion
                            # endregion
                            student[3] = new_national_code 
                            
                        elif edit_menu == 5:
                            # region get new student code
                            flag = True

                            while flag:
                                new_student_code = input('New Student Code : ')
                                system("cls")
                                temp = True
                                
                                while temp:
                                    
                                    if new_student_code != '':
                                        temp = False
                                    # region unique student code
                                    if new_student_code :
                                        check_exist = False

                                        for student in student_list:
                                            if student[3] == new_student_code:
                                                check_exist = True

                                        if check_exist:
                                            print('ERROR!!!!!!', new_student_code, 'exists', '\nPlease Try Again')
                                            sleep(5)
                                            system('cls')
                                            temp = False
                                        else:
                                            flag = False
                                    # endregion
                            # endregion
                            student[4] = new_student_code
                            
                        elif edit_menu == 6:
                            # region get new php score
                            flag = True

                            while flag:
                                new_php_score = input('New PHP Score : ')
                                system("cls")

                                if new_php_score != '':
                                    flag = False
                                else:
                                    print('Error!!!!')
                            # endregion
                            student[5] = new_php_score 
                             
                        elif edit_menu == 7:
                            # region get new python score
                            flag = True

                            while flag:
                                new_pythone_score = input('New PYTHON Score : ')
                                system("cls")

                                if new_pythone_score != '':
                                    flag = False
                                else:
                                    print('Error!!!')
                            # endregion
                            student[6] = new_pythone_score
                            
                        elif edit_menu == 8:
                            edit_continue = False
            # endregion
        elif select == 3:
                temp = False

    elif menu in ['5', 'SE']:
        
        search = int(input('Do You Want search With\n1. Name\n2. Family\n3. Gender\n4. National Code\n5. Student Code\n6. Exit\nSelect Number :'))
        select = search
        system('cls')
        
        temp = True
        
        while temp:
            
            
            if select == 1:
                # region search with name
                select = input('\n\nName (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                        
                        if student[0] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'Does Not Exist')
                    else:
                        print('\n\nName - Family - Gender - National - Student Code - PHP Score - PYTHON Score')
                        print("------------------------------------------------------------------")

                        i = 0

                        for student in student_list:
                            while i <= 6:
                                for item in find_student:
                                    i += 1
                                    print(item, end="\t")
                                print()
                        print("------------------------------------------------------------------")
                        sleep(7.5)
                        system('cls')
                        temp = False
                # endregion
            elif select == 2:
                # region search with family
                select = input('\n\nFamily (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                        
                        if student[1] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'Does Not Exist')
                        temp = False
                    else:
                        print('\n\nName - Family - Gender - Natonal - Student Code - PHP Score - PYTHON Score')
                        print("------------------------------------------------------------------")

                        i = 0

                        for student in student_list:
                            while i <= 6:
                                for item in find_student:
                                    i += 1
                                    print(item, end="\t")
                                print()
                        print("------------------------------------------------------------------")
                        sleep(7.5)
                        system('cls')
                        temp = False
                # endregion
            elif select == 3:
                # region search with gender
                select = input('\n\nGender (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                        
                        if student[2] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'Does Not Exist')
                    else:
                        print('\n\nName - Family - Gender - Natonal - Student Code - PHP Score - PYTHON Score')
                        print("------------------------------------------------------------------")

                        i = 0

                        for student in student_list:
                            while i <= 6:
                                for item in find_student:
                                    i += 1
                                    print(item, end="\t")
                                print()
                        print("------------------------------------------------------------------")
                        sleep(7.5)
                        system('cls')
                        temp = False
                # endregion
            elif select == 4:
                # region search with national code
                select = input('\n\nNatinal Code (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                        
                        if student[3] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'Does Not Exist')
                    else:
                        print('\n\nName - Family - Gender - Natonal - Student Code - PHP Score - PYTHON Score')
                        print("------------------------------------------------------------------")

                        i = 0

                        for student in student_list:
                            while i <= 6:
                                for item in find_student:
                                    i += 1
                                    print(item, end="\t")
                                print()
                        print("------------------------------------------------------------------")
                        sleep(7.5)
                        system('cls')
                        temp = False
                # endregion
            elif select == 5:
                # region search with student code
                select = input('\n\nStudent Code (exit) :')
                system('cls')


                if select == 'exit':
                    temp = False
                else:
                    find_student = None

                    for student in student_list:
                        
                        if student[4] == select:
                            find_student = student


                    if find_student == None:
                        print(select, 'Does Not Exist')
                    else:
                        print('\n\nName - Family - Gender - Natonal - Student Code - PHP Score - PYTHON Score')
                        print("------------------------------------------------------------------")

                        i = 0

                        for student in student_list:
                            while i <= 6:
                                for item in find_student:
                                    i += 1
                                    print(item, end="\t")
                                print()
                        print("------------------------------------------------------------------")
                        sleep(7.5)
                        system('cls')
                        temp = False
                # endregion
            elif select == 6:
                temp = False

    elif menu in ['6', 'PHP']:
               
        # region get bigest php
        best_php = 0
        i = 0

        for _ in range(len(student_list)):
            
            if best_php < float(student_list[i][5]):
                best_php = float(student_list[i][5])
            i += 1
        # endregion

        # region get all students with bigest php
        i = 0

        print('\n\nName - Family - Gender - National - Student Code - PHP Score')
        print("------------------------------------------------------------------")
        for _ in range(len(student_list)):
            
            
            if best_php == float(student_list[i][5]):
                print(student_list[i][0], end='\t')
                print(student_list[i][1], end='\t')
                print(student_list[i][2], end='\t')
                print(student_list[i][3], end='\t')
                print(student_list[i][4], end='\t')
                print(student_list[i][5], end='\n')
                print()
            i += 1 
        print('----------------------------------------------------') 
        sleep(7.5)
        # endregion

    elif menu in ['7', 'PYTHON']:
                
        # region get bigest python
        best_python = 0
        i = 0

        for _ in range(len(student_list)):
            
            
            if best_python < float(student_list[i][6]):
                best_python = float(student_list[i][6])
            i += 1
        # endregion  

        # region get all students with bigest python
        i = 0

        print('\n\nName - Family - Gender - Natonal - Student Code - PYTHON Score')
        print("------------------------------------------------------------------")
        
        for _ in range(len(student_list)):
            
            
            if best_python == float(student_list[i][6]):
                print(student_list[i][0], end='\t')
                print(student_list[i][1], end='\t')
                print(student_list[i][2], end='\t')
                print(student_list[i][3], end='\t')
                print(student_list[i][4], end='\t')
                print(student_list[i][6], end='\n')
                print()
            i += 1 
        print('----------------------------------------------------') 
        sleep(7.5)
    # endregion

    elif menu in ['8', 'AV']:
            
        # region add average to info
        best_average = 0
        i = 0

        for _ in range(len(student_list)):
            best_average = (float(student_list[i][5]) + float(student_list[i][6])) / 2
            for student in student_list:
                student_list[i].append(best_average)
            i += 1
        # endregion
         
        # region get bigest average
        best_average = 0
        i = 0

        for _ in range(len(student_list)):
                
                
            if best_average < float(student_list[i][7]):
                best_average = float(student_list[i][7])
            i += 1
        # endregion  

        # region get all students with bigest average
        i = 0

        print('\n\nName - Family - Gender - Natonal - Student Code - Average')
        print("------------------------------------------------------------------")
        for _ in range(len(student_list)):
                    
                    
            if best_average == float(student_list[i][7]):
                print(student_list[i][0], end='\t')
                print(student_list[i][1], end='\t')
                print(student_list[i][2], end='\t')
                print(student_list[i][3], end='\t')
                print(student_list[i][4], end='\t')
                print(student_list[i][7], end='\n')
                print()
            i += 1 
        print('----------------------------------------------------')
        sleep(7.5)
        # endregion 
        
    elif menu in ['9', 'Exit']:
        continue_ = False

    else:
        print('ERROR!!!!\nPlease Try Again')
        sleep(2)
        system('cls')
1