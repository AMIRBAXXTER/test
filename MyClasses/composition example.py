# composition
class Question:
    def __init__(self, question: str, answer: list):
        self.question = question
        self.answer = answer


class ExamPaper:
    def __init__(self):
        self.question = Question("what is your name?", ["amir", "mmd"])

    def __str__(self):
        return f"{self.question.question}\n{self.question.answer}"


x = ExamPaper()
print(x)
print("=" * 40)


# -----------------------------------------------------------------------------
# aggregation
class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"{self.name}:{self.student_id}"


class University:
    def __init__(self, students: list):
        self.students = students


st = [Student("amir", 55), Student("mmd", 56)]
un = University(st)
for s in un.students:
    print(s)
