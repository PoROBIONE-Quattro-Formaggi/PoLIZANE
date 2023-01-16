from database_init import Ingredient, Session, engine

# generating some test values
test_ingredient = Ingredient(name="test ingredient", unit="g", amount=1)
test_ingredient2 = Ingredient(name="test ingredient2", unit="g", amount=2)

local_session = Session(bind=engine)
local_session.add(test_ingredient)
local_session.add(test_ingredient2)
local_session.commit()
