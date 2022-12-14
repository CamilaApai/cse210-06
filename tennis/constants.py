from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "tennis"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "assets/sounds/boing.wav"
WELCOME_SOUND = "assets/sounds/start.wav"
OVER_SOUND = "assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
UP = "up"
UP2 = "w"
DOWN = "down"
DOWN2 = "s"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP1 = "stats1"
STATS_GROUP2 = "stats2"
MAXIMUM_ROUND = 15

# HUD
HUD_MARGIN = 15
SCORE1_GROUP = "score1"
SCORE1_FORMAT = "Player 1: {}"
SCORE2_GROUP = "score2"
SCORE2_FORMAT = "Player 2: {}"
ROUND_GROUP = "round"
ROUND_FORMAT = "Round: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 7

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"assets/images/{n:03}.png" for n in range(100, 102)]
RACKET2_IMAGES = [f"assets/images/{n:03}.png" for n in range(103, 105)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 100
RACKET_RATE = 6
RACKET_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING THE GAME"
WAS_GOOD_GAME = "GAME OVER"

