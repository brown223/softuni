deposit_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())

annual_interest_rate_percent = annual_interest_rate / 100
sum = deposit_amount + deposit_months * ((deposit_amount * annual_interest_rate_percent) / 12)

print(sum)