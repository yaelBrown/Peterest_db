from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt

from config.dbController import con

import json
import jwt

import services.userService as userService
u = userService.userService()

userController = Blueprint('userController', __name__)

_rounds = 12

@userController.route('/login', methods=['POST'])
def login():
  data = request.get_json()

  username = data["username"]
  password = data["password"]

  out = u.login(username, password)

  if out != False: 
    out = jwt.encode(out, 'secret', algorithm='HS256')

  return {"data": str(out)[2:len(out)-1]}, 200

@userController.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  
  if data == None: 
    return {"msg": "Empty Request"}, 422

  if "isAdmin" not in data.keys():
    data["isAdmin"] = False

  newUser = {}
  newUser["username"] = data["username"]
  newUser["password"] = Bcrypt.generate_password_hash(None, data["password"], _rounds)
  newUser["isAdmin"] = data["isAdmin"]
  newUser["name"] = data["name"]

  nU = u.register(newUser)

  if nU == False:
    return {"msg": "Unable to create new user"}, 422
  else: 
    return {"msg": f"New user {newUser['username']} added", "data": nU }, 200 

@userController.route('/edit', methods=["PUT"])
def edit():
  data = request.get_json()
  print(data)
  if data == None:
    return {"msg": "Invalid User Request"}, 422

  eU = u.edit(data)

  return {"msg": f"edited {data['username']}", "data": eU}, 200

@userController.route('/delete', methods=["DELETE"])
def delete():
  data = request.get_json()

  dU = u.delete(data)

  if dU == False: 
    return {"msg": f"Unable to delete {data['id']}"}, 422 
  else:
    return {"msg": f"deleted user: {data['id']}"}, 200