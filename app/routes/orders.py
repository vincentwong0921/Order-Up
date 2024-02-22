from flask import Blueprint, render_template
from flask_login import login_required
from app.models import MenuItem
from app.forms import TableAssignmentForm

bp = Blueprint("orders", __name__, url_prefix="")

@bp.route('/')
@login_required
def index():
    form = TableAssignmentForm()
    items = MenuItem.query.all()
    return render_template('orders.html', items=items, form=form)

