import json
import os
from app import create_app
from app.extensions import db
from app.models.culture import Country
from app.utils.maps_api import get_coordinates

app = create_app()

def seed():
    with app.app_context():
        db.create_all()
        
        if Country.query.first():
            print("Database already seeded.")
            return

        json_path = os.path.join(os.path.dirname(__file__), 'data', 'pilot_data.json')
        with open(json_path, 'r') as file:
            data = json.load(file)

        for item in data:
            lat, lng = get_coordinates(item['history_query'])
            country = Country(
                name=item['name'],
                status='Approved',
                food_narrative=item['food_narrative'],
                food_query=item['food_query'],
                history_narrative=item['history_narrative'],
                history_query=item['history_query'],
                culture_narrative=item['culture_narrative'],
                culture_query=item['culture_query'],
                latitude=lat,
                longitude=lng
            )
            db.session.add(country)
            
        db.session.commit()
        print("Pilot data seeded successfully.")

if __name__ == '__main__':
    seed()