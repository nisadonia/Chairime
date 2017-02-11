# The script of the game goes in this file.

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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
