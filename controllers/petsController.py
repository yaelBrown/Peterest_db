from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt

from config.dbController import con

import json

import services.petsService as petsService
p = petsService.petsService()

petsController = Blueprint('petsController', __name__)

_nothing = None

@petsController.route('/create', methods=['POST'])
def createPet():
  data = request.get_json()

  newPet = {}
  newPet["owner_id"] = data['owner_id']
  newPet["catOrDog"] = data['catOrDog']
  newPet["name"] = data['name']
  newPet["birthday"] = data['birthday']
  newPet["gender"] = data['gender']
  newPet["pictureUrl"] = data['pictureUrl']

  return p.createPet(newPet)

@petsController.route('/getPet', methods=['GET'])
def getPet():
  data = request.get_json()

  return p.getPet(data["id"])

""" Find all pets by user """
@petsController.route('/getPets', methods=['GET'])
def getPets():
  data = request.get_json()

  pets = data["ids"]
  if len(pets) <= 1:
    return p.getPet(data["ids"])

  return p.getPets(data["ids"])

@petsController.route('/edit', methods=["PUT"])
def editPet():
  data = request.get_json()

  newPetData = {}
  newPetData["owner_id"] = data['owner_id']
  newPetData["catOrDog"] = data['catOrDog']
  newPetData["name"] = data['name']
  newPetData["birthday"] = data['birthday']
  newPetData["gender"] = data['gender']
  newPetData["pictureUrl"] = data['pictureUrl']

  return p.editPet(newPetData)

@petsController.route('/delete', methods=["DELETE"])
def deletePet():
  data = request.get_json()

  return p.deletePet(data["id"])

@petsController.route('/test', methods=['GET'])
def test():
  return "PetsContoller works"