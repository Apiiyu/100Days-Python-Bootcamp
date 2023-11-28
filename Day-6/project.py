def jump():
    move()
   
while not at_goal():
   if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
   elif front_is_clear():
        move()
   else:
       turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
# Platform: Run this code on Reeborg's World
################################################################
