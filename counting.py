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


def times_combination():
    if variables.amount_loot_now == 0:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["0_150_150"] += 1
    if variables.amount_loot_now == 25:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["25_150_150"] += 1
    if variables.amount_loot_now == 50:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["50_150_150"] += 1
    if variables.amount_loot_now == 75:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["75_150_150"] += 1
    if variables.amount_loot_now == 100:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["100_150_150"] += 1
    if variables.amount_loot_now == 125:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["125_150_150"] += 1
    if variables.amount_loot_now == 150:
        if variables.amount_roll_now == 0:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_0_150"] += 1
        elif variables.amount_roll_now == 25:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_25_150"] += 1
        elif variables.amount_roll_now == 50:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_50_150"] += 1
        elif variables.amount_roll_now == 75:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_75_150"] += 1
        elif variables.amount_roll_now == 100:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_100_150"] += 1
        elif variables.amount_roll_now == 125:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_125_150"] += 1
        elif variables.amount_roll_now == 150:
            if variables.amount_fish_now == 0:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_0"] += 1
            elif variables.amount_fish_now == 25:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_25"] += 1
            elif variables.amount_fish_now == 50:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_50"] += 1
            elif variables.amount_fish_now == 75:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_75"] += 1
            elif variables.amount_fish_now == 100:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_100"] += 1
            elif variables.amount_fish_now == 125:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_125"] += 1
            elif variables.amount_fish_now == 150:
                variables.values_data["total"]["times"]["combination"]["order_important"]["150_150_150"] += 1
