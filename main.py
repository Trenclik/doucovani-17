import psutil # importování knihovny pro získání informací baterie

while True:
    battery = psutil.sensors_battery() # vytvoření proměnné držící informace baterie
    # musí být uvnitř smyčky, jinak se neobnoví hodnota
    percent = int(battery.percent) # procenta baterie zaokrouhlené na celé číslo
    if percent == 67: # pokud se procento baterie rovná 67 vypíše "six seven" a opustí smyčku
        print("six seven")
        break
    elif percent == 69:
        print("nice")
        break
    else:
        continue