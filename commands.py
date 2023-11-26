import calculating
import user_output
import variables
import json
import os


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
    if input('are you sure you want to reset all values? if so please write "yes": ') == "yes":

        times_reset = variables.values_data["total"]["times"]["reset"]
        times_reset += 1

        os.mkdir(f"saves/reset_{times_reset}")

        raw_data_before = json.dumps(variables.values_data, indent=4)
        with open(f"saves/reset_{times_reset}/values.json", "w") as file:
            file.write(raw_data_before)

        with open("saves.txt", "r") as saves_old:
            saves_old.seek(0)
            lines = saves_old.read()
            with open(f"saves/reset_{times_reset}/saves.txt", "w") as saves_new:
                saves_new.write(lines)
        with open("saves.txt", "w") as saves_old:
            saves_old.write("")

        variables.values_data["total"]["times"]["reset"] = times_reset

        for i in variables.values_data["total"]["times"]["loot"].keys():
            variables.values_data["total"]["times"]["loot"][i] = 0

        for i in variables.values_data["total"]["times"]["roll"].keys():
            variables.values_data["total"]["times"]["roll"][i] = 0

        for i in variables.values_data["total"]["times"]["fish"].keys():
            variables.values_data["total"]["times"]["fish"][i] = 0

        for i in variables.values_data["total"]["times"]["all"].keys():
            variables.values_data["total"]["times"]["all"][i] = 0

        for i in variables.values_data["total"]["amount"].keys():
            variables.values_data["total"]["amount"][i] = 0

        for i in variables.values_data["total"]["times"]["combination"]["order_important"].keys():
            variables.values_data["total"]["times"]["combination"]["order_important"][i] = 0

        calculating.average_times_loot()
        calculating.average_times_roll()
        calculating.average_times_fish()
        calculating.average_times_all()
        calculating.average_amount()
        calculating.total_times_combination()
        calculating.average_times_combination_important()
        calculating.average_times_combination_unimportant()

        variables.values_data["total"]["times"]["played"] = 0

        variables.run = False
        raw_data_before = json.dumps(variables.values_data, indent=4)
        with open("values.json", "w") as values_file:
            values_file.write(raw_data_before)
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
