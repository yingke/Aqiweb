from flask_script import Manager
from app import creat_app

app =creat_app()

manager = Manager(app=app)

if __name__ == '__main__':
   manager.run()