from flask import Blueprint, jsonify
from app.models.culture import Country
from app.utils.maps_api import generate_google_maps_url

public_bp = Blueprint('public', __name__)

@public_bp.route('/countries', methods=['GET'])
def get_approved_countries():
    countries = Country.query.filter_by(status='Approved').all()
    
    result = []
    for c in countries:
        c_dict = c.to_dict()
        c_dict['food_map_url'] = generate_google_maps_url(c.food_query)
        c_dict['history_map_url'] = generate_google_maps_url(c.history_query)
        c_dict['culture_map_url'] = generate_google_maps_url(c.culture_query)
        result.append(c_dict)
        
    return jsonify(result), 200