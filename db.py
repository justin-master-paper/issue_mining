#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: db.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Sun Nov  1 13:15:09 2015
#########################################################################

import os
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')

client = MongoClient(MONGO_URI)

db = client.sun_flower

