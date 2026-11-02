from app.extensions import db
from datetime import datetime

class Country(db.Model):
    __tablename__ = 'countries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending') 
    
    # Subjective Data - Food
    food_narrative = db.Column(db.Text, nullable=False)
    food_query = db.Column(db.String(255), nullable=False) 
    
    # Subjective Data - History
    history_narrative = db.Column(db.Text, nullable=False)
    history_query = db.Column(db.String(255), nullable=False)
    
    # Subjective Data - Culture (Norms, rules, religion, etiquette)
    culture_narrative = db.Column(db.Text, nullable=False)
    culture_query = db.Column(db.String(255), nullable=False)
    
    # Geospatial Data 
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "food_narrative": self.food_narrative,
            "food_query": self.food_query,
            "history_narrative": self.history_narrative,
            "history_query": self.history_query,
            "culture_narrative": self.culture_narrative,
            "culture_query": self.culture_query,
            "latitude": self.latitude,
            "longitude": self.longitude
        }