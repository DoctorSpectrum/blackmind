label barbara_thought_pr_01:
    barbara "(What...[wait_05]what happened?[wait_1] I feel...[wait_05]kind of light-headed.)" (name="Bartender")
    return

label barbara_thought_pr_02:
    barbara "(Did he?[wait_1] I didn’t think that he had, but I guess if he says that he has...)" (name="Bartender")
    return

label barbara_thought_pr_03:
    barbara "(Did I take his money and close the cashier without realising it?)" (name="Bartender")
    return

label barbara_thought_pr_04:
    show screen conversation_history
    barbara "(How much money does he need, exactly?)" (name="Bartender")
    barbara "(I’ll need to look it up without him realising that I’ve forgotten the amount.)" (name="Bartender")
    if (not check_boolean("mind_read_tutorial")):
        jump prologue_post_mind_read_tutorial
    else:
        return

label barbara_thought_pr_05:
    barbara "(Yeah, right...[wait_1]there’s no way that this idiot paid me that much money.)" (name="Bartender")
    return

label barbara_thought_pr_06:
    barbara "(If numbers don’t mean anything, then why are you trying to get so much from me?)" (name="Bartender")
    return

label barbara_thought_pr_07:
    barbara "(You’re an idiot.)" (name="Bartender")
    return

label barbara_thought_pr_08:
    barbara "(Since it’s a touch screen, I guess I can technically touch them, too...)" (name="Bartender")
    return

label barbara_thought_pr_09:
    barbara "(We do have issues processing some cards, true...[wait_05]but you’re still nowhere near the mark, buddy.)" (name="Bartender")
    jack thinking "(That’s interesting to know...[wait_1]I might be able to use that.)"
    $ add_boolean("mind_read_tutorial_card_processing")
    return

label barbara_thought_pr_10:
    barbara "(Have you never heard of online banking?!)" (name="Bartender")
    return

label barbara_thought_pr_11:
    barbara "(Just because I’m using a computer, it doesn’t make the bar any worse than it was under mum or grandma!)" (name="Bartender")
    barbara "(I’m - it’s just as good as it was when they were running it!)" (name="Bartender")
    jack thinking "(That’s an interesting reaction...[wait_1]I’d better remember it.)"
    $ add_boolean("mind_read_tutorial_bar_quality")
    return

label barbara_thought_pr_12:
    barbara "(Calculators are computers, you idiot.)" (name="Bartender")
    jack angry "(Oh yeah?[wait_1] Let’s see you try to play games on a calculator, then)"
    return

label barbara_thought_pr_13:
    barbara "(I’ll be amazed if I owe him more than a few coins in change.)" (name="Bartender")
    return

label barbara_thought_pr_14:
    barbara "(It doesn’t look like he did pay me anything...[wait_1]why am I not surprised?)" (name="Bartender")
    return

label barbara_thought_pr_15:
    barbara "(That isn’t a bad point, actually...[wait_1]it’s not as infallible as I’d like it to be.)" (name="Bartender")
    return

label barbara_thought_pr_16:
    barbara "(I should really follow that up...[wait_1]it’s been a few weeks now.)" (name="Bartender")
    return

label barbara_thought_pr_17:
    barbara "(What’s taking them so long?[wait_1] It doesn’t help with my problems!)" (name="Bartender")
    return

label barbara_thought_pr_18:
    barbara "(What are the odds that what I owe you is much less than you’ve said it is?)" (name="Bartender")
    return

label barbara_thought_pr_19:
    barbara "(No surprises there: he hasn’t actually paid me.)" (name="Bartender")
    return

label barbara_thought_pr_20:
    barbara "(He’s going to try and get out of this, I’m sure...[wait_1]do I need to start hiring security?)" (name="Bartender")
    barbara "(More damn fees on top of everything else...)" (name="Bartender")
    return

label barbara_thought_pr_21:
    barbara "(Not receiving excess change isn’t harassment!)" (name="Bartender")
    jack angry "(Like hell it isn’t)."
    return

label barbara_thought_pr_22:
    barbara "(Thank god.[wait_1] Anything to get him out of here.)" (name="Bartender")
    return

label barbara_thought_pr_23:
    barbara "(I know that it’s selfish, but I want him out of here.)" (name="Bartender")
    barbara "(If I’m going to have patrons like him, then I’d rather not be running a bar.)" (name="Bartender")
    return

label barbara_thought_pr_24:
    barbara "(Then again...[wait_1]can I afford to throw out everybody that I don’t like?)" (name="Bartender")
    barbara "(I -[wait_05] I do want to keep the bar...)" (name="Bartender")
    return

label barbara_thought_pr_25:
    barbara "(Maybe I am the problem.)" (name="Bartender")
    barbara "(Maybe the customer numbers aren’t as high because they do feel like I’m harassing them.)" (name="Bartender")
    barbara "(He might be a shit, but he didn’t choose to feel the way he is.)" (name="Bartender")
    return

label barbara_thought_pr_26:
    barbara "(I need to do what’s good for the bar, and that means not pushing back against customers so much.)" (name="Bartender")
    return

label barbara_thought_pr_27:
    barbara "(I still feel like the numbers here don’t add up, but I don’t know what’s going on with him - maybe he’s down on his luck, or maybe I really did miscount something.)" (name="Bartender")
    barbara "(I want this bar to feel like a safe space for people, where they feel comfortable, so I’ll give him the benefit of the doubt...[wait_05]this time.)" (name="Bartender")
    return

label barbara_thought_pr_28:
    barbara "(Will I regret this?[wait_1] ...Probably, but I can’t ask for it back now.)" (name="Bartender")
    return

label barbara_thought_pr_29:
    barbara "(...Did he seriously just say what I think he did?)" (name="Bartender")
    return

label docherty_thought_pr_1:
    docherty "(...)"
    jack worried "(What the fuck?[wait_1] I can’t read this guy’s mind!)"
    return