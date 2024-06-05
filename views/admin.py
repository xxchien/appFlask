# views/admin.py
import logging

from flask import Blueprint, request, url_for

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin')
def admin_home():
    return 'Admin Home Page'


@admin_bp.route('/')
def admin_name_home():
    return "admin_name_home"


@admin_bp.app_errorhandler(404)
def handle_api_error(ex):
    if request.path.startswith(f'{url_for('admin.admin_name_home')}'):
        logging.error('Admin Blueprint Error Handler Invoked: %s', ex)
        return '展示未找到页面Blueprint admin_bp.app_errorhandler'
    else:
        return "其他页面"
