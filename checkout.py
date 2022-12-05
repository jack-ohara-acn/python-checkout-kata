prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

discounts = {
    'A': (3, 130),
    'B': (2, 45)
}

basket = {}

def scan(item: str):
    if item not in prices:
        print(f"ERROR: Item '{item}' not recognised")
        return

    if item in basket:
        basket[item] += 1
    else:
        basket[item] = 1

def scan_many(*items: str):
    for item in items:
        scan(item)

def checkout():
    total_price = 0

    for item, count in basket.items():
        if item in discounts:
            [number_required, new_price] = discounts[item]

            number_of_discounts = count // number_required
            number_of_non_discounts = count % number_required

            total_price += number_of_discounts * new_price
            total_price += number_of_non_discounts * prices[item]
        else:
            total_price += count * prices[item]


    return total_price

def main():
    # scan('A')
    # scan('A')
    # scan('A')
    # scan('X')
    # scan('A')
    # scan('B')
    # scan_many('C', 'B')
    scan_many('A', 'X', 'A','A')

    print(checkout())

if __name__ == "__main__":
    main()
