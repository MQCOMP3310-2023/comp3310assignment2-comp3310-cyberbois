from project import db, create_app, models
from project.models import Restaurant, MenuItem

def populate_db():
   # Delete all menu items
    MenuItem.query.delete()

    # Delete all restaurants
    Restaurant.query.delete()

    # Commit the changes
    db.session.commit()
    # Menu for UrbanBurger
    restaurant1 = Restaurant(name="Urban Burger")
    
    session = db.session()
    session.add(restaurant1)
    session.commit()

    menu_item1 = MenuItem(name="French Fries", description="with garlic and parmesan",
                          price="$2.99", course="Appetizer", restaurant=restaurant1)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                          price="$5.50", course="Entree", restaurant=restaurant1)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                          price="$3.99", course="Dessert", restaurant=restaurant1)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Sirloin Burger", description="Made with grade A beef",
                          price="$7.99", course="Entree", restaurant=restaurant1)
    session.add(menu_item4)
    session.commit()

    menu_item5 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                          price="$1.99", course="Beverage", restaurant=restaurant1)
    session.add(menu_item5)
    session.commit()

    menu_item6 = MenuItem(name="Iced Tea", description="with Lemon",
                          price="$.99", course="Beverage", restaurant=restaurant1)
    session.add(menu_item6)
    session.commit()

    menu_item7 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                          price="$3.49", course="Entree", restaurant=restaurant1)
    session.add(menu_item7)
    session.commit()

    menu_item8 = MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                          price="$5.99", course="Entree", restaurant=restaurant1)
    session.add(menu_item8)
    session.commit()

    # Menu for Super Stir Fry
    restaurant2 = Restaurant(name="Super Stir Fry")
    session.add(restaurant2)
    session.commit()

    menu_item1 = MenuItem(name="Chicken Stir Fry", description="with your choice of noodles vegetables and sauces",
                          price="$7.99", course="Entree", restaurant=restaurant2)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(
        name="Peking Duck", description=" a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", restaurant=restaurant2)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Spicy Tuna Roll", description="Spicy roll of tuna and vegetables",
                          price="$4.99", course="Entree", restaurant=restaurant2)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Nepali Momo ", description="Traditional Nepali dumplings filled with meat or vegetables",
                          price="10.99", course="Entree", restaurant=restaurant2)
    session.add(menu_item4)
    session.commit()

    menu_item5 = MenuItem(name="Beef Noodle Soup", description="A hearty soup with tender beef and noodles",
                         price="$9.99", course="Entree", restaurant=restaurant2)
    session.add(menu_item5)
    session.commit()

    menu_item6 = MenuItem(name="Ramen", description="Japanese noodle soup dish with various toppings",
                          price="$9.99", course="Entree", restaurant=restaurant2)
    session.add(menu_item6)
    session.commit()

    # Menu for Panda Garden
    restaurant3 = Restaurant(name="Panda Garden")
    session.add(restaurant3)
    session.commit()

    menu_item1 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                          price="", course="", restaurant=restaurant3)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", price="$11.99", course="Appetizer", restaurant=restaurant3)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner", price="$15.99", course="Appetizer", restaurant=restaurant3)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                          price="$15.99", course="Entree", restaurant=restaurant3)
    session.add(menu_item4)
    session.commit()

    # Menu for Thyme for That
    restaurant4 = Restaurant(name="Thyme for That Vegetarian Cuisine ")
    session.add(restaurant4)
    session.commit()

    menu_item1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                          price="$19.99", course="Dessert", restaurant=restaurant4)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                          price="$23.99", course="Entree", restaurant=restaurant4)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Honey Boba Shaved Snow",
                          description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price="$17.99", course="Dessert", restaurant=restaurant4)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Cauliflower Manchurian",
                          description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price="$24.99", course="Entree", restaurant=restaurant4)
    session.add(menu_item4)
    session.commit()

    menu_item5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                          price="$10.99", course="Entree", restaurant=restaurant4)
    session.add(menu_item5)
    session.commit()

    # Menu for Tony's Bistro
    restaurant5 = Restaurant(name="Tony\'s Bistro ")
    session.add(restaurant5)
    session.commit()

    menu_item1 = MenuItem(name="Shellfish Tower", description="A stack of Delicious Shellfish",
                          price="$24.99", course="Entree", restaurant=restaurant5)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Chicken and Rice", description="Grilled Chicken and served with hot basmati Rice",
                          price="$10.99", course="Entree", restaurant=restaurant5)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                          price="$17.99", course="Entree", restaurant=restaurant5)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                          description="choclate and mint ice cream that feels refreshing on a hot day", price="$8.99", course="Dessert", restaurant=restaurant5)
    session.add(menu_item4)
    session.commit()

    menu_item5 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                          price="$13.87", course="Entree", restaurant=restaurant5)
    session.add(menu_item5)
    session.commit()

    # Menu for Andala's
    restaurant6 = Restaurant(name="Andala\'s")
    session.add(restaurant6)
    session.commit()

    menu_item1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                          price="$19.87", course="Entree", restaurant=restaurant6)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                          price="$22.65", course="Entree", restaurant=restaurant6)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                          price="$14.99", course="Appetizer", restaurant=restaurant6)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Nigiri SamplerMaguro, Sake, Hamachi, Unagi, Uni, TORO!",
                          description="A delicious assortment of nigiri sushi including Maguro (tuna), Sake (salmon), Hamachi (yellowtail), Unagi (grilled eel), Uni (sea urchin), and TORO (fatty tuna)!", price="$34.99", course="Entree", restaurant=restaurant6)
    session.add(menu_item4)
    session.commit()

    # Menu for Auntie Ann's
    restaurant7 = Restaurant(name="Auntie Ann\'s Diner ")
    session.add(restaurant7)
    session.commit()

    menu_item9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                          price="$8.99", course="Entree", restaurant=restaurant7)
    session.add(menu_item9)
    session.commit()

    menu_item1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                          price="$16.76", course="Dessert", restaurant=restaurant7)

    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                          price="$23.99", course="Entree", restaurant=restaurant7)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Morels on toast (seasonal)",
                          description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$12.99", course="Appetizer", restaurant=restaurant7)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                          price="$18.99", course="Entree", restaurant=restaurant7)
    session.add(menu_item4)
    session.commit()

    menu_item5 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                          price="$16.99", course="Entree", restaurant=restaurant7)
    session.add(menu_item5)
    session.commit()

    menu_item6 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                          price="$13.99", course="Dessert", restaurant=restaurant7)
    session.add(menu_item6)
    session.commit()

    # Menu for Cocina Y Amor
    restaurant8 = Restaurant(name="Cocina Y Amor ")
    session.add(restaurant8)
    session.commit()

    menu_item1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                          price="$13.89", course="Entree", restaurant=restaurant8)
    session.add(menu_item1)
    session.commit()

    menu_item2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                          price="$14.99", course="Appetizer", restaurant=restaurant8)
    session.add(menu_item2)
    session.commit()

    menu_item3 = MenuItem(name="Chantrelle Toast",
                          description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms", price="$12.99", course="Appetizer", restaurant=restaurant8)
    session.add(menu_item3)
    session.commit()

    menu_item4 = MenuItem(name="Guanciale Chawanmushi",
                          description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$18.99", course="Dessert", restaurant=restaurant8)
    session.add(menu_item4)
    session.commit()

    menu_item5 = MenuItem(name="Lemon Curd Ice Cream Sandwich",
                          description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", price="$13.99", course="Dessert", restaurant=restaurant8)
    session.add(menu_item5)
    session.commit()

    menu_item6 = MenuItem(name="Szechuan Ribeye Steak",
                          description="Served with wilted spinach and garlic", price="$49.99", course="Entree", restaurant=restaurant8)
    session.add(menu_item6)
    session.commit()

    print("Added menu items to the database.")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
            db.create_all()
            populate_db()