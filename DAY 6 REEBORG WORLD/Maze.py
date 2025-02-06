def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() == False:
    if front_is_clear() == True:
        move()
        if right_is_clear() == True:
            turn_right()

    else:
        if right_is_clear() == True:
            turn_right()
        else:
            turn_left()
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
