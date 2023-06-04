from flask import Blueprint, render_template, request, flash, redirect, url_for
from project.models import User
from .models import Restaurant, MenuItem
from flask_login import login_required, current_user
from sqlalchemy import asc, desc
from . import db

main = Blueprint('main', __name__)
show_all = 'main.show_restaurants'
show_menu_all = 'main.show_menu'
warning_msg  = 'You do not have permission to access this page.'

# Show all restaurants
@main.route('/')
@main.route('/restaurant/')
def show_restaurants():
    search_query = request.args.get('search_query', '') # Get search query from URL
    sort_order = request.args.get('sort_order', 'A-Z') # Get sort order from URL and user input selection

    if search_query: # If there is a search query, filter the restaurants by name
        restaurants = db.session.query(Restaurant).filter(Restaurant.name.ilike(f'%{search_query}%')) # ilike is case-insensitive
    else:
        restaurants = db.session.query(Restaurant) # Otherwise, just get all restaurants

    if sort_order == 'A-Z': # If sorting order request chosen is A-Z
        restaurants = restaurants.order_by(asc(Restaurant.name)) # Sort by ascending alphabetical order (asc()), starting from names A-Z
    elif sort_order == 'Z-A': # If sorting order requese chosen is Z-A
        restaurants = restaurants.order_by(desc(Restaurant.name)) # Sort by descending alphabetical order (desc()), starting from names Z-A

    return render_template('restaurants.html', restaurants=restaurants, search_query=search_query, sort_order=sort_order)


@main.route('/restaurant/new/', methods=['GET', 'POST']) # Create a new restaurant
@login_required # Only logged in owners and admins can access this route
def new_restaurant():
    if current_user.role not in ['owner', 'admin']: # If the user is not an owner or admin, deny access
        flash(warning_msg, 'error') # Flash an error message
        return redirect(url_for(show_all))

    if request.method == 'POST':
        new_restaurant = Restaurant(name=request.form['name'], owner_id=current_user.id) 
        db.session.add(new_restaurant)
        db.session.commit()
        flash('New Restaurant %s Successfully Created' % new_restaurant.name)
        return redirect(url_for(show_all))
    else:
        return render_template('newRestaurant.html')

@main.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST']) # Edit a restaurant
@login_required
def edit_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id) # Get the restaurant from the database

    if current_user.role not in ['owner', 'admin']:
        flash(warning_msg, 'error')
        return redirect(url_for(show_all))

    if request.method == 'POST':
        restaurant.name = request.form['name']
        db.session.commit()
        flash('Restaurant Successfully Edited %s' % restaurant.name)
        return redirect(url_for(show_all))
    else:
        return render_template('editRestaurant.html', restaurant=restaurant)


@main.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST']) # Delete a restaurant
@login_required
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if current_user.role not in ['owner', 'admin']:
        flash(warning_msg, 'error')
        return redirect(url_for(show_all))

    if request.method == 'POST':
        db.session.delete(restaurant)
        db.session.commit()
        flash('%s Successfully Deleted' % restaurant.name)
        return redirect(url_for(show_all))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurant)

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
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if current_user.role not in ['owner', 'admin']:
        flash(warning_msg, 'error')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))

    if request.method == 'POST':
        new_item = MenuItem(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            course=request.form['course'],
            restaurant_id=restaurant_id
        )
        db.session.add(new_item)
        db.session.commit()
        flash('New Menu Item "%s" Successfully Created' % new_item.name)
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant=restaurant)


# Edit a menu item
@main.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_menu_item(restaurant_id, menu_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    edited_item = MenuItem.query.get_or_404(menu_id)

    if current_user.role not in ['owner', 'admin']:
        flash(warning_msg, 'error')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))

    if request.method == 'POST':
        edited_item.name = request.form['name']
        edited_item.description = request.form['description']
        edited_item.price = request.form['price']
        edited_item.course = request.form['course']
        db.session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant=restaurant, item=edited_item)


# Delete a menu item
@main.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_menu_item(restaurant_id, menu_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    item_to_delete = MenuItem.query.get_or_404(menu_id)

    if current_user.role not in ['owner', 'admin']:
        flash(warning_msg, 'error')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))

    if request.method == 'POST':
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for(show_menu_all, restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant=restaurant, item=item_to_delete)

