import json

from flask_bcrypt import Bcrypt
from config.dbController import con

cur = con.cursor()

class userService: 

  def login(self, u, p):
    try:
      sql = "SELECT * FROM users where username = %s"
      cur.execute(sql, u) # get the user info from database
      dbUser = cur.fetchone()
    finally:
      print("\n")

    isLoggedIn = Bcrypt.check_password_hash(None, dbUser["pw"], p)

    if isLoggedIn:
      out = {}
      out["id"] = dbUser["id"]
      out["username"] = dbUser["username"]
      out["isAdmin"] = dbUser["isAdmin"]
      out["name"] = dbUser["NAME"]

      return out
    else:
      return False

  def register(self, nU): 
    try:
      _ = {"test": "cookies"}
      sql = "INSERT INTO users (username, pw, isAdmin, name, settings) values (%s, %s, %s, %s, %s)"
      cur.execute(sql, (nU["username"], nU["password"], int(nU["isAdmin"]), nU["name"], json.dumps(_)))
      con.commit()

      return nU
    except Exception as e:
      print(e)
      return False
    finally:
      print("\n")

  def edit(self, u):
    try:
      sql = "SELECT * FROM users WHERE id = %s"
      cur.execute(sql, u["id"])
      dbUser = cur.fetchone()

      if dbUser == None:
        return "User ID not found"

      u["pw"] = Bcrypt.generate_password_hash(None, u["pw"], 12)

      sql = "UPDATE users SET isAdmin=%s, name=%s, pw=%s, username=%s, settings=%s where id=%s"
      cur.execute(sql, (u["isAdmin"], u["name"], u["pw"], u["username"], u["settings"], u["id"]))
      con.commit()
      
      out = {}
      out["id"] = u["id"]
      out["username"] = u["username"]
      out["isAdmin"] = u["isAdmin"]
      out["name"] = u["name"]

      return out
    except Exception as e:
      print(e)
      return False
    finally:
      print("\n")

  def delete(self, u):
    try:
      sql = "DELETE FROM users WHERE id=%s"
      cur.execute(sql, u["id"])
      con.commit()
      
      return f"User with ID: {u['id']}, was deleted"
    except Exception as e:
      print(e)
      return False
    finally:
      print("\n")  
    