from . import db
import enum

class Post(db.Model):
    """Simple post model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Status(enum.Enum):
    OPEN = "Open"
    CLOSED  = "Closed"
    LIMIT = "Limited"

class Country(db.Model):
    """Country model"""
    __tablenbame__="country"
    id = db.Column(db.Integer, primary_key=True)
    iso = db.Column(db.String)
    name = db.Column(db.String)
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