import csv

def write_csv(info_list):
    with open ("student_details.csv",'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["name","age","phone number","email"])
        writer.writerow(info_list)
student_list=[]
student_info=1
condition = True
while (condition): 
    stud_name =input("enter {} student name:".format(student_info))
    stud_age=int(input("enter {} student age:".format(student_info)))
    stud_contact=int(input("enter {} student phone number:".format(student_info)))
    stud_email = input("enter {} student email:".format(student_info))
    stud_info=(stud_name+" "+str(stud_age)+" "+str(stud_contact)+" "+stud_email)
    student_list.append(stud_info)
    print(stud_info)
    stud_info_list=stud_info.split(' ')
    print("after splitting of information"+ str(stud_info_list))
    print("\n entered information is \nName: {}\nAge:{}\nphone number:{}\nemail:{}".format(stud_info_list[0],stud_info_list[1],stud_info_list[2],stud_info_list[3]))
    choice=input("is the entered input is correct?(yes/no) ")
    if choice=="yes":
        
        write_csv(stud_info_list)

        cond_check=input("if you want to enter add one more(yes/no):")

        if cond_check == "yes":
            condition =True
            student_info=student_info+1
        elif cond_check=='no':
            condition = False
            print(student_list)
    elif choice=="no":
        print("\n please re-enter values:")
