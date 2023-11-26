import calculating
import commands
import variables
import user_input
import counting
import save_file

possible_values = [0, 25, 50, 75, 100, 125, 150]
possible_value_loot = False
possible_value_roll = False
possible_value_fish = False

print("\n\nwelcome to xp_analysis. these are all commands you can use:")
commands.info()

while variables.run:
    variables.command = user_input.commands()

    if variables.command == "stop":
        commands.stop()
    elif variables.command == "reset":
        commands.reset()
    elif variables.command == "loot":
        commands.times_loot()
    elif variables.command == "roll":
        commands.times_roll()
    elif variables.command == "fish":
        commands.times_fish()
    elif variables.command == "all":
        commands.times_all()
    elif variables.command == "times":
        commands.total_times()
    elif variables.command == "average":
        commands.average_times()
    elif variables.command == "amount":
        commands.amount()
    elif variables.command == "played":
        commands.times_played()
    elif variables.command == "help":
        commands.info()
    else:
        variables.amount_loot_now = user_input.loot_now()
        variables.amount_roll_now = user_input.roll_now()
        variables.amount_fish_now = user_input.fish_now()

        possible_value = False

        try:
            variables.amount_loot_now = int(variables.amount_loot_now)
            try:
                variables.amount_roll_now = int(variables.amount_roll_now)
                try:
                    variables.amount_fish_now = int(variables.amount_fish_now)

                    variables.amount_all_now = variables.amount_loot_now + variables.amount_roll_now + variables.amount_fish_now

                    for i in possible_values:
                        if i == variables.amount_loot_now:
                            possible_value_loot = True
                        if i == variables.amount_roll_now:
                            possible_value_roll = True
                        if i == variables.amount_fish_now:
                            possible_value_fish = True

                    if possible_value_loot and possible_value_roll and possible_value_fish:
                        counting.times_loot()
                        counting.times_roll()
                        counting.times_fish()
                        counting.times_all()
                        counting.times_played()
                        counting.times_combination()

                        calculating.total_amount()
                        calculating.average_times_loot()
                        calculating.average_times_roll()
                        calculating.average_times_fish()
                        calculating.average_times_all()
                        calculating.average_amount()
                        calculating.total_times_combination()
                        calculating.average_times_combination_important()
                        calculating.average_times_combination_unimportant()

                        save_file.save()
                    if not possible_value_loot:
                        print("your value for /loot is not a possible value, please try again")
                    if not possible_value_roll:
                        print("your value for /roll is not a possible value, please try again")
                    if not possible_value_fish:
                        print("your value for /fish is not a possible value, please try again")

                except ValueError:
                    print("your value of /fish is not a number, please try again")
            except ValueError:
                print("your value of /roll is not a number, please try again")
        except ValueError:
            print("your value of /loot is not a number, please try again")
    print("")
