from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt

from config.dbController import con

import json
import sys

guestController = Blueprint('guestController', __name__)

_nothing = None

# returns random pictures for guests not Users
# comments disabled
@guestController.route('/', methods=['GET'])
def getHome():
  # https://www.mysqltutorial.org/select-random-records-database-table.aspx
  # https://www.w3schools.com/sql/sql_join.asp
  return "https://images.pexels.com/photos/617278/pexels-photo-617278.jpeg", 200

@guestController.route('/test', methods=['GET'])
def testGuest():
  return "Guest Controller is working", 200