def cake3(eggs, flour, butter, sugar):
    limited_by_eggs = eggs // 5
    limited_by_flour = flour // 250
    limited_by_butter = butter // 200
    limited_by_sugar = sugar // 250
    return min(limited_by_eggs, limited_by_flour, limited_by_butter, limited_by_sugar)
