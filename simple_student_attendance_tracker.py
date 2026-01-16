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
