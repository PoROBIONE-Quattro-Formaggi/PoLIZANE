from database.database_init import Ingredient, ShoppingList, Recipe, Step, Timer, Session, engine

local_session = Session(bind=engine)


# Add ==================================================================================
def add(db_object):
    local_session.add(db_object)
    local_session.commit()


# Delete ==================================================================================
def delete(db_object):
    local_session.delete(db_object)
    local_session.commit()


# Getters ==================================================================================

def get_ingredient_by_id(ingredient_id):
    return local_session.query(Ingredient).filter(Ingredient.id == ingredient_id).first()


def get_ingredients_in_fridge():
    return local_session.query(Ingredient).filter(
        Ingredient.recipe_id.is_(None), Ingredient.shop_list_id.is_(None)).all()


def get_ingredients_with_recipe_id(recipe_id):
    return local_session.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).all()


def get_ingredients_with_recipe_obj(recipe: Recipe):
    return get_ingredients_with_recipe_id(recipe.id)


def get_ingredients_with_shop_list_id(list_id):
    return local_session.query(Ingredient).filter(Ingredient.shop_list_id == list_id).all()


def get_ingredients_with_shop_list_obj(shop_list: ShoppingList):
    return get_ingredients_with_shop_list_id(shop_list.id)


def get_recipe_of_the_ingredient(ingredient: Ingredient):
    return local_session.query(Recipe).filter(Recipe.id == ingredient.recipe_id).first()


def get_shopping_list_of_the_ingredient(ingredient):
    return local_session.query(ShoppingList).filter(ShoppingList.id == ingredient.shop_list_id).first()


def get_steps_with_recipe_id(recipe_id):
    return local_session.query(Step).filter(Step.recipe_id == recipe_id).all()


def get_steps_with_recipe_obj(recipe: Recipe):
    return get_steps_with_recipe_id(recipe.id)


def get_recipe_of_the_step(step: Step):
    return local_session.query(Recipe).filter(Recipe.id == step.recipe_id).first()


def get_timers_with_recipe_id(recipe_id):
    return local_session.query(Timer).filter(Timer.recipe_id == recipe_id).all()


def get_timers_with_recipe_obj(recipe: Recipe):
    return get_timers_with_recipe_id(recipe.id)


def get_recipe_of_the_timer(timer: Timer):
    return local_session.query(Recipe).filter(Recipe.id == timer.recipe_id).first()


# Updates ==================================================================================
def update(db_object):
    if isinstance(db_object, Ingredient):
        __update_ingredient(db_object)
    elif isinstance(db_object, Recipe):
        __update_recipe(db_object)
    elif isinstance(db_object, ShoppingList):
        __update_shopping_list(db_object)
    elif isinstance(db_object, Step):
        __update_step(db_object)
    elif isinstance(db_object, Timer):
        __update_timer(db_object)


def __update_ingredient(ingredient: Ingredient):
    ingredient_to_update = local_session.query(Ingredient).filter(Ingredient.id == ingredient.id).first()
    ingredient_to_update.id = ingredient.id
    ingredient_to_update.recipe_id = ingredient.recipe_id
    ingredient_to_update.shop_list_id = ingredient.shop_list_id
    ingredient_to_update.name = ingredient.name
    ingredient_to_update.unit = ingredient.unit
    ingredient_to_update.amount = ingredient.amount
    local_session.commit()


def __update_recipe(recipe: Recipe):
    recipe_to_update = local_session.query(Recipe).filter(Recipe.id == recipe.id).first()
    recipe_to_update.id = recipe.id
    recipe_to_update.name = recipe.name
    recipe_to_update.licks = recipe.licks
    recipe_to_update.image = recipe.image
    local_session.commit()


def __update_shopping_list(shop_list: ShoppingList):
    list_to_update = local_session.query(ShoppingList).filter(ShoppingList.id == shop_list.id).first()
    list_to_update.id = shop_list.id
    list_to_update.name = shop_list.name
    local_session.commit()


def __update_step(step: Step):
    step_to_update = local_session.query(Step).filter(Step.id == step.id).first()
    step_to_update.id = step.id
    step_to_update.recipe_id = step.recipe_id
    step_to_update.number = step.number
    step_to_update.description = step.description
    local_session.commit()


def __update_timer(timer: Timer):
    timer_to_update = local_session.query(Timer).filter(Timer.id == timer.id).first()
    timer_to_update.id = timer.id
    timer_to_update.recipe_id = timer.recipe_id
    timer_to_update.name = timer.name
    timer_to_update.time_val = timer.time_val
