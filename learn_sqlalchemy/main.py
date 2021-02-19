"""
Demo of the ORM functionality of SQLAlchemy.
"""
from models import Product
from db_session import session


def main():
    """Demo SQLAlchemy"""
    add_one()
    add_many()

    print_milk()
    print_products()


def add_one():
    """Add the product toothpaste."""
    toothpaste = Product(name="Toothpaste", price=179)
    session.add(toothpaste)
    session.commit()


def add_many():
    """Add multiple products in one go."""
    session.bulk_save_objects(
        [
            Product(name="Shampoo", price=215),
            Product(name="Milk", price=113),
            Product(name="Cheese", price=499),
        ]
    )
    session.commit()


def print_milk():
    """Query one product and print it."""
    milk = session.query(Product).filter_by(name="Milk").first()
    print(milk)


def print_products():
    """Query all products and loop over results."""
    products = session.query(Product).all()
    for p in products:
        print(f"{p.name}: {p.price}")


if __name__ == "__main__":
    main()
