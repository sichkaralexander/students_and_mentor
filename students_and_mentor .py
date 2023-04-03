class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def rate_lecturer(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'

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
		res = f'Имя: {self.name} \n' \
			f'Фамилия: {self.surname}'
		return res
 
 
class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.grades= {} 
		
	def _get_avg_grade(self):
		sum_grades = 0
		count = 0
		for coerce in self.grades.values():
			sum_grades += sum(course)
			count += len(course)
			return sum_grades / count

	def __str__(self):
		res = f'Имя: {self.name} \n' \
				f'Фамилия: {self.surname} \n' \
				f'Средняя оценка: {self._get_avg_grade()}'
		return res

	def __lt__(self, other_lecturer):
		res =self._get_avg_grade() < other_lecturer._get_avg_grade()
		return res

	def __eq__():
	
		pass

	def __gte__():
		pass




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']
next_student = Student('Some', 'Name', 'm')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']

cool_reviwer = Reviewer('Some', 'Name')
cool_reviwer.coursees_attached = ['Python']
cool_reviwer.coursees_attached = ['Git']
cool_reviwer.rate_hw(best_student, 'Python', 6)
cool_reviwer.rate_hw(best_student, 'Python', 9)
cool_reviwer.rate_hw(best_student, 'Python', 8)
cool_reviwer.rate_hw(best_student, 'Git', 10)
cool_reviwer.rate_hw(best_student, 'Git', 24)

cool_reviwer.rate_hw(next_student, 'Python', 5)
cool_reviwer.rate_hw(next_student, 'Python', 6)
cool_reviwer.rate_hw(next_student, 'Python', 8)
cool_reviwer.rate_hw(next_student, 'Git', 10)
cool_reviwer.rate_hw(next_student, 'Git', 5)

cool_lecturer = Lecturer('Some', 'Name')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

next_lecturer = Lecturer('Some', 'Name')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']

best_student .rate_lecturer (cool_lecturer, 'Python', 3)
best_student .rate_lecturer (cool_lecturer, 'Git', 12)

next_student .rate_lecturer (next_lecturer, 'Python', 6)
next_student .rate_lecturer (next_lecturer, 'Git', 10)
print(cool_reviwer)


student_list = [best_student, next_student]

def get_avg_student_grade(student_list, course):
	total_sum = 0
	for student in student_list:
		for c, grades_list in student.grades.items():
			if c == course:
				total_sum += sum(grades_list) / len(grades_list)
	return round(total_sum / len(student_list), 2)

print(get_avg_student_grade(student_list, 'Python'))










