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
            action NullAction()

screen psychic_powers():
    frame:
        xalign 1.0
        yalign 0.0
        background Solid("#ffea00")
        padding (5, 5, 5, 5)
        
        vbox:
            if (current_thought is not None):
                textbutton _("Read Mind" if minds_read < max_mind_reads else "Power Exhausted"):
                    text_color "#000"
                    action [
                        SetVariable("minds_read", (minds_read + 1 if minds_read < max_mind_reads else max_mind_reads)),
                        (Call(current_thought, from_current=True) if minds_read < max_mind_reads else NullAction())
                    ]
            if (current_conversation is not None):
                textbutton _("Rewind Mind" if minds_rewound < max_rewinds else "Power Exhausted"):
                    text_color "#000"
                    action [
                        SetVariable("minds_rewound", (minds_rewound + 1 if minds_rewound < max_rewinds else 1)),
                        (Jump("activate_rewind") if minds_rewound < max_rewinds else NullAction())
                    ]

screen conversation_progress():
    if (progress_convo):
        bar: 
            style "convo_progress_bar"
            value AnimatedValue(convo_progress, convo_length, 1.0, (convo_progress - 1 if progress_convo else convo_progress))

        text _(str(convo_progress)):
            color "#FFEA00"
            xalign 0.5
            yalign 0.15

style convo_progress_bar:
    left_bar "#ffea00"
    right_bar "#141414"
    xmaximum 500
    xalign 0.5
    yalign 0.1

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
    background Solid("#FFEA00")

style map_x_coord:
    ymaximum 2
    xfill True
    background Solid("#FFEA00")

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
            color "#FFF"
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

        background Solid("#ffec17ff")

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