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

# initialize values
username = ""
email = ""
username_error = ""
password_error = ""
email_error = ""

signup_form = """
<form method="post">
    <table>
        <tr>
            <td>Username:</td> <td><input type="text" name="username" value="{0}"/>{1}</td>
        </tr>
        <tr>
            <td>Password:</td> <td><input type="password" name="password"/>{2}</td>
        </tr>
        <tr>
            <td>Re-enter password:</td> <td><input type="password" name="verify_password"/></td>
        <tr>
            <td>E-mail:</td> <td><input type="email" name="email" value="{3}"/>{4}</td>
        </tr>
    </table>
    <input type="submit" value="Sign Up!"/>
</form>
""".format(username, username_error, password_error, email, email_error)

class welcome(webapp2.RequestHandler):
    def post(self):
        self.request.get("username")
        self.response.write("Welcome " + username + "!")


class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = page_header + signup_form + page_footer
        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        self.response.write("Hello " + username)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', welcome)
], debug=True)
