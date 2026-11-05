label variables:
    
    define barbara= Character("Barbara", what_color="#000")
    define cat = Character("Cat", what_color="#000")
    define docherty = Character("???", what_color="#000")
    define eddie = Character("Eddie", what_color="#000")
    define graves = Character("Graves", what_color="#000")
    define jack = Character("Jack", what_color="#000", image="jack")
    define lloyd = Character("Lloyd", what_color="#000", image="lloyd")
    define narrator = Character(None, what_color="#000")

    define character_thoughts = Character(who_color="#F2EE29", what_color="#F2EE29", namebox_style="namebox_inverted", window_style="window_inverted", what_prefix="(", what_suffix=")")
    define barbara_thoughts = Character(kind=character_thoughts, name="Barbara")
    define bartender = Character(kind=barbara, name="Bartender")
    define bartender_thoughts = Character(kind=barbara_thoughts, name="Bartender")
    define cat_thoughts = Character(kind=character_thoughts, name="Cat")
    define detective = Character(kind=graves, name="Detective")
    define detective_thoughts = Character(kind=character_thoughts, name="Detective")
    define docherty_thoughts = Character(kind=character_thoughts, name="???")
    define dying_jack = Character(kind=jack, name="Dying Man", image=None, what_size=20)
    define eddie_thoughts = Character(kind=character_thoughts, name="Eddie")
    define employee = Character(kind=eddie, name="Employee")
    define employee_thoughts = Character(kind=character_thoughts, name="Employee")
    define graves_thoughts = Character(kind=character_thoughts, name="Graves")
    define librarian = Character(kind=cat, name="Librarian")
    define librarian_thoughts = Character(kind=cat_thoughts, name="Librarian")
    define lloyd_thinking = Character(kind=lloyd, what_prefix="(", what_suffix=")")
    define lloyd_narrating = Character(kind=lloyd, what_color="#3B3B3B")
    define mental_jack = Character(kind=jack, name="???", image=None)
    define phone = Character("Phone", what_color="#000")
    define unknown = Character("???", what_color="#000")

    #Persistent variables
    default persistent.game_launched = False
    default persistent.cgs = [
        {
            "images": [{
                "file": "cg1_0.png",
                "locked": True
            }, {
                "file": "cg1_1.png",
                "locked": True 
            }, {
                "file": "cg1_2.png",
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
        xalign 1.0
        alpha 0.0
        linear 2.0:
            alpha 1.0

    transform cg_1_reveal:
        zoom 3.0
        xoffset -600
        yoffset -200
        pause 2.0

        linear 7.0:
            xoffset -550
            yoffset -1800

        linear 3.0:
            zoom 1.0
            xoffset 0
            yoffset 0

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

    transform greyscale_instant:
        matrixcolor SaturationMatrix(0.0)

    transform opening_text:
        xsize 0.6

    transform drunk_cycle(blur, angle, zoom = 1.0):
        rotate 0
        zoom (zoom if zoom != 1.0 else 1.0)
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
                zoom (zoom if zoom != 1.0 else 1.0)
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

    image side lloyd friendly:
        "images/sprites/lloyd_friendly.png"
        portrait_crop

    image side lloyd neutral:
        "images/sprites/lloyd_neutral.png"
        portrait_crop
    
    image side lloyd scared:
        "images/sprites/lloyd_scared.png"
        portrait_crop

    image side lloyd thinking:
        "images/sprites/lloyd_thinking.png"
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

    image detective_office = ConditionSwitch(
        "reading_mind == True",
        "detective_office_greyscale",
        "True",
        "images/backgrounds/detective_office.png"
    )

    image detective_office_greyscale:
        "images/backgrounds/detective_office.png"
        greyscale

    image library_day = ConditionSwitch(
        "reading_mind == True",
        "library_day_greyscale",
        "True",
        "images/backgrounds/library_day.png"
    )

    image library_day_greyscale:
        "images/backgrounds/library_day.png"
        greyscale

    image library_night = ConditionSwitch(
        "reading_mind == True",
        "library_night_greyscale",
        "True",
        "images/backgrounds/library_night.png"
    )

    image library_night_greyscale:
        "images/backgrounds/library_night.png"
        greyscale

    image office_interview_room = ConditionSwitch(
        "reading_mind == True",
        "office_interview_room_greyscale",
        "True",
        "images/backgrounds/office_interview_room.png"
    )

    image office_interview_room_greyscale:
        "images/backgrounds/office_interview_room.png"
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

    default ineffective_rewinds = ["prologue_montage_rewind", "prologue_12"]
    default paused_ineffective_rewinds = ["prologue_12"]

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
    #default game_id = persistent.game_id
    #$ persistent.game_id += 1
    default day = 0
    default branch = None
    default person = "barbara_prologue"
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
    default booleans = ["call_future_sight"]
    default wait_2 = ("{w=2.0}" if preferences.text_cps > 0 else "")
    default wait_1 = ("{w=1.0}" if preferences.text_cps > 0 else "")
    default wait_05 = ("{w=0.5}" if preferences.text_cps > 0 else "")
    default current_input = "KB"
    default history_expanded = False

    jump prologue_01