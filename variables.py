import user_input
import json

ask_input = False
run = True

command = ""
amount_loot_now = ""
amount_roll_now = ""
amount_fish_now = ""

with open("values.json") as values_file:
    raw_data_values = values_file.read()
values_data = json.loads(raw_data_values)

amount_all_now = 0
