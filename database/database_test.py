import os

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'app_database.db')
Base = declarative_base()
engine = create_engine(connection_string, echo=True)
Session = sessionmaker()


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer(), nullable=True, default=None)
    shop_list_id = Column(Integer(), nullable=True, default=None)
    name = Column(String(), nullable=False)
    unit = Column(String(), nullable=False)
    amount = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"<Ingredient: id={self.id}, recipe_id={self.recipe_id}, shop_list_id={self.shop_list_id}, " \
               f"name={self.name}, unit={self.unit}, amount={self.amount}>"
