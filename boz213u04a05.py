
def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons


def miles_gallon_to_liters_100km(miles):
    distance = 100 * 1000 / 1609.344
    gallons = distance / miles
    liters = gallons * 3.785411784
    return liters


liters = float(input())
miles = float(input())

print(liters_100km_to_miles_gallon(liters))
print(miles_gallon_to_liters_100km(miles))
