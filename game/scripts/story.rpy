label story:
    scene black_bg with quick_dissolve
    #Text and subtitle

    scene bar with quick_dissolve
    jack smug "(Ah...[wait_1]nothing like going to the bar on a Monday.)"
    jack smug "(Lots of lovely booze, lots of quiet, and best of all...[wait_05]a sexy bartender, who literally only has eyes for me)."
    $ swap_sprites("barbara_annoyed", slow_dissolve)
    barbara "Hello?[wait_1] Did you hear me?" (name="Bartender")
    jack worried "(Shit![wait_1] Has she been talking this whole time?)"
    jack worried "(What’s gotten her turned off all of a sudden?)"
    jack worried "Hmm?[wait_1] Hi, is something...[wait_05]wrong?"
    barbara "I said, I’m going to need you to pass that drink over and leave." (name="Bartender")
    barbara "You’ve clearly had too much to drink, and I can’t have you hanging around here." (name="Bartender")
    jack angry "(Whatever happened to the good old national binge drink?)"
    jack angry "(Used to be that we were told off for not drinking enough...[wait_1]it’s political correctness gone mad.)"
    jack thinking "(Still though, I’d better listen to her.)"
    jack thinking "( I don’t think she’s the type of angry that makes me feel horny.)"
    #SFX: Glass sliding
    jack smug "Right, there you go then."
    jack smug "Farewell, sweet mademoiselle, and thank you for bringing pleasure to a thirsty man."
    barbara "..." (name="Bartender")
    jack angry "(What’s she still looking angry for?[wait_1] That’s barely an innuendo!)"
    barbara "The bar’s policy is that all tabs have to be paid before leaving.[wait_1] No exceptions." (name="Bartender")
    jack worried "(Shit.[wait_05] How much money do I have?)"
    #Add the interface showing our money
    jack worried "(That's...[wait_05]not a lot.)"
    barbara "We take both cash and card." (name="Bartender")
    barbara "Can even split it between the two if that’s easier for you, but it’s got to be paid." (name="Bartender")
    jack smug "(Alright, no biggie.)"
    jack smug "(Just have to do a little rewrite without letting the alcohol affect me.[wait_1] Easy.)"

    return
    
label test_mind_reading:
    $ current_conversation = None
    $ convo_length = 10
    $ convo_progress = 0
    $ progress_convo = True

    jack "I'm not shit. Am I?"
    $ current_thought = "barbara_thought_01_01"
    $ current_conversation = "test_mind_reading"
    barbara "I've scraped shit off my shoe that was less shitty than you."

    jack "Yeah, that's what everybody thinks. That I'm a piece of shit."
    $ current_thought = "barbara_thought_01_02"
    barbara "If you're trying to get me to stop thinking of you as shit, it's not exactly working."

    jack "But...maybe shit could be appealing? Everybody says they don't like shit, but it's something that's part of all our lives...yeah?"
    $ current_thought = "barbara_thought_01_03"
    barbara "I generally try to get it out of my life as much as possible."

    jack "Exactly! So you've never thought about how shit might actually be...not shit?"
    jack "How shit can shit be, if you've never really experienced it?"
    $ current_thought = "barbara_thought_01_04"
    barbara "I'm not going to try and find out."

    $ current_thought = None
    $ current_conversation = None
    jack "(She left. How shit!)"
    
    jump story

label test_money:
    $ current_conversation = None
    $ convo_length = 3
    $ convo_progress = 0
    $ progress_convo = True

    jack "(I currently have $[money])"
    $ current_thought = "barbara_thought_01_01"
    barbara "I need money for the drinks."
    if (money > 0):
        $ money -= 100
        jack "(I now have $[money])"
    else:
        jack "(I can't afford the drinks)"
    jump story

label test_choices:
    jack "(I have a choice to make...)"

    menu:
        "Rewind the conversation" (locked=minds_rewound > 0, message="You have already rewound a mind today"):
            jack "(Yes, that should do it.)"
        "Punch him":
            jack "(Fuck you, dickweed!)"

    jump story

label bar:
    $ visit_location("bar")
    jack "I am in the bar"
    call screen map_navigation

label alt_shop:
    $ visit_location("alt_shop")
    jack "I am in the alt shop"
    call screen map_navigation

label cafe:
    $ visit_location("cafe")
    jack "I am in the cafe"
    call screen map_navigation

label detective:
    $ visit_location("detective")
    jack "I am at the detective's office"
    call screen map_navigation

label barbara_thought_01_01:
    $ progress_convo = False
    barbara "(This guy is definitely shit)."
    $ convo_progress -= 1
    $ progress_convo = True
    return

label barbara_thought_01_02:
    $ progress_convo = False
    barbara "(Well, at least he can admit it)."
    $ convo_progress -= 1
    $ progress_convo = True
    return

label barbara_thought_01_03:
    $ progress_convo = False
    barbara "(Is this supposed to be a pickup line?)"
    $ convo_progress -= 1
    $ progress_convo = True
    return

label barbara_thought_01_04:
    $ progress_convo = False
    barbara "(If you're trying to pick somebody up, maybe don't admit that you're shit)."
    $ convo_progress -= 1
    $ progress_convo = True
    return

label activate_rewind:
    $ progress_convo = False
    jack "(This conversation has been a total bollocks-up. I think we'll just wipe her memory and see how things go...)"

    jump expression current_conversation