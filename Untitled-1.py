
python_students = {"Alice", "Bob", "Charlie", "Diana"}
data_science_students = {"Bob", "Diana", "Eve", "Frank"}

print("Initial enrollment:")
print(f"Python: {python_students}")
print(f"Data Science: {data_science_students}")
print()


python_students.add("Grace")
print("After adding Grace to Python:")
print(f"Python: {python_students}")
print()


removed_student = data_science_students.pop()  
print(f"Removed {removed_student} from Data Science")
print(f"Data Science: {data_science_students}")
print()


both_courses = python_students & data_science_students
print(f"Students in both courses: {both_courses}")
print()


only_python = python_students - data_science_students
print(f"Students only in Python: {only_python}")
print()


all_students = python_students | data_science_students
print(f"All unique students: {all_students}")
print()


enrollment_data = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}


print("Current enrollment numbers:")
for course, count in enrollment_data.items():
    print(f"Course: {course}, Students: {count}")
print()


expected_growth = {course: count * 2 for course, count in enrollment_data.items()}
print("Expected enrollment after growth:")
for course, count in expected_growth.items():
    print(f"Course: {course}, Students: {count}")