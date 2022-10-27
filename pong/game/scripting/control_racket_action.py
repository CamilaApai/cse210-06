from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down(UP): 
            racket.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            racket.swing_down()  
        else: 
            racket.stop_moving()       

        #racket2 = cast.get_second_actor(RACKET_GROUP)
        racket2 = cast.get_actors(RACKET_GROUP[1])
        if self._keyboard_service.is_key_down(UP2): 
            racket2.swing_up()
        elif self._keyboard_service.is_key_down(DOWN2): 
            racket2.swing_down()  
        else: 
            racket2.stop_moving()     