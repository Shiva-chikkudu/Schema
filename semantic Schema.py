from dataclasses import dataclass, field
from dataclasses import dataclass

# define classes
class person:
    name: str
    
    @dataclass
    class person:
        name: str


    @dataclass
    class student(person):
        student_id: str


    @dataclass
    class teacher(person):
        employee_id: int


    @dataclass
    class course:
        course_code: str


    @dataclass
    class Department:
        name: str
        
    @dataclass
    class principal(person):
        employee_id: int
        
    @dataclass
    class attendor(person):
        employee_id: int
        
# define Relationships

class KnowledgeGraph:
    student: dict = field(default_factory=dict)
    teacher: dict = field(default_factory=dict)     
    course: dict = field(default_factory=dict) 
    departments: dict = field(default_factory=dict)
    enrollments: list = field(default_factory=list)
    teachings: list = field(default_factory=list)
    course_departments: list = field(default_factory=list)
    
    def add_student(self,student):
        self.student[student.student_id] = student
        
    def add_teacher(self, teacher):
        self.teacher[teacher.employee_id] = teacher
        
    def add_course(self, course):
        self.course[course.course_code] = course
        
    def add_Department(self, Department):
        self.departments[Department.name] = Department
        
    def enroll(self, student_id, course_code):
        self.enrollments.append((student_id, course_code)) 
        
    def assign_teacher(self, employee_id, course_code):
        self.teachings.append((employee_id, course_code))
        
    def assign_course_to_department(self, course_code, department_name): 
        self.course_departments.append((course_code, department_name)) 
        
# query the Semantic Relationships

def course_for_student(self, student_id):
    return [
        self.courses[code].title
        for sid, code in self.enrollments
        if sid == student_id
    ]          

def teacher_for_course(self, course_code):
    return [
        self.teachers[emp_id].name
        for emp_id, code in self.teachings
        if code == course_code
    ]       
    
def course_for_departments(self, department_name):
    return [
        self.course[course_code].name
        for course_code, name in self.departments
        if name == department_name
    ] 
    
# make and create the instances

kg = KnowledgeGraph()


# Repair the graph model and student definition before adding data

@dataclass
class Person:
    name: str

@dataclass
class Student(Person):
    student_id: str

@dataclass
class Teacher(Person):
    employee_id: str

@dataclass
class Course:
    course_code: str
    title: str

@dataclass
class Department:
    name: str

@dataclass
class KnowledgeGraph:
    students: dict = field(default_factory=dict)
    teachers: dict = field(default_factory=dict)
    courses: dict = field(default_factory=dict)
    departments: dict = field(default_factory=dict)
    enrollments: list = field(default_factory=list)
    teachings: list = field(default_factory=list)
    course_departments: list = field(default_factory=list)

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_teacher(self, teacher):
        self.teachers[teacher.employee_id] = teacher

    def add_course(self, course):
        self.courses[course.course_code] = course

    def add_Department(self, department):
        self.departments[department.name] = department

    def enroll(self, student_id, course_code):
        self.enrollments.append((student_id, course_code))

    def assign_teacher(self, employee_id, course_code):
        self.teachings.append((employee_id, course_code))

    def assign_course_to_department(self, course_code, department_name):
        self.course_departments.append((course_code, department_name))

    def course_for_student(self, student_id):
        return [
            self.courses[code].title
            for sid, code in self.enrollments
            if sid == student_id
        ]

    def teacher_for_course(self, course_code):
        return [
            self.teachers[emp_id].name
            for emp_id, code in self.teachings
            if code == course_code
        ]

    def course_for_departments(self, department_name):
        return [
            self.courses[code].title
            for code, name in self.course_departments
            if name == department_name
        ]

# Recreate the graph instance so its fields are actual dicts, not dataclass Field objects
kg = KnowledgeGraph()

# Now it works
kg.add_student(Student("Shankar", "34"))
kg.add_teacher(Teacher("Shymala", "G35"))
kg.add_course(Course("CS301", "Artificial Intelligence"))
kg.add_Department(Department("Computer Science"))

# add semantic Relationships
kg.enroll("34", "CS301")
kg.assign_teacher("G35", "CS301")
kg.assign_course_to_department("CS301", "Computer Science")

print(kg.course_for_student("34"))
print(kg.teacher_for_course("CS301"))    