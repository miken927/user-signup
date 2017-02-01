#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
#import re

#USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
#PASSWORD_RE = re.compile(r"^.{3,20}$")
#EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# html boilerplate for the top of every page
page_header = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Signup</title>
        <style type="text/css">
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
        <h1>
            <a href="/">User Signup</a>
        </h1>
    """

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def build_form(username, username_error, password_error, email, email_error):
    signup_form = """
        <form method="post">
        <table>
            <tr>
                <td>Username:</td> <td><input type="text" name="username" value="{0}"/><span class="error">{1}</span></td>
            </tr>
            <tr>
                <td>Password:</td> <td><input type="password" name="password"/><span class="error">{2}</span></td>
            </tr>
            <tr>
                <td>Re-enter password:</td> <td><input type="password" name="verify_password"/></td>
            <tr>
                <td>E-mail (optional):</td> <td><input name="email" value="{3}"/><span class="error">{4}</span></td>
            </tr>
        </table>
        <input type="submit" value="Sign Up!"/>
        </form>
    """.format(username, username_error, password_error, email, email_error)

    return signup_form

def check_input(field, input):
    if len(input) > 20 or len(input) < 3:
        return(" " + field + " must be between 3 and 20 characters!")
    for char in input:
        if char == " ":
            return(" " + field + " cannot contain spaces!")
    return("")


class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = page_header + build_form("", "", "", "", "") + page_footer
        self.response.write(content)

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        email = self.request.get("email")
        email_error = ""

        username_error = check_input("Username", username)

        if password != verify_password:
            password_error = " Passwords must match!"
        else:
            password_error = check_input("Password", password)

        if username_error == "" and password_error == "" and email_error == "":
            content = page_header + "<h1>Welcome " + username + "!</h1>"
        else:
            content = page_header + build_form(username, username_error, password_error, email, email_error) + page_footer

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
