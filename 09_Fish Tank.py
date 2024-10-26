length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_cm3 = length * width * height
volume_liters = volume_cm3 / 1000

available_liters = volume_liters * (1 - percentage / 100)
print(f"{available_liters:.7f}")