from flask import Flask, request, Blueprint, jsonify

from config.config_mongo import db

test_db = db.test

# create method or something for pulling a string from mongodb

testController = Blueprint('testController', __name__)

@testController.route('/test', methods=['GET'])
def test():
  return test_db.find_one({})['msg']