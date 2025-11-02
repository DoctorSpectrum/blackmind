label variables:
    
    define narrator = Character(None, what_color="#FFF")
    define jack = Character("Jack", what_color="#FFF")
    define barbara = Character("Barbara", what_color="#FFF")

    #Persistent variables
    default persistent.game_launched = False
    default persistent.cgs_unlocked = []
    default preferences.fullscreen = True
    default preferences.music_volume = 0.75 

    #Transforms
    transform center:
        xalign 0.5 
        yalign 0.5

    transform trans_fade (pause_time, time=5.0):
        alpha 0.0
        pause pause_time
        linear time alpha 1.0

    transform portrait_crop:
        zoom 0.2
        xalign 0.1
        yalign 0.9
        yoffset 20
        xoffset 60
        crop (0, 0, 900, 700)

    transform dark_tint:
        matrixcolor TintMatrix("#6d6d6d")

    transform opening_text:
        xsize 0.6

    define quick_dissolve = Dissolve(0.5)
    define slow_dissolve = Dissolve(2.0)

    #Images
    image character_pose = ConditionSwitch(
        "_last_say_who == 'character' or not renpy.get_screen('say')", 
        "images/sprites/character_pose.png", 
        "not _last_say_who == 'character'", 
        "character_pose_tint"
    )

    image character_pose_tint:
        "images/sprites/character_pose.png"
        dark_tint

    image side charactername pose:
        "images/sprites/character_pose.png"
        portrait_crop

    #Psychic powers
    default current_thought = None
    default current_conversation = None
    default convo_length = 0
    default minds_read = 0
    default minds_rewound = 0
    default convo_progress = 0
    default progress_convo = False

    default money = 1000

    #Misc. variables
    image black_bg = Solid("#000")
    image white_bg = Solid("#FFF")
    default wait_2 = ("{w=2.0}" if preferences.text_cps > 0 else "")
    default wait_1 = ("{w=1.0}" if preferences.text_cps > 0 else "")
    default wait_05 = ("{w=0.5}" if preferences.text_cps > 0 else "")

    jump story