def softuni_students(*args, **course_id_course_name_dict):
    course_id_student_name_dict = {}
    for tuple in args:
        course_id = tuple[0]
        student_name = tuple[1]

        if course_id not in course_id_student_name_dict.keys():
            course_id_student_name_dict[course_id] = [student_name]
        else:
            course_id_student_name_dict[course_id].append(student_name)

    valid_students = {}
    invalid_students = []

    for key, value in course_id_student_name_dict.items():
        if key not in course_id_course_name_dict.keys():
            for name in value:
                invalid_students.append(name)
        else:
            for name in value:
                valid_students[name] = {key:course_id_course_name_dict[key]}

    sorted_valid_students = dict(sorted(valid_students.items(), key=lambda x: x[0]))

    output = ""

    for student, course_data in sorted_valid_students.items():
        output += f"*** A student with the username {student} has successfully finished the course {course_data[list(course_data.keys())[0]]}!\n"

    if invalid_students:
        output += f"!!! Invalid course students: {', '.join(i for i in sorted(invalid_students))}"


    return output


print(softuni_students(    ('id_7', 'Silvester1'),    ('id_32', 'Katq21'),   ('id_7', 'The programmer'),   id_76='Spring Fundamentals',  id_7='Spring Advanced'))