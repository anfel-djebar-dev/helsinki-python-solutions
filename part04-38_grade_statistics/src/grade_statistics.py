# -------------- The help functions : --------------- 
# 1/ function to calculate the point of the exercises :
def  exercises_point(exercises : int):
    point = exercises // 10 
    return point 

# 2/ function to calculte the sum of the exam note + the point of the exercises :
def students_points(exam_note , the_point_of_exercises : int):
    point = exam_note + the_point_of_exercises  
    return point 

# 3/ function to  calculate the grade 0-5 ,result mean the result of the previous function (point):
def  students_grade(result , exam_note : int) :
    if exam_note < 10 or result <= 14 :
        return 0
    elif result >= 15 and result <= 17 :
        return 1
    elif result >= 18 and result <= 20 :
        return 2
    elif result >= 21 and result <= 23 :
        return 3
    elif result >= 24 and result <= 27 :
        return 4
    elif result >= 28 and result <= 30 :
        return 5

# 4/ function to calculate the average of points :
def average_points(points , nbr_student):
    result = points / nbr_student 
    return result 

# 5/ function to calculate the percentage of passager :
def pass_percentage(student_nbr , n_success_student):
    result = (n_success_student * 100 ) / student_nbr
    return result

# 6/ function to calculate the count of grades:
def pass_grades(grades_list ) :
    grade_stars = [""] * 6 # we can use it insted of this["", "", "", "", "", ""] 

    for grade in grades_list:
        grade_stars[grade] += "*"

    return grade_stars
        
    
def main():
    students_nbr = 0
    success_student = 0 
    student_grades_list = []
    all_students_point = 0
    gradelist = []
    while True:
        line = input("Exam points and exercises completed: ").strip()
        if not line:
            break

        parts = line.split()
        exam_points = int(parts[0])
        exercises_completed = int(parts[1])
        students_nbr += 1
        
        if not students_nbr :
            break

        exrcs_point = exercises_point(exercises_completed)
        the_point = students_points(exam_points, exrcs_point)
        all_students_point += the_point
        grades = students_grade(the_point , exam_points)
        student_grades_list.append(grades) 
        if grades >= 1 :
            success_student += 1
        
    print("Statistics:")
    print(f"Points average: {average_points(all_students_point , students_nbr):.1f}")
    print(f"Pass percentage: {pass_percentage(students_nbr , success_student):.1f}")
    print("Grade distribution:")    
    gradelist = pass_grades(student_grades_list)
    for grade in range(5,-1,-1):
        print(f"{grade}: {gradelist[grade]}")


#15 87
# 10 55
# 11 40
# 4 17

main()    
