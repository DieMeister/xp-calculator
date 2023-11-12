import variables


def total_amount():
    variables.values_data["total"]["amount"]["loot"] = variables.values_data["total"]["amount"]["loot"] + variables.amount_loot_now
    variables.values_data["total"]["amount"]["roll"] = variables.values_data["total"]["amount"]["roll"] + variables.amount_roll_now
    variables.values_data["total"]["amount"]["fish"] = variables.values_data["total"]["amount"]["fish"] + variables.amount_fish_now
    variables.values_data["total"]["amount"]["all"] = variables.values_data["total"]["amount"]["loot"] + variables.values_data["total"]["amount"]["roll"] + variables.values_data["total"]["amount"]["fish"]


def average_times_loot():
    variables.values_data["average"]["times"]["loot"]["0"] = variables.values_data["total"]["times"]["loot"]["0"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["loot"]["25"] = variables.values_data["total"]["times"]["loot"]["25"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["loot"]["50"] = variables.values_data["total"]["times"]["loot"]["50"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["loot"]["75"] = variables.values_data["total"]["times"]["loot"]["75"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["loot"]["100"] = variables.values_data["total"]["times"]["loot"]["100"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["loot"]["125"] = variables.values_data["total"]["times"]["loot"]["125"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["loot"]["150"] = variables.values_data["total"]["times"]["loot"]["150"] / variables.values_data["total"]["times"]["played"] * 100


def average_times_roll():
    variables.values_data["average"]["times"]["roll"]["0"] = variables.values_data["total"]["times"]["roll"]["0"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["roll"]["25"] = variables.values_data["total"]["times"]["roll"]["25"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["roll"]["50"] = variables.values_data["total"]["times"]["roll"]["50"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["roll"]["75"] = variables.values_data["total"]["times"]["roll"]["75"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["roll"]["100"] = variables.values_data["total"]["times"]["roll"]["100"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["roll"]["125"] = variables.values_data["total"]["times"]["roll"]["125"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["roll"]["150"] = variables.values_data["total"]["times"]["roll"]["150"] / variables.values_data["total"]["times"]["played"] * 100


def average_times_fish():
    variables.values_data["average"]["times"]["fish"]["0"] = variables.values_data["total"]["times"]["fish"]["0"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["fish"]["25"] = variables.values_data["total"]["times"]["fish"]["25"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["fish"]["50"] = variables.values_data["total"]["times"]["fish"]["50"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["fish"]["75"] = variables.values_data["total"]["times"]["fish"]["75"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["fish"]["100"] = variables.values_data["total"]["times"]["fish"]["100"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["fish"]["125"] = variables.values_data["total"]["times"]["fish"]["125"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["fish"]["150"] = variables.values_data["total"]["times"]["fish"]["150"] / variables.values_data["total"]["times"]["played"] * 100


def average_times_all():
    variables.values_data["average"]["times"]["all"]["0"] = variables.values_data["total"]["times"]["all"]["0"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["25"] = variables.values_data["total"]["times"]["all"]["25"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["50"] = variables.values_data["total"]["times"]["all"]["50"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["75"] = variables.values_data["total"]["times"]["all"]["75"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["100"] = variables.values_data["total"]["times"]["all"]["100"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["125"] = variables.values_data["total"]["times"]["all"]["125"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["150"] = variables.values_data["total"]["times"]["all"]["150"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["175"] = variables.values_data["total"]["times"]["all"]["175"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["200"] = variables.values_data["total"]["times"]["all"]["200"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["225"] = variables.values_data["total"]["times"]["all"]["225"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["250"] = variables.values_data["total"]["times"]["all"]["250"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["275"] = variables.values_data["total"]["times"]["all"]["275"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["300"] = variables.values_data["total"]["times"]["all"]["300"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["325"] = variables.values_data["total"]["times"]["all"]["325"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["350"] = variables.values_data["total"]["times"]["all"]["350"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["375"] = variables.values_data["total"]["times"]["all"]["375"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["400"] = variables.values_data["total"]["times"]["all"]["400"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["425"] = variables.values_data["total"]["times"]["all"]["425"] / variables.values_data["total"]["times"]["played"] * 100
    variables.values_data["average"]["times"]["all"]["450"] = variables.values_data["total"]["times"]["all"]["450"] / variables.values_data["total"]["times"]["played"] * 100


def average_amount():
    variables.values_data["average"]["amount"]["loot"] = variables.values_data["total"]["amount"]["loot"] / variables.values_data["total"]["times"]["played"]
    variables.values_data["average"]["amount"]["roll"] = variables.values_data["total"]["amount"]["roll"] / variables.values_data["total"]["times"]["played"]
    variables.values_data["average"]["amount"]["fish"] = variables.values_data["total"]["amount"]["fish"] / variables.values_data["total"]["times"]["played"]
    variables.values_data["average"]["amount"]["all"] = variables.values_data["total"]["amount"]["all"] / variables.values_data["total"]["times"]["played"]
    variables.values_data["average"]["amount"]["all/3"] = variables.values_data["average"]["amount"]["all"] / 3
