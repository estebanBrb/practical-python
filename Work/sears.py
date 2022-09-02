# sears.py
import numbers


bill_thickness = 0.11 * 0.001 # Metros (0.11 mm)
sears_height = 442 # Altura en metros de la torre
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Numero de dias', day)
print('Numero de billetes', num_bills)
print('Altura final', num_bills * bill_thickness)