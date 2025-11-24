label barbara_thought_pr_01:
    barbara_thoughts "(What...[wait_05]what happened?[wait_1] I feel...[wait_05]kind of light-headed.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_02:
    barbara_thoughts "(Did he?[wait_1] I didn’t think that he had, but I guess if he says that he has...)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_03:
    barbara_thoughts "(Did I take his money and close the cashier without realising it?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_04:
    show screen conversation_history
    show screen psychic_powers
    barbara_thoughts "(How much money does he need, exactly?)" (name="Bartender")
    barbara_thoughts "(I’ll need to look it up without him realising that I’ve forgotten the amount.)" (name="Bartender")
    $ ignore_thoughts_length()
    if (not check_boolean("mind_read_tutorial")):
        jump prologue_post_mind_read_tutorial
    else:
        return

label barbara_thought_pr_05:
    barbara_thoughts "(Yeah, right...[wait_1]there’s no way that this idiot paid me that much money.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_06:
    barbara_thoughts "(If numbers don’t mean anything, then why are you trying to get so much from me?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_07:
    barbara_thoughts "(You’re an idiot.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_08:
    barbara_thoughts "(Since it’s a touch screen, I guess I can technically touch them, too...)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_09:
    barbara_thoughts "(We do have issues processing some cards, true...[wait_05]but you’re still nowhere near the mark, buddy.)" (name="Bartender")
    jack thinking "(That’s interesting to know...[wait_1]I might be able to use that.)"
    $ add_boolean("mind_read_tutorial_card_processing")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_10:
    barbara_thoughts "(Have you never heard of online banking?!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_11:
    barbara_thoughts "(Just because I’m using a computer, it doesn’t make the bar any worse than it was under mum or grandma!)" (name="Bartender")
    barbara_thoughts "(I’m - it’s just as good as it was when they were running it!)" (name="Bartender")
    jack thinking "(That’s an interesting reaction...[wait_1]I’d better remember it.)"
    $ add_boolean("mind_read_tutorial_bar_quality")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_12:
    barbara_thoughts "(Calculators are computers, you idiot.)" (name="Bartender")
    jack angry "(Oh yeah?[wait_1] Let’s see you try to play games on a calculator, then)"
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_13:
    barbara_thoughts "(I’ll be amazed if I owe him more than a few coins in change.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_14:
    barbara_thoughts "(It doesn’t look like he did pay me anything...[wait_1]why am I not surprised?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_15:
    barbara_thoughts "(That isn’t a bad point, actually...[wait_1]it’s not as infallible as I’d like it to be.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_16:
    barbara_thoughts "(I should really follow that up...[wait_1]it’s been a few weeks now.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_17:
    barbara_thoughts "(What’s taking them so long?[wait_1] It doesn’t help with my problems!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_18:
    barbara_thoughts "(What are the odds that what I owe you is much less than you’ve said it is?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_19:
    barbara_thoughts "(No surprises there: he hasn’t actually paid me.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_20:
    barbara_thoughts "(He’s going to try and get out of this, I’m sure...[wait_1]do I need to start hiring security?)" (name="Bartender")
    barbara_thoughts "(More damn fees on top of everything else...)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_21:
    barbara_thoughts "(Not receiving excess change isn’t harassment!)" (name="Bartender")
    jack angry "(Like hell it isn’t)."
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_22:
    barbara_thoughts "(Thank god.[wait_1] Anything to get him out of here.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_23:
    barbara_thoughts "(I know that it’s selfish, but I want him out of here.)" (name="Bartender")
    barbara_thoughts "(If I’m going to have patrons like him, then I’d rather not be running a bar.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_24:
    barbara_thoughts "(Then again...[wait_1]can I afford to throw out everybody that I don’t like?)" (name="Bartender")
    barbara_thoughts "(I -[wait_05] I do want to keep the bar...)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_25:
    barbara_thoughts "(Maybe I am the problem.)" (name="Bartender")
    barbara_thoughts "(Maybe the customer numbers aren’t as high because they do feel like I’m harassing them.)" (name="Bartender")
    barbara_thoughts "(He might be a shit, but he didn’t choose to feel the way he is.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_26:
    barbara_thoughts "(I need to do what’s good for the bar, and that means not pushing back against customers so much.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_27:
    barbara_thoughts "(I still feel like the numbers here don’t add up, but I don’t know what’s going on with him - maybe he’s down on his luck, or maybe I really did miscount something.)" (name="Bartender")
    barbara_thoughts "(I want this bar to feel like a safe space for people, where they feel comfortable, so I’ll give him the benefit of the doubt...[wait_05]this time.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_28:
    barbara_thoughts "(Will I regret this?[wait_1] ...Probably, but I can’t ask for it back now.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_29:
    barbara_thoughts "(...Did he seriously just say what I think he did?)" (name="Bartender")
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