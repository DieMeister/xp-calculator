import user_output
import variables
import json


def stop():
    variables.run = False
    print("here are all tracked values:")
    print("")
    user_output.total_times_loot()
    user_output.total_times_roll()
    user_output.total_times_fish()
    user_output.total_times_all()
    user_output.average_times_loot()
    user_output.average_times_roll()
    user_output.average_times_fish()
    user_output.average_times_all()
    user_output.total_amount()
    user_output.average_amount()
    user_output.total_times_played()

    raw_data = json.dumps(variables.values_data, indent=4)
    with open("values.json", "w") as values_file:
        values_file.write(raw_data)


def times_loot():
    user_output.total_times_loot()
    user_output.average_times_loot()


def times_roll():
    user_output.total_times_roll()
    user_output.average_times_roll()


def times_fish():
    user_output.total_times_fish()
    user_output.average_times_fish()


def times_all():
    user_output.total_times_all()
    user_output.average_times_all()


def total_times():
    user_output.total_times_loot()
    user_output.total_times_roll()
    user_output.total_times_fish()
    user_output.total_times_all()


def average_times():
    user_output.average_times_loot()
    user_output.average_times_roll()
    user_output.average_times_fish()
    user_output.average_times_all()


def amount():
    user_output.total_amount()
    user_output.average_amount()


def times_played():
    user_output.total_times_played()


def reset():
    if input("are you sure you want to reset all values? if so please write yes") == "yes":
        variables.values_data["total"]["times"]["played"] = 0

        variables.values_data["total"]["times"]["loot"]["0"] = 0
        variables.values_data["total"]["times"]["loot"]["25"] = 0
        variables.values_data["total"]["times"]["loot"]["50"] = 0
        variables.values_data["total"]["times"]["loot"]["75"] = 0
        variables.values_data["total"]["times"]["loot"]["100"] = 0
        variables.values_data["total"]["times"]["loot"]["125"] = 0
        variables.values_data["total"]["times"]["loot"]["150"] = 0

        variables.values_data["total"]["times"]["roll"]["0"] = 0
        variables.values_data["total"]["times"]["roll"]["25"] = 0
        variables.values_data["total"]["times"]["roll"]["50"] = 0
        variables.values_data["total"]["times"]["roll"]["75"] = 0
        variables.values_data["total"]["times"]["roll"]["100"] = 0
        variables.values_data["total"]["times"]["roll"]["125"] = 0
        variables.values_data["total"]["times"]["roll"]["150"] = 0

        variables.values_data["total"]["times"]["fish"]["0"] = 0
        variables.values_data["total"]["times"]["fish"]["25"] = 0
        variables.values_data["total"]["times"]["fish"]["50"] = 0
        variables.values_data["total"]["times"]["fish"]["75"] = 0
        variables.values_data["total"]["times"]["fish"]["100"] = 0
        variables.values_data["total"]["times"]["fish"]["125"] = 0
        variables.values_data["total"]["times"]["fish"]["150"] = 0

        variables.values_data["total"]["times"]["all"]["0"] = 0
        variables.values_data["total"]["times"]["all"]["25"] = 0
        variables.values_data["total"]["times"]["all"]["50"] = 0
        variables.values_data["total"]["times"]["all"]["75"] = 0
        variables.values_data["total"]["times"]["all"]["100"] = 0
        variables.values_data["total"]["times"]["all"]["125"] = 0
        variables.values_data["total"]["times"]["all"]["150"] = 0
        variables.values_data["total"]["times"]["all"]["175"] = 0
        variables.values_data["total"]["times"]["all"]["200"] = 0
        variables.values_data["total"]["times"]["all"]["225"] = 0
        variables.values_data["total"]["times"]["all"]["250"] = 0
        variables.values_data["total"]["times"]["all"]["275"] = 0
        variables.values_data["total"]["times"]["all"]["300"] = 0
        variables.values_data["total"]["times"]["all"]["325"] = 0
        variables.values_data["total"]["times"]["all"]["350"] = 0
        variables.values_data["total"]["times"]["all"]["375"] = 0
        variables.values_data["total"]["times"]["all"]["400"] = 0
        variables.values_data["total"]["times"]["all"]["425"] = 0
        variables.values_data["total"]["times"]["all"]["450"] = 0

        variables.values_data["total"]["amount"]["loot"] = 0
        variables.values_data["total"]["amount"]["roll"] = 0
        variables.values_data["total"]["amount"]["fish"] = 0
        variables.values_data["total"]["amount"]["all"] = 0

        variables.values_data["average"]["times"]["loot"]["0"] = 0
        variables.values_data["average"]["times"]["loot"]["25"] = 0
        variables.values_data["average"]["times"]["loot"]["50"] = 0
        variables.values_data["average"]["times"]["loot"]["75"] = 0
        variables.values_data["average"]["times"]["loot"]["100"] = 0
        variables.values_data["average"]["times"]["loot"]["125"] = 0
        variables.values_data["average"]["times"]["loot"]["150"] = 0

        variables.values_data["average"]["times"]["roll"]["0"] = 0
        variables.values_data["average"]["times"]["roll"]["25"] = 0
        variables.values_data["average"]["times"]["roll"]["50"] = 0
        variables.values_data["average"]["times"]["roll"]["75"] = 0
        variables.values_data["average"]["times"]["roll"]["100"] = 0
        variables.values_data["average"]["times"]["roll"]["125"] = 0
        variables.values_data["average"]["times"]["roll"]["150"] = 0

        variables.values_data["average"]["times"]["fish"]["0"] = 0
        variables.values_data["average"]["times"]["fish"]["25"] = 0
        variables.values_data["average"]["times"]["fish"]["50"] = 0
        variables.values_data["average"]["times"]["fish"]["75"] = 0
        variables.values_data["average"]["times"]["fish"]["100"] = 0
        variables.values_data["average"]["times"]["fish"]["125"] = 0
        variables.values_data["average"]["times"]["fish"]["150"] = 0

        variables.values_data["average"]["times"]["all"]["0"] = 0
        variables.values_data["average"]["times"]["all"]["25"] = 0
        variables.values_data["average"]["times"]["all"]["50"] = 0
        variables.values_data["average"]["times"]["all"]["75"] = 0
        variables.values_data["average"]["times"]["all"]["100"] = 0
        variables.values_data["average"]["times"]["all"]["125"] = 0
        variables.values_data["average"]["times"]["all"]["150"] = 0
        variables.values_data["average"]["times"]["all"]["175"] = 0
        variables.values_data["average"]["times"]["all"]["200"] = 0
        variables.values_data["average"]["times"]["all"]["225"] = 0
        variables.values_data["average"]["times"]["all"]["250"] = 0
        variables.values_data["average"]["times"]["all"]["275"] = 0
        variables.values_data["average"]["times"]["all"]["300"] = 0
        variables.values_data["average"]["times"]["all"]["325"] = 0
        variables.values_data["average"]["times"]["all"]["350"] = 0
        variables.values_data["average"]["times"]["all"]["375"] = 0
        variables.values_data["average"]["times"]["all"]["400"] = 0
        variables.values_data["average"]["times"]["all"]["425"] = 0
        variables.values_data["average"]["times"]["all"]["450"] = 0

        variables.values_data["average"]["amount"]["loot"] = 0
        variables.values_data["average"]["amount"]["roll"] = 0
        variables.values_data["average"]["amount"]["fish"] = 0
        variables.values_data["average"]["amount"]["all"] = 0

        variables.run = False
        raw_data = json.dumps(variables.values_data, indent=4)
        with open("values.json", "w") as values_file:
            values_file.write(raw_data)
    else:
        print("the reset process was successfully canceled")


def info():
    print(f'''
loot = total_times_loot; average_times_loot
roll = total_times_roll; average_times_roll
fish = total_times_fish; average_times_fish
all = total_times_all; average_times_all
times = times_loot; times_roll; times_fish; times_all
average = average_times_loot; average_times_roll; average_times_fish; average_times_all
amount = average_amount_each; amount_total
played = times_played
reset = resets all values and stops the program
stop = stops the program
help = shows this
''')
