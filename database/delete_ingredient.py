from database_test import Session, engine, Ingredient

local_session = Session(bind=engine)

ingredient_to_delete = local_session.query(Ingredient).filter(Ingredient.id == 10).first()
local_session.delete(ingredient_to_delete)

local_session.commit()
