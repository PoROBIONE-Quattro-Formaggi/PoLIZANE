from database_test import Ingredient, engine, Session

local_session = Session(bind=engine)

# get all
ingredients = local_session.query(Ingredient).all()

for i in ingredients:
    print(i)

# get one
ingredient = local_session.query(Ingredient).filter(Ingredient.id == 1).first()
print(ingredient)
