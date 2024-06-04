# views/admin.py
from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')


@admin_bp.route('/admin')
def admin_home():
    return 'Admin Home Page'
