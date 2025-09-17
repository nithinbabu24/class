frontend = {"Alice", "Bob", "Charlie", "David"}
backend = {"Eve", "Frank", "Charlie", "Grace"}

backend.add("Helen")
frontend.remove("David")

both_courses = frontend & backend
print("Students in both courses:", both_courses)

only_backend = backend - frontend
print("Students only in Backend:", only_backend)

unique_students = frontend | backend
print("Total unique students:", len(unique_students))

course_dict = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, count in course_dict.items():
    print(course, ":", count)

full_course_dict = {**course_dict, "Fullstack": len(frontend | backend)}
print(full_course_dict)
