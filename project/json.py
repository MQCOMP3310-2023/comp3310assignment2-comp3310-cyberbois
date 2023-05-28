from flask import Blueprint, jsonify
from .models import Restaurant, MenuItem
from sqlalchemy import text
from . import db
import json as pyjs

json = Blueprint('json', __name__)

#JSON APIs to view Restaurant Information
@json.route('/restaurant/<restaurant_id>/menu/JSON')
def restaurant_menu_json(restaurant_id):
    items = db.session.execute(
    text('SELECT * FROM menu_item WHERE restaurant_id = :restaurant_id'),
    {'restaurant_id': restaurant_id}
)
    items_list = [ i._asdict() for i in items ]
    return pyjs.dumps(items_list)


@json.route('/restaurant/<restaurant_id>/menu/<int:menu_id>/JSON')
def menu_item_json(restaurant_id, menu_id):
    menu_item = db.session.execute(text('select * from menu_item where id = ' + str(menu_id) + ' limit 1'))
    items_list = [ i._asdict() for i in menu_item ]
    return pyjs.dumps(items_list)

@json.route('/restaurant/JSON')
def restaurants_json():
    restaurants = db.session.execute(text('select * from restaurant'))
    rest_list = [ r._asdict() for r in restaurants ]
    return pyjs.dumps(rest_list)


