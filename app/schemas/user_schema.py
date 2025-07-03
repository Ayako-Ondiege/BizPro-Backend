# app/schemas/user_schema.py

from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "customer", "storekeeper", "supplier"]))

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
