import os

from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'app_database.db')
Base = declarative_base()
engine = create_engine(connection_string)  # Here add 'echo=True' if needed
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
    name = Column(String(), nullable=False)
    licks = Column(Integer(), nullable=False)
    image = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Recipe: id={self.id}, name={self.name}, licks={self.licks}, image={self.image}>"


class Step(Base):
    __tablename__ = 'steps'
    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer(), ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipe", backref="steps")
    number = Column(Integer(), nullable=False)
    description = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Step: id={self.id}, recipe_id={self.recipe_id}, number={self.number}, description={self.description}>"


class Timer(Base):
    __tablename__ = 'timers'
    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer(), ForeignKey("recipes.id"), nullable=False)
    recipe = relationship("Recipe", backref="timers")
    name = Column(String(), nullable=False)
    time_val = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"<Timer: id={self.id}, recipe_id={self.recipe_id}, name={self.name}, time_val={self.time_val}>"


Base.metadata.create_all(engine)
