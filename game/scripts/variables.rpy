label variables:
    
    define narrator = Character(None, what_color="#000")
    define jack = Character("Jack", what_color="#000", image="jack")
    define barbara= Character("Barbara", what_color="#000")
    define character_thoughts = Character(who_color="#F2EE29", what_color="#F2EE29", namebox_style="namebox_inverted", window_style="window_inverted")
    define barbara_thoughts = Character(kind=character_thoughts, name="Barbara")
    define docherty = Character("???", what_color="#000")
    define docherty_thoughts = Character(kind=character_thoughts, name="???")

    define bartender = Character(kind=barbara, name="Bartender")
    define bartender_thoughts = Character(kind=barbara_thoughts, name="Bartender")

    #Persistent variables
    default persistent.game_launched = False
    default persistent.cgs = [
        {
            "images": [{
                "file": "cg1_docherty.png",
                "locked": True
            }, {
                "file": "cg1_placeholder.png",
                "locked": True
            }]
        }
    ]
    default persistent.music_tracks = [
        {
            "file": "brain_matter.mp3",
            "title": "Brain Matter",
            "handle": "brain_matter",
            "unlocked": True,
            "length": 125
        },
        {
            "file": "bourbon_mood.mp3",
            "title": "Bourbon Mood",
            "handle": "neutral_1",
            "unlocked": False,
            "length": 277
        },
        {
            "file": "blundering_mistake.mp3",
            "title": "Blundering Mistake",
            "handle": "tense_1",
            "unlocked": False,
            "length": 90
        },
        {
            "file": "before_midnight.mp3",
            "title": "Before Midnight",
            "handle": "ambient_1",
            "unlocked": False,
            "length": 137
        },
        {
            "file": "beware_murderer.mp3",
            "title": "Beware! Murderer!",
            "handle": "tense_2",
            "unlocked": False,
            "length": 99
        },
        {
            "file": "bitter_memories.mp3",
            "title": "Bitter Memories",
            "handle": "neutral_2",
            "unlocked": False,
            "length": 137
        }
    ]
    default persistent.game_id = 0
    default persistent.senses_attuned = False
    default persistent.psychic_splash = "always"

    default preferences.fullscreen = True
    default preferences.music_volume = 0.75 

    #Transforms
    transform center:
        zoom 0.33
        xalign 0.5 
        yalign 0.0

    transform zener_card_col_up (time):
        zoom 0.3
        ypos 960        #Start out offscreen, at the bottom
        pause time      #Pause for a while, unique time for each card

        block:          #Move up - we're all moving at the same rate but with the delay in pause that should create natural spacing between cards
            ypos 960
            linear 45.8:
                ypos -345

            repeat      #Reset so we're not constantly rendering new cards

    transform zener_card_col_down (time):
        zoom 0.3
        ypos -345
        pause time

        block:
            ypos -345
            linear 33.1:
                ypos 940

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
                    xoffset 100
            parallel:
                pause 2.0
                linear 1.0:
                    alpha 0.0
        
        xoffset 0
        pause (0.2 if pause_time == 3.0 else 0.0)
        repeat

    transform menu_button (delay):
        alpha 0.0
        yoffset -50
        pause delay
        linear 0.5:
            alpha 1.0
            yoffset 0

    transform menu_bottom_left_slide:
        alpha 0.0
        pause 0.5
        alpha 1.0
        rotate 45
        linear 0.33:
            xoffset 400
            yoffset 400

    transform menu_top_right_slide:
        alpha 0.0
        pause 0.5
        alpha 1.0
        rotate 45
        linear 0.33:
            xoffset -700
            yoffset -800

    transform menu_bottom_right_slide:
        alpha 0.0
        pause 0.5
        alpha 1.0
        rotate 135
        linear 0.33:
            xoffset -400
            yoffset 400

    transform trans_fade (pause_time, time=5.0):
        alpha 0.0
        pause pause_time
        linear time alpha 1.0

    transform trans_fade_out (pause_time, time=5.0):
        alpha 1.0
        pause pause_time
        linear time alpha 0.0

    transform fade_side_to_side(offset=50, pause_time=0.0):
        xoffset offset
        pause pause_time
        linear 1.0:
            xoffset 0

    transform fade_up_down(offset=50, pause_time=0.0):
        yoffset offset
        pause pause_time
        linear 1.0:
            yoffset 0

    transform portrait_crop:
        zoom 0.2
        xanchor 0.5
        yanchor 0.5
        xalign 0.0
        yalign 1.0
        yoffset 350
        xoffset -240
        rotate -5
        #crop (0, 0, 900, 700)

    transform cg_1_teaser:
        zoom 1.2
        xalign 1.0
        yalign 1.4
        alpha 0.0
        linear 2.0:
            alpha 1.0

    transform dark_tint:
        matrixcolor TintMatrix("#6d6d6d")

    transform greyscale:
        matrixcolor SaturationMatrix(1.0)
        linear 0.66:
            matrixcolor SaturationMatrix(0.0)

    transform greyscale_cycle:
        matrixcolor SaturationMatrix(1.0)
        linear 1.0:
            matrixcolor SaturationMatrix(0.0)
        pause 0.5
        linear 1.0:
            matrixcolor SaturationMatrix(1.0)

    transform tinted_greyscale_cycle:   #Prolly not needed any more but keep it here just in case
        matrixcolor SaturationMatrix(1.0) * TintMatrix("#6d6d6d")
        linear 1.0:
            matrixcolor SaturationMatrix(0.0) * TintMatrix("#6d6d6d")
        pause 0.5
        linear 1.0:
            matrixcolor SaturationMatrix(1.0) * TintMatrix("#6d6d6d")

    transform opening_text:
        xsize 0.6

    transform drunk_cycle(blur, angle, zoom):
        rotate 0
        zoom (1.1 if zoom != 1.0 else 1.0)
        blur 0
        xanchor 0.5
        yanchor 0.5
        xoffset 960
        yoffset 540

        parallel:
            linear 2.5:
                blur blur
            linear 2.5:
                blur 0
            repeat

        parallel:
            linear 2.5:
                rotate angle
            linear 2.5:
                rotate 0
            linear 2.5:
                rotate (angle * -1)
            linear 2.5:
                rotate 0
            repeat

        parallel:
            linear 2.5:
                zoom zoom
            linear 2.5:
                zoom (1.1 if zoom != 1.0 else 1.0)
            repeat

    transform ring_mind_read_expand(xoffset=0, yoffset=0):
        zoom 0.1
        xalign 0.5 
        yalign 0.0
        xoffset xoffset
        yoffset yoffset
        xanchor 0.5
        yanchor 0.5
        alpha 0.0

        parallel:
            linear 0.25:
                alpha 1.0
        parallel:
            linear 2.0:
                zoom 5.0

    transform ring_mind_rewind_pause(xoffset=0, yoffset=0):
        zoom 5.0
        xalign 0.5 
        yalign 0.0
        xoffset xoffset
        yoffset yoffset
        xanchor 0.5
        yanchor 0.5
        alpha 1.0

        parallel:
            pause 0.35
            linear 0.25:
                alpha 0.0
        parallel:
            linear 0.5:
                zoom 0.1

    transform pulse:
        alpha 0.0
        linear 2.0:
            alpha 1.0
        linear 2.0:
            alpha 0.0
        repeat

    transform restaurant:
        zoom 1.25
        yoffset -130

    define quick_dissolve = Dissolve(0.5)
    define slow_dissolve = Dissolve(2.0)

    #Sprites
    image barbara_angry = ConditionSwitch(
        "rewound_mind == True",
        "barbara_angry_greyscale",
        "_last_say_who in ['barbara', 'bartender', 'bartender_thoughts'] or not renpy.get_screen('say')", 
        "images/sprites/barbara_angry.png", 
        "not _last_say_who == 'barbara'", 
        "barbara_angry_tint"
    )

    image barbara_sad = ConditionSwitch(
        "rewound_mind == True",
        "barbara_sad_greyscale",
        "_last_say_who in ['barbara', 'bartender', 'bartender_thoughts'] or not renpy.get_screen('say')",
        "images/sprites/barbara_sad.png",
        "not _last_say_who == 'barbara'",
        "barbara_sad_tint"
    )

    image barbara_smiling = ConditionSwitch(
        "rewound_mind == True",
        "barbara_smiling_greyscale",
        "_last_say_who in ['barbara', 'bartender', 'bartender_thoughts'] or not renpy.get_screen('say')",
        "images/sprites/barbara_smiling.png",
        "not _last_say_who == 'barbara'",
        "barbara_smiling_tint"
    )

    image barbara_thinking = ConditionSwitch(
        "rewound_mind == True",
        "barbara_thinking_greyscale",
        "_last_say_who in ['barbara', 'bartender', 'bartender_thoughts'] or not renpy.get_screen('say')",
        "images/sprites/barbara_thinking.png",
        "not _last_say_who == 'barbara'",
        "barbara_thinking_tint"
    )

    image docherty_neutral = ConditionSwitch(
        "rewound_mind == True",
        "docherty_neutral_greyscale",
        "_last_say_who in ['docherty', 'docherty_thoughts'] or not renpy.get_screen('say')",
        "images/sprites/docherty_neutral.png",
        "not _last_say_who == 'docherty'",
        "docherty_neutral_tint"
    )

    image barbara_angry_tint:
        "images/sprites/barbara_angry.png"
        dark_tint

    image barbara_angry_greyscale:
        "images/sprites/barbara_angry.png"
        greyscale_cycle

    image barbara_sad_tint:
        "images/sprites/barbara_sad.png"
        dark_tint

    image barbara_sad_greyscale:
        "images/sprites/barbara_sad.png"
        greyscale_cycle

    image barbara_smiling_tint:
        "images/sprites/barbara_smiling.png"
        dark_tint

    image barbara_smiling_greyscale:
        "images/sprites/barbara_smiling.png"
        greyscale_cycle

    image barbara_thinking_tint:
        "images/sprites/barbara_thinking.png"
        dark_tint

    image barbara_thinking_greyscale:
        "images/sprites/barbara_thinking.png"
        greyscale_cycle

    image docherty_neutral_tint:
        "images/sprites/docherty_neutral.png"
        dark_tint

    image docherty_neutral_greyscale:
        "images/sprites/docherty_neutral.png"
        greyscale_cycle

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

    #Backgrounds
    image bar = ConditionSwitch(
        "reading_mind == True",
        "bar_greyscale",
        "True",
        "images/backgrounds/bar.png"
    )

    image bar_greyscale:
        "images/backgrounds/bar.png"
        greyscale

    image street = ConditionSwitch(
        "reading_mind == True",
        "street_greyscale",
        "True",
        "images/backgrounds/street.png"
    )

    image street_greyscale:
        "images/backgrounds/street.png"
        greyscale

    image red_pulse:
        Solid("#cc0000")
        pulse
        

    #Other images
    image rewind = Image("gui/icons/mind_wipe_icon_idle.png", tag="rewind")

    #Psychic powers
    default current_thought_block = ""
    default current_thought = None
    default current_conversation = None
    default progress_convo = False
    default convo_length = 0

    default max_mind_reads = None
    default max_rewinds = None
    default max_flash_forwards = 0

    default minds_read = 0
    default minds_rewound = 0
    default convo_progress = 0
    
    default rewind_point = "prologue_02"
    default thoughts_read = []
    default reading_mind = False
    default rewound_mind = False

    default ineffective_rewinds = ["prologue_montage_rewind", "prologue_10"]
    default paused_ineffective_rewinds = ["prologue_10"]

    default money = 12

    # Global(ish) variables
    default destinations = [
        {
            "id": 1,
            "key": "venue",
            "label": "Music Venue",
            "xcoord": 200,
            "ycoord": 300,
        },
        {
            "id": 2,
            "key": "restaurant",
            "label": "Restaurant",
            "xcoord": 250,
            "ycoord": 350
        },
        {
            "id": 3,
            "key": "detective",
            "label": "Detective's Office",
            "xcoord": 100,
            "ycoord": 600
        },
        {
            "id": 4,
            "key": "bar",
            "label": "Local Bar",
            "xcoord": 200,
            "ycoord": 350
        },
        {
            "id": 5,
            "key": "newspaper",
            "label": "Newspaper",
            "xcoord": 450,
            "ycoord": 50
        },
        {
            "id": 6,
            "key": "alt_shop",
            "label": "New Age Shop",
            "xcoord": 500,
            "ycoord": 300
        }
    ]

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
    default red_flash = Fade(0.25, 0.25, 0.25, color='#cc0000')
    default white_flash = Fade(0.05, 0.25, 0.25, color='#FFF')
    default booleans = []
    default wait_2 = ("{w=2.0}" if preferences.text_cps > 0 else "")
    default wait_1 = ("{w=1.0}" if preferences.text_cps > 0 else "")
    default wait_05 = ("{w=0.5}" if preferences.text_cps > 0 else "")

    jump prologue_01