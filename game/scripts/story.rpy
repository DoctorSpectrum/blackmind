label story:
    call screen debug
    
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

label bar:
    jack "I am in the bar"
    call screen map_navigation

label alt_shop:
    jack "I am in the alt shop"
    call screen map_navigation

label cafe:
    jack "I am in the cafe"
    call screen map_navigation

label detective:
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