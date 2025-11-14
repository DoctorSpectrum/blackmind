label variables:
    
    define narrator = Character(None, what_color="#FFF")
    define jack = Character("Jack", what_color="#FFF", image="jack")
    define barbara = Character("Barbara", what_color="#FFF")
    define docherty = Character("???", what_color="#FFF")

    #Persistent variables
    default persistent.game_launched = False
    default persistent.cgs_unlocked = []
    default persistent.game_id = 0

    default preferences.fullscreen = True
    default preferences.music_volume = 0.75 

    #Transforms
    transform center:
        xalign 0.5 
        yalign 0.5

    transform zener_card_col_down (init_y, time):
        zoom 0.3
        ypos init_y
        linear (time):
            ypos 1280

        block:
            ypos -200
            linear 12.0:
                ypos 1280

            repeat

    transform zener_card_col_up (init_y, time):
        zoom 0.3
        ypos init_y
        linear (time):
            ypos -200

        block:
            ypos 1280
            linear 12.0:
                ypos -200

            repeat

    transform title_card_slide (direction):
        yoffset (1080 if direction == "up" else -1080)
        linear 0.5:
            yoffset 0

    transform menu_expand_ring (pause_time):
        zoom 0.1
        alpha 0.0
        pause pause_time

        block:
            alpha 1.0
            parallel:
                linear 3.0:
                    zoom 2.0
                    xoffset 300
            parallel:
                pause 2.0
                linear 1.0:
                    alpha 0.0
        
        xoffset 0
        pause (0.2 if pause_time == 3.0 else 0.0)
        repeat

    transform trans_fade (pause_time, time=5.0):
        alpha 0.0
        pause pause_time
        linear time alpha 1.0

    transform trans_fade_out (pause_time, time=5.0):
        alpha 1.0
        pause pause_time
        linear time alpha 0.0

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
    image barbara_angry = ConditionSwitch(
        "_last_say_who == 'barbara' or not renpy.get_screen('say')", 
        "images/sprites/barbara_angry.png", 
        "not _last_say_who == 'barbara'", 
        "barbara_angry_tint"
    )

    image barbara_sad = ConditionSwitch(
        "_last_say_who == 'barbara' or not renpy.get_screen('say')",
        "images/sprites/barbara_sad.png",
        "not _last_say_who == 'barbara'",
        "barbara_sad_tint"
    )

    image barbara_smiling = ConditionSwitch(
        "_last_say_who == 'barbara' or not renpy.get_screen('say')",
        "images/sprites/barbara_smiling.png",
        "not _last_say_who == 'barbara'",
        "barbara_smiling_tint"
    )

    image barbara_thinking = ConditionSwitch(
        "_last_say_who == 'barbara' or not renpy.get_screen('say')",
        "images/sprites/barbara_thinking.png",
        "not _last_say_who == 'barbara'",
        "barbara_thinking_tint"
    )

    image docherty_neutral = ConditionSwitch(
        "_last_say_who == 'docherty' or not renpy.get_screen('say')",
        "images/sprites/docherty_neutral.png",
        "not _last_say_who == 'docherty'",
        "docherty_neutral_tint"
    )

    image barbara_angry_tint:
        "images/sprites/barbara_angry.png"
        dark_tint

    image barbara_sad_tint:
        "images/sprites/barbara_sad.png"
        dark_tint

    image barbara_smiling_tint:
        "images/sprites/barbara_smiling.png"
        dark_tint

    image barbara_thinking_tint:
        "images/sprites/barbara_thinking.png"
        dark_tint

    image docherty_neutral_tint:
        "images/sprites/docherty_neutral.png"
        dark_tint

    image side jack angry:
        "images/sprites/jack_angry.png"
        portrait_crop

    image side jack smug:
        "images/sprites/jack_smug.png"
        portrait_crop
    
    image side jack thinking:
        "images/sprites/jack_thinking.png"
        portrait_crop
    
    image side jack worried:
        "images/sprites/jack_worried.png"
        portrait_crop

    #Psychic powers
    default current_thought = None
    default current_conversation = None
    default progress_convo = False
    default convo_length = 0

    default max_mind_reads = 3
    default max_rewinds = 1
    default max_flash_forwards = 0

    default minds_read = 0
    default minds_rewound = 0
    default convo_progress = 0

    default money = 1000

    #Timeline variables
    default game_id = persistent.game_id
    $ persistent.game_id += 1
    default days = [
        [],
        [],
        [],
        []
    ]

    #Misc. variables
    image black_bg = Solid("#000")
    image white_bg = Solid("#FFF")
    default wait_2 = ("{w=2.0}" if preferences.text_cps > 0 else "")
    default wait_1 = ("{w=1.0}" if preferences.text_cps > 0 else "")
    default wait_05 = ("{w=0.5}" if preferences.text_cps > 0 else "")

    jump prologue_01