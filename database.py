from dotenv import load_dotenv
from app.models import Menu, MenuItem, MenuItemType

load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    db.session.add_all([employee, beverages, entrees, sides])
    db.session.commit()

    dinner = Menu(name="Dinner")
    db.session.add(dinner)
    db.session.commit()

    fries = MenuItem(name="French fries", price=3.50, menu_id=dinner.id, menu_type_id=sides.id)
    drp = MenuItem(name="Dr. Pepper", price=1.0, menu_id=dinner.id, menu_type_id=beverages.id)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, menu_id=dinner.id, menu_type_id=entrees.id)

    db.session.add_all([dinner, fries, drp, jambalaya])
    db.session.commit()
