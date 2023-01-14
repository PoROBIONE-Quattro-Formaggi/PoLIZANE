from database_init import Session, engine, Ingredient

local_session = Session(bind=engine)

ingredient_to_update = local_session.query(Ingredient).filter(Ingredient.id == 1).first()
ingredient_to_update.shop_list_id = 1

local_session.commit()
