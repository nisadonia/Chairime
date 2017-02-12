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
image bg school = "bg-school_outside.jpg"
image bg aud = "bg-school_aud.jpg"

#declare cg images
image cg 1 = "cg_1.png"
image cg 2 = "cg_2.png"
image cg 3 = "cg_3.png"
image cg 4 = "cg_4.png"
image cg 5 = "cg_5.png"
image cg 6 = "cg_6.png"

#declare profile pics
image pro bed = "profile_bed.png"
image pro lamp = "profile_lamp.png"
image pro fan = "profile_fan.png"
image pro fridge = "profile_fridge.png"
image pro chair = "profile_chair.png"

#declare spirites
image spr bed = "bed-senpai.png"
image spr lamp = "lamp-senpai.png"
image spr fan = "fan-senpai.png"
image spr fridge = "fridge_senpai.png"
image spr left = "left-chair-senpai.png"
image spr right = "right-chair-senpai.png"
image spr desk = "desk-sensei.png"

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
define me = Character("[me]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom_morning
    with fade

    python:
        me = renpy.input("What is your name?")
        me = me.strip()

        if not me:
             me = "Eileen"
    
    me "It’s the first day of being a high school student and I’m all geared up to go!"
    me "It’s a beautiful, sunny day in April and all the cherry blossom trees are in bloom! I can feel that it’s going to be great year."

    scene cg 1
    with fade
        
    "Bed-kun is waiting outside the house"

    scene bg house
    with fade

    show spr bed
    
    "It’s my childhood friend, Bed-kun! We’ve been friends ever since pre-school. "
    bed "[me]! You're up early!"
    me "How long have you been waiting for me?"
    bed "..."
    bed "Are you excited for school?"

    me "I am! This year is going to be great! My goal is to:"

    menu:

            "Get a boyfriend":
                jump menu_1_01
                
            "Score the highest on my exams":
                jump menu_1_01
                
            "Join a sports team":
                jump menu_1_01
                
            "Beat my rivals, Right-Chair-san and Left-Chair-san!":
                jump menu_1_01

            "Enjoy my life to the fullest!":
                jump menu_1_02

label menu_1_01:
    bed "I wish you luck on your goal, [me]! My goal is to enjoy life to the fullest!"
    bed "It’s about the journey, not the destination, in my opinion."
    
    jump go_school_01
    
label menu_1_02:
    bed "That’s my goal! Let’s enjoy life to the fullest together? Wouldn’t that be fun!"
    
    jump go_school_01
    
label go_school_01:
    hide spr bed
    "We headed off to school."
    
    scene bg school
    with fade
        
    "There are a lot of students crowding in front of school. I wonder what they’re looking at…"
    
    show spr bed
    
    bed "Hey, there are the class assignments! I hope we’re in the same class together. Let’s go up and check."
    "I push and shove my way up to the front."
    me "There’s my name! I’m in Class 3-A."
    bed "Look! We’re both in Class 3-A"
    "It appears so. Another year with Bed-kun in my class. I wonder who else is in our class…"
    "Oh no, it’s the Chair twins, my rivals."
    bed "Let’s go in, [me]!"
    
    hide spr bed
    
    "We go into school and head towards the auditorium. It’s almost time for the school assembly!"
    
    scene bg aud 
    with fade
        
    "We find seats in the freshmen group."

    "A dazzling student appears on stage."
    
    show spr lamp
    "Our eyes meet and he winks at me!!!"
    hide spr lamp
    
    scene cg 2
    "A lamp winking from on stage standing behind a podium"
    
    lamp "Good morning, student body❤~   I’m Lamp-senpai, your student council treasurer."
    lamp "I encourage you all this week to visit and try out all the clubs that interest you!"
    lamp "Student council is always looking for new members, but regardless of whether or not you come to visit me❤,~ I hope to see all you being active members at school"
    
    scene bg aud
    with dissolve
    "The crowd goes wild. I think most of the female population is swooning. I know I am."
    
    scene cg 3
    with vpunch
    "SLAM"
    "The door of the auditorium swings open as a delinquent fridge is dragged in by a teacher."
    
    scene bg aud
    with dissolve
        
    show spr fridge
    fridge "Stop draggin’ me! I wasn’t planning on attendin’ this stupid ceremony!"
    
    show spr desk
    desk "Fridge-kun! It’s important to attend the opening ceremony. Please sit down."
    
    hide spr desk
    "Fridge-kun is forced to sit down and notices how much attention he has drawn to himself."
    
    scene bg aud
    with vpunch
    "He glares at everyone looking at him and everyone quickly looks away, except for me!"
    "I was too late and I received the full strength of his glare. Scaary~ but I kinda like his attention."
    
    show trashcan happy
    "A trash can gets on up the stage and concludes the ceremony with a nice farewell and reminder."
    "Furniture’s reason and spirit have often solved the seemingly unsolvable - and we believe they can do it again."
    "Best of luck and godspeed to your exquisitely sculpted future and remember - no littering allowed!"
    
    hide trashcan happy
    "The ceremony is over. It's time to get to class"
    
    scene bg class_morning
    with fade
    "After leaving the auditorium, Bed-kun and I go back to our homeroom. Bed-kun enters the classroom and I’m entering the room when I notice that the Chair twins are already in the room."
    
    show cg 4
    with fade
    "Two chairs in a classroom. They’re cool and alluring."
    
    leftChair "Oh, look who it is"
    rightChair "It’s [me]"
    me "Please take care of me"
    
    "They’ve been my rivals ever since I was younger. We met at a local music competition and I’ve never been able to win against them. Left plays the piano and Right plays the violin. They’re known as the prodigious twins in the music world. "
    
    scene bg class_morning
    with vpunch
        
    "CRASH!"
    
    scene cg 5
    with dissolve
    
    "Someone crashed into me while I was standing in the middle of the doorway."
    
    me "Ouch…"
    fan "I’m so sorry! I wasn’t looking where I was going. I was just rushing to my class. I was worried that I was going to be late."
    me "Can you get off me?"

    scene bg class_morning
    with dissolve
    "The fan gets off me quickly."
    
    show spr fan
    fan "I’m so sorry! I forgot. I apologize! I’m Fan-kun. I just moved here this month due my father’s job transfer. My blood type is O and I plan on joining the track team as a sprinter! I use to go an all-boy’s school a town over. Please treat me well this year!"
    "Why did he give me all this information."
    me "Please treat me well this year as well"

    desk "Why are you blocking the entry way?"

    scene cg 6
    
    desk "Please get back to your seats"
    
    scene bg class_morning
    with dissolve
        
    show protag sorry
    me "Sorry, desk-sensei!"
    hide protag sorry
    
    "We all move to our seats."

    show spr desk
    desk "I’m Desk-sensei and I’ll be your homeroom teacher this year as well as your math teacher. "
    desk "Please do no hesitate to come to me if you have any problems or concerns during the school year."
    desk "I will do my best to help you. I’m also in charge of Math Club. It’s required that each student join a club at our school, so please take this week to explore each club to figure which suits you the best."
    desk "Please hand in your club intent form by Monday. Now, let’s get homeroom started"
    
    scene bg class_after
    with fade
        
    "This is going to the best year"
    "I can feel that there's going to be great things happening"
    "To be Continued: Doki Doki Kira Kira"
    
    scene pro bed
    $ renpy.pause()
    
    
    scene pro lamp
    $ renpy.pause()
    
    
    scene pro fan
    $ renpy.pause()
    
    
    scene pro fridge
    $ renpy.pause()
    
    
    scene pro chair
    $ renpy.pause()
    
    
    # This ends the game.

    return
