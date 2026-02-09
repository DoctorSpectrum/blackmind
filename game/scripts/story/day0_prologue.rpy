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
    bartender "Sorry![wait_1] I was out back, changing over a keg." 
    bartender "How are you doing?" 
    jack smug "Not too bad, although I’d definitely be doing better if I had a drink...[wait_05]or two!"
    jack smug "(God I'm funny!)"
    bartender "I can help you out with that.[wait_1] What exactly were you hoping for?" 
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
    bartender "Just shoot the payment through and we’re good." 
    jack worried "(What?![wait_1] I can’t rewind her mind if she doesn’t make it!)"
    bartender "Or would you rather pay with cash?[wait_1] That’s fine too." 
    jack worried "I...[wait_05]actually, come to think of it, I’d rather order something else."
    show screen cash_money
    jump prologue_02

label prologue_03:
    jack thinking "(She’s happy to give me what I want?[wait_1] This bar is fucking amazing!)"
    $ current_thought = "barbara_thought_pr_02"
    jack thinking "You’re good to give me a glass of whiskey, yeah?"
    bartender "And coke?[wait_1] Sure thing - just tap your card when you’re ready and I’ll be right with you." 
    $ current_thought = "barbara_thought_pr_03"
    jack angry "Tap my - what do you mean?[wait_1] I thought you were going to give me it for free!"
    $ swap_sprites("barbara_angry")
    bartender "And why the hell would I do that?" 
    $ current_thought = "barbara_thought_pr_04"
    jack angry "You thought it![wait_1] Don’t try and deny it, I know you did!"
    bartender "What the hell?![wait_1] Just - who the hell are you?" 
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

    $ remove_boolean("prologue_interior_designing_2")
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_pr_05"
    bartender "Urgh...[wait_05]my head..." 
    bartender "I - sorry mate, I was out back, changing over a keg.[wait_1] At least...[wait_05]that’s what I thought I was doing." 
    $ current_thought = "barbara_thought_pr_06"
    $ swap_sprites("barbara_smiling")
    bartender "How are you doing?" 
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
    bartender "I’d hope so, given that I’m the owner." 
    $ current_thought = "barbara_thought_pr_10"
    jack smug "Oh, really?[wait_05] You’ve done a great job with it - I love the aesthetic you’ve got going."
    jack worried "(What the hell is the name of this style?[wait_1] The only one I know is gothic, and it definitely isn’t that)."
    $ current_thought = "barbara_thought_pr_11"
    jack smug "It's a very...[wait_05] ...[wait_05] ...gothic style, if I'm not mistaken?"
    bartender "You are mistaken, but that’s neither here nor there." 
    bartender "Anyway, did you want a drink?" 

label prologue_05:
    menu:
        "No":
            $ current_thought = "barbara_thought_pr_12"
            jack angry "At the prices you’re offering?[wait_1] No thanks."
            bartender "Then what are you even doing here?!" 
            jack worried "Um..."
            jack worried "(What, exactly, was I thinking with that, again?)"
            $ current_thought = "barbara_thought_pr_13"
            bartender "If you’re not ordering, then please leave.[wait_1] I’ve got better things to do than entertain beggars." 
            jack thinking "(Okay, so I’ll need to read more of her thoughts so that I can work out what she might want to talk about, to get her to like me more.)"
            jack thinking "(First of all I’ll need to rewind her mind, though.)"
            hide screen conversation_history
            call screen psychic_powers
        "Ask about the history of the bar" (locked=not check_boolean("prologue_bar_history"), message="You have not read this information in the bartender's mind"):
            jack smug "Oh, of course, of course."
            jump prologue_06
        "Ask about interior design" (locked=not check_boolean("prologue_interior_designing"), message="You have not read this information in the bartender's mind"):
            $ current_thought = "barbara_thought_pr_14"
            jack smug "What I really wanted was to talk about interior design."
            jack smug "I think that your work is...[wait_1]beautiful, really.[wait_1] Really beautiful, yeah."
            if (check_boolean("prologue_interior_designing_2") == False):
                $ swap_sprites("barbara_smiling")
                bartender "Oh, thank you![wait_1] But it’s not actually my work - I just hired an interior designer for it." 
                $ current_thought = "barbara_thought_pr_15"
                jack thinking "What?[wait_05] But you wanted to teach me a lesson or two about it.[wait_05] That’s what you thought before."
                $ swap_sprites("barbara_thinking")
                $ current_thought = "barbara_thought_pr_16"
                bartender "I’m...[wait_05]not sure what exactly to tell you.[wait_1] My job is running a bar, not doing interior design." 
                $ swap_sprites("barbara_smiling")
                bartender "And on that note - you never answered me when I asked before." 
                bartender "Did you want a drink?" 
                $ add_boolean("prologue_interior_designing_2")
                jump prologue_05
            else:
                $ swap_sprites("barbara_smiling")
                bartender "Yes, I heard you the first time." 
                bartender "But you still haven’t answered my question - do you want a drink?" 
                jump prologue_05

label prologue_06:
    show screen conversation_history
    show screen psychic_powers
    $ rewind_point = "prologue_06"
    $ current_thought = "barbara_thought_pr_17"
    
    jack smug "How could I be in such a...[wait_05]historic place and not want to have a drink?"
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_pr_18"
    bartender "You’ve heard of our bar before, then?" 
    $ current_thought = "barbara_thought_pr_19"
    jack worried "\"Our\" bar?"
    $ current_thought = "barbara_thought_pr_20"
    bartender "Oh, this bar has been in my family for three generations now." 
    bartender "Although I’ve only been running it for the last...[wait_05]I want to say eight months?" 
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_pr_21"
    bartender "Which doesn’t sound like a lot, but I’ve got a lot of good ideas about how to make it even better!" 
    bartender "Before you know it, this will be your favourite bar in the area - no, in the city!" 
    $ current_thought = "barbara_thought_pr_22"
    bartender "In fact, I can start out by showing you how good our drinks are - what exactly did you want to drink, again?" 

    menu:
        "Nothing":
            $ current_thought = "barbara_thought_pr_23"
            jack smug "Oh, no need to worry about it.[wait_1] I’m not looking to drink anything."
            $ swap_sprites("barbara_angry")
            bartender "Then why, exactly, did you come in here?" 
            $ current_thought = "barbara_thought_pr_24"
            jack worried "Uh..."
            jack worried "(I had something I wanted to say here...[wait_05]didn’t I?)"
            $ current_thought = "barbara_thought_pr_25"
            jack worried "To...[wait_05]talk to you?"
            bartender "I’m flattered, but please - just leave." 
            jack thinking "(I’ll wipe her memory of this part of the conversation, and try this again...)"
            jack thinking "(I need to start nudging her towards the idea of free drinks, or I’ll never get anywhere)."
            hide screen conversation_history
            call screen psychic_powers
        "That depends upon your drinks policies" (locked=not check_boolean("prologue_drink_policies"), message="You have not read information about the bar's drinks policies in her mind"):
            jump prologue_07

label prologue_07:
    show screen conversation_history
    show screen psychic_powers
    $ rewind_point = "prologue_07"

    $ current_thought = "barbara_thought_pr_26"
    jack smug "Well before I answer you that, I’m going to need an answer of my own: what are your drinks policies?"
    $ current_thought = "barbara_thought_pr_27"
    $ swap_sprites("barbara_thinking")
    bartender "Drink policies?[wait_1] What exactly do you mean?" 
    $ current_thought = "barbara_thought_pr_28"
    jack smug "You know, things like - like happy hour, or jugs being cheaper than the equivalent in pints."
    jack smug "Surely you’ve got to have something to offer me, yeah?"
    $ current_thought = "barbara_thought_pr_29"
    bartender "Happy hour ended at six o’clock, sorry." 
    bartender "As for discounts - tell me what exactly you want, and I’ll tell you what I can do." 

    menu:
        "Give me a whiskey":
            jack smug "(It sounds like she’s pretty keen to give me it for cheaper - I knew that listening to her bang on about all that boring stuff would be worth it)."
            $ current_thought = "barbara_thought_pr_30"
            jack smug "Can I have a whiskey? With all of the discounts applied, of course."
            $ swap_sprites("barbara_smiling")
            bartender "Sure! Just so you know, there aren’t any discounts for it, so that’ll be $14." 
            $ current_thought = "barbara_thought_pr_31"
            jack angry "What?![wait_1] This is bullshit, you’re not willing to give me even a little bit off the top?"
            $ swap_sprites("barbara_angry")
            $ current_thought = "barbara_thought_pr_32"
            bartender "What for?[wait_1] If that’s going to be the way you want it, then I’ll do you one better and ask you to get out - right now."
            jack thinking "(If I do that, then I won’t get any of that lovely booze...)"
            jack thinking "(I guess I’ll need a good reason why she should give me a discount, since apparently I’m not good enough for her.)"
            jack thinking "(Let’s rewind her mind and try again.)"
            hide screen conversation_history
            call screen psychic_powers
        "How about you give me a discount since I’m a regular?" (locked=not check_boolean("prologue_drink_discounts"), message="You have not read information about discounts in the bartender's mind"):
            jack smug "(Alright, there’s no way that this can go wrong.[wait_1] That drink is as good as mine)."
            $ current_thought = "barbara_thought_pr_33"
            jack smug "How about you give me a drink with a bit of a discount?[wait_1] As a bit of a treat, for one of your regulars?"
            $ current_thought = "barbara_thought_pr_34"
            $ swap_sprites("barbara_angry")
            bartender "Interesting idea, although that’s not actually a policy that I run here." 
            $ current_thought = "barbara_thought_pr_35"
            jack smug "Oh come now - you don’t want to reward your loyal customers?[wait_1] The people who are basically paying your wages for you?"
            $ current_thought = "barbara_thought_pr_36"
            bartender "Sorry, but it doesn’t work that way."  
            bartender "So are you going to order a drink - at its full price - or not?" 
            $ current_thought = "barbara_thought_pr_37"
            jack thinking "(Bitch doesn’t want to give me a discount, but I know that there’s a way to convince her!)"
            jack thinking "(I just need to rewind her mind and try again.)"
            hide screen conversation_history
            call screen psychic_powers
        "I’ll write a good review if you give me a free drink" (locked=not check_boolean("prologue_drink_review"), message="You have not read information about the bar's publicity in the bartender's mind"):
            $ current_thought = "barbara_thought_pr_38"
            jack smug "Tell me - how would you feel about a bit of an exchange?[wait_1] A free drink, and in return I’ll make sure to write a good review."
            $ swap_sprites("barbara_thinking")
            $ current_thought = "barbara_thought_pr_39"
            bartender "You mean...[wait_05]for a blog or something, right?[wait_1] Or a - a Google review?" 
            jack smug "Let me put it this way:[wait_05] I’m not supposed to name any names, but I’m thinking of a magazine right now, and it’s definitely one that you’ve heard before."
            jack thinking "(That’s not a lie.[wait_05] I’m thinking of a magazine, but I never explicitly said that I worked for them.)"
            jack thinking "(It’s not my fault if she misinterprets that.)"
            $ swap_sprites("barbara_smiling")
            $ current_thought = "barbara_thought_pr_40"
            bartender "Well I - if you really are working for someone big, then I - yeah, I - a review would be - yes please!" 
            $ current_thought = "barbara_thought_pr_41"
            bartender "Is it - are you sure that it’s alright, though?" 
            jack smug "Only if you’re alright with getting flooded with customers after they hear what I have to say about this place.[wait_1] Ha!"
            jack smug "(It’s fine.[wait_05] I’ll just get her to give me a single free drink, then I’ll definitely be heading off.)"
            jack smug "(It’s not like I’m going to exploit this or anything.)"
            $ current_thought = "barbara_thought_pr_42"
            bartender "Well in that case - what exactly can I get you?" 
            $ current_thought = "barbara_thought_pr_43"
            if (drink == "cocktail"):
                jack smug "How about a cocktail?[wait_1] That’d really wet my whistle."
                bartender "Anything in particular?"
                jack smug "Surprise me."
            elif (drink in ["whiskey", "wine"]):
                jack smug "How about a [drink]?[wait_1] That'd really wet my whistle."
            else:
                jack smug "How about a whiskey and coke?[wait_1] That'd really wet my whistle."
            bartender "Coming right up!"

label prologue_08:
    scene black_bg with quick_dissolve
    $ play_sound("ice_cube_clink.mp3")
    $ current_thought = "barbara_thought_pr_44"
    jack thinking "(I’ve definitely had better, and I bet she’s probably watered this down, just like every other bloody bar.)"
    jack thinking "(But I guess if I was a reviewer, I’d pretend to like it.)"
    scene bar with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_45"
    bartender "How was it?[wait_05] You certainly looked like you enjoyed it; you drank it quickly enough!"
    jack thinking "(Well obviously.[wait_1] The faster I drink it, the faster I’ll get drunk)."
    $ current_thought "barbara_thought_pr_46"
    jack smug "Well, it wasn’t bad.[wait_1] But I think I’d probably have a better opinion if I could have a follow-up...?"
    bartender "Heh, nice try, but one freebie’s all that I can give you."
    bartender "Technically I shouldn’t have even done that, but I doubt it’ll make that much difference in the long run."
    jack angry "(Bloody typical - you ask for one small favour and they act like you’re asking for the world.[wait_1] Only out for herself, just like everybody else.)"
    $ current_thought "barbara_thought_pr_47"
    jack smug "(Well, luckily for me, I have a nice solution for that...)"
    $ rewind_point = "prologue_09"
    hide screen conversation_history
    call screen psychic_powers

label prologue_montage_rewind:
    jack smug "(No need to do that quite yet - I haven’t gotten the next drink yet!)"
    return

label prologue_09:
    show screen conversation_history
    show screen psychic_powers
    $ rewind_point = "prologue_cancel"
    
    $ current_thought = "barbara_thought_pr_38"
    jack smug "Tell me - how would you feel about a bit of an exchange?[wait_1] A free drink, and in return I’ll make sure to write a good review."
    jack smug "(Just one more drink, that’s all.[wait_1] Get a nice buzz going, and then I’ll be on my way)."
    scene black_bg with quick_dissolve
    scene bar with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_41"
    bartender "Is it - are you sure that it’s alright, though?"
    jack smug "Are you alright with getting more customers?[wait_1] Because if so, then you’d better get pouring!"
    scene black_bg with quick_dissolve
    scene bar with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_48"


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