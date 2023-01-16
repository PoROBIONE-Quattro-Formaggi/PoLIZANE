from database_init import Ingredient, ShoppingList, Recipe, Step, Timer, Session, engine

local_session = Session(bind=engine)


def add(db_object):
    local_session.add(db_object)
    local_session.commit()


def delete(db_object):
    local_session.delete(db_object)
    local_session.commit()


def get_fridge_ingredients():
    return local_session.query(Ingredient).filter(Ingredient.recipe_id is None and Ingredient.shop_list_id is None)


def get_ingredients_with_recipe_id(recipe_id):
    return local_session.query(Ingredient).filter(Ingredient.recipe_id == recipe_id)


def get_ingredients_with_recipe_obj(recipe):
    return get_ingredients_with_recipe_id(recipe.id)


def get_ingredients_with_recipe_obj(recipe):
    return local_session.query(Ingredient).filter(Ingredient.recipe == recipe)


def get_ingredients_with_shop_list_id(list_id):
    return local_session.query(Ingredient).filter(Ingredient.shop_list_id == list_id)


def get_ingredients_with_shop_list_obj(shop_list):
    return local_session.query(Ingredient).filter(Ingredient.shopping_list == shop_list)


def get_recipe_of_the_ingredient(ingredient):
    return local_session.query(Recipe).filter(Recipe.id == ingredient.recipe_id).first()


def get_shopping_list_of_the_ingredient(ingredient):
    return local_session.query(ShoppingList).filter(ShoppingList.id == ingredient.shop_list_id).first()
