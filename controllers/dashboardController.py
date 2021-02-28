from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt

from config.dbController import con

import json
import sys

dashboardController = Blueprint('dashboardController', __name__)

_nothing = None

@dashboardController.route('/', methods=['GET'])
def getHome():
  return "Dashboard Controller home", 200

@dashboardController.route('/test', methods=['GET'])
def testDashboard():
  return "Dashboard controller works", 200