import calculating
import commands
import variables
import user_input
import counting
import save_file

possible_values = [0, 25, 50, 75, 100, 125, 150]

print("\n\nwelcome to xp_analysis. these are all commands you can use:")
commands.info()

while variables.run:
    variables.command = user_input.commands("")

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
        variables.amount_loot_now = user_input.loot_now("")
        variables.amount_roll_now = user_input.roll_now("")
        variables.amount_fish_now = user_input.fish_now("")

        possible_value = False

        try:
            variables.amount_loot_now = int(variables.amount_loot_now)
            variables.amount_roll_now = int(variables.amount_roll_now)
            variables.amount_fish_now = int(variables.amount_fish_now)
            variables.amount_all_now = variables.amount_loot_now + variables.amount_roll_now + variables.amount_fish_now

            for i in possible_values:
                if i == variables.amount_loot_now:
                    for i in possible_values:
                        if i == variables.amount_roll_now:
                            for i in possible_values:
                                if i == variables.amount_fish_now:
                                    counting.times_loot()
                                    counting.times_roll()
                                    counting.times_fish()
                                    counting.times_all()
                                    counting.times_played()

                                    calculating.total_amount()
                                    calculating.average_times_loot()
                                    calculating.average_times_roll()
                                    calculating.average_times_fish()
                                    calculating.average_times_all()
                                    calculating.average_amount()

                                    save_file.save()

                                else:
                                    print("your value for /fish is not a possible value, please try again")
                        else:
                            print("your value for /roll is not a possible value, please try again")
                else:
                    print("your value for /loot is not a possible value, please try again")

            else:
                print("at least one input is not a possible value, please try again")

        except ValueError:
            print("at least one value is not a number, please try again")
    print("")
