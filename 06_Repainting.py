
nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())


price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
price_bags = 0.40


total_nylon = nylon + 2
total_paint = paint + (paint * 0.10)


cost_nylon = total_nylon * price_nylon
cost_paint = total_paint * price_paint
cost_thinner = thinner * price_thinner


total_materials = cost_nylon + cost_paint + cost_thinner + price_bags


cost_workers = (total_materials * 0.30) * hours

final_cost = total_materials + cost_workers


print(f"{final_cost:.2f}")
