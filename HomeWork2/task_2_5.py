"""
A. Create manually a list containing product prices (10–20 products).
Display these prices on one line, separated by commas, the price should be displayed as (<r> rub <kk> kop)
<r> руб <kk> коп, for example "5 руб 04 коп".
B. Display prices sorted in ascending order, do not create a new list
(prove that the list object remains the same after sorting).
C. Create a new list containing the same prices, but sorted in descending order.
D. Display the prices of the five most expensive items.
Can you display the prices of these products in ascending order with a minimum of code?
"""
commodity_prices = [57.8, 46.51, 97, 34.05, 123.99, 4, 1000, 234.75, 0.45,
                    1.99, 30500, 0.5, 10.03, 10.65, 1000.55, 10, 124, 123]
# A.
last = len(commodity_prices) - 1
for i, price in enumerate(commodity_prices):
    rubles, penny = int(price), int(price * 100 % 100)
    if i == last:
        print(f'{rubles} руб {penny:02d} коп')
    else:
        print(f'{rubles} руб {penny:02d} коп', end=',')

# B.
print(id(commodity_prices))
commodity_prices.sort()
print(commodity_prices)
print(id(commodity_prices))

# C.
prices_sorted_in_descending_order = sorted(commodity_prices, reverse=True)
print(prices_sorted_in_descending_order)
print(id(prices_sorted_in_descending_order), id(commodity_prices))

# D.
print(*reversed(prices_sorted_in_descending_order[:5]))
