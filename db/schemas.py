from pydantic import BaseModel, constr
from datetime import date

{
    "title": "PatientSchema",
    "type": "object",
    "properties": {
        "name": {
            "title": "Name",
            "minLength": 1,
            "maxLength": 255,
            "type": "string"
        },
        "dob": {
            "title": "Dob",
            "type": "string",
            "format": "date"
        },
        "gender": {
            "title": "Gender",
            "minLength": 1,
            "maxLength": 10,
            "type": "string"
        }
    },
    "required": [
        "name",
        "dob",
        "gender"
    ]
}