label story:
    call screen debug
    
label test_mind_reading:
    jack "I'm not shit. Am I?"
    $ current_thought = "barbara_thought_01_01"
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
    jack "(She left. How shit!)"
    
    jump story

label barbara_thought_01_01:
    barbara "(This guy is definitely shit)."
    return

label barbara_thought_01_02:
    barbara "(Well, at least he can admit it)."
    return

label barbara_thought_01_03:
    barbara "(Is this supposed to be a pickup line?)"
    return

label barbara_thought_01_04:
    barbara "(If you're trying to pick somebody up, maybe don't admit that you're shit)."
    return