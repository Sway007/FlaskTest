from flask import Flask
from flask_script import Manager, Command

app = Flask(__name__)
manager = Manager(app)

# class Hello(Command):
#     '''
#     print hello
#     '''

#     def run(set):
#         print('Hello')

@manager.command
def hello():
    'Just say hello'
    print('hello')


if __name__=='__main__':

    # manager.add_command('hello', Hello())
    manager.run()