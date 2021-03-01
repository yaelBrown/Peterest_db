from flask import Flask

from config.config_mongo import db

users_db = db.users

# create method or something for pulling a string from mongodb