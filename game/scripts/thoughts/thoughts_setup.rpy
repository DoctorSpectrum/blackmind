label mind_read_effects:
    hide screen psychic_powers
    $ hide_history()
    
    $ renpy.choice_for_skipping()

    $ _window_hide()
    if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_read"))):
        $ line = mind_read_line()
        show screen psychic_splash(line)
        $ renpy.pause(line["time"], hard=True)
        $ add_boolean("psychic_splash_read")

    $ progress_convo = False
    $ reading_mind = True

    if (current_thought not in thoughts_read):
        $ thoughts_read.append(current_thought)
        if (max_mind_reads is not None):
            $ minds_read += 1
    
    $ play_sound("mind_read.mp3", volume=0.5)
    show screen psychic_read
    $ show_history()
    jump expression current_thought_block

label mind_wipe_pause:
    #$ _history_list = []   #Potentially wipe history on a mind wipe?
    $ hide_history()

    if (rewind_point not in ineffective_rewinds):
        $ _window_hide()
        hide screen psychic_powers

        if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind"))):
            $ line = mind_rewind_line()
            show screen psychic_splash(line)
            $ renpy.pause(line["time"], hard=True)
            $ add_boolean("psychic_splash_rewind")

        $ rewound_mind = True
        if (max_rewinds is not None):
            $ minds_rewound += 1
        $ play_sound("mind_rewind.mp3")
        $ narrator.add_history(kind="adv", who=None, what=_("__breakpoint__"))
        
        show screen psychic_wipe
        $ renpy.pause(2.5, hard=True)
        $ rewound_mind = False
    else:
        if (rewind_point in paused_ineffective_rewinds):
            $ _window_hide()
            hide screen psychic_powers

            $ line = { "time": 2.0 }
            if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind"))):
                $ line = mind_rewind_line()
                show screen psychic_splash(line)
                $ add_boolean("psychic_splash_rewind")
            $ renpy.pause(line["time"] + 2.5 if persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind")) else line["time"], hard=True)
                
            show screen psychic_powers

    $ show_history()
    jump expression rewind_point

label future_sight:
    if (not check_boolean("future_sight_tutorial_1")):
        show screen future_sight(get_future_sight_info(1), False, True, False)
        call screen modal_popup("From here, you can see the keyword which will get Jack what he wants.")
        hide screen future_sight
        call screen future_sight(get_future_sight_info(1), True, False)
        $ add_boolean("future_sight_tutorial_1")
    elif (not check_boolean("future_sight_tutorial_2")):
        show screen future_sight(get_future_sight_info(2), False, True, False)
        call screen modal_popup("You’ve got several keywords available now. Keep these in mind as you proceed through the conversation, and use them to identify the thoughts which will give you the information you need to continue.")
        hide screen future_sight
        call screen future_sight(get_future_sight_info(2), True, False)
        $ add_boolean("future_sight_tutorial_2")
    else:
        show screen future_sight
    $ remove_boolean("call_future_sight")