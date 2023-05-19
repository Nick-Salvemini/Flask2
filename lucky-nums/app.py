from flask import Flask, request, redirect, render_template, flash, session, jsonify
from models import db, connect_db, LuckyNumber

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky-number'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


# *****************************
# RESTFUL API
# *****************************

@app.route('/api/get_lucky_num', methods=['POST'])
def get_lucky_num():
