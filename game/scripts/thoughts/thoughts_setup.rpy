label mind_read_effects:
    show screen conversation_history
    hide screen psychic_powers
    $ renpy.choice_for_skipping()

    $ _window_hide()
    if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_read"))):
        show screen psychic_splash
        #Play a random line
        $ renpy.pause(2.0, hard=True)
        $ add_boolean("psychic_splash_read")

    $ progress_convo = False
    $ reading_mind = True

    if (current_thought not in thoughts_read):
        $ thoughts_read.append(current_thought)
        if (max_mind_reads is not None):
            $ minds_read += 1
    
    $ play_sound("mind_read.mp3", volume=0.5)
    show ring at ring_mind_read_expand(-25, 200)

    jump expression current_thought_block

label mind_wipe_pause:
    #$ _history_list = []   #Potentially wipe history on a mind wipe?
    $ renpy.choice_for_skipping()

    if (rewind_point not in ineffective_rewinds):
        $ _window_hide()
        hide screen psychic_powers

        if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind"))):
            show screen psychic_splash
            #Play a random line
            $ renpy.pause(2.0, hard=True)
            $ add_boolean("psychic_splash_rewind")

        show screen conversation_history
        $ rewound_mind = True
        if (max_rewinds is not None):
            $ minds_rewound += 1
        $ play_sound("mind_rewind.mp3")
        $ narrator.add_history(kind="adv", who=None, what=_("__breakpoint__"))
        show ring at ring_mind_rewind_pause(-25, 200)
        $ renpy.pause(2.5, hard=True)
        hide ring
        $ rewound_mind = False
    else:
        if (rewind_point in paused_ineffective_rewinds):
            $ _window_hide()
            hide screen psychic_powers

            if (persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind"))):
                show screen psychic_splash
                #Play a random line
                $ add_boolean("psychic_splash_rewind")
            $ renpy.pause(4.5 if persistent.psychic_splash == "always" or (persistent.psychic_splash == "scene" and not check_boolean("psychic_splash_rewind")) else 2.0, hard=True)
                
            show screen psychic_powers

    jump expression rewind_point