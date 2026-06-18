screen trailer():
    default movie = None

    frame:
        xfill True
        yfill True
        background Solid("#000")

    timer 14.0:
        action SetScreenVariable("movie", 1)

    image "images/cgs/cg1_docherty.png":
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


    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")
        at transform:
            alpha 0.0
            pause 6.0

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
                    pause 7.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset 2000
            text _("STALKING THE STREETS"):
                style "trailer_text"
                at transform:
                    xoffset 2000
                    pause 7.0
                    linear 1.0:
                        xoffset 0
                    pause 5.0
                    linear 1.0:
                        xoffset -1800

    if (movie == 1):
        add Movie(size=(1920, 1080), play="videos/trailer_clip_1.ogv", loop=False)

    #" Their victims have nothing in common. There is no way to tell where they will strike next."

    #flowchart footage, choices footage

    #"Will your psychic powers be the deciding factor in capturing them?"

    #"You can't hide from me"

    #Title, CTA

    textbutton _("Return"):
        xalign 1.0
        yalign 1.0
        xoffset -10
        yoffset -10
        text_color "#FFF"
        action Hide("trailer")

style trailer_text:
    color "#000"
    outlines [ (8, "#F2EE29", 0, 0) ]
    font "gui/Roboto-Medium.ttf"
    size 140