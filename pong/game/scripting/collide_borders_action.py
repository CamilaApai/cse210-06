from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        racket = cast.get_first_actor(RACKET_GROUP[0])

        ball2 = cast.get_second_actor(BALL_GROUP)
        body2 = ball2.get_body()
        position2 = body2.get_position()
        racket2 = cast.get_first_actor(RACKET_GROUP[1])

        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        stats = cast.get_actors(STATS_GROUP[0])
        stats2 = cast.get_actors(STATS_GROUP[1])
        score1 = stats.get_score()
        score2 =stats2.get_score()
                
        if x <= FIELD_LEFT:
            points2 = racket2.get_points()
            stats2.add_points(points2)

            if score1 == 5 or score2 == 5:
                callback.on_next(GAME_OVER) 
                self._audio_service.play_sound(over_sound)
            else:
                callback.on_next(TRY_AGAIN) 
                
        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            
            points = racket.get_points()
            stats.add_points(points)

            if score2 == 5 or score1 == 5:
                callback.on_next(GAME_OVER) 
                self._audio_service.play_sound(over_sound)
            else:
                callback.on_next(TRY_AGAIN) 

        if y < FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
           
        