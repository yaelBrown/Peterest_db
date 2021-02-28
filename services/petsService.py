from config.dbController import con

cur = con.cursor()

class petsService: 

  def createPet(self, nP):
    try: 
      sql = "INSERT INTO pets (owner_id, catOrDog, name, birthday, gender, pictureUrl) values (%s, %s, %s, %s, %s, %s)"
      cur.execute(sql, (nP["owner_id"], nP["catOrDog"], nP["name"], nP["birthday"], nP["gender"], nP["pictureUrl"]))
      con.commit()

      return {"msg": "Successfully Created new pet", "data": f"{nP}"}, 200
    except Exception as e: 
      print(e)
      return {"msg": "Unable to add {}: {}".format(newPet["name"], e)}, 400
    finally:
      print("\n")

  def getPet(self, nP):
    try: 
      sql = "SELECT * FROM pets where id = %s"
      cur.execute(sql, nP["id"])
      dbPet = cur.fetchone()

      return {"msg": "Pet found", "data": dbPet}, 200
    except Exception as e:
      print(e)
      return {"msg": "{} was not found: {}".format(data["id"], e)}, 400
    finally:
      print("\n")

  def getPets(self, nP):
    try: 
      sql = "SELECT * FROM pets WHERE id IN ("
      for pId in nP["ids"]:
          sql += "{}, ".format(pId)
      sql = sql[0:-2] + ")"

      cur.execute(sql)
      rows = cur.fetchmany(size=len(nP["ids"]))

      return {"msg": "Found the pets", "data": rows}, 200
    except Exception as e:
      print(e)
      return {"msg": "{} was not found: {}".format(pet, e)}
    finally: 
      print("\n")

  def editPet(self, nP):
    try: 
      sql = "SELECT * FROM pets Where id = %s"
      cur.execute(sql, data["id"])
      dbPet = cur.fetchone()

      if dbPet == None:
        return {"msg": "{} was not found :(".format(nP["name"])}

      sql = "UPDATE pets SET owner_id=%s, catOrDog=%s, name=%s, birthday=%s, gender=%s, pictureUrl=%s where id=%s"
      cur.execute(sql, (nP["owner_id"], nP["catOrDog"], nP["name"], nP["birthday"], nP["gender"], nP["pictureUrl"], nP["id"]))
      con.commit()

      return {"msg": "Updated {}".format(nP["name"]), "newPetData": newPetData}, 200
    except Exception as e: 
      print(e)
      return {"msg": "unable to update {}: {}".format(nP["name"], e)}, 400
    finally: 
      print("\n")

  def deletePet(self, nP):
    try: 
      sql = "SELECT * FROM pets Where id = %s"
      cur.execute(sql, nP["id"])
      dbPet = cur.fetchone()

      if dbPet == None:
        return {"msg": "{} was not found :(".format(nP["name"])}

      sql = "DELETE FROM pets WHERE id=%s"
      cur.execute(sql, nP["id"])
      con.commit()

      return {"msg": "{} was deleted :(".format(nP["name"])}
    except Exception as e: 
      print(e)
      return {"msg": "unable to delete pet {}".format(e)}, 400
    finally: 
      print("\n")