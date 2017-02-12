# The script of the game goes in this file.

# declare bg images
image bg class_after = "bg-classroom_afternoon.jpg"
image bg class_morning = "bg-classroom_morning.jpg"
image bg council = "bg-school_council.jpg"
image bg hallway = "bg-school_hallway.jpg"
image bg math = "bg-school_math.jpg"
image bg music = "bg-school_music.jpg"
image bg track = "bg-school_track.jpg"
image bg bedroom_morning = "bg-bed-morning.jpg"
image bg bedroom_night = "bg-bed-night.jpg"
image bg house = "bg-house_outside.jpg"

#declare cg images
image cg 1 = "cg_1.png"
image cg 2 = "cg_2.png"
image cg 3 = "cg_3.png"
image cg 4 = "cg_4.png"
image cg 5 = "cg_5.png"
image cg 6 = "cg_6.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fan = Character("Fan-kun")
define leftChair = Character("Left-Chair-san")
define rightChair = Character("Right-Chair-san")
define fridge = Character("Fridge-senpai")
define lamp = Character("Lamp-senpai")
define bed = Character("Bed-kun")
define desk = Character("Desk-sensei")
define stand = Character("Stand-sensei")
define me = Character()

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom_morning
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show protag happy

    # These display lines of dialogue.

    "Hello, world."

    me "You've created a new Ren'Py game."

    me "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
