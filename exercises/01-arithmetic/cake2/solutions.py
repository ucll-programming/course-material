def cake2(eggs, flour):
    limited_by_eggs = eggs // 5
    limited_by_flour = flour // 250
    return min(limited_by_eggs, limited_by_flour)
