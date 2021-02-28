"""
picture
  id
  conversationId
  authorId
  datetime
  caption
  imgUrl
  likes
  pet_id
"""

from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt
from datetime import datetime

from config.dbController import con

import json
import sys
import random
import math

pictureController = Blueprint('pictureController', __name__)

_nothing = None

# dynamically get one or many pictures of pets
@pictureController.route('/getPics')
def getPics():
  query = {}
  try:
    data = request.get_json()
    qStr = ""
    qVal = ""

    for k, v in data.items():
      if v != None:
        query[k] = v
        qStr = k
        qVal = v

    with con.cursor() as cur:
      sql = f"SELECT * FROM pictures WHERE {qStr} = {qVal}"
      cur.execute(sql)
      rows = cur.fetchall()

    out = []
    for row in rows:
      out.append(row)

    print(query)
    print(out)
    return {"data": out}, 200
  except Exception as e:
    return {"msg": "Unable to get picture(s): {}".format(e)}, 400
  finally:
    print("\n")

@pictureController.route('/addPic', methods=['POST'])
def addPictures():
  now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

  try:
    data = request.get_json()

    newPic = {}
    newPic["comments"] = []
    newPic["author_id"] = data["author_id"]
    newPic["caption"] = data["caption"]
    newPic["imgUrl"] = data["imgUrl"]
    newPic["pet_id"] = data["pet_id"]

    print(newPic)

    with con.cursor() as cur:
      sql = "INSERT INTO pictures (comments, author_id, dt, caption, imgUrl, likes, pet_id) VALUES (%s, %s, %s, %s, %s, 0, %s)"
      cur.execute(sql, (newPic["comments"], newPic["author_id"], now, newPic["caption"], newPic["imgUrl"], newPic["pet_id"]))
      con.commit()
  except Exception as e:
    return {"msg": "Unable to add picture: {}".format(e)}, 400
  finally:
    print("\n")

  return {"msg": "New picture added!"}, 200

@pictureController.route('/editPic', methods=['PUT'])
def editPictures():
  try:
    data = request.get_json()

    editedPic = {}
    editedPic["id"] = data["id"]
    editedPic["caption"] = data["caption"]
    editedPic["pet_id"] = data["pet_id"]

    with con.cursor() as cur:
      sql = "UPDATE pictures SET caption=%s, pet_id=%s WHERE id = %s"
      cur.execute(sql, (editedPic["caption"], editedPic["pet_id"], editedPic["pet_id"]))
      con.commit()

    return {"msg": f"Updated picture with ID: {editedPic['id']}", "pet_id": f"{editedPic['pet_id']}", "caption": f"{editedPic['caption']}"}
  except Exception as e:
    return {"msg": f"Unable to update picture with id of {editedPic['id']}"}
  finally:
    print("\n")

@pictureController.route('/deletePic', methods=['DELETE'])
def deletePicture():
  try:
    data = request.get_json()

    with con.cursor() as cur:
      sql = "DELETE FROM pictures WHERE id = %s"
      cur.execute(sql, (data["id"]))
      con.commit()

    return {"msg": f"Deleted picture with id {data['id']}"}
  except Exception as e:
    return {"msg": f"Unable to delete picture with id {data['id']}"}
  finally:
    print("\n")

@pictureController.route('/comments', methods=['GET', 'PUT', 'DELETE'])
def pictureComments():
  try:
    data = request.get_json()

    pId = data["id"]
    cIdx = data["commentIndex"]
    cContent = data["commentContent"]

    def getComments(pictureId):
      with con.cursor() as cur:
        sql = f"SELECT comments FROM pictures WHERE ID = {pictureId}"
        cur.execute(sql)
        temp = cur.fetchone()

        return temp

    def saveComments(pictureId, cmts):
      with con.cursor() as cur:
        sql = f"INSERT INTO pictures (comments) VALUES ({cmts}) WHERE ID = {pictureId}"

    comments = getComments(pId)

    if request.method == 'GET':
      out = {}
      out["id"] = pId
      out["comments"] = comments

      return out, 200
    elif request.method == 'PUT':
      if cIdx is None:
        comments.append(cContent)
      else:
        comments.pop(cIdx)
        comments.insert(cIdx, cContent)

      saveComments(pId, comments)

      out = {}
      out["msg"] = f"Successfully added comment at index: {cIdx}"
      out["id"] = pId
      out["comment"] = cContent

      return out, 200
    elif request.method == 'DELETE':
      comments.pop(cIdx)
      saveComments(pId, comments)

      out = {}
      out["msg"] = f"Successfully deleted comment at index: {cIdx}"
      out["id"] = pId

      return out, 200
    else:
      return {"msg": "Method must either be GET, PUT, or DELETE"}, 400
  except Exception as e:
    return {"msg": f"Unable to modify comments to this picture with id: {pId}"}, 400
  finally:
    print("\n")

@pictureController.route('/test', methods=['GET'])
def testPictures():
  return "Picture controller works", 200


# Dynamic logic for getting pictures could be converted and used in petsController