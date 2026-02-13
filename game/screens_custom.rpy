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
    default icon_hint = None

    frame:
        background None
        xalign 1.0
        yalign 0.0
        yoffset 40
        xoffset -5
        xsize 275
        ysize 82

        frame:
            background Frame("gui/button/button_idle.png")
            padding (10, 10, 10, 10)
            xalign 0.5

            hbox:
                spacing 20

                #image "gui/icons/psychic_icon_idle.png":
                #    at transform:
                #        zoom 0.5

                imagebutton:
                    auto "gui/icons/mind_read_icon_%s.png"
                    yalign 0.5
                    action [
                        SetLocalVariable("icon_hint", None),
                        Show("conversation_history"),
                        (Hide("psychic_powers") if max_mind_reads is not None and current_thought not in thoughts_read else NullAction()),
                        SetVariable("progress_convo", False),
                        (SetVariable("minds_read", (minds_read + 1 if minds_read < max_mind_reads else max_mind_reads)) if max_mind_reads is not None and current_thought not in thoughts_read else NullAction()),
                        (Function(play_sound, "mind_read.mp3", volume=0.5) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
                        Function(renpy.choice_for_skipping),
                        (AddToSet(thoughts_read, current_thought) if (current_thought not in thoughts_read and (max_mind_reads == None or minds_read < max_mind_reads)) else NullAction()),
                        (Call(current_thought_block, from_current=True) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
                    ]
                    hovered SetLocalVariable("icon_hint", "mind_read")
                    unhovered SetLocalVariable("icon_hint", None)

                if (check_boolean("mind_wipe_available")):
                    imagebutton:
                        auto "gui/icons/mind_wipe_icon_%s.png"
                        yalign 0.5
                        action [
                            SetLocalVariable("icon_hint", None),
                            Show("conversation_history"),
                            Function(renpy.choice_for_skipping),
                            (SetVariable("minds_rewound", (minds_rewound + 1 if minds_rewound < max_rewinds else 1)) if max_rewinds is not None else NullAction()),
                            (Call(rewind_point, from_current=True) if (max_rewinds == None or minds_rewound < max_rewinds) else NullAction())
                        ]
                        hovered SetLocalVariable("icon_hint", "mind_wipe")
                        unhovered SetLocalVariable("icon_hint", None)

                if (check_boolean("future_sight_available")):
                    imagebutton:
                        auto "gui/icons/future_sight_icon_%s.png"
                        action [
                            SetLocalVariable("icon_hint", None),
                            NullAction(),
                        ]
                        hovered SetLocalVariable("icon_hint", "future_sight")
                        unhovered SetLocalVariable("icon_hint", None)
        
        if (icon_hint != None):
            frame:
                background Frame("gui/namebox.png", xsize=120, ysize=25)
                xalign 0.5
                yoffset 15
                xsize 120
                ysize 25
                at transform:
                    rotate 3
                    alpha 0.0
                    linear 0.1:
                        alpha 1.0

                text _("Read Mind" if icon_hint == "mind_read" else ("Rewind Mind" if icon_hint == "mind_wipe" else "Future Sight")):
                    color "#000"
                    xalign 0.5
                    yalign 0.5
                    size 15

    key "K_1":
        action [
            SetLocalVariable("icon_hint", None),
            Show("conversation_history"),
            (Hide("psychic_powers") if max_mind_reads is not None and current_thought not in thoughts_read else NullAction()),
            SetVariable("progress_convo", False),
            (SetVariable("minds_read", (minds_read + 1 if minds_read < max_mind_reads else max_mind_reads)) if max_mind_reads is not None and current_thought not in thoughts_read else NullAction()),
            (Function(play_sound, "mind_read.mp3", volume=0.5) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
            Function(renpy.choice_for_skipping),
            (AddToSet(thoughts_read, current_thought) if (current_thought not in thoughts_read and (max_mind_reads == None or minds_read < max_mind_reads)) else NullAction()),
            (Call(current_thought_block, from_current=True) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
        ] 

    if (check_boolean("mind_wipe_available")):
        key "K_2":
            action [
                SetLocalVariable("icon_hint", None),
                Show("conversation_history"),
                Function(renpy.choice_for_skipping),
                (SetVariable("minds_rewound", (minds_rewound + 1 if minds_rewound < max_rewinds else 1)) if max_rewinds is not None else NullAction()),
                (Call(rewind_point, from_current=True) if (max_rewinds == None or minds_rewound < max_rewinds) else NullAction())
            ]

    if (check_boolean("future_sight_available")):
        key "K_3":
            action [
                SetLocalVariable("icon_hint", None),
                NullAction(),
            ]

style convo_progress_bar:
    left_bar Frame("gui/bar/progress_bar_left.png", gui.vbar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/progress_bar_right.png", gui.vbar_borders, tile=gui.bar_tile)
    xmaximum 450
    ysize 30

screen map_navigation(destinations):
    default xpos = 0
    default ypos = 0
    default fade_delay = 1
    default selected_destination = None

    timer 1.0:
        action SetScreenVariable("fade_delay", 0)

    frame:
        background Solid("#D1CE21")
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

        text _("SELECT YOUR DESTINATION"):
            font "gui/Decade__.ttf"
            color "#000"
            size 80
            xalign 0.5
            yalign 0.05
            at trans_fade(0.5, 0.5), fade_side_to_side(-300, 0.25)

        hbox:
            xalign 0.5
            yalign (0.7 if selected_destination == None else 0.5)
            spacing 100

            if (selected_destination == None):
                vbox:
                    ysize 751
                    xsize 300
                    vbox:
                        yalign 0.0
                        spacing 25
                        for i, destination in enumerate(destinations):
                            textbutton _(destination["label"]):
                                style "yellow_button"
                                xminimum 300
                                text_font "gui/chubhand.ttf"
                                text_yoffset 2
                                action [
                                    SetScreenVariable("selected_destination", destination),
                                    SetScreenVariable("xpos", 0),
                                    SetScreenVariable("ypos", 0),
                                ]
                                hovered [
                                    SetScreenVariable("xpos", destination["xcoord"]),
                                    SetScreenVariable("ypos", destination["ycoord"])
                                ]
                                selected False
                                at trans_fade((0.5 * i + fade_delay), 1.0), fade_side_to_side(-100, (0.5 * i + fade_delay))
                    textbutton _("SAVE GAME"):
                        xalign 0.5
                        yalign 1.0
                        text_color "#000"
                        text_font "gui/Decade__.ttf"
                        text_hover_underline True
                        action ShowMenu("saves_list", title="SAVE")
                        at trans_fade((0.5 * (len(destinations)) + 1.0), 1.0)

                frame:
                    xsize 640
                    ysize 763
                    background Frame("images/map.png")
                    at trans_fade((0.5 + fade_delay), 1.0), fade_side_to_side(75, (0.25 + fade_delay))

                    frame:
                        style "map_y_coord"
                        xpos 0
                        at transform:
                            ease 1.0:
                                xpos xpos

                    frame: 
                        style "map_x_coord"
                        ypos 0
                        at transform:
                            ease 1.0:
                                ypos ypos
            else:
                vbox:
                    xsize 300
                    spacing 50
                    text _(selected_destination["label"]):
                        color "#000"
                        font "gui/chubhand.ttf"
                        size 52
                        xalign 0.5
                        textalign 0.5
                        at trans_fade(0.25, 0.5), fade_side_to_side(-100, 0.25)

                    #Worry about more dynamic text later
                    if (selected_destination["key"] == "venue"):
                        text _("Isn’t there some small underground place near here that plays jazz or one of those made-up music genres? They’ve got to have some booze there...people wouldn’t go there if they didn’t have any."):
                            style "destination_description"
                            at trans_fade(0.5, 0.5), fade_side_to_side(-100, 0.5)
                    elif (selected_destination["key"] == "restaurant"):
                        text _("Do they have chips at this place? I kind of want chips now...Oh, I know! I’ll trick them into thinking they have chips if they don’t, and make them make some for me!"):
                            style "destination_description"
                            at trans_fade(0.5, 0.5), fade_side_to_side(-100, 0.5)

                    vbox:
                        xsize 300
                        spacing 15
                        at trans_fade(0.75, 0.5), fade_side_to_side(-100, 0.75)
                        textbutton _("CONFIRM"):
                            style "yellow_button"
                            text_font "gui/chubhand.ttf"
                            xsize 250
                            xalign 0.5
                            text_yoffset 2
                            #Again, worry about making this more dynamic later
                            action Jump("prologue_music_venue" if selected_destination["key"] == "venue" else "prologue_restaurant")
                        textbutton _("RETURN"):
                            style "yellow_button"
                            text_font "gui/chubhand.ttf"
                            xsize 250
                            xalign 0.5
                            text_yoffset 2
                            action SetScreenVariable("selected_destination", None)
                frame:
                    xsize 960
                    ysize 540
                    background Frame("images/backgrounds/venue_exterior.png" if selected_destination["key"] == "venue" else "images/backgrounds/restaurant_night.png")
                    at trans_fade(0.5, 1.0), fade_side_to_side(75, 0.25)
            

style map_y_coord:
    xmaximum 2
    yfill True
    background Solid("#000")

style map_x_coord:
    ymaximum 2
    xfill True
    background Solid("#000")

style destination_description:
    color "#000"
    xalign 0.5
    size 24

screen locked_message(message):
    frame:
        background Frame("gui/textbox.png")
        padding (50, 50, 50, 50)
        xalign 0.5
        yalign 0.9
        at transform:
            alpha 0.0
            xoffset -50
            linear 0.3:
                alpha 1.0
                xoffset 0

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
    tag menu
    default hover_row = None
    default selected_save = None
    default show_content = False

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu(title, 96, Return() if title == "SAVE" else None):

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

                                textbutton _(renpy.slot_json("1-" + (str(i + 1))).get('_save_name', '')):
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

                vbox:
                    xsize 450
                    if (title == "SAVE" and find_next_save() != "0"):
                        textbutton _("NEW SAVE"):
                            style "light_yellow_button_small"
                            action Show("save_name", filename=default_save_name()) 
                            xsize 240
                            ysize 45
                            text_font "gui/chubhand.ttf"
                            text_yoffset 3
                            text_size 40
                            text_selected_color "#000"
                            text_hover_color "#FFFC5E"
                            xalign 0.5
                            padding (40, 25, 40, 25)
                    if (selected_save is not None):
                        add FileScreenshot(selected_save + 1):
                            xalign 0.5

                        text _(renpy.slot_json("1-" + (str(selected_save + 1))).get('_save_name', '')):
                            style "save_name"
                        text _("Prologue"):
                            style "save_details"
                        text _(add_date_suffix(FileTime(selected_save + 1, format="%d", empty=(0))) + FileTime(selected_save + 1, format=_("{#file_time}%B %Y, %H:%M"))):
                            style "save_date"

                        hbox:
                            xfill True
                            spacing 5
                            box_align 0.5
                            if (title == "LOAD"):
                                textbutton _("Load"):
                                    style "light_yellow_button_small"
                                    action (Function(renpy.load, "1-" + str(selected_save + 1)))
                                    xsize 120
                                    text_font "gui/chubhand.ttf"
                                    text_yoffset 2
                                    text_size 28
                            else:
                                textbutton _("Save"):
                                    style "light_yellow_button_small"
                                    action Show("modal_popup", message="Are you sure you want to overwrite this save?", option_labels=["Yes", "No"], option_actions=[[Function(renpy.save, "1-" + str(selected_save + 1), renpy.slot_json("1-" + (str(selected_save + 1))).get('_save_name', '')), Hide("modal_popup")], Hide("modal_popup")])
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

screen modal_base():
    modal True
    zorder 200

    frame:
        xfill True
        yfill True
        background Solid ("#f2ef2973")
        at trans_fade(0.0, 0.5)

        frame:
            background Solid("#000000")
            xsize 940
            ysize 490
            xalign 0.5
            yalign 0.5

            frame:
                background Solid("#F2EE29")
                xsize 900
                ysize 450
                xalign 0.5
                yalign 0.5

                vbox:
                    xalign .5
                    yalign .5
                    spacing 45

                    transclude

screen modal_popup(message, option_labels, option_actions):
    modal True
    use modal_base:
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

    if (len(option_labels) == 1):
        key "K_RETURN":
            action option_actions[0]

screen save_name(filename):
    modal True
    default input_variable = (filename if len(filename) > 0 else '')

    use modal_base:
        text "Save File Name":
            font "gui/chubhand.ttf"
            color "#000"
            size 50
            xalign 0.5

        vbox:
            spacing 2
            ysize 50

            input:
                yalign 0.5
                xmaximum 700
                value ScreenVariableInputValue('input_variable')
                length 40
                exclude "\[\{"
            frame:
                background Solid("#000")
                ysize 2
                xsize 700

        hbox:
            xsize 700
            textbutton _("Cancel"):
                xalign 0.0
                text_hover_underline True
                action [
                    Hide("save_name"),
                ]

            textbutton _("Save"):
                xalign 1.0
                text_hover_underline True
                action [
                    Function(renpy.save, find_next_save(), input_variable if len(input_variable) > 0 else default_save_name()),
                    Hide("save_name"),
                ]

    key "K_RETURN":
        action [
            Function(renpy.save, find_next_save(), input_variable if len(input_variable) > 0 else default_save_name()),
            Hide("save_name"),
        ]

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
        yalign 0.05
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
        yalign 0.55
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
        textbutton _("Help"):
            style "black_button_on_black"
            action (ShowMenu("help") if clickable_button() else NullAction())
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
        xalign 0.035
        yalign 0.05
        size 20
        at trans_fade(1.25, 1.5), fade_side_to_side(-50, 0.75)

    text _("SOCIAL PSYCHIC SIMULATOR"):
        color "#F2EE29"
        xalign 0.98
        yalign 0.05
        size 20
        at trans_fade(1.25, 1.5), fade_side_to_side(50, 0.75)

    vbox:
        xalign 0.05
        yalign 0.6
        spacing 50
        xmaximum 700
        
        text _(title):
            color "#000"
            font "gui/chubhand.ttf"
            size 100
            xoffset -10
            at trans_fade(1.25, 1.5), fade_side_to_side(-100, 0.75)

        text _(paragraph):
            color "#000"
            at trans_fade(2.0, 1.5), fade_side_to_side(-100, 1.5)

    if (can_continue):
        text _("Press any key to continue"):
            color "#F2EE29"
            xalign 0.98
            yalign 0.95
            at transform:
                alpha 0.0
                linear 1.0:
                    alpha 1.0
                linear 0.5:
                    alpha 0.0
                repeat

        use any_key(Return())
    
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

screen conversation_history(initial_expanded = False, show_button = True, initial_opened=False):
    zorder 20
    default expanded = initial_expanded
    default opened = initial_opened

    if (show_button and renpy.get_screen("say")):
        textbutton _("HISTORY" if not expanded else "HIDE"):
            style "yellow_button"
            text_font "gui/chubhand.ttf"
            text_yoffset 2

            xalign 0.96
            yalign 0.8
            xsize 195
            action [
                SetScreenVariable("expanded", expanded == False),
                SetScreenVariable("opened", True),
            ]
            selected False
            text_selected_color "#F2EE29"
            text_hover_color "#F2EE29"

    if (opened):
        frame:
            background None
            xsize 500
            ysize 650
            yalign 0.415
            xalign 0.95
            xoffset 60

            image Solid("#000"):
                yanchor 1.0
                yoffset 630
                if (expanded):
                    at transform:
                        ysize 0
                        linear 0.5:
                            ysize 650
                else:
                    at transform:
                        ysize 650
                        linear 0.5:
                            ysize 0

            image Solid("#F2EE29"):
                yanchor 1.0
                yoffset 625
                ysize 640
                xoffset 5
                xsize 480

                if (expanded):
                    at transform:
                        ysize 0
                        linear 0.5:
                            ysize 640
                else:
                    at transform:
                        ysize 640
                        linear 0.5:
                            ysize 0

            side ("c r"):
                area (-20, 10, 500, 540)
                if (expanded):
                    viewport id "history_viewport":
                        draggable True 
                        mousewheel True
                        arrowkeys True
                        yadjustment ui.adjustment()
                        yinitial 1.0
                    
                        vbox:
                            for i, h in enumerate(_history_list[0:len(_history_list) - 1 if not renpy.get_screen("choice") else len(_history_list)]):
                                if (h.who and _history_list[i - 1] is not None and _history_list[i - 1].who and _history_list[i - 1].who is not h.who):
                                    label h.who:
                                        style "history_who"
                                        at trans_fade(0.5, 0.5)
                                elif (i == 0 and h.who):
                                    label h.who:
                                        style "history_who"
                                        at trans_fade(0.5, 0.5)
                                text _(h.what + "\n"):
                                    color (h.what_args["color"] if "color" in h.what_args else "#000")
                                    if ("color" in h.what_args and h.what_args["color"] == "#F2EE29"):
                                        outlines [ (2, "#000005", 0, 0) ]
                                    xoffset 50
                                    xmaximum 400
                                    size 20
                                    at trans_fade(0.5, 0.5)
                else:
                    null
                if (len(_history_list) - 1 > 0 and expanded):
                    vbar: 
                        value YScrollValue("history_viewport")
                        xsize 10
                        xoffset 15
                        base_bar "#000"
                        thumb "gui/bar/history_scrollbar_thumb.png"
                        if (expanded):
                            at trans_fade(0.5, 0.5)
                else:
                    null

            if (progress_convo and expanded):
                vbox:
                    xalign 0.5
                    yalign 0.95
                    spacing 5
                    at trans_fade(0.5, 0.5)

                    bar: 
                        style "convo_progress_bar"
                        value AnimatedValue(convo_progress, convo_length, 1.0, (convo_progress - 1 if progress_convo else convo_progress))

                    if (config.developer):
                        text _(str(convo_progress) + "/" + str(convo_length)):
                            color "#000"
                            xalign 0.5
                            size 15

style history_who is label

style history_who_text is label_text:
    bottom_padding 15
    xoffset 35

screen cash_money(style="left_small"):
    zorder 20

    if (style == "left_small"):
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
    elif (style == "right_large"):
        frame:
            background Solid("#F2EE29")
            xsize 225
            ysize 75
            xalign 1.0
            yalign 0.3
            xoffset 200
            at transform:
                on show:
                    xoffset 0
                    ease 0.5:
                        xoffset -200
                on hide:
                    ease 0.5:
                        xoffset 200

            text _("{font=DejaVuSans.ttf}${/font}" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.5
                font "gui/chubhand.ttf"
                size 66
                yoffset -10

screen attune_senses():
    #default transparency = 0.33

    #timer 0.5:
    #    action SetScreenVariable("transparency", random.randint(0, 100) / 100)
    #    repeat True

    image "images/sprites/jack_smug.png":
        at center

    text _("Tonight's a good night to continue working on the plan. Where should I go first?"):
        color "#F2EE29"
        xalign 0.75
        yalign 0.25
        xmaximum 350
        at transform:
            alpha 0.0
            block:
                ease 1.0:
                    alpha random.randint(31, 70) / 100
                pause 0.5
                linear 1.0:
                    alpha random.randint(0, 30) / 100
                pause 0.5
                repeat

    frame:
        background "gui/textbox.png"
        xalign 0.5
        yalign 0.95
        xsize 1376
        ysize 288
        at trans_fade(0.0, 1.0), fade_side_to_side(1800, 0.0)

        text _("Attune your psychic senses until the thoughts are barely visible"):
            xalign 0.5
            yalign 0.25
            color "#000"
            at trans_fade(1.0, 0.5)

        textbutton _("START GAME"):
            xalign 0.5
            yalign 0.8
            text_font "gui/chubhand.ttf"
            text_color "#000"
            text_hover_color "#F2EE29"
            text_hover_outlines [ (4, "#000005", 0, 0) ]
            text_size 72
            text_yoffset 5
            action [
                SetVariable("persistent.senses_attuned", True),
                Return()
            ]
            at trans_fade(6.0, 0.5)

    key "mouseup_3":
        action NullAction()

screen any_key(action):
    key "K_RETURN":
        action action
    key "K_SPACE":
        action action
    key "mouseup_1":
        action action
    key "mouseup_2":
        action action
    key "mouseup_3":
        action action
    key "K_ESCAPE":
        action action

    key "K_q":
        action action
    key "K_w":
        action action
    key "K_e":
        action action
    key "K_r":
        action action
    key "K_t":
        action action
    key "K_y":
        action action
    key "K_u":
        action action
    key "K_i":
        action action
    key "K_o":
        action action
    key "K_p":
        action action
    key "K_a":
        action action
    key "K_s":
        action action
    key "K_d":
        action action
    key "K_f":
        action action
    key "K_g":
        action action
    key "K_h":
        action action
    key "K_j":
        action action
    key "K_k":
        action action
    key "K_l":
        action action
    key "K_z":
        action action
    key "K_x":
        action action
    key "K_c":
        action action
    key "K_v":
        action action
    key "K_b":
        action action
    key "K_n":
        action action
    key "K_m":
        action action
    key "K_1":
        action action
    key "K_2":
        action action
    key "K_3":
        action action
    key "K_4":
        action action
    key "K_5":
        action action
    key "K_6":
        action action
    key "K_7":
        action action
    key "K_8":
        action action
    key "K_9":
        action action
    key "K_0":
        action action

    key "K_F1":
        action action
    key "K_F2":
        action action
    key "K_F3":
        action action
    key "K_F4":
        action action
    key "K_F5":
        action action
    key "K_F6":
        action action
    key "K_F7":
        action action
    key "K_F8":
        action action
    key "K_F9":
        action action
    key "K_F10":
        action action
    key "K_F11":
        action action
    key "K_F12":
        action action
    key "K_TAB":
        action action
    key "K_BACKSPACE":
        action action
    key "K_UP":
        action action
    key "K_DOWN":
        action action
    key "K_LEFT":
        action action
    key "K_RIGHT":
        action action
    key "K_LSHIFT":
        action action
    key "K_RSHIFT":
        action action
    key "K_LCTRL":
        action action
    key "K_RCTRL":
        action action
    key "K_LALT":
        action action
    key "K_RALT":
        action action
    key "K_CAPSLOCK":
        action action

    key "K_COMMA":
        action action
    key "K_PERIOD":
        action action
    key "K_SLASH":
        action action
    key "K_SEMICOLON":
        action action
    key "K_QUOTE":
        action action
    key "K_LEFTBRACKET":
        action action
    key "K_RIGHTBRACKET":
        action action
    key "K_BACKSLASH":
        action action
    key "K_BACKQUOTE":
        action action
    key "K_DELETE":
        action action
    key "K_MINUS":
        action action
    key "K_EQUALS":
        action action