import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

terminal_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)


class Student:

    def __init__(self, name, date_of_birth, sex):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex

    def __str__(self):
        return f'{self.name}'


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.max_students = max_students
        self.__students = []

    def add_student(self, student: Student):
        logger.debug(f'{type(student)} {student}')
        if not isinstance(student, Student):
            logger.warning(f'Wrong type {type(student)}')
            raise TypeError('Not a Student')
        if student in self.__students:
            logger.warning(f'Student {student} already in group {self.title}')
            raise ValueError('Student already in group')
        if len(self.__students) == self.max_students:
            logger.warning(f'Limit of students is {self.max_students}')
            raise Exception(self.max_students)

        self.__students.append(student)
        logger.info(f'Student {student} added to group {self.title}')


if __name__ == '__main__':
    st_1 = Student('Ivan', '01/01/2000', 'M')
    st_2 = Student('Anna', '01/02/2000', 'F')

    st_3 = Student('Ivan1', '01/01/2000', 'M')
    st_4 = Student('Anna1', '01/02/2000', 'F')

    group = Group('Group1', 3)
    try:
        group.add_student(st_1)
        group.add_student(st_1)
        group.add_student('Petro')
        group.add_student(st_2)
        group.add_student(st_3)
        group.add_student(st_4)
    except Exception as e:
        pass