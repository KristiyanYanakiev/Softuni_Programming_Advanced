n = int(input())

students_grades = {}

for _ in range(n):
    name, grade_as_str = input().split()
    grade = float(grade_as_str)

    if name not in students_grades.keys():
        students_grades[name] = [grade]
    else:
        students_grades[name].append(grade)


for key, value in students_grades.items():
    avg = sum(value) / len(value)
    formatted_list = f"{' '.join([f'{i:.2f}' for i in value])}"

    print(f"{key} -> {formatted_list} (avg: {avg:.2f})")





