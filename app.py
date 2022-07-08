from flask import Flask
from controller.customer_controller import cc
from controller.account_controller import ac

# The purpose of this if statement is so that if another file imports this file, then
# the code inside of the if block will not run, since __name__ would not be __main__
# in that situation
if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(cc)
    app.register_blueprint(ac)

    app.run(port=8080, debug=True)