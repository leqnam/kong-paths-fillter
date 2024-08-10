import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, Integer
from datetime import datetime
from __init__ import db
from sqlalchemy import inspect

class kong_model(db.Model):  # Define the model globally
    __tablename__ = 'kong'
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)
    service_name = db.Column(db.String(200), nullable=False, unique=True)
    yaml         = Column(db.Text, nullable=False)
    def __repr__(self):
        return f"<KongModel id={self.id}>"
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }