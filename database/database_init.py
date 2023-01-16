import os

from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'app_database.db')
Base = declarative_base()
engine = create_engine(connection_string, echo=True)
Session = sessionmaker()


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer(), ForeignKey("recipes.id"), nullable=True, default=None)
    recipe = relationship("Recipe", backref="ingredients")
    shop_list_id = Column(Integer(), ForeignKey("shopping_lists.id"), nullable=True, default=None)
    shopping_list = relationship("ShoppingList", backref="ingredients")
    name = Column(String(), nullable=False)
    unit = Column(String(), nullable=False)
    amount = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"<Ingredient: id={self.id}, recipe_id={self.recipe_id}, shop_list_id={self.shop_list_id}, " \
               f"name={self.name}, unit={self.unit}, amount={self.amount}>"


class ShoppingList(Base):
    __tablename__ = 'shopping_lists'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    def __repr__(self):
        return f"<ShoppingList: id={self.id}, name={self.name}>"


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer(), primary_key=True)
    name = Column(String, nullable=False)
    licks = Column(Integer(), nullable=False)
    image = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Recipe: id={self.id}, name={self.name}, licks={self.licks}, image={self.image}>"


Base.metadata.create_all(engine)
