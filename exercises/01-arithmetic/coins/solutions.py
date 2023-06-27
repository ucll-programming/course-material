def coins(amount):
    five_coins = amount // 5
    amount_after_five = amount - 5 * five_coins
    two_coins = amount_after_five // 2
    one_coins = amount_after_five - 2 * two_coins
    return five_coins + two_coins + one_coins
