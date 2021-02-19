"""
Demo of models Product & Review (with placeholders for exercises).
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer:
    """YOUR CODE (don't forget to inherit from Base)"""


class Order:
    """YOUR CODE (don't forget to inherit from Base)"""


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)  # in cents
    reviews = relationship("Review", backref="product")

    def __repr__(self):
        return f'Product(name="{self.name}", price={self.price})'


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    rating = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))

    def __repr__(self):
        return (
            f'Review(title="{self.title}", '
            f'rating={self.rating}, '
            f'product_id={self.product_id})'
        )
