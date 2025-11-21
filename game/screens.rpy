################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    thumb "#F2EE29"
    base_bar "#000"

style slider:
    ysize gui.slider_size
    left_bar "#000"
    right_bar "gui/bar/right.png"
    thumb None

style vslider:
    xsize gui.slider_size
    bottom_bar "#000"
    top_bar "gui/bar/top.png"
    thumb None


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
                at transform:
                    rotate 354

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    key "mousedown_4":
        if (renpy.get_widget("conversation_history", "history_viewport")):
            action SetField(renpy.get_widget("conversation_history", "history_viewport").yadjustment, "value", (renpy.get_widget("conversation_history", "history_viewport").yadjustment.value - 30))
        else:
            action NullAction()

    key "mousedown_5":
        if (renpy.get_widget("conversation_history", "history_viewport")):
            action SetField(renpy.get_widget("conversation_history", "history_viewport").yadjustment, "value", (renpy.get_widget("conversation_history", "history_viewport").yadjustment.value + 30))
        else:
            action NullAction()


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xalign 0.175
    xanchor 0.5
    yanchor 0.5
    yalign 0.1

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding (40, 5, 40, 10)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            if ("locked" not in i.kwargs or i.kwargs["locked"] == False):
                textbutton (i.caption):
                    action i.action
            else:
                textbutton _("LOCKED"):
                    background "gui/button/choice_idle_background.png"
                    action NullAction()
                    hovered Show("locked_message", message=i.kwargs["message"])
                    unhovered Hide("locked_message")


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if (config.developer):
        textbutton _("DEBUG"):
            xalign 1.0
            yalign 1.0
            xoffset -10
            yoffset -10
            action [
                Hide("say"),
                Show("debug")
            ]

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
screen social_links:
    default links_opened = False
    default transform_links = False
    default social_frame = "circle_frame"
    default social_timer = False

    if (social_timer):
        timer 0.2:
            repeat False
            action [
                SetScreenVariable("social_frame", "circle_frame"),
                SetScreenVariable("social_timer", False)
            ]

    frame:
        style_prefix "social_links"
        background Frame("gui/" + social_frame + ".png")
        if (transform_links):
            at transform:
                alpha 1.0
                xsize (100 if links_opened == True else 280)
                linear 0.2 xsize (280 if links_opened == True else 100)
        else:
            at trans_fade(1.0, 1.0) 

        if (links_opened == False):
            imagebutton:
                auto "gui/icons/links_%s.png"
                action [
                    SetScreenVariable("transform_links", True),
                    SetScreenVariable("social_frame", "oval_frame"),
                    SetScreenVariable("links_opened", True)
                ]
                at (trans_fade(0.0, 0.0) if transform_links == False else trans_fade(0.2, 1.0))
                at transform:
                    alpha (1.0 if links_opened == False else 0.0)
        else:
            hbox:
                style "parent_social_links_box"
                at trans_fade(0.2, 1.0)
                hbox:
                    imagebutton:
                        auto "gui/icons/website_%s.png"
                        action OpenURL("https://toomanyteeth.net")
                    
                    imagebutton:
                        auto "gui/icons/discord_%s.png"
                        action OpenURL("https://discord.gg/HYkSGNa5MZ")

                    imagebutton:
                        auto "gui/icons/bluesky_%s.png"
                        action OpenURL("https://bsky.app/profile/toomanyteeth.net")

                imagebutton:
                    auto "gui/close_%s.png"
                    xoffset -10
                    action [
                        SetScreenVariable("links_opened", False),
                        SetScreenVariable("social_timer", True)
                    ]

screen main_menu():
    default confirmed = False
    default confirmable = False

    ## This ensures that any other menu screen is replaced.
    tag menu

    timer 1.0:
        action SetScreenVariable("confirmable", True)

    if (confirmed):
        frame:
            background Solid("#3B3B3B")

        for i in range(27):
            frame:
                style_prefix "zener_rows"
                background Solid("#D1CE21", ysize=1620, xsize=50, yanchor=0.25)
                xoffset (i * 100) -700
                at transform:
                    #alpha 0.3
                    rotate 35

                if (i % 2 == 0):        #Col going up
                    vbox:
                        yoffset -140
                        spacing 5
                        at transform:
                            linear (1400 / 116.5):
                                ypos -1480
                        for j in range(4):
                            for k in range(1, 6):
                                image "gui/card_[k].png":
                                    at transform:
                                        zoom 0.3
                    for j in range(4):
                        for k in range(1, 6):
                            image "gui/card_[k].png":
                                at zener_card_col_up(-600, (1280 - (70 * ((j * 5) + k) - 70)) / 116.5)
                else:                   #Col going down
                    vbox:
                        spacing 5
                        yoffset -80
                        at transform:
                            linear (1300 / 116.5):
                                ypos 1380
                        for j in range(4):
                            for k in range(1, 6):
                                image "gui/card_[k].png":
                                    at transform:
                                        zoom 0.3

                    for j in range(4):
                        for k in range(1, 6):
                            image "gui/card_[k].png":
                                at zener_card_col_down(1200, (1280 - (70 * ((j * 5) + k) - 70)) / 116.5)
        frame:
            background Solid("#00000041")

        use social_links

        image "images/menu/ring.png":
            xalign 0.45
            yalign 0.5
            at menu_expand_ring(3.0)
        image "images/menu/ring.png":
            xalign 0.45
            yalign 0.5
            at menu_expand_ring(3.2)
        image "images/menu/menu_placeholder.png":
            at transform:
                zoom 0.8
                alpha 0.0
                xoffset -180
                yoffset 220
                pause 1.0
                linear 2.0:
                    xoffset 20
                    alpha 1.0


        vbox:
            xalign 0.9
            yalign 0.85
            spacing 10

            textbutton _("START"):
                style "main_menu_button"
                action (ShowMenu("preferences", start=True) if persistent.game_launched == False else Start())
                at menu_button(1.0)
            textbutton _("LOAD"):
                style "main_menu_button"
                xoffset -66
                action ShowMenu("saves_list")
                at menu_button(1.5)
            textbutton _("SETTINGS"):
                style "main_menu_button"
                xoffset -132
                action ShowMenu("preferences")
                at menu_button(2.0)
            textbutton _("EXTRAS"):
                style "main_menu_button"
                xoffset -198
                action Show("modal_popup", message="This doesn't do anything right now; it's just there for working out menu button placement", option_labels=["OK"], option_actions=[Hide("modal_popup")])
                at menu_button(2.5)
            textbutton _("CREDITS"):
                style "main_menu_button"
                xoffset -264
                action ShowMenu("about")
                at menu_button(3.0)
            textbutton _("QUIT"):
                style "main_menu_button"
                xoffset -334
                action Quit()
                at menu_button(3.5)
    else:
        key "K_RETURN":
            action (SetScreenVariable("confirmed", True) if confirmable else NullAction())

    use main_logo(confirmed)

screen main_logo(confirmed):
    if (not confirmed):
        frame:
            background Solid("#000")
            style "title_half_card"
        frame:
            background Solid("#F2EE29")
            style "title_half_card_right"

    frame:
        background Solid("#F2EE29")
        style "title_half_card"
        if (confirmed):
            at trans_fade_out(0, 1.0)
        else:
            at title_card_slide("down")

    frame: 
        background Solid("#000")
        style "title_half_card_right"
        if (confirmed):
            at trans_fade_out(0, 1.0)
        else:
            at title_card_slide("up")

    if (not confirmed):
        text _("{color=#000}Press{/color} {color=#F2EE29}Enter{/color}"):
            xalign 0.5
            yalign 0.8
            color "#FFF"
            font "gui/chubhand.ttf"
            size 50
            at transform:
                alpha 0.0
                pause 0.5

                block:
                    alpha 1.0
                    linear 2.0:
                        alpha 0.0
                    linear 1.0:
                        alpha 1.0
                    repeat
        
    text _("{color=#000}BLACK{/color}{color=#F2EE29}MIND{/color}"):
        style "logo_text"
        if (not confirmed):
            at transform:
                alpha 0.0
                pause 0.5
                alpha 1.0
        else:
            at transform:
                linear 2.0:
                    yalign 0.15
                    zoom 0.75

        

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style title_half_card:
    xsize 960

style title_half_card_right is title_half_card:
    xoffset 960

style logo_text:
    font "gui/Decade__.ttf"
    size 128
    xalign 0.5
    yalign 0.25
    xoffset -25
    spacing 0

style yellow_button:
    background Frame("gui/button/button_idle.png")
    hover_background Frame("gui/button/button_hover.png")
    padding (40, 10, 40, 10)

style yellow_button_text:
    hover_color "#F2EE29"
    selected_color "#F2EE29"
    textalign 0.5
    xalign 0.5

style yellow_button_small is yellow_button:
    padding (20, 5, 20, 5)

style yellow_button_small_text is yellow_button_text

style main_menu_button is yellow_button:
    xsize 343
    padding (60, 15, 60, 15)

style main_menu_button_text is yellow_button_text:
    font "gui/chubhand.ttf"
    yoffset 5
    size 60

style social_links_frame:
    xalign 0.0
    yalign 0.0
    xoffset 25
    yoffset 25
    padding (20, 20, 20, 20)
style social_links_hbox:
    spacing 20
style parent_social_links_box:
    xoffset 20
    xsize 280
style social_links_image_button:
    yalign 0.5

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, title_size=88):
    frame:
        background Solid("#F2EE29")
        xfill True
        yfill True

    frame:
        style "bottom_left_frame"
        at menu_bottom_left_slide

    frame:
        style "top_right_frame"
        at menu_top_right_slide

    frame:
        style "bottom_right_frame"
        at menu_bottom_right_slide
        
    text _(title):
        font "gui/Decade__.ttf"
        size title_size
        color "#F2EE29"
        xalign (0.025 if title_size > 90 else 0.0125)
        yalign 0.95
        at transform:
            xoffset -400
            pause 1.0
            ease 0.33:
                xoffset 0

    textbutton _("Return"):
        xalign 0.975
        yalign 0.975
        text_font "gui/chubhand.ttf"
        text_color "#F2EE29"
        text_hover_underline True
        text_size 38
        action (Return() if main_menu else ShowMenu("pause_menu"))
        at transform:
            xoffset 400
            pause 1.0
            ease 0.33:
                xoffset 0

    transclude


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button:
    xalign 0.5
    yalign 0.95
    background Solid("#990000")
    hover_background Frame("gui/frame.png")
    left_padding 10
    right_padding 10

style return_button_text:
    size 40
    color "#FFF"
    hover_color "#990000"

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    xalign 0.5
    ymaximum 975

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1600

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    default show_content = False
    default hide_content = False
    default selected_tab = "game"
    tag menu

    timer 1.2:
        action SetScreenVariable("show_content", True)

    if (hide_content):
        timer 0.5:
            action SetScreenVariable("hide_content", False)

    use game_menu(_("CREDITS")):

        if (show_content):
            vbox:
                style_prefix "credits_tabs"
                at trans_fade(0.0, 0.5)

                textbutton _("Game"):
                    action [
                        SetScreenVariable("hide_content", True),
                        SetScreenVariable("selected_tab", "game")
                    ]
                    selected selected_tab == "game"
                textbutton _("Visuals"):
                    action [
                        SetScreenVariable("hide_content", True),
                        SetScreenVariable("selected_tab", "visuals")
                    ]
                    selected selected_tab == "visuals"
                textbutton _("Audio"):
                    action [
                        SetScreenVariable("hide_content", True),
                        SetScreenVariable("selected_tab", "audio")
                    ]
                    selected selected_tab == "audio"
                textbutton _("Assets"):
                    action [
                        SetScreenVariable("hide_content", True),
                        SetScreenVariable("selected_tab", "assets")
                    ]
                    selected selected_tab == "assets"
                textbutton _("Other"):
                    action [
                        SetScreenVariable("hide_content", True),
                        SetScreenVariable("selected_tab", "other")
                    ]
                    selected selected_tab == "other"

            frame:
                background None
                xsize 1275
                ysize 700
                xalign 0.6
                yalign 0.2

                if (hide_content == False):

                    vbox:
                        spacing 80
                        at trans_fade(0.0, 0.5), fade_side_to_side

                        if (selected_tab == "game"):
                            vbox:
                                spacing 10
                                text _("Harry Sewalski"):
                                    style "credit_heading"
                                text _("Writing, Programming, Directing"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Beta Testing"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Another Credit"):
                                    style "credit_person"
                        elif (selected_tab == "visuals"):
                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Sprite and CG Artwork"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Background Artwork"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Another Credit"):
                                    style "credit_person"
                        elif (selected_tab == "audio"):
                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Voice of Character #1"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Voice of Character #2"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("TBA"):
                                    style "credit_heading"
                                text _("Original Music"):
                                    style "credit_person"

                            vbox:
                                spacing 10
                                text _("{a=https://www.zapsplat.com/}{font=gui/chubhand.ttf}Zapsplat.com{/font}{/a}"):
                                    style "credit_heading"
                                text _("Sound Effects"):
                                    style "credit_person"
                        elif (selected_tab == "assets"):
                            vbox:
                                spacing 10
                                text _("{a=https://watabou.itch.io/medieval-fantasy-city-generator}{font=gui/chubhand.ttf}Medieval Fantasy City Generator{/font}{/a}"):
                                    style "credit_heading"
                                text _("Map Generator"):
                                    style "credit_person"
                        elif (selected_tab == "other"):
                            vbox:
                                spacing 10
                                text _("BLACKMIND"):
                                    font "gui/Decade__.ttf"
                                    color "#000"
                                    size 72
                                text _("Version [config.version!t]\n"):
                                    color "#000"

                            if gui.about:
                                text "[gui.about!t]\n":
                                    color "#000"

                            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
                                color "#000"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style credits_tabs_vbox:
    xoffset 50
    yalign 0.15
    spacing 15

style credits_tabs_button:
    selected_background Solid("#000")
    xsize 267
    padding (20, 10, 20, 10)

style credits_tabs_button_text:
    font "gui/chubhand.ttf"
    color "#000"
    size 72
    selected_color "#F2EE29"
    yoffset 6

style credit_heading:
    font "gui/chubhand.ttf"
    color "#000"
    size 60

style credit_person:
    color "#000"
    size 28


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences(start=False):
    tag menu
    default display_sample_text_speed = False
    default update_count = 0
    default hover_radio = None
    default show_content = False

    use game_menu(_("SETTINGS"), 76):

        if (not display_sample_text_speed):
            timer 1.7:
                action [
                    SetScreenVariable("display_sample_text_speed", True),
                    Hide("sample_text_speed_2"),
                    Show("sample_text_speed_1")
                ]
        timer 1.2:
            action SetScreenVariable("show_content", True)

        if (show_content):
            hbox:
                xfill True
                yalign 0.35
                spacing 50
                at trans_fade(0.0, 0.5)

                vbox:
                    xalign 1.0
                    hbox:
                        spacing 10
                        xalign 0.5
                        label _("READING"):
                            style "section_label"
                    frame:
                        xsize 600
                        ysize 550

                        padding (20, 20, 20, 20)
                        vbox:
                            vbox:
                                style_prefix "reading_box"
                                label _("Text Speed")
                                bar:
                                    value Preference("text speed")
                                    released [
                                        SetScreenVariable("display_sample_text_speed", False),
                                        SetVariable("wait_2", ("" if preferences.text_cps == 0 else "{w=2.0}")),
                                        SetVariable("wait_1", ("" if preferences.text_cps == 0 else "{w=1.0}")),
                                        SetVariable("wait_05", ("" if preferences.text_cps == 0 else "{w=0.5}")),
                                        Hide("sample_text_speed_1"),
                                        Hide("sample_text_speed_2")
                                    ]
                                hbox:
                                    xsize 320
                                    text _("Slow")
                                    text _("Fast"):
                                        xalign 1.0

                                #text _(str(preferences.text_cps))

                            vbox:
                                style_prefix "reading_box"
                                yoffset 20
                                label _("Auto-Forward Time")
                                bar:
                                    value Preference("auto-forward time")
                                    released [
                                        SetScreenVariable("display_sample_text_speed", False),
                                        Hide("sample_text_speed_1"),
                                        Hide("sample_text_speed_2")
                                    ]
                                hbox:
                                    xsize 320
                                    text _("Instant")
                                    text _("Never"):
                                        xalign 1.0
                                #text _(str(preferences.afm_time))

                            image Solid("#000"):
                                xsize 0.9
                                ysize 4
                                yoffset 30
                
                vbox:
                    xsize 0.5
                    spacing 20
                    vbox:
                        hbox:
                            spacing 10
                            xalign 0.5
                            label _("AUDIO"):
                                style "section_label"
                        frame:
                            xsize 550
                            ysize 288
                            padding (80, 20, 80, 20)
                            hbox:
                                spacing 40
                                vbox:
                                    hbox:
                                        style_prefix "audio_bars"
                                        vbox:
                                            vbar:
                                                value Preference("music volume")
                                                if preferences.get_mute("music"):
                                                    base_bar Frame("gui/slider/vertical_insensitive_bar.png", gui.vslider_borders, tile=gui.slider_tile)
                                                    thumb "gui/slider/vertical_insensitive_thumb.png"

                                            text _("Music"):
                                                color ("#000" if not preferences.get_mute("music") else "#707070")

                                            imagebutton:
                                                idle ("gui/icons/mute_hover.png" if preferences.get_mute("music") or preferences.get_mute("all") else "gui/icons/mute_idle.png")
                                                hover "gui/icons/mute_hover.png"
                                                xalign 0.5 
                                                action Preference("music mute", "toggle")

                                        vbox:
                                            vbar:
                                                value Preference("sound volume")
                                                if preferences.get_mute("sfx"):
                                                    base_bar Frame("gui/slider/vertical_insensitive_bar.png", gui.vslider_borders, tile=gui.slider_tile)
                                                    thumb "gui/slider/vertical_insensitive_thumb.png"
                                            text _("Effects"):
                                                color ("#000" if not preferences.get_mute("sfx") else "#707070")

                                            imagebutton:
                                                idle ("gui/icons/mute_hover.png" if preferences.get_mute("sfx") or preferences.get_mute("all") else "gui/icons/mute_idle.png")
                                                hover "gui/icons/mute_hover.png"
                                                action Preference("sound mute", "toggle")
                                                xalign 0.5 

                                        #vbox:
                                        #    vbar:
                                        #        value Preference("voice volume")
                                        #        if preferences.get_mute("voice"):
                                        #            base_bar Frame("gui/slider/vertical_insensitive_bar.png", gui.vslider_borders, tile=gui.slider_tile)
                                        #            thumb "gui/slider/vertical_insensitive_thumb.png"
                                        #    text _("Voice"):
                                        #        color ("#0099FF" if not preferences.get_mute("voice") else "#707070")
                                        #    imagebutton:
                                        #        idle ("gui/icons/mute_hover.png" if preferences.get_mute("voice") or preferences.get_mute("all") else "gui/icons/mute_idle.png")
                                        #        hover "gui/icons/mute_hover.png"
                                        #        action Preference("voice mute", "toggle")
                                
                                vbox:
                                    style_prefix "audio_options"
                                    yfill True
                                    vbox:
                                        spacing 10
                                        yalign 0.8
                                        if (not preferences.get_mute("sfx")):
                                            textbutton _("Sample Effect"):
                                                style "yellow_button_dark_hover"
                                                action Play("sound", config.sample_sound)
                                                text_size 15
                                        #if (not preferences.get_mute("voice")):
                                        #    textbutton _("Sample Voice"):
                                        #        action Play("voice", config.sample_voice)

                                    hbox:
                                        style_prefix "radio_button"
                                        yalign 1.0
                                        yoffset 5

                                        imagebutton:
                                            idle ("gui/checkbox_selected_hover_smol.png" if hover_radio == "mute" or (preferences.get_mute("music") and preferences.get_mute("sfx") and preferences.get_mute("voice")) else ("gui/checkbox_unselected_hover_smol.png" if hover_radio == "mute" else ("gui/checkbox_selected_idle_smol.png" if (preferences.get_mute("music") and preferences.get_mute("sfx") and preferences.get_mute("voice")) else "gui/checkbox_unselected_idle_smol.png")))
                                            hover ("gui/checkbox_unselected_hover_smol.png" if hover_radio != "mute" else "gui/checkbox_selected_hover_smol.png") 
                                            action Preference("all mute", "toggle")
                                            hovered SetScreenVariable("hover_radio", "mute")
                                            unhovered SetScreenVariable("hover_radio", None)
                                            yoffset 8
                                        textbutton _("Mute All"):
                                            action Preference("all mute", "toggle")
                                            hovered SetScreenVariable("hover_radio", "mute")
                                            unhovered SetScreenVariable("hover_radio", None)
                                            text_color ("#3B3B3B" if hover_radio == "mute" else ("#000" if (preferences.get_mute("music") and preferences.get_mute("sfx") and preferences.get_mute("voice")) else "#707070"))
                                            text_bold hover_radio == "mute" or (preferences.get_mute("music") and preferences.get_mute("sfx") and preferences.get_mute("voice"))

                    vbox:
                        hbox:
                            spacing 15
                            xalign 0.5
                            label _("OTHER"):
                                style "section_label"
                        frame:
                            xsize 550
                            ysize 198
                            
                            vbox:
                                xalign 0.5
                                spacing 15
                                yoffset 40
                                vbox:
                                    label _("Display"):
                                        text_size 28
                                    hbox:
                                        spacing 25
                                        hbox:
                                            style_prefix "radio_button"

                                            imagebutton:
                                                idle ("gui/radio_hover.png" if hover_radio == "fullscreen" else ("gui/radio_selected.png" if preferences.fullscreen else "gui/radio_idle.png"))
                                                selected "gui/radio_selected.png"
                                                hover "gui/radio_hover.png"
                                                action Preference("display", "fullscreen")
                                                hovered SetScreenVariable("hover_radio", "fullscreen")
                                                unhovered SetScreenVariable("hover_radio", None)
                                            textbutton _("Fullscreen"):
                                                action Preference("display", "fullscreen")
                                                hovered SetScreenVariable("hover_radio", "fullscreen")
                                                unhovered SetScreenVariable("hover_radio", None)
                                                text_color ("#3B3B3B" if hover_radio == "fullscreen" else ("#000" if preferences.fullscreen else "#707070"))
                                                text_bold preferences.fullscreen

                                        hbox:
                                            style_prefix "radio_button"

                                            imagebutton:
                                                idle ("gui/radio_hover.png" if hover_radio == "windowed" else ("gui/radio_selected.png" if not preferences.fullscreen else "gui/radio_idle.png"))
                                                selected "gui/radio_selected.png"
                                                hover "gui/radio_hover.png"
                                                action Preference("display", "window")
                                                hovered SetScreenVariable("hover_radio", "windowed")
                                                unhovered SetScreenVariable("hover_radio", None)
                                            textbutton _("Windowed"):
                                                action Preference("display", "window")
                                                hovered SetScreenVariable("hover_radio", "windowed")
                                                unhovered SetScreenVariable("hover_radio", None)
                                                text_color ("#3B3B3B" if hover_radio == "windowed" else ("#000" if not preferences.fullscreen else "#707070"))
                                                text_bold not preferences.fullscreen
            
            if (start):
                frame:
                    xalign 0.5
                    yalign 0.9
                    xsize 800
                    ysize 150

                    textbutton _("START GAME"):
                        xalign 0.5
                        yalign 0.15
                        text_size 45
                        text_color "#000"
                        text_hover_color "#3B3B3B"
                        text_font "gui/chubhand.ttf"
                        action [
                            Hide("preferences", quick_dissolve),
                            SetVariable("persistent.game_launched", True),
                            Start()
                        ]

                    text _("These settings can be changed from the Settings menu at any time"):
                        xalign 0.5
                        yalign 0.85
                        xmaximum 600
                        size 20
                        text_align 0.5
                        color "#000"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style section_label:
    xalign 0.5
    yalign 0.5
    bottom_margin 10

style section_label_text is label_text:
    font "gui/chubhand.ttf"

style reading_box_label_text:
    size 28

style reading_box_vbox:
    spacing 5

style reading_box_hbox:
    spacing 20

style reading_box_slider:
    xsize 300

style reading_box_text:
    color "#000"
    size 20
    yalign 0.5

style audio_bars_hbox:
    spacing 15

style audio_bars_vbox:
    spacing 10

style audio_bars_vslider:
    ysize 170
    xalign 0.5

style audio_bars_text:
    color "#000"
    size 20

style audio_options_button:
    xsize 180
    background Frame("gui/frame_thicc.png")

style audio_options_button_text:
    color "#000"
    font "DejaVuSans.ttf"
    xalign 0.5
    size 20
    hover_bold True

style radio_button_hbox:
    spacing 0

style radio_button_image_button:
    yoffset 7

style radio_button_button_text:
    size 20
    font "DejaVuSans.ttf"
    hover_color "#000"
    selected_color "#000"

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    selected_color "#000"

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    selected_color "#000"

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

screen sample_text_speed_1:
    timer (209 / (preferences.text_cps if preferences.text_cps > 0 else 209) + preferences.afm_time):
        repeat True
        action [
            Show("sample_text_speed_2")
        ]

    if (renpy.get_screen("preferences")):
        text _("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi"):
            style "sample_text"
            slow_cps preferences.text_cps
    
screen sample_text_speed_2:
    if (renpy.get_screen("preferences")):
        text _("Ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat"):
            style "sample_text"
            slow_cps preferences.text_cps
            yalign 0.66
            xoffset 2

style sample_text:
    color "#000"
    size 22
    xalign 0.27
    yalign 0.52
    xmaximum 500

style yellow_button_dark_hover is yellow_button:
    hover_background Frame("gui/button/button_dark.png")

style yellow_button_dark_hover_text is yellow_button_text:
    hover_color "#000"

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    frame:
        xfill True
        yfill True
        
        background Solid("#000000b1")

        text _("History")

        side ("c r"):
            area (50, 200, 1860, 820)
            viewport id "history_viewport":
                draggable True 
                mousewheel True
                yinitial 1.0
                vbox:
                    for h in _history_list:
                        if (h.who):
                            label h.who:
                                text_color h.who_args["color"]
                        text _(h.what + "\n"):
                            color (h.what_args["color"] if "color" in h.what_args else "#FFF")
                            xoffset 50
                            xmaximum 1800
            if (len(_history_list) > 0):
                vbar value YScrollValue("history_viewport"):
                    xsize 10
            else:
                null
        
        textbutton _("Return"):
            style "return_button"
            action Return()
            yoffset 6

        if not _history_list:
            label _("The dialogue history is empty."):
                xalign 0.5
                yalign 0.5

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_window:
    xfill True
    ysize gui.history_height

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#000"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    hover_underline True

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
