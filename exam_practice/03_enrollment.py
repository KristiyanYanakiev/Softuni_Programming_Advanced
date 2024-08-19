def gather_credits(needed_credits, *tuples):
    gathered_credits = 0
    enrolled_courses = []
    result = ""
    success = False
    if needed_credits <= 0:
        success = True
    else:
        for tuple in tuples:

            course_name = tuple[0]
            course_credits = tuple[1]
            if course_name not in enrolled_courses:
                enrolled_courses.append(course_name)
                gathered_credits += course_credits

            if gathered_credits >= needed_credits:
                success = True
                break

    if success:
        sorted_courses = sorted(enrolled_courses)
        result += (f"Enrollment finished! Maximum credits: {gathered_credits}."
                   f"\nCourses: {', '.join(sorted_courses)}")

    else:
        result += (f"You need to enroll in more courses! "
                   f"You have to gather {needed_credits - gathered_credits} credits more.")

    return result



print(gather_credits(
    0,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))