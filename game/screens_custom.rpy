screen debug():
    
    vbox:
        xalign 0.5
        yalign 0.2

        textbutton _("Test Mind Reading"):
            action [
                Hide("debug"),
                SetVariable("minds_read", 0),
                SetVariable("minds_rewound", 0),
                SetVariable("progress_convo", True),
                Call("test_mind_reading", from_current=True)
            ]

        textbutton _("Test Map Jump"):
            action [
                Hide("debug"),
                SetVariable("progress_convo", False),
                Show("map_navigation")
            ]

        textbutton _("Test Money"):
            action [
                Hide("debug"),
                Call("test_money", from_current=True)
            ]

        textbutton _("Test Locking Choices"):
            action [
                Hide("debug"),
                Call("test_choices", from_current=True)
            ]

        textbutton _("Test Upgrading Psychic Abilities"):
            action [
                Hide("debug"),
                Show("upgrades_screen")
            ]

        textbutton _("Test Flow Chart"):
            action [
                Hide("debug"),
                Show("flow_chart")
            ]

screen psychic_powers():
    default powers_open = False
    default icon_hint = None
    default focusable = False

    if (focusable == False and powers_open):
        timer 0.25:
            action SetLocalVariable("focusable", True)

    image Solid("#000"):
        xalign 1.0
        yalign 1.0
        xoffset 25
        yoffset 35
        xsize 215
        ysize 215
        at transform:
            rotate 3
    frame:
        background Solid("#FFFC5E")
        xalign 1.0
        yalign 1.0
        xoffset -25
        yoffset -15
        xsize 205
        ysize 205

        imagebutton:
            auto "gui/icons/psychic_icon_%s.png"
            xalign 0.75
            yalign 0.5
            action [
                (Show("modal_popup", message="Click the Rewind Mind option to make the bartender forget the last few minutes of conversation", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if not check_boolean("mind_wipe_tutorial") else NullAction()),
                (ToggleLocalVariable("powers_open") if check_boolean("mind_wipe_tutorial") else SetLocalVariable("powers_open", True)),
                SetLocalVariable("focusable", False)
            ]
            hovered SetLocalVariable("icon_hint", "powers")
            unhovered SetLocalVariable("icon_hint", None)

        if (powers_open):
            if (check_boolean("mind_read_available")):
                imagebutton:
                    auto "gui/icons/mind_read_icon_%s.png"
                    xalign 0.65
                    yalign 0.65
                    action ([
                        SetLocalVariable("powers_open", False),
                        SetLocalVariable("icon_hint", None),
                        (SetVariable("minds_read", (minds_read + 1 if minds_read < max_mind_reads else max_mind_reads)) if max_mind_reads is not None else NullAction()),
                        (Call(current_thought, from_current=True) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
                    ] if focusable else NullAction())
                    hovered (SetLocalVariable("icon_hint", "mind_read") if focusable else NullAction())
                    unhovered SetLocalVariable("icon_hint", None)
                    at transform:
                        alpha 0.0
                        xoffset 0
                        linear 0.25:
                            xoffset -90
                            alpha 1.0

            imagebutton:
                auto "gui/icons/mind_wipe_icon_%s.png"
                xalign 0.65
                yalign 0.35
                action ([
                    SetLocalVariable("powers_open", False),
                    SetLocalVariable("icon_hint", None),
                    (SetVariable("minds_rewound", (minds_rewound + 1 if minds_rewound < max_rewinds else 1)) if max_rewinds is not None else NullAction()),
                    (Jump(rewind_point) if (max_rewinds == None or minds_rewound < max_rewinds) else NullAction())
                ] if focusable else NullAction())
                hovered (SetLocalVariable("icon_hint", "mind_wipe") if focusable else NullAction())
                unhovered SetLocalVariable("icon_hint", None)
                at transform:
                    alpha 0.0
                    xoffset 0
                    pause 0.2
                    linear 0.25:
                        xoffset -90
                        yoffset -50
                        alpha 1.0

            if (check_boolean("future_sight_available")):
                imagebutton:
                    auto "gui/icons/future_sight_icon_%s.png"
                    xalign 0.6
                    yalign 0.35
                    action ([
                        SetLocalVariable("powers_open", False),
                        SetLocalVariable("icon_hint", None),
                        NullAction(),
                    ] if focusable else NullAction())
                    hovered (SetLocalVariable("icon_hint", "future_sight") if focusable else NullAction())
                    unhovered SetLocalVariable("icon_hint", None)
                    at transform:
                        alpha 0.0
                        xoffset 0
                        pause 0.4
                        linear 0.25:
                            yoffset -60
                            xoffset 60
                            alpha 1.0
        
        if (icon_hint != None):
            frame:
                background Frame("gui/namebox.png", xsize=150, ysize=25)
                xalign 0.65
                yalign 1.0
                xsize 150
                ysize 25
                yoffset 60
                at transform:
                    rotate 3
                    alpha 0.0
                    linear 0.1:
                        alpha 1.0

                text _(("Activate Powers" if icon_hint == "powers" and powers_open == False else ("Deactivate Powers" if icon_hint == "powers" else ("Read Mind" if icon_hint == "mind_read" else ("Rewind Mind" if icon_hint == "mind_wipe" else "Future Sight"))))):
                    color "#000"
                    xalign 0.5
                    yalign 0.5
                    size (12 if icon_hint == "powers" and powers_open == True else 15)

screen conversation_progress():
    if (progress_convo):
        vbox:
            xalign 0.955
            yalign 0.855
            spacing 0

            bar: 
                style "convo_progress_bar"
                value AnimatedValue(convo_progress, convo_length, 1.0, (convo_progress - 1 if progress_convo else convo_progress))
                at transform:
                    rotate 3

            #text _(str(convo_progress)):
            #    color "#000"
            #    xalign 0.5
            #    yoffset -210

style convo_progress_bar:
    left_bar "#F2EE29"
    right_bar "#141414"
    xmaximum 450
    ysize 10

screen map_navigation():
    default xpos = 0
    default ypos = 0

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100

        vbox:
            textbutton _("Bar"):
                action [
                    Hide("map_navigation"),
                    Jump("bar")
                ]
                hovered [
                    SetScreenVariable("xpos", 200),
                    SetScreenVariable("ypos", 300)
                ]

            textbutton _("Alternative Shop"):
                action [
                    Hide("map_navigation"),
                    Jump("alt_shop")
                ]
                hovered [
                    SetScreenVariable("xpos", 100),
                    SetScreenVariable("ypos", 75)
                ]

            textbutton _("Cafe"):
                action [
                    Hide("map_navigation"),
                    Jump("cafe")
                ]
                hovered [
                    SetScreenVariable("xpos", 280),
                    SetScreenVariable("ypos", 20)
                ]

            textbutton _("Detective's Office"):
                action [
                    Hide("map_navigation"),
                    Jump("detective")
                ]
                hovered [
                    SetScreenVariable("xpos", 150),
                    SetScreenVariable("ypos", 450)
                ]

            textbutton _("Return"):
                yoffset 100
                action [
                    Hide("map_navigation"),
                    Jump("story")
                ]

        frame:
            xsize 300
            ysize 500
            background Solid("#141414")
            #image here

            frame:
                style "map_y_coord"
                xpos 0
                at transform:
                    pause 0.2
                    linear 1.0:
                        xpos xpos

            frame: 
                style "map_x_coord"
                ypos 0
                at transform:
                    pause 0.2
                    linear 1.0:
                        ypos ypos

style map_y_coord:
    xmaximum 2
    yfill True
    background Solid("#F2EE29")

style map_x_coord:
    ymaximum 2
    xfill True
    background Solid("#F2EE29")

screen locked_message(message):
    frame:
        background Frame("gui/textbox.png")
        padding (50, 50, 50, 50)
        xalign 0.5
        yalign 0.9
        at transform:
            alpha 0.0
            linear 0.3:
                alpha 1.0

        text _(message):
            text_align 0.5
            color "#000"
            xalign 0.5
            yalign 0.5
            size 25

screen upgrades_screen():
    default selected = None

    frame:
        xsize 1400
        ysize 800
        xalign 0.5
        yalign 0.5
        padding (50, 50, 50, 50)

        background Solid("#F2EE29")

        text _("Psychic Upgrades"):
            xalign 0.5
            yalign 0.0

        vbox:
            yalign 0.4

            hbox:
                text _("Mind Reads")
                textbutton _(str(3)):
                    action NullAction()
                textbutton _(str(4)):
                    action (NullAction() if max_mind_reads != 3 else SetScreenVariable("selected", "mr_4"))
                textbutton _(str(5)):
                    action (NullAction() if max_mind_reads != 4 else SetScreenVariable("selected", "mr_5"))
                textbutton _(str(6)):
                    action (NullAction() if max_mind_reads != 5 else SetScreenVariable("selected", "mr_6"))

            hbox:
                text _("Rewinds")
                textbutton _(str(1)):
                    action NullAction()
                textbutton _(str(2)):
                    action (NullAction() if max_rewinds != 1 else SetScreenVariable("selected", "rw_2"))
                textbutton _(str(3)):
                    action (NullAction() if max_rewinds != 2 else SetScreenVariable("selected", "rw_3"))
                textbutton _(str(4)):
                    action (NullAction() if max_rewinds != 3 else SetScreenVariable("selected", "rw_4"))

            hbox:
                text _("Future Visions")
                textbutton _(str(0)):
                    action NullAction()
                textbutton _(str(1)):
                    action (NullAction() if max_flash_forwards != 0 else SetScreenVariable("selected", "fv_1"))
                textbutton _(str(2)):
                    action (NullAction() if max_flash_forwards != 1 else SetScreenVariable("selected", "fv_2"))
                textbutton _(str(3)):
                    action (NullAction() if max_flash_forwards != 2 else SetScreenVariable("selected", "fv_3"))

        #Deffo throw some flavour text in somewhere, and at the bottom do a "You will be able to do X Y times" or whatever

        if (selected != None):
            textbutton _("Confirm"):
                xalign 0.5
                yalign 1.0
                action [        #Prolly a better way to do this - should I set two variables on the textbuttons?
                    (SetVariable("max_mind_reads", 4) if selected == "mr_4" else NullAction()),
                    (SetVariable("max_mind_reads", 5) if selected == "mr_5" else NullAction()),
                    (SetVariable("max_mind_reads", 6) if selected == "mr_6" else NullAction()),
                    (SetVariable("max_rewinds", 2) if selected == "rw_2" else NullAction()),
                    (SetVariable("max_rewinds", 3) if selected == "rw_3" else NullAction()),
                    (SetVariable("max_rewinds", 4) if selected == "rw_4" else NullAction()),
                    (SetVariable("max_flash_forwards", 1) if selected == "fv_1" else NullAction()),
                    (SetVariable("max_flash_forwards", 2) if selected == "fv_2" else NullAction()),
                    (SetVariable("max_flash_forwards", 3) if selected == "fv_3" else NullAction()),
                    Hide("upgrades_screen"),
                    Show("debug")
                ]

screen flow_chart():
    tag menu
    default zoom_level = 0.25
    default offset = 0
    default zooming_in = False
    default zooming_out = False
    default scrolling_up = False
    default scrolling_down = False
    default active_control = None

    if (zooming_in):
        timer (0.01):
            action SetScreenVariable("zoom_level", zoom_level + 0.01 if zoom_level < 1 else 1)
            repeat True
    
    if (zooming_out):
        timer (0.01):
            action SetScreenVariable("zoom_level", zoom_level - 0.01 if zoom_level > 0.25 else 0.25)
            repeat True

    if (scrolling_up):
        timer (0.01):
            action SetScreenVariable("offset", offset - 2 if offset > -350 else -350)
            repeat True
    
    if (scrolling_down):
        timer (0.01):
            action SetScreenVariable("offset", offset + 2 if offset < 350 else 350)
            repeat True
                
    frame:
        xfill True
        yfill True
        xalign 0.5
        yalign 0.5
        background None

        at transform:
            yoffset offset
            zoom zoom_level

        vbox:
            xalign 0.5
            yalign 0.5

            textbutton _("End of Day #1" if renpy.can_load(str(game_id) + "_A_01_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_01_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_01_03")
                ])
            textbutton _("End of Day #2" if renpy.can_load(str(game_id) + "_A_02_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_02_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_02_03")
                ])
            textbutton _("End of Day #3" if renpy.can_load(str(game_id) + "_A_03_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_03_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_03_03")
                ])
            textbutton _("End of Day #4" if renpy.can_load(str(game_id) + "_A_04_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_04_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_04_03")
                ])

    vbox:
        xalign 0.95
        yalign 0.9

        textbutton _("Up"):
            if (active_control == "up"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("scrolling_up", True)
            alternate SetScreenVariable("scrolling_up", False)
            hovered SetScreenVariable("active_control", "up")
            unhovered SetScreenVariable("active_control", None)

        textbutton _("Down"):
            if (active_control == "down"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("scrolling_down", True)
            alternate SetScreenVariable("scrolling_down", False)
            hovered SetScreenVariable("active_control", "down")
            unhovered SetScreenVariable("active_control", None)

        textbutton _("Zoom In"):
            if (active_control == "zoom_in"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("zooming_in", True)
            alternate SetScreenVariable("zooming_in", False)
            hovered SetScreenVariable("active_control", "zoom_in")
            unhovered SetScreenVariable("active_control", None)
        
        textbutton _("Zoom Out"):
            if (active_control == "zoom_out"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("zooming_out", True)
            alternate SetScreenVariable("zooming_out", False)
            hovered SetScreenVariable("active_control", "zoom_out")
            unhovered SetScreenVariable("active_control", None)

        textbutton _("Return"):
            xalign 0.95
            yalign 0.95
            
            action [
                Hide("flow_chart"),
                Show("debug")
            ]

screen saves_list(title="LOAD"):
    default hover_row = None
    default selected_save = None
    default show_content = False

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu(title, 96):

        if (show_content):
            vbox:
                yalign 0.25
                at trans_fade(0.0, 0.5)

                for i in range(15):
                    frame:
                        style_prefix "save_row"
                        background Solid("#F2EE29" if (hover_row is not i and selected_save is not i) else "#000")
                        xoffset ((i * 50) -400 if i > 9 else 65)

                        if (renpy.can_load("1-" + str(i + 1))):     #Will prolly need to fix this up when I add in proper save functionality
                            hbox:
                                spacing 0

                                textbutton _("Save Name"):
                                    text_color ("#F2EE29" if hover_row == i or selected_save == i else "#000")
                                    text_underline selected_save == i
                                    hovered SetScreenVariable("hover_row", i)
                                    unhovered SetScreenVariable("hover_row", None)
                                    xsize 525
                                    action SetScreenVariable("selected_save", i)
                                textbutton _(add_date_suffix(FileTime(i + 1, format="%d")) + FileTime(i + 1, format=_("{#file_time}%B %Y, %H:%M"), empty=_("empty slot"))):
                                    text_color ("#F2EE29" if hover_row == i or selected_save == i else "#000")
                                    text_underline selected_save == i
                                    hovered SetScreenVariable("hover_row", i)
                                    unhovered SetScreenVariable("hover_row", None)
                                    action SetScreenVariable("selected_save", i)
                        else:
                            hbox

                    image Solid("#3B3B3B"):
                        xsize 875
                        ysize 2
                        xoffset ((i * 50) -400 if i > 9 else 65)

            frame:
                style_prefix "save_details"
                background None #Solid("#FFFC5E")
                xalign 0.69
                yalign 0.135
                xsize 450
                ysize 525

                if (selected_save is not None):
                    vbox:
                        add FileScreenshot(selected_save + 1):
                            xalign 0.5

                        text _("Save Name"):
                            style "save_name"
                        text _("Day 1, Morning"):
                            style "save_details"
                        text _(add_date_suffix(FileTime(selected_save + 1, format="%d", empty=(0))) + FileTime(selected_save + 1, format=_("{#file_time}%B %Y, %H:%M"))):
                            style "save_date"

                        hbox:
                            xfill True
                            spacing 5
                            box_align 0.5
                            textbutton _("Load"):
                                style "light_yellow_button_small"
                                action (Function(renpy.load, "1-" + str(selected_save + 1)))
                                xsize 120
                                text_font "gui/chubhand.ttf"
                                text_yoffset 2
                                text_size 28
                            textbutton _("Delete"):
                                style "light_yellow_button_small"
                                action ([FileDelete(selected_save + 1), SetScreenVariable("selected_save", None)])
                                text_font "gui/chubhand.ttf"
                                text_yoffset 2
                                text_size 28
                
style bottom_left_frame:
    background Solid("#000")
    xsize 850
    ysize 400
    xalign 0.0
    yalign 0.8
    xoffset -750

style top_right_frame:
    background Solid("#000")
    xsize 1050
    ysize 500
    xalign 1.0
    yalign 0.0
    xoffset 1200
    yoffset 300

style bottom_right_frame:
    background Solid("#000")
    xsize 1050
    ysize 500
    xalign 1.0
    yalign 1.0
    xoffset 1250

style save_row_hbox:
    xsize 863
    ysize 36

style save_row_button_text:
    size 20

style save_details_vbox:
    spacing 10

style save_name:
    font "gui/chubhand.ttf"
    color "#000"
    xalign 0.5
    size 35

style save_details:
    color "#000"
    xalign 0.5
    text_align 0.5
    size 24

style save_date is save_details:
    size 20

style light_yellow_button is yellow_button:
    background Frame("gui/button/button_light_idle.png")
    hover_background Frame("gui/button/button_light_hover.png")

style light_yellow_button_text is yellow_button_text:
    hover_color "#FFFC5E"

style light_yellow_button_small is light_yellow_button:
    padding (20, 5, 20, 5)

style light_yellow_button_small_text is light_yellow_button_text

screen modal_popup(message, option_labels, option_actions):
    modal True

    zorder 200

    style_prefix "confirm"

    frame:
        xfill True
        yfill True
        background Solid ("#f2ef2973")
        at trans_fade(0.0, 0.5)

        frame:
            background Solid("#000000")
            xsize 900
            ysize 450

            frame:
                background Solid("#F2EE29")
                xsize 900
                ysize 450

                vbox:
                    xalign .5
                    yalign .5
                    spacing 45

                    label _(message):
                        style "confirm_prompt"
                        text_color "#000"
                        xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 150

                        for (i, label) in enumerate(option_labels):
                            textbutton _(label):
                                action option_actions[i]

screen pause_menu():
    tag menu
    
    frame:
        background Solid("#000")
        style "title_half_card"
    frame:
        background Solid("#F2EE29")
        style "title_half_card_right"

    frame:
        background Solid("#F2EE29")
        style "title_half_card"
        at title_card_slide("down")

    frame: 
        background Solid("#000")
        style "title_half_card_right"
        at title_card_slide("up")

    text _("{color=#000}BLACK{/color}{color=#F2EE29}MIND{/color}"):
        xalign 0.5
        yalign 0.1
        font "gui/Decade__.ttf"
        size 90
        xoffset -18
        at trans_fade(0.5, 0.5)

    vbox:
        xalign 0.3
        yalign 0.75
        spacing 50
        at trans_fade(1.0, 0.5), fade_side_to_side(-1000, 0.5)
        textbutton _("Flow Chart"):
            style "yellow_button_on_yellow"
            #action ShowMenu("flow_chart")
            action (Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Characters"):
            style "yellow_button_on_yellow"
            #action ShowMenu("characters")
            action (Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Load"):
            style "yellow_button_on_yellow"
            action (ShowMenu("saves_list") if clickable_button() else NullAction())
        textbutton _("Menu"):
            style "yellow_button_on_yellow"
            action (MainMenu() if clickable_button() else NullAction())
        textbutton _("Quit"):
            style "yellow_button_on_yellow"
            action (Quit() if clickable_button() else NullAction())

    vbox:
        xalign 0.775
        yalign 0.7
        spacing 50
        at trans_fade(1.0, 0.5), fade_side_to_side(1000, 0.5)
        textbutton _("Psychic Powers"):
            style "black_button_on_black"
            #action ShowMenu("upgrades_screen")
            action (Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Notes"):
            style "black_button_on_black"
            #action ShowMenu("notes")
            action (Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Settings"):
            style "black_button_on_black"
            action (ShowMenu("preferences") if clickable_button() else NullAction())
        textbutton _("Return"):
            style "black_button_on_black"
            action (Return() if clickable_button() else NullAction())

style yellow_button_on_yellow:
    background Frame("gui/button/button_idle.png")
    hover_background Frame("gui/button/button_idle.png")
    padding (80, 20, 80, 20)
    xsize 486

style yellow_button_on_yellow_text:
    color "#000"
    font "gui/chubhand.ttf"
    hover_underline True
    size 65
    yoffset 5
    xalign 0.5

style black_button_on_black is yellow_button_on_yellow:
    background Frame("gui/button/button_hover.png")
    hover_background Frame("gui/button/button_hover.png")
    padding (80, 20, 80, 20)
    xsize 603

style black_button_on_black_text is yellow_button_on_yellow_text:
    color "#F2EE29"

screen chapter_breaks(title, paragraph):
    default can_continue = False

    timer 2.75:
        action SetScreenVariable("can_continue", True)

    frame:
        background Solid("#000")
        style "title_half_card"
    frame:
        background Solid("#F2EE29")
        style "title_half_card_right"

    frame:
        background Solid("#F2EE29")
        style "title_half_card"
        at title_card_slide("down")

    frame: 
        background Solid("#000")
        style "title_half_card_right"
        at title_card_slide("up")

    text _("BLACKMIND"):
        font "gui/Decade__.ttf"
        size 150
        xalign 0.98
        yalign 0.2
        color "#F2EE29"
        at trans_fade(0.5, 0.5), fade_side_to_side(100)

    text _("OPEN YOUR THIRD EYE"):    
        color "#000"
        xalign 0.05
        yalign 0.05
        size 20
        at trans_fade(1.25, 1.5), fade_side_to_side(-50, 0.75)

    text _("SOCIAL PSYCHIC SIMULATOR"):
        color "#F2EE29"
        xalign 0.95
        yalign 0.05
        size 20
        at trans_fade(1.25, 1.5), fade_side_to_side(50, 0.75)

    vbox:
        xalign 0.1
        yalign 0.75
        spacing 100
        xmaximum 700
        
        text _(title):
            color "#000"
            font "gui/chubhand.ttf"
            size 100
            at trans_fade(1.25, 1.5), fade_side_to_side(-100, 0.75)

        text _(paragraph):
            color "#000"
            at trans_fade(2.0, 1.5), fade_side_to_side(-100, 1.5)

    if (can_continue):
        text _("Click to Continue"):
            color "#F2EE29"
            xalign 0.95
            yalign 0.95
            at transform:
                alpha 0.0
                linear 1.0:
                    alpha 1.0
                linear 0.5:
                    alpha 0.0
                repeat

        key "mouseup_1":
            action Return()
    
    key "mouseup_3":
        action NullAction()

screen calendar(day, section, sections=4):
    frame: 
        background None
        xsize 600
        ysize 80

        xpos 270
        ypos -550
        
        at transform:
            rotate -40
        
        image Solid("#000"):
            xsize 50
            xanchor 1.0
            at transform:
                linear 0.5:
                    xsize 600
    
    frame:
        background None
        xsize 600
        ysize 80
        
        ypos -225
        xpos -80
        at transform:
            rotate -30

        image Solid("#F2EE29"):
            xsize 50
            at transform:
                linear 0.5:
                    xsize 600

        text _(day):
            yalign 0.5
            yoffset 3
            xalign 0.15
            color "#000"
            font "gui/chubhand.ttf"
            size 50

            at transform:
                xoffset -400
                pause 0.25
                linear 0.5:
                    xoffset 0

        hbox:
            xalign (0.6 if sections == 4 else 0.5)
            yalign 0.5
            spacing 5
            at transform:
                xoffset 400
                pause 0.25
                linear 0.5:
                    xoffset 0

            for i in range(sections):
                frame: 
                    background Solid("#000")
                    xsize 20
                    ysize 20
                    padding (3, 3, 3, 3)
                    at transform:
                        rotate -45

                    if (i <= section - 1):
                        image Solid("#F2EE29")

screen conversation_history():
    frame:
        background None
        xsize 500
        ysize 900
        xalign 0.95

        image Solid("#000"):
            xsize 500
            ysize 825
            yoffset -60
            xoffset -170
            at transform:
                alpha 0.8
                rotate 3

        image Solid("#F2EE29"):
            xsize 500
            ysize 800
            yoffset -50
            xoffset -190
            at transform:
                alpha 0.8
                rotate 3

        side ("c r"):
            area (40, 40, 500, 675)
            at transform:
                rotate 3
                xoffset -180
                yoffset -90

            viewport id "history_viewport":
                draggable True 
                mousewheel True
                arrowkeys True
                yadjustment ui.adjustment()
                yinitial 0.0
                vbox:
                    for h in _history_list[0:len(_history_list) - 1]:
                        #if (h.who):
                        #    label h.who
                        text _(h.what + "\n"):
                            color (h.what_args["color"] if "color" in h.what_args else "#FFF")
                            xoffset 50
                            xmaximum 400
                            size 20
            if (len(_history_list) - 1 > 0):
                vbar value YScrollValue("history_viewport"):
                    xsize 10
                    xoffset -5
            else:
                null

    use conversation_progress
    if (check_boolean("psychic_powers_available")):
        use psychic_powers

screen cash_money():
    frame:
        background Solid("#F2EE29")
        xsize 200
        ysize 50
        xalign 0.0
        yalign 0.3
        at transform:
            on show:
                xoffset -200
                ease 0.5:
                    xoffset 0
            on hide:
                ease 0.5:
                    xoffset -200

        text _("{font=DejaVuSans.ttf}${/font}" + str(f'{money:.2f}')):
            color "#000"
            xalign 0.25
            font "gui/chubhand.ttf"
            size 40
            yoffset -5