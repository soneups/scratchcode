this - "IDEs and multidimensional lists"
Here is a list of other free IDEs which support Python:

Eclipse plus PyDev
PyScripter
Eric Python IDE
PyCharm Community Edition
CodeSkulptor

multidimensional lists
my_students=[["fred",1,2,3,4],["george"],5,6,7,8]]
so... z=my_course[1][2] is george (element 1) and 6 (0..1..2) the 3rd (2nd) sub-element...
for student_data in my_course:
    for grade_index in range(1,len(my_course)):
        print(student_data[grade_index])
        
for student_data in my_course:
    total_grade=0
    for grade_index in range(1,len(my_course)):
        total_grade=total_grade+student_data[grade_index]
        print(student_data[grade_index])
        print (total_grade/3.0)
