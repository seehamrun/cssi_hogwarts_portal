from google.appengine.ext import ndb

# House is a standalone entity, it doesn't have any dependencies on our other
# models
class House(ndb.Model):
      name = ndb.StringProperty(required=True)
      mascot = ndb.StringProperty(required=False)

class Student(ndb.Model):
    student_num =  ndb.IntegerProperty(required=True)
    first_name =  ndb.StringProperty(required=True)
    last_name =  ndb.StringProperty(required=True)
    # house_name is the house this student belongs to so there is a
    # corresponding House entry with House.name == Student.house_name
    house_name = ndb.StringProperty(required=True)

class Wand(ndb.Model):
    length = ndb.FloatProperty(required=True)
    material = ndb.StringProperty(required=True)
    core = ndb.StringProperty(required=True)
    # owner_num is the num of the person who this wand belongs to so there is a
    # corresponding Student entry with Student.student_num == Wand.owner_num
    owner_num = ndb.IntegerProperty(required=True)

# Course is a standalone entity, it doesn't have any dependencies on our other
# models
class Course(ndb.Model):
      name = ndb.StringProperty()
      location = ndb.StringProperty()

# Enrollment tells us which student is enrolled in each class
# student_num is the num of the student so there is a corresponding Student entry
# with Student.student_num == Enrollment.student_num
# course_name is the name of the class they are in, so there is a corresponding
# Course entry with Course.name == Enrollment.course_name
class Enrollment(ndb.Model):
      student_num = ndb.IntegerProperty(required=True)
      course_name = ndb.StringProperty(required=True)

# Generally, teachers teach more than one class, as a super stretch, we can
# make it a repeated field, but we will not be doing that right now.
class Teacher(ndb.Model):
    name = ndb.StringProperty(required=True)
    years_experience = ndb.IntegerProperty()
    class_taught = ndb.StringProperty()
