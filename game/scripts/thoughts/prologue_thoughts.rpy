label barbara_thought_pr_01:
    show screen conversation_history
    barbara_thoughts "(Is there some sort of issue with the menu?[wait_1] I’m happy to give him whatever he wants, he just has to order it.)" (name="Bartender")
    $ ignore_thoughts_length()

    if (not check_boolean("mind_read_tutorial")):
        jump prologue_03
    
    return

label barbara_thought_pr_02:
    barbara_thoughts "(He might have come in when I’ve got more things to do than I have time for, but at least he’s ordered something that’s quick to prepare.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_03:
    barbara_thoughts "(What the hell sort of place does this guy think this is?!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_04:
    barbara_thoughts "(Could he have - no, surely he couldn’t have...[wait_05]could he?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_05:
    barbara_thoughts "(I don’t remember coming out here...[wait_05] Are the alcohol fumes getting to me?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_06:
    barbara_thoughts "(Focus, Barbara...[wait_05]check on what the customer is feeling; what his needs are.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_07:
    barbara_thoughts "(I’d hope you think so, given its history![wait_1] Some of the stories that I could tell you about this place...)" (name="Bartender")
    if (check_boolean("prologue_bar_history") == False):
        jack thinking "(There we go - that’s something that I could focus on)."
        $ add_boolean("prologue_bar_history")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_08:
    barbara_thoughts "(Oh god, he’s one of those guys.[wait_05] I haven’t even served him a drink and he already thinks that he’s got a chance.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_09:
    barbara_thoughts "(And now he’ll probably be shocked, thinking that a woman shouldn’t - or couldn’t - own a bar." (name="Bartender")
    barbara_thoughts "(I wonder what he’d say if he knew about the history of the place?)" (name="Bartender")
    if (check_boolean("prologue_bar_history") == False):
        jack thinking "(The history of the bar?[wait_05] That might be something to talk about)."
        $ add_boolean("prologue_bar_history")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_10:
    barbara_thoughts "(That...[wait_05]doesn’t sound like he’s lying? That’s something, at least.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_11:
    barbara_thoughts "(This idiot clearly knows nothing about interior design.[wait_1] I could definitely teach him a lesson or two.)" (name="Bartender")
    if (check_boolean("prologue_interior_designing") == False):
        jack thinking "(Maybe I could ask her to tell me about different interior design styles?)"
        jack thinking "(That might get her to like me more.)"
        $ add_boolean("prologue_interior_designing")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_12:
    barbara_thoughts "(The prices are better than most places in the area, you idiot!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_13:
    barbara_thoughts "(I hate to be rude, but I just don’t have time to deal with this guy.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_14:
    barbara_thoughts "(He likes what I’ve done with it![wait_1] I knew that it was worth giving the bar a bit of a facelift!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label docherty_thought_pr_1:
    docherty_thoughts "(...)"
    jack worried "(What the fuck?[wait_1] I can’t read this guy’s mind!)"
    $ ignore_thoughts_length()
    return

label prologue_docherty_wipe:
    $ progress_convo = False
    docherty_thoughts "(...)"
    jack worried "(He...[wait_05]I don't think that did anything to him?)"
    $ ignore_thoughts_length()
    return