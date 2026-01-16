'''Create a daily student attendence traker program'''

def tot_student():
    while True:
        number_all_students= input('Enter number of all students in class: ')
        try:
            number_all_students= int(number_all_students)
            break
        except ValueError:
            print('invalid input')
    return number_all_students

def stu_attendence_func():
    global count
    global number_all_students
    while True:
        print()
        student_name= input('Enter Student Name: ')
        stu_attendence= int(input('Enter student presence or absent(1/0): ')) # get the student present(1) or absent(0)
        if stu_attendence == 1 or stu_attendence == 0:
            stu_attendence_dict[student_name] = stu_attendence
        else:
            print('Invalid input.Press 1 or 0')
            continue
        if count == number_all_students:
            break
        count+= 1
    return stu_attendence_dict

'''call functions and print outputs'''
number_all_students=tot_student() # call the function 
stu_attendence_dict= {} # empty dict
print(f"Present - 1\nAbsent - 0")
count=1
stu_attendence_dict=stu_attendence_func()
stu_attendence_func()

