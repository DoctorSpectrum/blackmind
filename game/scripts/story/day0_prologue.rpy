label prologue_01:
    $ quick_menu = False
    #if (not persistent.senses_attuned):
    #    call screen attune_senses

    $ renpy.music.stop()
    docherty "I apologise for this, young man, but you are in the way of my plan." (name="???")
    $ play_sound("gunshot.mp3", pause=2.0, transition=white_flash)

    call screen chapter_breaks("PROLOGUE", "A young man with psychic powers is currently walking the streets downtown. He has no idea of what destiny will lead him to tonight.")
    $ quick_menu = True

    $ play_music("neutral_1")
    scene street with slow_dissolve
    $ scene_setup(40, "Monday", True, 1, 2, True, True)
    
    jack angry "(God, it took the cops long enough to let me go.)"
    jack angry "(Absolutely no evidence at all that I stole those wallets, but they still managed to draw it out into hours of questioning.)"
    jack angry "(What’s the big deal, anyway?)"
    jack angry "(Pickpocketing’s considered a petty crime.[wait_1] That basically means that they shouldn’t be wasting any time on it, especially when they’ve got no evidence.)"
    jack smug "(Anyway, how much cash was I able to get from those suckers before the cops spotted me?)"
    show screen cash_money
    jack thinking "(Damn, I was hoping for a bit more than that...if I could take plastic things’d be easier, but it’s just too easy to trace or be blocked)."
    jack smug "(Well, whatever.[wait_1] This should still be enough for me to get a drink or two)."
    hide screen cash_money
    scene black_bg with quick_dissolve
    
    scene bar with slow_dissolve
    jack thinking "(Is there no bartender here?[wait_1] And...also no customers?)"
    jack thinking "Hello![wait_1] Anybody home?"
    jack smug "(I’ll give it thirty seconds, then I’m grabbing all the bottles I can hold.)"
    jack smug "(They probably want people to do that anyway.[wait_1] You wouldn’t just leave things unattended and then be annoyed that they’re missing; you know what you’re getting in for.)"
    $ swap_sprites("barbara_smiling", slow_dissolve)
    $ current_thought = "barbara_thought_pr_01"
    barbara "Sorry![wait_1] I was out back, changing over a keg." (name="Bartender")
    barbara "How are you doing?" (name="Bartender")
    jack smug "Not too bad, although I’d definitely be doing better if I had a drink...[wait_05]or two!"
    jack smug "(God I'm funny!)"
    barbara "I can help you out with that.[wait_1] What exactly were you hoping for?" (name="Bartender")
    show screen cash_money

label prologue_02:
    menu:
        "Lemonade ($6)":
            hide screen cash_money
            show screen conversation_history

            jack worried "(I guess I’ll have to order a lemonade since it’s the only thing that I have the money for.)"
            jack worried "(But I was really looking forward to some booze...)"
            jack thinking "(Unless...[wait_05]I might be able to trick her into giving me a drink for free, if I use my abilities right.)"
            jack thinking "(Yeah...[wait_05]that’s a pretty good idea.)"
            jack smug "(She probably already really likes me - it’s not even going to be that much effort to convince her probably.)"
            jack smug "(What’s she thinking about right now?)"

            hide screen say
            hide screen conversation_history
            $ add_boolean("psychic_powers_available")
            call screen modal_popup("Click on the Read Mind button in the top right-hand corner, or press the 1 key, to read the bartender’s mind.", ["OK"], [Return()])
            call screen psychic_powers

        "Whiskey ($14)":
            $ drink = "whiskey"
        "Wine ($21)":
            $ drink = "wine"
        "Cocktail ($26)":
            $ drink = "cocktail"
    
    hide screen cash_money
    show screen conversation_history
    jack smug "(It doesn’t matter that I can’t afford it - all that I need is for her to serve it, then I’ll rewind her mind so she doesn’t remember that I haven’t paid)."
    jack smug "Can you get me a [drink]?"
    barbara "Just shoot the payment through and we’re good." (name="Bartender")
    jack worried "(What?![wait_1] I can’t rewind her mind if she doesn’t make it!)"
    barbara "Or would you rather pay with cash?[wait_1] That’s fine too." (name="Bartender")
    jack worried "I...[wait_05]actually, come to think of it, I’d rather order something else."
    show screen cash_money
    jump prologue_02

label prologue_03:
    jack thinking "(She’s happy to give me what I want?[wait_1] This bar is fucking amazing!)"
    $ current_thought = "barbara_thought_pr_02"
    jack thinking "You’re good to give me a glass of whiskey, yeah?"
    barbara "And coke?[wait_1] Sure thing - just tap your card when you’re ready and I’ll be right with you." (name="Bartender")
    $ current_thought = "barbara_thought_pr_03"
    jack angry "Tap my - what do you mean?[wait_1] I thought you were going to give me it for free!"
    $ swap_sprites("barbara_angry")
    barbara "And why the hell would I do that?" (name="Bartender")
    $ current_thought = "barbara_thought_pr_04"
    jack angry "You thought it![wait_1] Don’t try and deny it, I know you did!"
    barbara "What the hell?![wait_1] Just - who the hell are you?" (name="Bartender")
    jack worried "(Shit![wait_05] I shouldn’t have said that - I’d better wipe that from her memory!)"
    hide screen say
    hide screen conversation_history
    $ rewind_point = "prologue_04"
    $ add_boolean("mind_wipe_available")
    call screen modal_popup("Click on the Rewind Mind button, or press the 2 key, to make the bartender forget the last few minutes of conversation.", ["OK"], [Return()])
    call screen psychic_powers

label prologue_04:
    show screen conversation_history
    show screen psychic_powers

    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_pr_05"
    barbara "Urgh...[wait_05]my head..." (name="Bartender")
    barbara "I - sorry mate, I was out back, changing over a keg.[wait_1] At least...[wait_05]that’s what I thought I was doing." (name="Bartender")
    $ current_thought = "barbara_thought_pr_06"
    $ swap_sprites("barbara_smiling")
    barbara "How are you doing?" (name="Bartender")
    if (check_boolean("jack_tutorial_psychic_explanation") == False):
        jack thinking "(If I use my psychic abilities correctly, I can definitely trick her into giving me something for free.)"
        jack thinking "(For now I should try to avoid talking about drinks, and focus on getting her to like me first.)"
        $ add_boolean("jack_tutorial_psychic_explanation")
    $ current_thought = "barbara_thought_pr_07"
    jack smug "You know, this is a really nice bar."
    $ current_thought = "barbara_thought_pr_08"
    jack smug "Whoever the owner is, they’ve done a really good job with it...[wait_05]especially at hiring staff."
    $ swap_sprites("barbara_angry")
    $ current_thought = "barbara_thought_pr_09"
    barbara "I’d hope so, given that I’m the owner." (name="Bartender")
    $ current_thought = "barbara_thought_pr_10"
    jack smug "Oh, really?[wait_05] You’ve done a great job with it - I love the aesthetic you’ve got going."
    jack worried "(What the hell is the name of this style?[wait_1] The only one I know is gothic, and it definitely isn’t that)."
    $ current_thought = "barbara_thought_pr_11"
    jack smug "It's a very...[wait_05] ...[wait_05] ...gothic style, if I'm not mistaken?"
    barbara "You are mistaken, but that’s neither here nor there." (name="Bartender")
    barbara "Anyway, did you want a drink?" (name="Bartender")

    menu:
        "No":
            $ current_thought = "barbara_thought_pr_12"
            jack angry "At the prices you’re offering?[wait_1] No thanks."
            barbara "Then what are you even doing here?!" (name="Bartender")
            jack worried "Um..."
            jack worried "(What, exactly, was I thinking with that, again?)"
            $ current_thought = "barbara_thought_pr_13"
            barbara "If you’re not ordering, then please leave.[wait_1] I’ve got better things to do than entertain beggars." (name="Bartender")
            jack thinking "(Okay, so I’ll need to read more of her thoughts so that I can work out what she might want to talk about, to get her to like me more.)"
            jack thinking "(First of all I’ll need to rewind her mind, though.)"
            hide screen conversation_history
            call screen psychic_powers
        "Ask about the history of the bar" (locked=not check_boolean("prologue_bar_history"), message="You have not read this information in the bartender's mind"):
            jack thinking "test"
        "Ask about interior design" (locked=not check_boolean("prologue_interior_designing"), message="You have not read this information in the bartender's mind"):
            $ current_thought = "barbara_thought_pr_14"
            jack smug "What I really wanted was to talk about interior design."
            jack smug "I think that your work is...[wait_1]beautiful, really.[wait_1] Really beautiful, yeah."

label prologue_post_mind_read_tutorial:
    $ add_boolean("mind_read_tutorial")
    if (convo_length == 11):
        $ set_convo_length(15)
    jack smug "It was, um, about fifty, that you owed me, by the way."
    jack smug "Fifty - and one hundred.[wait_1] One hundred and fifty."
    $ current_thought = "barbara_thought_pr_05"
    jack smug "That’s right, you owed me one hundred and fifty in change."
    $ swap_sprites("barbara_angry")
    barbara "Really?[wait_1] I think you might have miscalculated that a bit; that’s quite a lot of change to give." (name="Bartender")
    $ current_thought = "barbara_thought_pr_06"
    jack smug "Well, you know what they say about calculations...[wait_1]I mean, numbers don’t really mean anything, do they?"
    jack smug "What exactly is a number?[wait_1] Is it a thing you can see?"
    $ current_thought = "barbara_thought_pr_07"
    jack smug "Is it something you can touch, or...[wait_05]eat?"
    $ current_thought = "barbara_thought_pr_08"
    barbara "I think it’s safe to say that I’ll be able to see some numbers on the terminal." (name="Bartender")
    jack smug "Are you sure that you want to do that?"
    $ current_thought = "barbara_thought_pr_09"
    jack smug "Computers aren’t really all that good when it comes to numbers."
    jack smug "There’s a reason that banks are full of cash, and -[wait_05] and gold, rather than computers."
    $ current_thought = "barbara_thought_pr_10"
    jack smug "So thinking about it, they can’t really be that useful, can they?"
    $ current_thought = "barbara_thought_pr_11"
    jack smug "I mean, when this bar first opened, it wasn’t like they used computers, was it?[wait_1] And it was much better for it, I bet."
    $ current_thought = "barbara_thought_pr_12"
    jack smug "They didn’t -[wait_05] they would have used something more accurate, like calculators, or something, to work out the numbers, yeah?"
    $ current_thought = "barbara_thought_pr_13"
    barbara "Nice try, but I trust the terminal a lot more than I trust you." (name="Bartender")

    hide screen conversation_history
    hide screen psychic_powers
    menu:
        "Let her open it":
            $ set_convo_length(7)
            $ play_music("tense_1")
            show screen conversation_history
            show screen psychic_powers
            jack smug "(This will be fine.)"
            jack smug "(Just because I haven’t paid her, that doesn’t mean anything.[wait_1] It’s not like she can make me pay her.)"
            jack smug "(If she did, that would be a mugging, and I’d basically be allowed to run, wouldn’t I?)"
            $ current_thought = "barbara_thought_pr_14"
            barbara "Looks like I owe you quite a bit less than you said." (name="Bartender")
            barbara "In fact, I think you might have who owes who around the wrong way." (name="Bartender")
            jack worried "(Shit![wait_1] Okay, new plan: rewrite her mind, and try this again.)"
            jack worried "(I should probably try reading her mind a bit more next time...[wait_1]I might get a bit more information that I can use on her)."
            hide screen conversation_history
            call screen psychic_powers
        
        "But it has issues with certain cards" (locked=not check_boolean("mind_read_tutorial_card_processing"), message="You have not read this information in the bartender's mind"):
            $ set_convo_length(13)
            $ play_music("tense_1")
            show screen conversation_history
            show screen psychic_powers
            jack smug "Do you, though?[wait_1] That old thing?"
            $ current_thought = "barbara_thought_pr_15"
            jack smug "How much can you really trust a computer that has as many issues with cards as this one does?"
            $ swap_sprites("barbara_thinking")
            $ current_thought = "barbara_thought_pr_16"
            barbara "That’s true...[wait_1]it’s sometimes a little off when it comes to surcharges, and when I asked about it, they just said that they’d open a ticket about it." (name="Bartender")
            $ current_thought = "barbara_thought_pr_17"
            jack smug "Those bloody computer people.[wait_1] They’re always going on about tickets, aren’t they?"
            $ swap_sprites("barbara_smiling")
            barbara "They are![wait_1] It wouldn’t kill them to show a bit more support for their customers; I pay them enough fees each month!" (name="Bartender")
            jack smug "They’re taking the bloody piss![wait_1] And I - you know what, actually?"
            $ current_thought = "barbara_thought_pr_18"
            jack smug "I reckon that the time to support them is over![wait_1] Let’s just - let’s stop using terminals, and computers, and cards, and just pay customers what they’re owed!"
            barbara "Good point![wait_1] Give me a moment to check how much I do owe you, though - if it was calculated incorrectly, then that’s another issue that I can bring up to them." (name="Bartender")
            $ current_thought = "barbara_thought_pr_19"
            jack worried "Wait, but -"
            $ swap_sprites("barbara_angry")
            $ current_thought = "barbara_thought_pr_20"
            barbara "Looking at this, it looks like you might have who owes who around the wrong way." (name="Bartender")
            barbara "I don’t suppose you’d be willing to actually pay me, now?" (name="Bartender")
            jack worried "(Shit![wait_1] Okay, new plan: rewrite her mind, and try this again.)"
            jack worried "(I need to read her mind and find something that I can use to stop her from using the computer...[wait_1]there’s got to be something in there if I read it at the right time)."
            hide screen conversation_history
            call screen psychic_powers
        
        "This bar used to be better" (locked=not check_boolean("mind_read_tutorial_bar_quality"), message="You have not read this information in the bartender's mind"):
            $ set_convo_length(22)
            $ play_music("tense_1")
            show screen conversation_history
            show screen psychic_powers
            jack angry "This bar used to be better, you know."
            $ current_thought = "barbara_thought_pr_21"
            jack angry "It was a lot friendlier, and it didn’t feel like you were constantly getting harassed while you were drinking."
            $ current_thought = "barbara_thought_pr_22"
            jack angry "If this is the way that things are going to be moving forwards, then you can consider this to be my last drink here."
            $ current_thought = "barbara_thought_pr_23"
            barbara "Good! I don’t want clientele like yourself anyway!" (name="Bartender")
            jack angry "Oh, yeah, that’s great.[wait_1] I’m sure that saying that to your customers will totally get them coming back."
            $ current_thought = "barbara_thought_pr_24"
            jack angry "Yeah, this bar is going to last for years at this rate, and it definitely won’t get driven into the ground."
            $ current_thought = "barbara_thought_pr_25"
            barbara "..." (name="Bartender")
            jack thinking "(Was that...[wait_05]the right thing to say?)"
            $ swap_sprites("barbara_sad")
            $ play_music("neutral_1")
            barbara "Sorry, I...[wait_05]I shouldn’t have said that.[wait_1] I’m still getting the hang of this thing." (name="Bartender")
            barbara "What they teach you with a business degree doesn’t always apply to the real world." (name="Bartender")
            jack smug "(So...[wait_05]money now?)"
            jack smug "(You’re going to give me the money, aren’t you?)"
            $ current_thought = "barbara_thought_pr_26"
            barbara "I just - I’m trying not to lose more than I can afford to, but I guess that makes me a bit more cautious when I should be more trusting." (name="Bartender")
            jack smug "(Just keep smiling and nodding.)"
            jack smug "(She’s got to give me the money eventually if I just wait out this pathetic pity party.)"
            $ swap_sprites("barbara_smiling")
            $ current_thought = "barbara_thought_pr_27"
            barbara "Here - your change is...[wait_05]oh, sorry." (name="Bartender")
            jack angry "(What is it now?!)"
            $ swap_sprites("barbara_sad")
            $ current_thought = "barbara_thought_pr_28"
            barbara "This has been a fairly quiet night, and most people usually pay by card, so there’s not actually enough change in the till." (name="Bartender")
            $ swap_sprites("barbara_smiling")
            barbara "But if you give me a minute, then I can go get the rest." (name="Bartender")
            jack smug "Oh, yeah, of course.[wait_1] That would be great."
            jack smug "But...[wait_05]if you wouldn’t mind giving me what’s in there at the moment?"
            $ money = 62
            show screen cash_money
            $ current_thought = "barbara_thought_pr_29"
            barbara "Of course.[wait_1] Right -[wait_05] back in a minute, then." (name="Bartender")
            hide screen psychic_powers
            hide barbara_smiling with quick_dissolve
            $ progress_convo = False
            jack smug "(Good start to the night so far - I’m $50 richer, and I’m about to get some more money on top of it.)"
            jack smug "(I can basically go wherever I want and afford anything!)"
            hide screen cash_money
            jack smug "(Where to next?[wait_1] Entertainment?[wait_05] Food?)"
            jack smug "(Or maybe...[wait_05]maybe I should go get some more money from somebody!)"
            jack smug "(Yeah, that’s perfect![wait_1] At the right place, I could probably end up with even more money...[wait_05]maybe even over $300!)"
            jack smug "(I just need this bartender to hurry up and bring the money back...)"
            narrator "...[wait_1] ...[wait_1] ..."
            jack thinking "(She’s taking her time -[wait_05] is something wrong?)"
            jack thinking "(Does she not want to give me my bloody money?)"
            jack worried "(Wait...[wait_05]maybe that is it?)"
            jack worried "(Maybe she realised that something was off, and is calling the cops!)"
            jack angry "(I’ll be damned if I’ll let them catch me here!)"
            jack angry "(I’d better leave while I’ve got the opportunity -[wait_05] I’ve already gotten plenty of cash from this place.)"
            hide screen calendar
            scene black_bg with slow_dissolve

label prologue_04_og:
    $ play_music("ambient_1")
    jack thinking "(I want to avoid the cops, but there’s no need for me to go home just yet.)"
    jack thinking "(It’s not like they’ll go searching every place nearby, and I’d rather stay out a bit late.)"
    jack thinking "(I mean, when was the last time somebody got yelled at about overdue rent when staying out?[wait_1] Never happens.)"
    jack thinking "(Where should I go?)"
    $ _history_list = []
    call screen map_navigation(find_locations([1, 2]))

label prologue_music_venue:
    $ scene_setup(45, "Monday", True, 2, 2, True, True)
    $ play_music("neutral_2")
    $ location = "music_venue"
    scene black_bg with slow_dissolve
    jack smug "(Right, so here’s what I think the plan will be:[wait_05] I’ll go up to the door, make the door person forget that I haven’t paid the fee and get in for cheap.)"
    jack smug "(Then once I’m inside, I can read a few minds, find out who’s loaded, and...[wait_05]work the rest out from there.)"
    jack smug "(Yeah.[wait_1] Yeah, I think this is a pretty solid plan.)"
    narrator "Jack’s psychic abilities first emerged when he was a teenager."
    narrator "He has no idea where they came from, or why he was blessed with these powers, but he’s never been one to look a gift horse in the mouth."
    narrator "If it’s a resource that benefits him, then he’s all the happier to abuse it for as long as he can get away with it."
    jack thinking "(With a bit of luck I’ll find some fat cat in there who won’t notice anything missing...[wait_05]it’s got to happen some time, right?)"
    jack thinking "(Statistically speaking, I’ll eventually get more than just scraps and leftovers.[wait_1] I just haven’t found the right person yet.[wait_1] That’s the issue.)"
    jack angry "(Bloody millionaires thinking that they’re too good to go to cheap bars and down back alleys.)"
    jack angry "(One of them will one day, and I’ll finally get something good off them.[wait_1] Enough to pay rent and still have a fair bit left over.)"
    jack thinking "(All that I need is a good bit of money...[wait_05]I have some big plans for the future...)"
    scene venue_exterior with slow_dissolve
    jack smug "(Alright, same deal as always: start heading in, wipe the doorman’s memory, then keep going.[wait_1] Easy.)"
    jack angry "(God, not that I should have to do this.)"
    jack angry "(If I was a doorman I’d let anybody in for free.[wait_1] The venue owners would start out mad, but then they’d -)"
    call prologue_precognition from _current2
    scene venue_exterior with quick_dissolve
    jump prologue_end

label prologue_restaurant:
    $ scene_setup(47, "Monday", True, 2, 2, True, True)
    $ play_music("neutral_2")
    scene black_bg with slow_dissolve
    $ location = "restaurant"
    jack smug "(Do they have wine at this place?[wait_1] I don’t really like it, but I could buy a nice big bottle of it anyway and show everyone there how rich I currently am.)"
    jack smug "(Maybe I could even buy two bottles, and then drop one of them on purpose.)"
    jack smug "(Yeah...[wait_1]that’ll show them all!)"
    jack smug "(Some people would probably say that I shouldn’t spend this money so soon, that I should hold onto it, seeing as how I don’t have a job at the moment.)"
    jack smug "(But why shouldn’t I spend it?[wait_1] It’s mine, isn’t it?)"
    jack thinking "(Okay, so technically it isn’t mine, and I got it from that bartender, but so what?)"
    jack thinking "(She would have done the exact same thing if she had these powers, I’m sure of it.)"
    jack thinking "(Everybody’s just out for themselves.[wait_1] The people who say they aren’t are just lying, so that you’ll let your guard down and they can take advantage of you.)"
    jack thinking "(I’m just following the natural way of things, same as everybody else.)"
    jack thinking "(Anyway, it’s not like I keep all of the money I get for myself.)"
    jack angry "(Spent enough bloody money hiring that guy the other week, didn’t I?)"
    jack angry "(And yeah, he was able to find out the information I wanted, but christ, he didn’t need to spend so much.)"
    jack angry "(I wish he’d told me what a {i}per diem{/i} was beforehand...[wait_05]how was I supposed to know how much it would add up to be?)"
    scene restaurant_night with slow_dissolve
    jack angry "(They’d better have some fucking tables left inside; I don’t want to sit out in the cold.)"
    jack smug "(Although I guess if they don’t have any, I can probably use my abilities to get somebody to go outside.)"
    jack smug "(It’s not like they’d know that I - )"
    call prologue_precognition from _current
    scene restaurant_night with slow_dissolve
    jump prologue_end

label prologue_precognition:
    scene black_bg
    hide screen calendar
    hide screen conversation_history
    $ play_music("tense_2")
    $ play_sound("gunshot.mp3", pause=2.0, transition=white_flash)
    show screen calendar("Monday", 2, 2)
    show screen conversation_history
    return

label prologue_end:
    jack worried "(My -[wait_05] my stomach, I -[wait_05] what’s happened?!)"
    jack worried "(It feels so -[wait_05] so sharp, and, and -[wait_05] god, breathing is -[wait_05] I -[wait_05] I can feel it with every breath.)"
    jack worried "(I -[wait_05] I -[wait_05] oh god, I -[wait_05] I’m dying!)"
    jack worried "(I...[wait_05]{size=-8}Mum.[wait_1] Mum, please come and - and help me!{/size})"
    jack worried "{size=-8}(I -[wait_05] I’m sorry Mum, I -[wait_05] please make it go away!){/size}"
    jack worried "{size=-8}(I -[wait_05] I don’t want to die...[wait_05]why isn’t anybody helping me?){/size}"
    jack worried "{size=-8}(Nobody cares about me...[wait_05]nobody wants me...){/size}"
    jack worried "...[wait_05] ..."
    narrator "Looking around, Jack realises why nobody is looking his way."
    narrator "Why nobody is helping a dying man, and why he didn’t even see his attacker."
    narrator "It’s because the attack hasn’t happened yet."
    jack thinking "(I...[wait_05]if I go into that building, I’m going to die.)"
    jack worried "(Somebody will shoot me, and I -[wait_05] oh god, I can’t do that.)"
    jack worried "(I can’t -[wait_05] I don’t want to die![wait_1] It hurt so much, and I -[wait_05] okay.)"
    jack thinking "(Okay.[wait_1] I’m not dead yet, and thanks to my precognition, I don’t have to die.)"
    jack thinking "(I -[wait_05] I can work this out.)"
    narrator "The third of Jack’s psychic abilities is the one that he has the least control over."
    narrator "If he focused on it a bit, and trained himself to recognise the sensation that it brings with it, perhaps he could refine it a little, and he would be its master, rather than the other way around."
    narrator "At times like this, however, all that he can do is try to listen to it."
    jack worried "(Entering that building will lead to my death, so...[wait_05]I just -[wait_05] I need to get away!)"
    jack worried "(Fuck my plans -[wait_05] fuck everything!)"
    jack worried "(Whoever it is that wants to kill me -[wait_05] whatever they want to kill me for, I -[wait_05] I can get away from them![wait_1] I'm sure I can!)"
    jack worried "(In fact, they won’t even know that I was ever here.)"
    scene black_bg with quick_dissolve
    narrator "But no matter where Jack runs..."
    $ play_sound("gunshot.mp3", transition=white_flash)
    jack worried "(Argh![wait_1] I’m -[wait_05] it hurts so much!)"
    jack worried "(But -[wait_05] but they haven’t found me yet![wait_1] I -[wait_05] I can still run!)"
    $ play_sound("gunshot.mp3", transition=white_flash)
    jack worried "(No...[wait_05]not here!)"
    jack worried "(Maybe...[wait_05]if I turn around...)"
    $ play_sound("gunshot.mp3", transition=white_flash)
    jack worried "(No...[wait_05]no...[wait_05]where can I go...?)"
    jack worried "(Everywhere I go I get the sensation -[wait_05] the -[wait_05] the gunshot...)"
    jack worried "(But there’s got to be a way out...[wait_05]there’s got to be!)"
    $ scene_setup(11, "Monday", True, 2, 2, True, True)
    scene street with slow_dissolve
    narrator "Jack has been shot multiple times by now, yet he has no wounds on him at all."
    narrator "He’s running out of breath, not to mention places to run to."
    jack worried "(I -[wait_05] I -[wait_05] where the fuck can I go?!)"
    jack worried "(Think...[wait_05]there has to be somewhere!)"
    jack thinking "(Or...[wait_05]can I talk to whoever is going to kill me, get them to leave me alone?)"
    jack thinking "(They can’t have that good a reason to go after me -[wait_05] I -[wait_05] I’ve never even hurt a fly!)"
    $ rewind_point = "prologue_docherty_wipe"
    $ swap_sprites("docherty_neutral", quick_dissolve)
    show screen psychic_powers
    $ current_thought = "docherty_thought_pr_1"
    jack worried "I -[wait_05] mate![wait_1] I -[wait_05] can you help me?[wait_1] Please?!"
    jack worried "There’s -[wait_05] somebody’s after me, and they’re -[wait_05] I swear, I -[wait_05] I just need a bit of help."
    jack worried "Do you -[wait_05] do you have a car, or anything...?"
    docherty "I apologise for this, young man, but you are in the way of my plan."
    jack angry "What do you -"
    hide screen calendar
    hide screen conversation_history
    hide screen psychic_powers
    $ play_sound("gunshot.mp3", transition=white_flash)
    scene cg1_placeholder with slow_dissolve
    jack worried "(No...[wait_05]no!)"
    jack worried "(I -[wait_05] I can't die!)"
    jack worried "(I just wanted to -[wait_05] please, somebody...[wait_05]help me...)"
    scene black_bg with slow_dissolve

    if (not persistent.docs_link_shown):
        narrator "Thanks for playing the prototype!"
        narrator "I've written up a bit of a docco about where I'm hoping to go with the game, to make things a bit more transparent and get a bit of feedback."
        narrator "You can access it here: {a=https://docs.google.com/document/d/1wAlhH52z9H0CxoKjtVLBtCwZTfI9KdIqwNmada6nMtQ/edit?usp=sharing}Google Docs Link{/a}."
        narrator "This link also appears in the Credits screen."
        $ persistent.docs_link_shown = True
    $ MainMenu(confirm=False)()