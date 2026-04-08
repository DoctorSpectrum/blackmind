label mind_read_prologue:
    if (current_thought == "barbara_thought_pr_01"):
        bartender_thoughts "(He sure is taking his time deciding...[wait_1] I’m happy to give him whatever he wants, he just has to order it.)" 
        $ ignore_thoughts_length()

        if (not check_boolean("mind_read_tutorial")):
            jump prologue_03
    elif (current_thought == "barbara_thought_pr_02"):
        bartender_thoughts "(He might have come in when I’ve got more things to do than I have time for, but at least he’s ordered something that’s quick to prepare.)" 
    elif (current_thought == "barbara_thought_pr_03"):
        bartender_thoughts "(What the hell sort of place does this guy think this is?!)"
    elif (current_thought == "barbara_thought_pr_04"):
        bartender_thoughts "(Could he have - no, surely he couldn’t have...[wait_05]could he?)" 
    elif (current_thought == "barbara_thought_pr_05"):
        bartender_thoughts "(I don’t remember coming out here...[wait_05] Are the alcohol fumes getting to me?)" 
    elif (current_thought == "barbara_thought_pr_06"):
        bartender_thoughts "(Focus, Barbara...[wait_05]check on what the customer is feeling; what his needs are.)" 
    elif (current_thought == "barbara_thought_pr_07"):
        bartender_thoughts "(I’d hope you think so, given its history![wait_1] Some of the stories that I could tell you about this place...)" 
        if (check_boolean("prologue_bar_history") == False):
            jack thinking "(There we go - that’s something that I could focus on.)"
            $ add_boolean("prologue_bar_history")
    elif (current_thought == "barbara_thought_pr_08"):
        bartender_thoughts "(Oh god, he’s one of those guys.[wait_05] I haven’t even served him a drink and he already thinks that he’s got a chance.)" 
    elif (current_thought == "barbara_thought_pr_09"):
        bartender_thoughts "(And now he’ll probably be shocked, thinking that a woman shouldn’t - or couldn’t - own a bar.)" 
        bartender_thoughts "(I wonder what he’d say if he knew about the history of the place?)" 
        if (check_boolean("prologue_bar_history") == False):
            jack thinking "(The history of the bar?[wait_05] That might be something to talk about.)"
            $ add_boolean("prologue_bar_history")
    elif (current_thought == "barbara_thought_pr_10"):
        bartender_thoughts "(That...[wait_05]doesn’t sound like he’s lying? That’s something, at least.)" 
    elif (current_thought == "barbara_thought_pr_11"):
        bartender_thoughts "(This idiot clearly knows nothing about interior design.[wait_1] I could definitely teach him a lesson or two.)" 
        if (check_boolean("prologue_interior_designing") == False):
            jack thinking "(Maybe I could ask her to tell me about different interior design styles?)"
            jack thinking "(That might get her to like me more.)"
            $ add_boolean("prologue_interior_designing")
    elif (current_thought == "barbara_thought_pr_12"):
        bartender_thoughts "(The prices are better than most places in the area, you idiot!)" 
    elif (current_thought == "barbara_thought_pr_13"):
        bartender_thoughts "(I hate to be rude, but I just don’t have time to deal with this guy.)" 
    elif (current_thought == "barbara_thought_pr_14"):
        bartender_thoughts "(He likes what I’ve done with it![wait_1] I knew that it was worth giving the bar a bit of a facelift!)" 
    elif (current_thought == "barbara_thought_pr_15"):
        bartender_thoughts "(What I {i}thought{/i}?[wait_1] Did I hear that right?)"
    elif (current_thought == "barbara_thought_pr_16"):
        bartender_thoughts "(Let’s just move on, and assume that I misheard him.)" 
    elif (current_thought == "barbara_thought_pr_17"):
        bartender_thoughts "(Huh.[wait_1] You know, I’ve never thought of this place as being that historic, but I guess it has been around for decades now.)" 
    elif (current_thought == "barbara_thought_pr_18"):
        bartender_thoughts "(I wonder where he heard of it - if there’s a good review or coverage of it somewhere, I should see whether they want to do an interview!)" 
    elif (current_thought == "barbara_thought_pr_19"):
        bartender_thoughts "(If he doesn’t know of its ownership, then what {i}does{/i} he know about it?)" 
    elif (current_thought == "barbara_thought_pr_20"):
        bartender_thoughts "(No need to mention to him anything about what the profitability has been like lately...)" 
    elif (current_thought == "barbara_thought_pr_21"):
        bartender_thoughts "(I really need to review those drinks policies again, work out what the projected differences would be.)" 
        jack thinking "(Drinks policies?[wait_1] If she’s looking to change things, maybe I can convince her that she should lower her prices a bit...)"
        $ add_boolean("prologue_drink_policies")
    elif (current_thought == "barbara_thought_pr_22"):
        bartender_thoughts "(Crap, I got sidetracked there![wait_1] ABC, Barbara, ABC!)" 
    elif (current_thought == "barbara_thought_pr_23"):
        bartender_thoughts "(Then why, exactly, did you come in here?)" 
    elif (current_thought == "barbara_thought_pr_24"):
        bartender_thoughts "(He can’t even think up a good excuse...[wait_05]but what was his original plan?[wait_1] Burst in and demand alcohol for free?)" 
    elif (current_thought == "barbara_thought_pr_25"):
        bartender_thoughts "(The sooner this guy gets out of here, the better.)" 
    elif (current_thought == "barbara_thought_pr_26"):
        bartender_thoughts "(Does he mean something like happy hour?[wait_1] Or discounts for regulars?)" 
        jack thinking "(Discounts for regulars?[wait_1] That’s not a bad idea...)"
        $ add_boolean("prologue_drink_discounts")
    elif (current_thought == "barbara_thought_pr_27"):
        bartender_thoughts "(I still haven’t worked out all of the changes that I’m planning to make...[wait_05]but I’m getting ahead of myself.[wait_1] I should just find out what he means.)" 
    elif (current_thought == "barbara_thought_pr_28"):
        bartender_thoughts "(Odd that he thinks jugs being cheaper is some sort of special policy...[wait_05]that’s called good pricing, mate.)" 
    elif (current_thought == "barbara_thought_pr_29"):
        bartender_thoughts "(With happy hour over there’s not much that I can really do for him, but hopefully he’ll just order something and stick with it.)" 
    elif (current_thought == "barbara_thought_pr_30"):
        bartender_thoughts "(I wish I could afford to lower the price a bit, but business on Mondays is always pretty slow.)" 
        bartender_thoughts "(Still, nobody forced him to come here today.)" 
    elif (current_thought == "barbara_thought_pr_31"):
        bartender_thoughts "(Who the hell does this guy think he is?![wait_1] Does he think he deserves a discount just for talking to me a little bit?)" 
    elif (current_thought == "barbara_thought_pr_32"):
        bartender_thoughts "(I’d rather have a night with no profit than deal with entitled assholes like this.)" 
    elif (current_thought == "barbara_thought_pr_33"):
        bartender_thoughts "(One of my regulars?[wait_1] This is clearly the first time you’ve been here!)" 
    elif (current_thought == "barbara_thought_pr_34"):
        bartender_thoughts "(Would I define a regular as somebody who comes by at least three nights a week, or - no, this isn’t the time to think about this.)" 
    elif (current_thought == "barbara_thought_pr_35"):
        bartender_thoughts "(You haven’t paid for anything so far, you idiot.)" 
    elif (current_thought == "barbara_thought_pr_36"):
        bartender_thoughts "(Maybe if there was actually some benefit to it, like some publicity.[wait_1] But as much as I’d like to, I can’t afford to just throw money away like that.)" 
        jack thinking "(Publicity?[wait_1] Hmm...[wait_05]I think that might give me an idea.)"
        $ add_boolean("prologue_drink_review")
    elif (current_thought == "barbara_thought_pr_37"):
        bartender_thoughts "(I’m willing to bet he’ll just leave the bar now. I know his type.)" 
    elif (current_thought == "barbara_thought_pr_38"):
        bartender_thoughts "(Wait a second - did I hear that right?)"  
        bartender_thoughts "(This guy writes reviews?)" 
    elif (current_thought == "barbara_thought_pr_39"):
        bartender_thoughts "(I shouldn’t get my hopes up too much...[wait_05]but in the off chance that he works for somewhere big, this - this could be a really good opportunity.)" 
    elif (current_thought == "barbara_thought_pr_40"):
        bartender_thoughts "(He’s not too mad about how long it’s taken to get to being served, is he?)" 
        bartender_thoughts "(Or - I guess he was dragging things out because he wanted to know a bit more about me, and the bar, for his article.)" 
    elif (current_thought == "barbara_thought_pr_41"):
        bartender_thoughts "(This is - this could really make a big difference, and turn things around after some of the decisions I’ve made.)" 
        bartender_thoughts "(I - I can’t believe this, it - it seems too good to be true.)" 
    elif (current_thought == "barbara_thought_pr_42"):
        bartender_thoughts "(The drink will be fine.[wait_1] I’ve poured them a million times, and the odds are that he just wants something straight from a bottle.)" 
    elif (current_thought == "barbara_thought_pr_43"):
        bartender_thoughts "(Too easy!)"
    elif (current_thought == "barbara_thought_pr_44"):
        bartender_thoughts "(He looks as though he’s really enjoying it...[wait_05]no need to be so nervous, Barbara.)"
        bartender_thoughts "(It’s not like it’s a difficult drink to make.)"
    elif (current_thought == "barbara_thought_pr_45"):
        bartender_thoughts "(Almost too quickly, really...[wait_05]he probably has a few places he needs to get to tonight.)"
    elif (current_thought == "barbara_thought_pr_46"):
        bartender_thoughts "(I do want a good review, but I need to draw the line somewhere.)"
        bartender_thoughts "(He should also gauge the prices, after all.)"
    elif (current_thought == "barbara_thought_pr_47"):
        bartender_thoughts "(Is he annoyed?[wait_1] He’s gone fairly quiet...)"
    elif (current_thought == "barbara_thought_pr_48"):
        bartender_thoughts "(He seems a little out of it, but...[wait_05]it could make a really big difference, and turn things around a bit.)"
        bartender_thoughts "(I - I have to do what’s best for the bar.[wait_1] And I’m sure he can’t be under the influence that much.)"
    elif (current_thought == "barbara_thought_pr_49"):
        bartender_thoughts "(He’s slurring quite a bit now...where did that come from?)"
        bartender_thoughts "(But he’s been pretty good up until now, so it’s probably not as bad as it looks...[wait_05]and it would help out a lot...)"
    elif (current_thought == "barbara_thought_pr_50"):
        bartender_thoughts "(Water down the - what sort of horrible owner does he think I am?!)"
    elif (current_thought == "barbara_thought_pr_51"):
        bartender_thoughts "(I don’t know how I didn’t notice it earlier, but he’s too far gone.)"
        bartender_thoughts "(It would be easy to be a little selfish, and overlook it in exchange for a good review, but I just don’t feel right doing that.)"
    elif (current_thought == "barbara_thought_pr_52"):
        bartender_thoughts "(Maybe if any reviews had been run since I took over, I’d like it.)"
    elif (current_thought == "barbara_thought_pr_53"):
        bartender_thoughts "(He probably isn’t even a reviewer - just an addict looking for a free handout.)"
    elif (current_thought == "barbara_thought_pr_54"):
        bartender_thoughts "(He looks like he’s trying to fry my brain with his laser vision.)"
    elif (current_thought == "barbara_thought_pr_55"):
        bartender_thoughts "(I have no idea what he’s talking about and I don’t care.[wait_1] I’m over this shit.)"
    elif (current_thought == "docherty_thought_pr_1"):
        docherty_thoughts "(...)"
        jack worried "(No...[wait_05]my powers still aren’t working...[wait_05]I can’t read this guy’s mind!)"
    else:
        $ renpy.log("No corresponding mind read line found for [current_thought]")
    
    hide ring
    $ ignore_thoughts_length()
    return

label prologue_docherty_wipe:
    $ progress_convo = False
    docherty_thoughts "(...)"
    jack worried "(He...[wait_05]I don't think that did anything to him?)"
    $ ignore_thoughts_length()
    return