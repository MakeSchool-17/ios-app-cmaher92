from peewee import *

db = SqliteDatabase('students.db')
# creates Sqlite database


class Student(Model):
    # model always a singular name, because it represents one item
    username = CharField(max_length=255, unique=True)
    # charfield holds characters, unique says that usernames can't be the same
    points = IntegerField(deault=0)
    # inter fields hold integers, defaults to 0 if nothing set

    class Meta:
        database = db


# .create()
# .select()
# .save() update a row
# .get() get an instance
# .

# list of dictionaries
students = [
    {'username': 'kennethlove',
     'points': 4888},
    {'username': 'chalkers',
     'points': 11912},
    {'username': 'joykesten2',
     'points': 7263},
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()


def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now is {0.username}").format(top_student())
