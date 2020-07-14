from appliances import DishWasher, Washer, Dryer, Refrigerator, CoffeeMaker, CanOpener, Stove

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

cranky_canopener = CanOpener("black")
cranky_canopener.open_can()

# added the stove for fun
ge_stove = Stove("Stainless Steel")
ge_stove.bake_cookies()
