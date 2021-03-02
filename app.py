from flask import Flask, send_from_directory
from flask_cors import CORS

# from controllers.userController import userController
# from controllers.petsController import petsController
# from controllers.dashboardController import dashboardController
# from controllers.guestController import guestController
# from controllers.pictureController import pictureController
from controllers.testController import testController

app = Flask(
  __name__, 
  static_url_path='')
  # static_folder='/static',
  # template_folder='/template')

CORS(app)

# app.register_blueprint(userController, url_prefix='/api/users/')
# app.register_blueprint(petsController, url_prefix='/api/pets/')
# app.register_blueprint(dashboardController, url_prefix='/api/dashboard/')
# app.register_blueprint(guestController, url_prefix='/api/guest/')
# app.register_blueprint(pictureController, url_prefix='/api/pictures/')
app.register_blueprint(testController)

@app.route("/")
def testApi():
  return app.send_static_file('index.html')

@app.route("/test")
def testdb():
  return "0.o"

if __name__ == "__main__":
  app.run(port=5000, debug=True)