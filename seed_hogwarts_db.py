from hogwarts_models import Student, Wand, House, Course, Enrollment, Teacher

def seed_data():
    # initialize all the houses
    gryff = House(name="Gryffindor", mascot="Lion")
    snakes = House(name="Slytherin", mascot="Snake")
    hufflepuff = House(name="Hufflepuff", mascot="Badger")
    ravenclaw = House(name="Ravenclaw",  mascot="Eagle")
    gryff.put()
    snakes.put()
    hufflepuff.put()
    ravenclaw.put()

    # initialize all the classes
    potions = Course(name="Potions", location="dungeon")
    dada = Course(name="Defense Against the Dark Arts", location="3C")
    transfiguration = Course(name="Transfiguration", location="Class 34")
    potions.put()
    dada.put()
    transfiguration.put()

    # create some teachers for those classes
    snape = Teacher(name="Severus Snape", years_experience=5, class_taught=potions.name)
    snape.put()
    moody = Teacher(name="Alastor Moody", years_experience=1, class_taught=dada.name)
    moody.put()
    mcgonagall = Teacher(name="Minerva McGonagall", years_experience=12, class_taught=transfiguration.name)
    mcgonagall.put()

    # initialize some students
    ron = Student(student_num=423491377, first_name ="Ron", last_name = "Weasley", house_name=gryff.name)
    harry = Student (student_num=423491782, first_name ="Harry", last_name = "Potter", house_name=gryff.name)
    hermione = Student(student_num=423491249, first_name="Hermione", last_name="Granger", house_name=gryff.name)
    malfoy = Student(student_num=42391043, first_name="Draco", last_name="Malfoy", house_name=snakes.name)
    crabbe = Student(student_num=42391122, first_name="Vincent", last_name="Crabbe", house_name=snakes.name)
    goyle = Student(student_num=42391063, first_name="Gregory", last_name="Goyle", house_name=snakes.name)
    ron.put()
    harry.put()
    hermione.put()
    malfoy.put()
    crabbe.put()
    goyle.put()

    # create wands for the students
    ron_wand=Wand(length = 14.0, material = "willow", core="unicorn", owner_num=ron.student_num).put()
    harry_wand=Wand(length = 11.0, material = "holly", core="phoenix feather", owner_num=harry.student_num).put()
    hermione_wand = Wand(length=10.75, material="vinewood", core="dragon heartstring", owner_num=hermione.student_num).put()

    # enroll some students in defense against the dark arts
    Enrollment(student_num=ron.student_num, course_name=dada.name).put()
    Enrollment(student_num=harry.student_num, course_name=dada.name).put()
    Enrollment(student_num=hermione.student_num, course_name=dada.name).put()

    # enroll some students in potions
    Enrollment(student_num=hermione.student_num, course_name=potions.name).put()
    Enrollment(student_num=ron.student_num, course_name=potions.name).put()
    Enrollment(student_num=malfoy.student_num, course_name=potions.name).put()
    Enrollment(student_num=crabbe.student_num, course_name=potions.name).put()
    Enrollment(student_num=goyle.student_num, course_name=potions.name).put()

    # enroll some students in tranfirguration
    Enrollment(student_num=harry.student_num, course_name=transfiguration.name).put()
    Enrollment(student_num=hermione.student_num, course_name=transfiguration.name).put()
    Enrollment(student_num=crabbe.student_num, course_name=transfiguration.name).put()
    Enrollment(student_num=goyle.student_num, course_name=transfiguration.name).put()
