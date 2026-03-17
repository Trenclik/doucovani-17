import batterylib

while True:
    baterie = batterylib.get_percentage()
    if baterie == 67:
        print("six seven")
        break
    elif baterie == 69:
        print("nice")
        continue
    else:
        print("bruh")
