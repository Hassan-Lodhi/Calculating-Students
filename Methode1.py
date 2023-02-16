total_students = input('Total # of Students in class? ')
math_students = input('Total # of Math Students in class? ')
bio_students = input('Total # of Bio Students in Class? ')

total_students_excluding_mathBio = int(total_students) - int(math_students) - int(bio_students)
print(f'Total student Without Math and Bio {total_students_excluding_mathBio} ')

print(f'Total students Including Math and Bio {total_students}')
