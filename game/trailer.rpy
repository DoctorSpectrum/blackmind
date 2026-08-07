screen trailer():
    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")

        grid 2 4:
            xalign 0.5
            yalign 0.5

            textbutton _("Scene #1"):
                action Show("trailer_scene_1")
            textbutton _("Scene #2"):
                action Show("trailer_scene_2")
            textbutton _("Scene #3"):
                action Show("trailer_scene_3")
            textbutton _("Scene #4"):
                action Show("trailer_scene_4")
            textbutton _("Scene #5"):
                action Show("trailer_scene_5")
            textbutton _("Scene #6"):
                action Show("trailer_scene_6")
            textbutton _("Scene #7"):
                action Show("trailer_scene_7")
            textbutton _("Scene #8"):
                action [
                    Function(renpy.music.stop),
                    Show("trailer_scene_8")
                ]
        
        textbutton _("Full Trailer"):
            xalign 0.5
            text_color "#000"
            yalign 0.8
            action Show("full_trailer")

        textbutton _("Return"):
            xalign 1.0
            yalign 1.0
            xoffset -10
            yoffset -10
            text_color "#FFF"
            action Hide("trailer")

screen trailer_scene_1():
    timer 6.0:
        action Hide("trailer_scene_1")

    frame:
        xfill True
        yfill True
        background Solid("#000")

    image "images/cgs/cg1_0.png":
        at transform:
            zoom 1.5
            xalign 0.0
            yalign 0.9
            alpha 0.0

            parallel:
                linear 2.0:
                    alpha 1.0
                pause 2.0
                linear 2.0:
                    alpha 0.0

            parallel:
                linear 6.0:
                    xalign 1.0

screen trailer_scene_2():
    timer 9.0:
        action Hide("trailer_scene_2")

    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")
        at transform:
            alpha 0.0
            linear 1.0:
                alpha 1.0
            pause 7.0
            linear 1.0:
                alpha 0.0
        
        vbox:
            xalign 0.25
            yalign 0.25

            text _("A {color=#F2EE29}{outlinecolor=#000}SERIAL KILLER{/outlinecolor}{/color} IS"):
                style "trailer_text"
                at transform:
                    xoffset -1400
                    pause 1.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset 2000
            text _("STALKING THE STREETS"):
                style "trailer_text"
                at transform:
                    xoffset 2000
                    pause 1.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset -1800

screen trailer_scene_3():
    timer 2.8:
        action Hide("trailer_scene_3")

    add Movie(size=(1920, 1080), play="videos/trailer_clip_1.ogv", loop=False)

screen trailer_scene_4():
    timer 13.0:
        action Hide("trailer_scene_4")

    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")
        at transform:
            alpha 0.0
            linear 1.0:
                alpha 1.0
            pause 11.0
            linear 1.0:
                alpha 0.0
        
        vbox:
            xalign 0.25
            yalign 0.1

            text _("THEIR {color=#F2EE29}{outlinecolor=#000}VICTIMS{/outlinecolor}{/color} HAVE"):
                style "trailer_text"
                at transform:
                    xoffset -1600
                    pause 1.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset 2000
            text _("NOTHING IN COMMON."):
                style "trailer_text"
                at transform:
                    xoffset 2000
                    pause 1.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset -1600

        vbox:
            xalign 0.5
            yalign 0.9

            text _("THERE IS NO WAY TO TELL"):
                style "trailer_text"
                at transform:
                    xoffset -1800
                    pause 5.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset 2000
            text _("WHERE THEY WILL"):
                style "trailer_text"
                at transform:
                    xoffset 2000
                    pause 5.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset -1800
            text _("{color=#F2EE29}{outlinecolor=#000}STRIKE NEXT{/outlinecolor}{/color}."):
                style "trailer_text"
                at transform:
                    xoffset 2000
                    pause 5.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset -1800

screen trailer_scene_5():    
    timer 7.0:
        action Hide("trailer_scene_5")

    add Movie(size=(1920, 1080), play="videos/trailer_clip_2.ogv", loop=False)

screen trailer_scene_6():
    timer 9.0:
        action Hide("trailer_scene_6")

    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")
        at transform:
            alpha 0.0
            linear 1.0:
                alpha 1.0
            pause 7.0
            linear 1.0:
                alpha 0.0
        
        vbox:
            xalign 0.25
            yalign 0.25

            text _("WILL YOUR {color=#F2EE29}{outlinecolor=#000}PSYCHIC POWERS{/outlinecolor}{/color}"):
                style "trailer_text"
                size 120
                at transform:
                    xoffset -1800
                    pause 1.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset 2000
            text _("BE ENOUGH TO STOP THEM?"):
                style "trailer_text"
                size 120
                at transform:
                    xoffset 2000
                    pause 1.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset -1800

screen trailer_scene_7():
    default word_highlight = 0
    timer 6.0:
        action Hide("trailer_scene_7")

    timer 0.1:
        action [
            Play("voice", "audio/voice/partials/jack/jack_mind_read_02.ogg"),
            SetScreenVariable("word_highlight", 1)
        ]
    timer 0.6:
        action SetScreenVariable("word_highlight", 2)
    timer 0.8:
        action SetScreenVariable("word_highlight", 3)
    timer 1.4:
        action SetScreenVariable("word_highlight", 4)
    timer 1.6:
        action SetScreenVariable("word_highlight", 5)
    timer 2.1:
        action SetScreenVariable("word_highlight", 6)
    timer 2.6:
        action SetScreenVariable("word_highlight", 7)
    timer 3.0:
        action SetScreenVariable("word_highlight", 8)

    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")

        frame:
            background Solid("#000000d0")
            style "title_half_card_right"
            at transform:
                yoffset -1080
                linear 0.25:
                    yoffset -6

        if (word_highlight == 1):
            text _("{color=#F2EE29}{outlinecolor=#000}YOU{/outlinecolor}{/color} CAN'T\nHIDE YOUR\nSECRETS\nFROM ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        elif (word_highlight == 2):
            text _("YOU {color=#F2EE29}{outlinecolor=#000}CAN'T{/outlinecolor}{/color}\nHIDE YOUR\nSECRETS\nFROM ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        elif (word_highlight == 3):
            text _("YOU CAN'T\n{color=#F2EE29}{outlinecolor=#000}HIDE{/outlinecolor}{/color} YOUR\nSECRETS\nFROM ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        elif (word_highlight == 4):
            text _("YOU CAN'T\nHIDE {color=#F2EE29}{outlinecolor=#000}YOUR{/outlinecolor}{/color}\nSECRETS\nFROM ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        elif (word_highlight == 5):
            text _("YOU CAN'T\nHIDE YOUR\n{color=#F2EE29}{outlinecolor=#000}SECRETS{/outlinecolor}{/color}\nFROM ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        elif (word_highlight == 6):
            text _("YOU CAN'T\nHIDE YOUR\nSECRETS\n{color=#F2EE29}{outlinecolor=#000}FROM{/outlinecolor}{/color} ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        elif (word_highlight == 7):
            text _("YOU CAN'T\nHIDE YOUR\nSECRETS\nFROM {color=#F2EE29}{outlinecolor=#000}ME{/outlinecolor}{/color}!"):
                style "scene_7_text"
                at transform:
                    rotate -5
        else:
            text _("YOU CAN'T\nHIDE YOUR\nSECRETS\nFROM ME!"):
                style "scene_7_text"
                at transform:
                    rotate -5

        image "images/menu/jack_menu.png":
            xalign 1.0
            yalign 1.0

            at transform:
                alpha 0.0
                zoom 0.75
                crop (103, 0, 1397, 1300)
                xoffset 100
                yoffset 1000

                linear 0.25:
                    alpha 1.0
                    yoffset 10

screen trailer_scene_8():
    #timer 8.0:
    #    action Hide("trailer_scene_8")

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

    vbox:
        xalign 0.5
        yalign 0.5

        at transform:
            alpha 0.0
            pause 0.5
            alpha 1.0

            pause 4.0
            linear 2.0:
                yalign 0.15
                zoom 0.75

        text _("{color=#000}BLACK{/color}{color=#F2EE29}MIND{/color}"):
            style "logo_text"
            size 164
        text _("{color=#000}PSYCHIC SOCIAL {color=#F2EE29}SIMULATOR{/color}"):
            style "logo_subtitle"
            size 41
            xoffset -55
            kerning 20
            
    vbox:
        yalign 0.65
        xalign 0.25
        xoffset -800
        at transform:
            pause 5.5
            linear 1.0:
                xoffset 700

        text _("A Game By"):
            color "#000"
            xalign 0.5
            size 48

        image "gui/icons/tmt_black.png"

        text _("https://toomanyteeth.net"):
            color "#000"

    vbox:
        yalign 0.65
        xalign 0.75
        xoffset 810
        spacing 120
        at transform:
            pause 5.5
            linear 1.0:
                xoffset -710

        text _("Wishlist Now"):
            color "#F2EE29"
            xalign 0.5
            size 48

        hbox:
            spacing 45
            yoffset -60
            image "gui/icons/steam_hover.png"
            image "gui/icons/itch_yellow.png"

screen full_trailer():
    default countdown = 3

    timer 1.0:
        repeat True
        action SetScreenVariable("countdown", countdown - 1)

    timer 3.0:
        action [
            Play("music", "audio/music/brain_matter.mp3"),
            Show("trailer_scene_1")
        ]

    timer 8.5:
        action Show("trailer_scene_2")

    timer 17.0:
        action Show("trailer_scene_3")

    timer 19.3:
        action Show("trailer_scene_4")

    timer 31.8:
        action Show("trailer_scene_5")

    timer 37.1:
        action Show("trailer_scene_6")

    timer 45.6:
        action Show("trailer_scene_7")

    timer 51.0:
        action Show("trailer_scene_8")

    timer 62.6:
        action Hide("full_trailer")
    
    frame:
        xfill True
        yfill True
        background Solid("#000")

        if (countdown > 0):
            text _(str(countdown)):
                xalign 0.5
                yalign 0.5
                size 84
                color "#F2EE29"


style trailer_text:
    color "#000"
    outlines [ (8, "#F2EE29", 0, 0) ]
    font "gui/Roboto-Medium.ttf"
    size 140

style scene_7_text:
    color "#000"
    font "gui/twoweekendgo-bold.otf"
    xalign 0.025
    yalign 0.25
    size 116
    outlines [ (8, "#F2EE29", 0, 0) ]