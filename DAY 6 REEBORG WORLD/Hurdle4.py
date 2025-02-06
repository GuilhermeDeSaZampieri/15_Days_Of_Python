def turn_right():
    turn_left()
    turn_left()
    turn_left()


def movezao():
    turn_left()
    cont = 0
    while right_is_clear() == False:
        move()
        cont += 1
    turn_right()
    move()
    turn_right()
    while cont != 0:
        move()
        cont -= 1
    if front_is_clear() == False:
        turn_left()


while at_goal() == False:
    if front_is_clear() == True:
        move()
    else:
        movezao()
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
