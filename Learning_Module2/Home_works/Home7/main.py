
from Learning_Module1.Lections.Lesson2_5.functions import functional_programming as fp
from Learning_Module1.Home_works.Home2 import level1

choice = input("enter your choice: \n1) fizzbuzz\n2) square2d\n")

if choice == "1":
    operation = input("enter your operation: \n1) getResult()\n2) analysis for number\n")
    print(level1.get_result())

    if operation == "1":
        print("you selected getResult():", level1.get_result())
    elif operation == "2":
        element = input("enter element for analysis: ")
        print(level1.analysis(element))
    else:
        print("wrong operation")

elif choice == "2":
    operation = int(input("enter your operation: \n1) default triangle()\n2) your own triangle\n"))

    if operation == 1:
        print("default 3angle:",  fp.area_triangle_1())
    elif operation == 2:
        a = int(input("enter line a: "))
        h = int(input("enter line h: "))
        text = (input("enter info: "))
        print(fp.area_triangle_2(a,h,text))
    else:
        print("wrong operation")

else:
    print("error")

print("the end")


