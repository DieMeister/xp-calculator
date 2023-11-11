import variables


def times_loot():
    if variables.amount_loot_now == 0:
        variables.values_data["total"]["times"]["loot"]["0"] = variables.values_data["total"]["times"]["loot"]["0"] + 1
    elif variables.amount_loot_now == 25:
        variables.values_data["total"]["times"]["loot"]["25"] = variables.values_data["total"]["times"]["loot"]["25"] + 1
    elif variables.amount_loot_now == 50:
        variables.values_data["total"]["times"]["loot"]["50"] = variables.values_data["total"]["times"]["loot"]["50"] + 1
    elif variables.amount_loot_now == 75:
        variables.values_data["total"]["times"]["loot"]["75"] = variables.values_data["total"]["times"]["loot"]["75"] + 1
    elif variables.amount_loot_now == 100:
        variables.values_data["total"]["times"]["loot"]["100"] = variables.values_data["total"]["times"]["loot"]["100"] + 1
    elif variables.amount_loot_now == 125:
        variables.values_data["total"]["times"]["loot"]["125"] = variables.values_data["total"]["times"]["loot"]["125"] + 1
    elif variables.amount_loot_now == 150:
        variables.values_data["total"]["times"]["loot"]["150"] = variables.values_data["total"]["times"]["loot"]["150"] + 1


def times_roll():
    if variables.amount_roll_now == 0:
        variables.values_data["total"]["times"]["roll"]["0"] = variables.values_data["total"]["times"]["roll"]["0"] + 1
    elif variables.amount_roll_now == 25:
        variables.values_data["total"]["times"]["roll"]["25"] = variables.values_data["total"]["times"]["roll"]["25"] + 1
    elif variables.amount_roll_now == 50:
        variables.values_data["total"]["times"]["roll"]["50"] = variables.values_data["total"]["times"]["roll"]["50"] + 1
    elif variables.amount_roll_now == 75:
        variables.values_data["total"]["times"]["roll"]["75"] = variables.values_data["total"]["times"]["roll"]["75"] + 1
    elif variables.amount_roll_now == 100:
        variables.values_data["total"]["times"]["roll"]["100"] = variables.values_data["total"]["times"]["roll"]["100"] + 1
    elif variables.amount_roll_now == 125:
        variables.values_data["total"]["times"]["roll"]["125"] = variables.values_data["total"]["times"]["roll"]["125"] + 1
    elif variables.amount_roll_now == 150:
        variables.values_data["total"]["times"]["roll"]["150"] = variables.values_data["total"]["times"]["roll"]["150"] + 1


def times_fish():
    if variables.amount_fish_now == 0:
        variables.values_data["total"]["times"]["fish"]["0"] = variables.values_data["total"]["times"]["fish"]["0"] + 1
    elif variables.amount_fish_now == 25:
        variables.values_data["total"]["times"]["fish"]["25"] = variables.values_data["total"]["times"]["fish"]["25"] + 1
    elif variables.amount_fish_now == 50:
        variables.values_data["total"]["times"]["fish"]["50"] = variables.values_data["total"]["times"]["fish"]["50"] + 1
    elif variables.amount_fish_now == 75:
        variables.values_data["total"]["times"]["fish"]["75"] = variables.values_data["total"]["times"]["fish"]["75"] + 1
    elif variables.amount_fish_now == 100:
        variables.values_data["total"]["times"]["fish"]["100"] = variables.values_data["total"]["times"]["fish"]["100"] + 1
    elif variables.amount_fish_now == 125:
        variables.values_data["total"]["times"]["fish"]["125"] = variables.values_data["total"]["times"]["fish"]["125"] + 1
    elif variables.amount_fish_now == 150:
        variables.values_data["total"]["times"]["fish"]["150"] = variables.values_data["total"]["times"]["fish"]["150"] + 1


def times_all():
    if variables.amount_all_now == 0:
        variables.values_data["total"]["times"]["all"]["0"] = variables.values_data["total"]["times"]["all"]["0"] + 1
    elif variables.amount_all_now == 25:
        variables.values_data["total"]["times"]["all"]["25"] = variables.values_data["total"]["times"]["all"]["25"] + 1
    elif variables.amount_all_now == 50:
        variables.values_data["total"]["times"]["all"]["50"] = variables.values_data["total"]["times"]["all"]["50"] + 1
    elif variables.amount_all_now == 75:
        variables.values_data["total"]["times"]["all"]["75"] = variables.values_data["total"]["times"]["all"]["75"] + 1
    elif variables.amount_all_now == 100:
        variables.values_data["total"]["times"]["all"]["100"] = variables.values_data["total"]["times"]["all"]["100"] + 1
    elif variables.amount_all_now == 125:
        variables.values_data["total"]["times"]["all"]["125"] = variables.values_data["total"]["times"]["all"]["125"] + 1
    elif variables.amount_all_now == 150:
        variables.values_data["total"]["times"]["all"]["150"] = variables.values_data["total"]["times"]["all"]["150"] + 1
    elif variables.amount_all_now == 175:
        variables.values_data["total"]["times"]["all"]["175"] = variables.values_data["total"]["times"]["all"]["175"] + 1
    elif variables.amount_all_now == 200:
        variables.values_data["total"]["times"]["all"]["200"] = variables.values_data["total"]["times"]["all"]["200"] + 1
    elif variables.amount_all_now == 225:
        variables.values_data["total"]["times"]["all"]["225"] = variables.values_data["total"]["times"]["all"]["225"] + 1
    elif variables.amount_all_now == 250:
        variables.values_data["total"]["times"]["all"]["250"] = variables.values_data["total"]["times"]["all"]["250"] + 1
    elif variables.amount_all_now == 275:
        variables.values_data["total"]["times"]["all"]["275"] = variables.values_data["total"]["times"]["all"]["275"] + 1
    elif variables.amount_all_now == 300:
        variables.values_data["total"]["times"]["all"]["300"] = variables.values_data["total"]["times"]["all"]["300"] + 1
    elif variables.amount_all_now == 325:
        variables.values_data["total"]["times"]["all"]["325"] = variables.values_data["total"]["times"]["all"]["325"] + 1
    elif variables.amount_all_now == 350:
        variables.values_data["total"]["times"]["all"]["350"] = variables.values_data["total"]["times"]["all"]["350"] + 1
    elif variables.amount_all_now == 375:
        variables.values_data["total"]["times"]["all"]["375"] = variables.values_data["total"]["times"]["all"]["375"] + 1
    elif variables.amount_all_now == 400:
        variables.values_data["total"]["times"]["all"]["400"] = variables.values_data["total"]["times"]["all"]["400"] + 1
    elif variables.amount_all_now == 425:
        variables.values_data["total"]["times"]["all"]["425"] = variables.values_data["total"]["times"]["all"]["425"] + 1
    elif variables.amount_all_now == 450:
        variables.values_data["total"]["times"]["all"]["450"] = variables.values_data["total"]["times"]["all"]["450"] + 1


def times_played():
    variables.values_data["total"]["times"]["played"] = variables.values_data["total"]["times"]["played"] + 1
