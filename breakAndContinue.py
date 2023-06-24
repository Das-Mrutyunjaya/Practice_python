import random

vaccines = ["moderna", "flue", "covaxin", "covishield"]
random.shuffle(vaccines)
print(vaccines)

chosen_one=random.choice(vaccines);
print(chosen_one)

for vac in vaccines:
    print(f"F***********Testing Vaccine {vac}")
    if vac == chosen_one:
        print("######################")
        print(f"Vaccine tested successfully for {vac}")
        print("######################")
        print()
        break
