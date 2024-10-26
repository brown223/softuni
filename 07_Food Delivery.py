chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegetarian_menu = 8.15
delivery_cost = 2.50

total_chicken = chicken_menu * price_chicken_menu
total_fish = fish_menu * price_fish_menu
total_vegetarian = vegetarian_menu * price_vegetarian_menu

total_menus_price = total_chicken + total_fish + total_vegetarian
dessert_price = total_menus_price * 0.20
final_price = total_menus_price + dessert_price + delivery_cost

print(f"{final_price:.2f}")