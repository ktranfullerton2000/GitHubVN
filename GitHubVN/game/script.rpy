# The script of the game goes in this file.

#===================================================================================================
# DEFINE CHARACTERS HERE
#===================================================================================================

define hero = Character("Hero")
define witch = Character("Witch")
define prince = Character("Prince")
define king = Character("King")
define thief = Character("thief")

#===================================================================================================
# INITIALIZE IMAGES TO ADJUST THEIR SIZES
#===================================================================================================

init:
    #EXAMPLE BELOW
    image dragon:
        "dragon.png"
        zoom 0.8

#===================================================================================================
#POSITION FOR CHARACTERS
#===================================================================================================
transform left:
    xalign 0.12
    yalign 1.0

transform right:
    xalign 0.88
    yalign 1.0

transform middle:
    xalign 0.5
    yalign 1.0

#===================================================================================================
#THE GAME STARTS HERE
#===================================================================================================

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg castle.png" or "bg castle.jpeg") to the
    # images directory to show it.

    scene bg castle

    # This shows a character sprite.

    show hero at middle

    # These display lines of dialogue.

    hero "Hello, welcome to GitHubVN!"
    hero "It seems like I'm in a little pickle. I've just started my adventure but there's no where to go."
    hero "Hey! Maybe you can help me! Yeah, you!"
    hero "How should my adventure start?"

    menu:
        "Buy some potions.":
            jump route1
        "Placeholder: Route 2":
            jump route2
        "Placeholder: Route 3":
            jump route3
        "Placeholder: Route 4":
            jump route4
        "Placeholder: Route 5":
            jump route5
        "Placeholder: Route 6":
            jump route6

    # Return ends the game.

    return

#===================================================================================================
#ROUTE 1
#===================================================================================================

label route1:

    scene bg black

    #FEEL FREE TO USE THE THREE LINES BELOW TO START YOUR OWN ROUTE
    "Ever since Hero was a child, she heard stories about a dragon."
    "A beast that stole gold from city treasuries across the nation."
    "So in order to stop this monster, Hero set off to her biggest story yet."

    "But first she's going to visit the local witch for some potions."
    "She traveled miles and miles. Over the horizon she saw the foot of the mountain. The Witches' Domain."

    scene bg cave

    show hero at left

    show witch at right

    hero "Hello, Potion Seller, I am going into battle and I want your strongest potions."
    witch "My potions are too strong for you, traveler."
    hero "Potion Seller, I tell you I am going into battle, and I want only your strongest potions."
    witch "You can't handle my potions. They're too strong for you."

    hero "Potion Seller, listen to me; I want only your strongest potions."
    witch "My potions would kill you, traveler. You cannot handle my potions."
    hero "Potion Seller, enough of these games. I'm going into battle and I need your strongest potions."
    witch "My strongest potions would kill you, traveler. You can't handle my strongest potions. You'd better go to a seller that sells weaker potions."

    hero "Potion Seller, I'm telling you right now; I'm going into battle and I need only your strongest potions."
    witch "You don't know what you ask, traveler. My strongest potions will kill a dragon, let alone a man. You need a seller that sells weaker potions, because my potions are too strong."
    hero "Potion Seller, I'm telling you I need your strongest potions. I'm going into battle! I'm going to battle and I need your strongest potions!"
    witch "You can't handle my strongest potions! No one can! My strongest potions aren't fit for a beast let alone a man."

    hero "Potion Seller, what do I have to tell you to get your potions? Why won't you trust me with your strongest potions, Potion Seller? I need them if I'm to be successful in the battle!"
    witch "I can't give you my strongest potions because my strongest potions are only for the strongest beings and you are of the weakest."
    hero "Well then that's it, Potion Seller. I'll go elsewhere. I'll go elsewhere for my potions."
    witch "That's what you'd better do."

    hero "I'll go elsewhere for my potions and I'll never come back!"
    witch "Good. You're not welcome here! My potions are only for the strongest and you're clearly are not of the strongest you're clearly the weakest."
    hero "You've had your say, Potion Seller but I'll have mine. You're a rascal, you're a rascal with no respect for knights. No respect for anything... except your potions!"
    witch "Why respect knights... when my potions can do anything that you can."

    scene bg black

    "Hero soon returned home. Defeated by the dragon."
    "Apparently the potions from the other witch down the street wasn't strong enough."
    "The End: Example Route created by Kenny Tran"

    return

#===================================================================================================
#ROUTE 2
#===================================================================================================

label route2:

    scene bg black

    "If you're planning on making route 2, write in this portion!"
    "The End: Route 2 created by Your Name Here"

    return

#===================================================================================================
#ROUTE 3
#===================================================================================================

label route3:

    scene bg black

    "If you're planning on making route 3, write in this portion!"
    "The End: Route 3 created by Your Name Here"

    return

#===================================================================================================
#ROUTE 4
#===================================================================================================

label route4:

    scene bg black

    "If you're planning on making route 4, write in this portion!"
    "The End: Route 4 created by Your Name Here"

    return

#===================================================================================================
#ROUTE 5
#===================================================================================================

label route5:

    scene bg black

    "If you're planning on making route 5, write in this portion!"
    "The End: Route 5 created by Your Name Here"

    return

#===================================================================================================
#ROUTE 6
#===================================================================================================

label route6:

    scene bg black

    "If you're planning on making route 6, write in this portion!"
    "The End: Route 6 created by Your Name Here"

    return
