label mind_read_effects:
    show screen conversation_history
    hide screen psychic_powers
    $ renpy.choice_for_skipping()

    $ _window_hide()
    if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_read"))):
        $ pause_time = mind_read_line()
        show screen psychic_splash(pause_time)
        $ renpy.pause(pause_time, hard=True)
        $ add_boolean("psychic_splash_read")

    $ progress_convo = False
    $ reading_mind = True

    if (current_thought not in thoughts_read):
        $ thoughts_read.append(current_thought)
        if (max_mind_reads is not None):
            $ minds_read += 1
    
    $ play_sound("mind_read.mp3", volume=0.5)
    show screen psychic_read

    jump expression current_thought_block

label mind_wipe_pause:
    #$ _history_list = []   #Potentially wipe history on a mind wipe?
    $ renpy.choice_for_skipping()

    if (rewind_point not in ineffective_rewinds):
        $ _window_hide()
        hide screen psychic_powers

        if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind"))):
            $ pause_time = mind_rewind_line()
            show screen psychic_splash(pause_time)
            $ renpy.pause(pause_time, hard=True)
            $ add_boolean("psychic_splash_rewind")

        show screen conversation_history
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

            $ pause_time = 2.0
            if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind"))):
                $ pause_time = mind_rewind_line()
                show screen psychic_splash(pause_time)
                $ add_boolean("psychic_splash_rewind")
            $ renpy.pause(pause_time + 2.5 if persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind")) else pause_time, hard=True)
                
            show screen psychic_powers

    jump expression rewind_point