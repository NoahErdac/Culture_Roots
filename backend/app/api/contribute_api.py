from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.culture import Country
from app.utils.validators import validate_submission_payload
from app.utils.sanitization import sanitize_text
from app.utils.maps_api import get_coordinates

contribute_bp = Blueprint('contribute', __name__)

@contribute_bp.route('/submit', methods=['POST'])
def submit_country():
    data = request.get_json()
    
    is_valid, message = validate_submission_payload(data)
    if not is_valid:
        return jsonify({"error": message}), 400
        
    # Attempt to geocode the submitted history location query
    lat, lng = get_coordinates(data['history_query'])
    
    new_submission = Country(
        name=sanitize_text(data['name']),
        status='Pending',
        food_narrative=sanitize_text(data['food_narrative']),
        food_query=sanitize_text(data['food_query']),
        history_narrative=sanitize_text(data['history_narrative']),
        history_query=sanitize_text(data['history_query']),
        culture_narrative=sanitize_text(data['culture_narrative']),
        culture_query=sanitize_text(data['culture_query']),
        latitude=lat,
        longitude=lng
    )
    
    db.session.add(new_submission)
    db.session.commit()
    
    return jsonify({"message": "Submission received and is pending moderation.", "id": new_submission.id}), 201