#student record management system:

student_record=["Rafay","Zain","Ali"]

print("\n\t\t\t\t\t&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
      "\n\t\t\t\t\t&&&&&&&&&&&& Student record System &&&&&&&&&&&&"
      "\n\t\t\t\t\t&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")



#functions

def add():
    add_data = int(input("How many students do you want to add?  "))

    for i in range(add_data):
        student_name = input(f"Enter student {i + 1} name: ")
        student_record.append(student_name)

    print("\nStudents added successfully!\nUpdated student_record list is given below:")
    for student in student_record:
        print(f" {student}")



def remove():
     remove_data = input("Enter student name you want to remove:  ")

     if remove_data in student_record :
         student_record.remove(remove_data)
         print(f"'{remove_data}' remove for the student_record:\nReamining students are: ")
         for student in student_record:
             print(f"{student}")
         
     else:
         print(f"{remove_data} not found in the student_record:")


def view():
    print("Student record:")
    for student in student_record:
        print(f" {student}")



def edit():
    edit_data=input("Enter student's name you want to edit in student record ?  ")
    number= int(input("Enter the index no: "))
    if number >= 0 and number < len(student_record):
      
        student_record[number] = edit_data
        print(f"Student record changed with : '{edit_data}'.\nNew student list is:")
        for student in student_record:
            print(f" {student}")

    else:
        print(f"your given index no '{number}' is not match with list index. :"
              f"\nPlease check the total index of a student_record's list.  ")






#program strating
condition=True
while condition:
    print("\n1.Add student data"
          "\n2.Edit student data "
          "\n3.Remove data"
          "\n4.View data"
          "\n5.exit the program")



    option_no=input("Select option: ")

    if option_no == '1':
        add()
    elif option_no == '2':
        edit()
    elif option_no == '3':
        remove()
    elif option_no == '4':
        view()
    elif option_no == '5':
        print("The program has ended. Best of luck!")
        break
    else:
        print("Wrong option. Please select correct option between 1 to 5.")



