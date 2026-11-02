from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.culture import Country

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/review/<int:submission_id>', methods=['PUT'])
def review_submission(submission_id):
    data = request.get_json()
    new_status = data.get('status')
    
    if new_status not in ['Approved', 'Rejected']:
        return jsonify({"error": "Invalid status."}), 400
        
    submission = Country.query.get_or_404(submission_id)
    submission.status = new_status
    db.session.commit()
    
    return jsonify({"message": f"Submission {submission_id} marked as {new_status}."}), 200

@admin_bp.route('/admin/pending', methods=['GET'])
def get_pending():
    pending = Country.query.filter_by(status='Pending').all()
    return jsonify([p.to_dict() for p in pending]), 200