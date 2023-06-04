from flask import Blueprint, jsonify
from .models import Restaurant, MenuItem
from sqlalchemy import text
from . import db
import json as pyjs

json = Blueprint('json', __name__)

#JSON APIs to view Restaurant Information
@json.route('/restaurant/<restaurant_id>/menu/JSON')
def restaurant_menu_json(restaurant_id): # Renamed function 'restaurantMenuJSON' to match regular expression
    query = text('SELECT * FROM menu_item WHERE restaurant_id = :restaurant_id')
    items = db.session.execute(query, {'restaurant_id': restaurant_id})
    # Query previously depended on user-provided value: which used string formatting for restaurant_id
    # Vulnerability to SQL Injection Attack fixed through parameters and placeholders
    items_list = [ i._asdict() for i in items ]
    return pyjs.dumps(items_list)


@json.route('/restaurant/<restaurant_id>/menu/<int:menu_id>/JSON')
def menu_item_json(restaurant_id, menu_id): # Renamed function 'menuItemJSON' to match regular expression
    query = text('SELECT * FROM menu_items WHERE id = :menu_id LIMIT 1')
    menu_item = db.session.execute(query, {'menu_id': menu_id}).fetchone()
    # Query previously depended on user-provided value: which used string formatting for menu_id
    # Vulnerability to SQL Injection Attack fixed through parameters and placeholders
    items_list = [ i._asdict() for i in menu_item ]
    return pyjs.dumps(items_list)

@json.route('/restaurant/JSON')
def restaurants_json(): # Renamed function 'restaurantsJSON' to match regular expression
    restaurants = db.session.execute(text('select * from restaurant'))
    rest_list = [ r._asdict() for r in restaurants ]
    return pyjs.dumps(rest_list)