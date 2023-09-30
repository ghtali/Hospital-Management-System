
from marshmallow import Schema, fields, validate

class PatientSchema(Schema):
    id = fields.Int(dump_only=True)  # Should not be set during creation, so it's dump_only
    name = fields.Str(required=True, validate=validate.Length(min=1))
    dob = fields.Date(required=True)
    gender = fields.Str(required=True, validate=validate.OneOf(["male", "female", "other"]))
