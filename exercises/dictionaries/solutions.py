def ingredients():
    return {
        'chocolate': '250g',
        'eggs': '5',
        'sugar': '125g',
        'flour': '75g',
        'butter': '175g',
    }


def desktop(catalog, components):
    total = 0
    for component in components:
        total += catalog[component]
    return total


def rankings(participants):
    result = {}
    for index in range(len(participants)):
        participant = participants[index]
        ranking = index + 1
        result[participant] = ranking
    return result


def sell(stock, model):
    stock[model] -= 1
    if stock[model] == 0:
        del stock[model]


def group_by_first_letter(strings):
    result = {}
    for string in strings:
        key = string[0].upper()
        result.setdefault(key, []).append(string)
    return result


def counts(xs):
    result = {}
    for x in xs:
        result[x] = result.get(x, 0) + 1
    return result


def inverse_lookup(dictionary, value):
    result = []
    for k, v in dictionary.items():
        if v == value:
            result.append(k)
    return result


def combine(d1, d2):
    result = {}
    for key, value in d1.items():
        if value in d2:
            result[key] = d2[value]
    return result


def cake(stock, recipe_ingredients):
    amounts = []
    for ingredient, amount in recipe_ingredients.items():
        amounts.append(stock.get(ingredient, 0) // amount)
    return min(amounts)


def orbit_chain(orbits, start):
    current = start
    result = [start]
    while current in orbits:
        current = orbits[current]
        result.append(current)
    return result


def sell2(stock, model, size):
    if model not in stock:
        return False
    available_sizes = stock[model]
    if size not in available_sizes:
        return False
    available_sizes[size] -= 1
    if available_sizes[size] == 0:
        del available_sizes[size]
    if len(available_sizes) == 0:
        del stock[model]
    return True


def election_winner(votes):
    vote_counts = {}
    winner = None
    winner_vote_count = 0
    for vote in votes:
        updated_count = vote_counts.get(vote, 0) + 1
        vote_counts[vote] = updated_count
        if updated_count > winner_vote_count:
            winner = vote
            winner_vote_count = updated_count
    return winner
