annual_fee = int(input())

price_shoes = annual_fee * 0.60
price_clothes = price_shoes * 0.80
price_ball = price_clothes / 4
price_accessories = price_ball / 5

total_cost = annual_fee + price_shoes + price_clothes + price_ball + price_accessories
print(f"{total_cost:.2f}")