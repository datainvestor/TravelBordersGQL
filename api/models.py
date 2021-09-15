from . import db
import enum

class Status(enum.Enum):
    OPEN = "Open"
    CLOSED  = "Closed"
    LIMIT = "Limited"

class Country(db.Model):
    """Country model"""
    __tablenbame__="country"
    id = db.Column(db.Integer, primary_key=True)
    iso = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "iso": self.iso,
            "name": self.name,
        }

class Border(db.Model):
    """Border model that keeps status"""
    __tablenbame__="border"
    id = db.Column(db.Integer, primary_key=True)
    origin_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    destination_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    status = db.Column(db.Enum(Status))
    def to_dict(self):
        return {
            "id": self.id,
            "origin_id": self.origin_id,
            "destination_id": self.destination_id,
            "status": self.status
        }