
class Prescription:
    def __init__(self, prescrption_id, appointment_id, medicine_name, dosage,
                 instructions, date_created, date_expires):
        self.prescrption_id = prescrption_id,
        self.appointment_id = appointment_id,
        self.medicine_name = medicine_name,
        self.dosage = dosage,
        self.instructions = instructions,
        self.date_created = date_created,
        self.date_expires = date_expires
