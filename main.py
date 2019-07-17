#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import os
import jinja2
from hogwarts_models import Student, Wand, House, Course, Enrollment, Teacher
from seed_hogwarts_db import seed_data

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/welcome.html")
        self.response.write(template.render())

class HouseHandler(webapp2.RequestHandler):
    def get(self):
        hogwarts_houses = House.query().order(House.name).fetch()
        start_template = jinja_env.get_template("templates/houselist.html")
        self.response.write(start_template.render({'house_info' : hogwarts_houses}))

class StudentsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/studentlist.html")
        values = {}
        house_input = self.request.get("house")

        if house_input != "":
            # There should only be 1 house with that name, so the [0] at the end
            # gets the 1 element that is in the list, otherwise we have a list of house_infos
            values["house_info"] = House.query(House.name==house_input).fetch()[0]
            values["student_list"] = Student.query(Student.house_name==house_input).fetch()
            print(values["house_info"])
        else:
            # No house, so get all of the students
            values["student_list"] = Student.query().fetch()

        print(values["student_list"])
        self.response.write(template.render(values))


# This handler just creates some initial data in our datastore
class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/houses', HouseHandler),
    ('/students', StudentsHandler),
    ('/seed_data', LoadDataHandler)
], debug=True)
