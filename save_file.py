import variables


def save():
    with open("saves.txt", "a") as file:
        file.write(f'''
total times of /loot = 000: {variables.values_data["total"]["times"]["loot"]["0"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["0"]:<10d}  |  total times of /fish = 000: {variables.values_data["total"]["times"]["fish"]["0"]}
total times of /loot = 025: {variables.values_data["total"]["times"]["loot"]["25"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["25"]:<10d}  |  total times of /fish = 025: {variables.values_data["total"]["times"]["fish"]["25"]}
total times of /loot = 050: {variables.values_data["total"]["times"]["loot"]["50"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["50"]:<10d}  |  total times of /fish = 050: {variables.values_data["total"]["times"]["fish"]["50"]}
total times of /loot = 075: {variables.values_data["total"]["times"]["loot"]["75"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["75"]:<10d}  |  total times of /fish = 075: {variables.values_data["total"]["times"]["fish"]["75"]}
total times of /loot = 100: {variables.values_data["total"]["times"]["loot"]["100"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["100"]:<10d}  |  total times of /fish = 100: {variables.values_data["total"]["times"]["fish"]["100"]}
total times of /loot = 125: {variables.values_data["total"]["times"]["loot"]["125"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["125"]:<10d}  |  total times of /fish = 125: {variables.values_data["total"]["times"]["fish"]["125"]}
total times of /loot = 150: {variables.values_data["total"]["times"]["loot"]["150"]:<10d}  |  total times of /roll = 000: {variables.values_data["total"]["times"]["roll"]["150"]:<10d}  |  total times of /fish = 150: {variables.values_data["total"]["times"]["fish"]["150"]}

total of them combined = 000: {variables.values_data["total"]["times"]["all"]["0"]:<25d}  |  total of them combined = 250: {variables.values_data["total"]["times"]["all"]["250"]:<25d}
total of them combined = 025: {variables.values_data["total"]["times"]["all"]["25"]:<25d}  |  total of them combined = 275: {variables.values_data["total"]["times"]["all"]["275"]:<25d}
total of them combined = 050: {variables.values_data["total"]["times"]["all"]["50"]:<25d}  |  total of them combined = 300: {variables.values_data["total"]["times"]["all"]["300"]:<25d}
total of them combined = 075: {variables.values_data["total"]["times"]["all"]["75"]:<25d}  |  total of them combined = 325: {variables.values_data["total"]["times"]["all"]["325"]:<25d}
total of them combined = 100: {variables.values_data["total"]["times"]["all"]["100"]:<25d}  |  total of them combined = 350: {variables.values_data["total"]["times"]["all"]["350"]:<25d}
total of them combined = 125: {variables.values_data["total"]["times"]["all"]["125"]:<25d}  |  total of them combined = 375: {variables.values_data["total"]["times"]["all"]["375"]:<25d}
total of them combined = 150: {variables.values_data["total"]["times"]["all"]["150"]:<25d}  |  total of them combined = 400: {variables.values_data["total"]["times"]["all"]["400"]:<25d}
total of them combined = 175: {variables.values_data["total"]["times"]["all"]["175"]:<25d}  |  total of them combined = 425: {variables.values_data["total"]["times"]["all"]["425"]:<25d}
total of them combined = 200: {variables.values_data["total"]["times"]["all"]["200"]:<25d}  |  total of them combined = 450: {variables.values_data["total"]["times"]["all"]["450"]:<25d}
total of them combined = 225: {variables.values_data["total"]["times"]["all"]["225"]:<25d}

total amount of /loot: {variables.values_data["total"]["amount"]["loot"]:<32}  |  amount of /loot now:        {variables.amount_loot_now:<27}
total amount of /roll: {variables.values_data["total"]["amount"]["roll"]:<32}  |  amount of /roll now:        {variables.amount_roll_now:<27}
total amount of /fish: {variables.values_data["total"]["amount"]["fish"]:<32}  |  amount of /fish now:        {variables.amount_fish_now:<27}
total amount of all:   {variables.values_data["total"]["amount"]["all"]:<32}  |  amount of all combined now: {variables.amount_all_now:<27}

played games: {variables.values_data["total"]["times"]["played"]}

----------------------------------------------------------------------------------------------------------------------------
''')
