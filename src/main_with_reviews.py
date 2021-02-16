from models import Product, Review
from db_session import session


def main():
    """Demo table relationships"""
    beer = Product(name="Beer", price=150)
    session.add(beer)
    session.commit()

    add_one_review(beer)

    print_reviews(beer)


def add_one_review(product):
    """Add a review and save it in the database."""
    review = Review(title="Great taste", rating=5, product_id=product.id)
    session.add(review)
    session.commit()


def print_reviews(beer):
    """Show related table's data"""
    print(beer)
    print("Product reviews:", beer.reviews)


if __name__ == "__main__":
    main()
