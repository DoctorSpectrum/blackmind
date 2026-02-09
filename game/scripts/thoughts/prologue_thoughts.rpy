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

label barbara_thought_pr_15:
    barbara_thoughts "(What I {i}thought{/i}?[wait_1] Did I hear that right?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_16:
    barbara_thoughts "(Let’s just move on, and assume that I misheard him.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_17:
    barbara_thoughts "(Huh.[wait_1] You know, I’ve never thought of this place as being that historic, but I guess it has been around for decades now.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_18:
    barbara_thoughts "(I wonder where he heard of it - if there’s a good review or coverage of it somewhere, I should see whether they want to do an interview!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_19:
    barbara_thoughts "(If he doesn’t know of its ownership, then what {i}does{/i} he know about it?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_20:
    barbara_thoughts "(No need to mention to him anything about what the profitability has been like lately...)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_21:
    barbara_thoughts "(I really need to review those drinks policies again, work out what the projected differences would be.)" (name="Bartender")
    jack thinking "(Drinks policies?[wait_1] If she’s looking to change things, maybe I can convince her that she should lower her prices a bit...)"
    $ ignore_thoughts_length()
    $ add_boolean("prologue_drink_policies")
    return

label barbara_thought_pr_22:
    barbara_thoughts "(Crap, I got sidetracked there![wait_1] ABC, Barbara, ABC!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_23:
    barbara_thoughts "(Then why, exactly, did you come in here?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_24:
    barbara_thoughts "(He can’t even think up a good excuse...[wait_05]but what was his original plan?[wait_1] Burst in and demand alcohol for free?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_25:
    barbara_thoughts "(The sooner this guy gets out of here, the better.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_26:
    barbara_thoughts "(Does he mean something like happy hour?[wait_1] Or discounts for regulars?)" (name="Bartender")
    jack thinking "(Discounts for regulars?[wait_1] That’s not a bad idea...)"
    $ add_boolean("prologue_drink_discounts")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_27:
    barbara_thoughts "(I still haven’t worked out all of the changes that I’m planning to make...[wait_05]but I’m getting ahead of myself.[wait_1] I should just find out what he means.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_28:
    barbara_thoughts "(Odd that he thinks jugs being cheaper is some sort of special policy...[wait_05]that’s called good pricing, mate.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_29:
    barbara_thoughts "(With happy hour over there’s not much that I can really do for him, but hopefully he’ll just order something and stick with it.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_30:
    barbara_thoughts "(I wish I could afford to lower the price a bit, but business on Mondays is always pretty slow.)" (name="Bartender")
    barbara_thoughts "(Still, nobody forced him to come here today.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_31:
    barbara_thoughts "(Who the hell does this guy think he is?![wait_1] Does he think he deserves a discount just for talking to me a little bit?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_32:
    barbara_thoughts "(I’d rather have a night with no profit than deal with entitled assholes like this.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_33:
    barbara_thoughts "(One of my regulars?[wait_1] This is clearly the first time you’ve been here!)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_34:
    barbara_thoughts "(Would I define a regular as somebody who comes by at least three nights a week, or - no, this isn’t the time to think about this.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_35:
    barbara_thoughts "(You haven’t paid for anything so far, you idiot.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_36:
    barbara_thoughts "(Maybe if there was actually some benefit to it, like some publicity.[wait_1] But as much as I’d like to, I can’t afford to just throw money away like that.)" (name="Bartender")
    jack thinking "(Publicity?[wait_1] Hmm...[wait_05]I think that might give me an idea)."
    $ add_boolean("prologue_drink_review")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_37:
    barbara_thoughts "(I’m willing to bet he’ll just leave the bar now. I know his type.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_38:
    barbara_thoughts "(Wait a second - did I hear that right?)" (name="Bartender") 
    barbara_thoughts "(This guy writes reviews?)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_39:
    barbara_thoughts "(I shouldn’t get my hopes up too much...[wait_05]but in the off chance that he works for somewhere big, this - this could be a really good opportunity.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_40:
    barbara_thoughts "(He’s not too mad about how long it’s taken to get to being served, is he?)" (name="Bartender")
    barbara_thoughts "(Or - I guess he was dragging things out because he wanted to know a bit more about me, and the bar, for his article.)" (name="Bartender")
    $ ignore_thoughts_length()
    return

label barbara_thought_pr_41:
    barbara_thoughts "(This is - this could really make a big difference, and turn things around after some of the decisions I’ve made.)" (name="Bartender")
    barbara_thoughts "(I - I can’t believe this, it - it seems too good to be true.)" (name="Bartender")
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