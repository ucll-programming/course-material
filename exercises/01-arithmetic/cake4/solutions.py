def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    limited_by_eggs = eggs // eggs_per_cake
    limited_by_flour = flour // flour_per_cake
    limited_by_butter = butter // butter_per_cake
    limited_by_sugar = sugar // sugar_per_cake
    return min(limited_by_eggs, limited_by_flour, limited_by_butter, limited_by_sugar)
