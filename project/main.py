from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Restaurant, MenuItem
from flask_login import login_required, current_user
from sqlalchemy import asc
from . import db

main = Blueprint('main', __name__)
show_all = 'main.show_restaurants'
show_menu_all = 'main.show_menu'

# Show all restaurants


@main.route('/')
@main.route('/restaurant/')
def show_restaurants():
    restaurants = db.session.query(Restaurant).order_by(asc(Restaurant.name))
    return render_template('restaurants.html', restaurants=restaurants)

# Create a new restaurant


@main.route('/restaurant/new/', methods=['GET', 'POST'])
@login_required
def new_restaurant():
    if request.method == 'POST':
        new_restaurant = Restaurant(name=request.form['name'])
        db.session.add(new_restaurant)
        flash('New Restaurant %s Successfully Created' % new_restaurant.name)
        db.session.commit()
        return redirect(url_for(show_all))
    else:
        return render_template('newRestaurant.html')

# Edit a restaurant


@main.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit_restaurant(restaurant_id):
    edited_restaurant = db.session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_restaurant.name = request.form['name']
            flash('Restaurant Successfully Edited %s' % edited_restaurant.name)
            return redirect(url_for(show_all))
    else:
        return render_template('editRestaurant.html', restaurant=edited_restaurant)


# Delete a restaurant
@main.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_restaurant(restaurant_id):
    restaurant_to_delete = db.session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        db.session.delete(restaurant_to_delete)
        flash('%s Successfully Deleted' % restaurant_to_delete.name)
        db.session.commit()
        return redirect(url_for(show_all, restaurant_id=restaurant_id))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurant_to_delete)

# Show a restaurant menu


@main.route('/restaurant/<int:restaurant_id>/')
@main.route('/restaurant/<int:restaurant_id>/menu/')

def show_menu(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = db.session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return render_template('menu.html', items=items, restaurant=restaurant)


# Create a new menu item
@main.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
@login_required
def new_menu_item(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['name'], description=request.form['description'],
                            price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        db.session.add(new_item)
        db.session.commit()
        flash('New Menu %s Item Successfully Created' % (new_item.name))
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id, restaurant=restaurant)

# Edit a menu item


@main.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_menu_item(restaurant_id, menu_id):

    edited_item = db.session.query(MenuItem).filter_by(id=menu_id).one()
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_item.name = request.form['name']
        if request.form['description']:
            edited_item.description = request.form['description']
        if request.form['price']:
            edited_item.price = request.form['price']
        if request.form['course']:
            edited_item.course = request.form['course']
        db.session.add(edited_item)
        db.session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=edited_item, restaurant=restaurant)


# Delete a menu item
@main.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_menu_item(restaurant_id, menu_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    item_to_delete = db.session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=item_to_delete, restaurant=restaurant)
