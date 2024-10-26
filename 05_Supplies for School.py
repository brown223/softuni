pen_packets = int(input())
markers_packets = int(input())
litres_preparation = int(input())
persentage = int(input())

total_price = (pen_packets * 5.80 ) + (markers_packets * 7.20) + (litres_preparation * 1.20)
discount = persentage / 100
final_price = total_price - (total_price * discount)

print(f"{final_price:.2f}")