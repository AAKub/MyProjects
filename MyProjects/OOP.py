class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_to_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        if not self.grades:
            return 0
        grade_list = []
        for i in self.grades.values():
                grade_list.extend(i)
        return round(sum(grade_list) / len(grade_list), 1)

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.get_avg_grade()}
Курсы в процессе изучения: {self.courses_in_progress}
Завершённые курсы: {self.finished_courses}
'''

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_grade() < other.get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_grade() <= other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_grade() == other.get_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
    '''


class Lecturer(Mentor):
    grades = {}

    def get_avg_grade(self):
        if not self.grades:
            return 0
        grade_list = []
        for i in self.grades.values():
            grade_list.extend(i)
        return round(sum(grade_list) / len(grade_list), 1)

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.get_avg_grade()}
'''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_grade() < other.get_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_grade() <= other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_grade() == other.get_avg_grade()


# some_reviewer = Reviewer('Alex','Kub')
# print(some_reviewer)
# best_lecturer = Lecturer('Ruoy', 'Eman')
# best_lecturer.courses_attached += ['Java','Python']

# some_student = Student('Some', 'Buddy','some_gender')
# some_student.courses_in_progress += ['Java','Python']
# some_student.rate_to_lecturer(best_lecturer, 'Python', 10)
# some_student.rate_to_lecturer(best_lecturer, 'Python', 10)
# some_student.rate_to_lecturer(best_lecturer, 'Java', 5)
# print(best_lecturer.grades)
# print(best_lecturer)

some_student = Student('Some', 'Buddy', 'some_gender')
some_student.courses_in_progress += ['Java', 'Python']
some_student.finished_courses += ['C+']
some_reviewer = Reviewer('Mark', 'Pol')
some_reviewer.courses_attached += ['Java', 'Python']
some_reviewer.rate_hw(some_student, 'Java', 10)
# some_reviewer.rate_hw(some_student, 'Java', 5)
# some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer2 = Reviewer('Phil', 'Morris')
some_reviewer2.courses_attached += ['Python']
# some_reviewer2.rate_hw(some_student, 'Java', 10)
# print(some_student)

some_student2 = Student('Tom', 'Kirbi', 'some_gender')
some_student2.courses_in_progress += ['Java', 'Python']
some_student2.finished_courses += ['C+']
some_reviewer = Reviewer('Mark', 'Pol')
some_reviewer.courses_attached += ['Java', 'Python']
some_reviewer.rate_hw(some_student2, 'Python', 10)
# some_reviewer.rate_hw(some_student2, 'Java', 10)
some_reviewer2 = Reviewer('Phil', 'Morris')
some_reviewer2.courses_attached += ['Python']
# some_reviewer2.rate_hw(some_student, 'Java', 10)
print(some_student)
print(some_student2)
print(some_student >= some_student2)

some_lecturer = Lecturer('Ruoy', 'Eman')
some_lecturer.courses_attached += ['Java', 'Python']
some_lecturer2 = Lecturer('San', 'Oman')
some_lecturer2.courses_attached += ['Java', 'Python']
# some_student.rate_to_lecturer(some_lecturer, 'Python', 10)
# some_student.rate_to_lecturer(some_lecturer, 'Python', 10)
# some_student2.rate_to_lecturer(some_lecturer, 'Python', 8)
# some_student2.rate_to_lecturer(some_lecturer, 'Python', 9)
# print(some_lecturer2.grades)
# print(some_lecturer)
# print(some_lecturer == some_lecturer2)


def get_avg_grade_students(students_list, course):
    sum_list = []
    for i in students_list:
        if isinstance(i, Student) and course in i.grades:
            for j in i.grades.get(course):
                sum_list.append(j)
    print(sum_list)
    return f'Cредняя оценка за домашние задания по всем студентам по курсу {course}: {round(sum(sum_list) / len(sum_list), 1)}'


students_list = [some_student, some_student2]
# print(get_avg_grade_students(students_list, 'Python'))


def get_avg_grade_lecturers(lecturers_list, course):
    sum_list = []
    for i in lecturers_list:
        if isinstance(i, Lecturer) and course in i.grades:
            for j in i.grades.get(course):
                sum_list.append(j)
    print(sum_list)
    return f'Cредняя оценка за лекции всех лекторов по курсу {course}: {round(sum(sum_list) / len(sum_list), 1)}'


lecturers_list = [some_lecturer, some_lecturer2]
# print(get_avg_grade_lecturers(lecturers_list, 'Python'))