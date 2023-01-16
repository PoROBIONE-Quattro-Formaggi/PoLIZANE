from database_init import Session, engine, Ingredient
from sqlalchemy import desc

local_session = Session(bind=engine)

ingredients = local_session.query(Ingredient).order_by(Ingredient.amount).all()

for i in ingredients:
    print(i)

ingredients2 = local_session.query(Ingredient).order_by(desc(Ingredient.amount)).all()

for i in ingredients2:
    print(i)
