from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    #return 'Hello, Putotptptptptfla!'
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    #return 'Hello, Putotptptptptfla!'
    return render_template(page_name)


def write_to_file(data):#lo escribe en database de webdeveloping no en el venv
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database2.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/contact2.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again'




#
#     #     error = None
# #     if request.method == 'POST':
# #         if valid_login(request.form['username'],
# #                        request.form['password']):
# #             return log_the_user_in(request.form['username'])
# #         else:
# #             error = 'Invalid username/password'
# #     # the code below is executed if the request method
# #     # was GET or the credentials were invalid
#      return render_template('login.html', error=error)
# @app.route('/about.html')
# def my_about():
#     #return 'Hello, Putotptptptptfla!'
#     return render_template('about.html')
#
# @app.route('/work.html')
# def my_work():
#     #return 'Hello, Putotptptptptfla!'
#     return render_template('work.html')
#
# @app.route('/components.html')
# def my_components():
#     #return 'Hello, Putotptptptptfla!'
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def my_contact():
#     #return 'Hello, Putotptptptptfla!'
#     return render_template('contact.html')
# # @app.route('/favicon.ico')
# # def blog():
# #     return 'wacho piola puirengvuirngiurgnto!'
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dogfeifniji'

