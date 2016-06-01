drink = "beer"

print("\nWelcome to 'Bottles of Beer' lyric printer.\n")
count = int(input("How many bottles of {} would you like to place on the wall?".format(drink)))

while count > 0:
    if count > 1:
        print(str(count) + " bottles of {} on the wall,".format(drink))
        print(str(count) + " bottles of {},".format(drink))
        print("You take one down and pass it around,")
        count = count - 1
    elif count == 1:
        print(str(count) + " bottle of {} on the wall,".format(drink))
        print(str(count) + " bottle of {},".format(drink))
        print("You take one down and pass it around,")
        count = count - 1

    if count > 1:
        print(str(count) + " bottles of {} on the wall.\n".format(drink))
    elif count == 1:
    	print(str(count) + " bottle of {} on the wall.\n".format(drink))
    else:
        print("No more bottles of {} on the wall.\n".format(drink))
