from dotenv import load_dotenv
from app.models import Menu, MenuItem, MenuItemType, Table

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

    table1 = Table(number=1, capacity=10)
    table2 = Table(number=2, capacity=11)
    table3 = Table(number=3, capacity=12)
    table4 = Table(number=4, capacity=13)
    table5 = Table(number=5, capacity=14)
    table6 = Table(number=6, capacity=15)
    table7 = Table(number=7, capacity=16)
    table8 = Table(number=8, capacity=17)
    table9 = Table(number=9, capacity=18)
    table10 = Table(number=10, capacity=19)

    db.session.add_all([table1, table2, table3, table4, table5, table6, table7, table8, table9, table10])
    db.session.commit()
