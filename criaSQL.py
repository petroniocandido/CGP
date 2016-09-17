#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from DomainModel import db

db.create_all()
