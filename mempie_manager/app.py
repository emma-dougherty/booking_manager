from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.courses_controller import courses_blueprint
from controllers.bookings_controller import bookings_blueprint
from controllers.home_controller import home_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(courses_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(home_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/mempie")
def mempie():
    return render_template('mempie.html')

if __name__ == '__main__':
    app.run()
