# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define p = Character("You", color="#A0A0A0")
define b = Character("Blue", color="#4800FF")
define r = Character("Red", color="#CD1111")
define o = Character("Orange", color="##FF6A00")

screen character_map:
    imagemap:
        ground "map_background2.png"
        hover "map_hover2.png"

        hotspot (314, 154, 466 - 314, 291 - 154) clicked Call(story + ".blue") #blue
        hotspot (509, 112, 661 - 509, 260 - 112) clicked Call(story + ".red") #red
        hotspot (317, 332, 471 - 317, 468 - 332) clicked Call(story + ".red") #green
        hotspot (527, 281, 679 - 527, 433 - 281) clicked Call(story + ".red") #purple
        hotspot (331, 486, 495 - 331, 652 - 486) clicked Call(story + ".orange") #orange
        hotspot (532, 460, 679 - 532, 597 - 460) clicked Call(story + ".red") #pink

# The game starts here.

label start:

    $ story = renpy.random.choice(["aliens"])

    call expression story + ".start" from _call_expression

    return


## Aliens ############################################################
######################################################################

label aliens:

label .start:

    scene bg stadium day

    show player

        play sound "audio/vocals/male/Hello 1.wav"

    p "I got called out to a sports stadium because people reported seeing flying saucers, loud noises and people screaming"

    p "There's nothing in the sky now but the place is littered with scorch marked and occasional sprays of blood. Something definitely happened here"

    p "I've managed to gather a group of witnesses but they're all terribly traumatised."

    p "If I can help them find the person they're looking for, maybe I can get some answers to what happened here?"

    hide player

    ## Blue Initialization
    $ hadBlueIntro = False
    $ foundTicketStubs = False
    $ blueOptions = ["option1", "option2", "option3"]

    ## Red Intialization
    $ hadRedIntro = False
    $ sharedHotdog = False
    $ redOptions = ["option1", "option2"]

    ## Orange Initialization
    $ hadOrangeIntro = False
    $ orangeOptions = []

    call aliens.map from _call_aliens_map
        
    return

label .map:

    call screen character_map

    return

## Blue ##############################################################

label .blue:

    play sound "audio/vocals/male/Hello 1.wav"

    if hadBlueIntro == False:
        call aliens.blueIntro from _call_aliens_blueIntro
        $ hadBlueIntro = True
    else:
        call aliens.blueContinue from _call_aliens_blueContinue

    if len(blueOptions) == 0:
        call aliens.blueNoDialogue from _call_aliens_blueNoDialogue
    else:
        $ option = renpy.random.choice(blueOptions)
        $ blueOptions.remove(option)

        if option == "option1":
            call aliens.blueOption1 from _call_aliens_blueOption1
        elif option == "option2":
            call aliens.blueOption2 from _call_aliens_blueOption2
        elif option == "option3":
            call aliens.blueOption3 from _call_aliens_blueOption3

    if foundTicketStubs == False:
        call aliens.blueTicketStubs from _call_aliens_ticketStubs
        $ foundTicketStubs = True

    hide blue

    hide player

    call aliens.map from _call_aliens_map_1

label .blueIntro:

    show player at left

    show blue at right

    p "Excuse me sir, I'd like to ask you a few questions if you don't mind?"

    b "Huh? Oh. Of course. *distracted* What do you want?"

    p "Can you tell me what happened?"

    return

label .blueContinue:

    show player at left

    show blue at right

    p "Is there anything else you remember?"

    return

label .blueNoDialogue:

    b "I can't think of anything more to tell you."

    return

label .blueOption1:

    b "If I close my eyes I see large silver discs in the sky making a loud humming noise."

    b "Then a bright green light with incredible heat. I remember people screaming and running."

    return

label .blueOption2:

    b "I remember laughing at our team's mascot chasing the other mascot around. It was such a perfect day."

    b "Now I think the world will never be the same again. I don't think I could even crack a smile."

    return


label .blueOption3:

    b "I think our team was winning and they were going to send that new player onto the field. I was really excited to see his debut."

    return

label .blueTicketStubs:

    b "I also found this pair of ticket stubs in my pocket. I must have been in the stands with someone, but I can't remember who."

    return

## Red ###############################################################

label .red:

    if hadRedIntro == False:
        call aliens.redIntro
        $ hadRedIntro = True
    else:
        call aliens.redContinue

    if sharedHotdog == False:
        call aliens.redHotdog
        $ sharedHotdog = True

    if len(redOptions) == 0:
        call aliens.redNoDialogue
    else:
        $ option = renpy.random.choice(redOptions)
        $ redOptions.remove(option)

        if option == "option1":
            call aliens.redOption1
        elif option == "option2":
            call aliens.redOption2
        elif option == "option3":
            call aliens.redOption3

    hide red

    hide player

    call aliens.map

label .redIntro:

    show player at left

    show red at right

    p "Excuse me mam, can you tell me what you saw?"

    r "It was so horrifying, I think I blacked out."

    p "Please can you try and tell me what you can remember?"

    return

label .redContinue:

    show player at left

    show red at right

    p "Can you tell me anything else you remember?"

    r "Um..."

    return

label .redNoDialogue:

    hide player

    show red at center

    r "Please. Don't ask me any more questions. I don't want to remember."

    return

label .redHotdog:

    r "I remember sharing a hotdog with someone. The day was perfect. I think we were in love."

    p "I'm sorry to hear that"

    r "Please! You have to help me find them *sobs*"

    return

label .redOption1:

    r "We were watching the game when suddenly it went dark. Then there was a blinding light."

    r "I remember screaming and crying"

    return

label .redOption2:

    r "We were watching the game when suddenly it went dark. Then there was a blinding light."

    r "I remember screaming and crying"

    return

## Orange ############################################################

label .orange:

    if hadOrangeIntro == False:
        call aliens.orangeIntro
        $ hadOrangeIntro = True
    else:
        call aliens.orangeContinue

    if len(orangeOptions) == 0:
        call aliens.orangeNoDialogue
    else:
        $ option = renpy.random.choice(orangeOptions)
        $ orangeOptions.remove(option)

        if option == "option1":
            call aliens.orangeOption1
        elif option == "option2":
            call aliens.orangeOption2
        elif option == "option3":
            call aliens.orangeOption3

    hide orange

    hide player

    call aliens.map 

label .orangeIntro:

    show player at left

    show orange at right

    p "Excuse me mam, can you tell me what you saw?"

    r "It was so horrifying, I think I blacked out."

    p "Please can you try and tell me what you can remember?"

    return

label .orangeContinue:

    show player at left

    show orange at right

    p "Can you tell me anything else you remember?"

    r "Um..."

    return

label .orangeNoDialogue:

    hide player

    show orange at center

    r "Please. Don't ask me any more questions. I don't want to remember."

    return

## Kaiju #############################################################
######################################################################

label kaiju:

label .start:

    "This is the start of the kaiju story"

    call screen character_map

    return

label .chat:

    "This is kaiju chat"

    return

label .chat2:

    "This is kaiju chat 2"

    return

## Wizard ############################################################

label wizard:

label .start:

    "This is the start of the wizard story"

    call screen character_map

    return

label .chat:

    "This is wizard chat"

    return

label .chat2:

    "This is wizard chat 2"

    return

## Demons ############################################################

label demons:

label .start:

    "This is the start of the demons story"

    call screen character_map

    return

label .chat:

    "This is demons chat"

    return

label .chat2:

    "This is demons chat 2"

    return