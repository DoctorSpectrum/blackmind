label prologue_01:
    $ quick_menu = False

    $ renpy.music.stop()
    scene black_bg
    show cg1_docherty at cg_1_teaser
    $ unlock_cg(0, 0)
    docherty "I apologise for this, young man, but you are in the way of my plan." (name="???")
    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)

    hide cg1_docherty with quick_dissolve
    call screen chapter_breaks("PROLOGUE", "A young man with psychic powers is currently walking the streets downtown. He has no idea of what destiny will lead him to tonight.")
    $ quick_menu = True

    $ play_music("neutral_1")
    scene street with slow_dissolve
    $ scene_setup(16, "Monday", True, 1, 2, True, True)
    $ current_thought_block = "mind_read_prologue"
    
    jack angry "(God, it took the cops long enough to let me go.)"
    jack angry "(Absolutely no evidence at all that I stole those wallets, but they still managed to draw it out into hours of questioning.)"
    jack angry "(What’s the big deal, anyway?)"
    jack angry "(Pickpocketing’s considered a petty crime.[wait_1] That basically means that they shouldn’t be wasting any time on it, especially when they’ve got no evidence.)"
    jack smug "(Anyway, how much cash was I able to get from those suckers before the cops spotted me?)"
    show screen cash_money
    jack thinking "(Damn, I was hoping for a bit more than that...it'd be easier if I could take plastic, but it’s just too easy to trace or be blocked.)"
    jack smug "(Well, whatever.[wait_1] Not like I need any of it to get myself a whiskey.)"
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

label prologue_02:
    hide screen conversation_history
    menu (screens=["cash_money"]):
        "Whiskey ($0)":
            hide screen cash_money

            jack worried "(There’s no point in looking at the prices she’s got - it’ll all be overpriced, just like every other bloody place.)"
            jack worried "(Who’s out there making things affordable for the little guy?[wait_1] Nobody, that’s who.)"
            jack thinking "(So when you think about it, is it really an issue if I use my abilities and trick her into giving me a drink for free?[wait_1] Obviously not.)"
            jack thinking "(She’ll definitely make all that money back when the first fat cat of the night steps in {size=-10}maybe{/size}.)"
            jack smug "(I’ll just need to convince her that she’ll benefit from pouring me that drink.)"
            jack smug "(What’s she thinking about right now?)"

            hide screen say
            hide screen conversation_history
            $ add_boolean("psychic_powers_available")
            call screen modal_popup("Click on the Read Mind button in the top right-hand corner, or press the 1 key, to read the bartender’s mind.", ["OK"], [Return()])
            call screen psychic_powers

        "Lemonade ($6)":
            jack smug "(Ha ha ha.)"
            jack angry "(No.)"
            jump prologue_02
        "Whiskey ($14)" (locked=True, message="You cannot legally afford this drink"):
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
    show screen psychic_powers
    if (renpy.music.get_playing() != "audio/music/Blackmind Track 1 - 97 BPM (D minor)v2- LOOPABLE.wav"):
        $ play_music("neutral_1")

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
    jack worried "(What the hell is the name of this style?[wait_1] The only one I know is gothic, and it definitely isn’t that.)"
    $ current_thought = "barbara_thought_pr_11"
    jack smug "It's a very...[wait_05] ...[wait_05] ...gothic style, if I'm not mistaken?"
    bartender "You are mistaken, but that’s neither here nor there." 
    bartender "Anyway, did you want a drink?" 

label prologue_05:
    menu:
        "No":
            $ current_thought = "barbara_thought_pr_12"
            $ play_music("tense_1")
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
    show screen psychic_powers
    $ rewind_point = "prologue_06"
    $ current_thought = "barbara_thought_pr_17"
    if (renpy.music.get_playing() != "audio/music/Blackmind Track 1 - 97 BPM (D minor)v2- LOOPABLE.wav"):
        $ play_music("neutral_1")
    
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
            $ play_music("tense_1")
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
            jack thinking "(I need to start nudging her towards the idea of free drinks, or I’ll never get anywhere.)"
            hide screen conversation_history
            call screen psychic_powers
        "That depends upon your drinks policies" (locked=not check_boolean("prologue_drink_policies"), message="You have not read information about the bar's drinks policies in her mind"):
            jump prologue_07

label prologue_07:
    show screen conversation_history
    show screen psychic_powers
    $ rewind_point = "prologue_07"
    if (renpy.music.get_playing() != "audio/music/Blackmind Track 1 - 97 BPM (D minor)v2- LOOPABLE.wav"):
        $ play_music("neutral_1")

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
            jack smug "(It sounds like she’s pretty keen to give me it for cheaper - I knew that listening to her bang on about all that boring stuff would be worth it.)"
            $ current_thought = "barbara_thought_pr_30"
            jack smug "Can I have a whiskey? With all of the discounts applied, of course."
            $ swap_sprites("barbara_smiling")
            bartender "Sure! Just so you know, there aren’t any discounts for it, so that’ll be $14." 
            $ current_thought = "barbara_thought_pr_31"
            $ play_music("tense_1")
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
            jack smug "(Alright, there’s no way that this can go wrong.[wait_1] That drink is as good as mine.)"
            $ current_thought = "barbara_thought_pr_33"
            jack smug "How about you give me a drink with a bit of a discount?[wait_1] As a bit of a treat, for one of your regulars?"
            $ current_thought = "barbara_thought_pr_34"
            $ swap_sprites("barbara_angry")
            $ play_music("tense_1")
            bartender "Interesting idea, although that’s not actually a policy that I run here." 
            $ current_thought = "barbara_thought_pr_35"
            jack smug "Oh come now - you don’t want to reward your loyal customers?[wait_1] The people who are basically paying your wages for you?"
            $ current_thought = "barbara_thought_pr_36"
            bartender "Sorry, but it doesn’t work that way."  
            bartender "So are you going to order a drink - at its full price - or not?" 
            $ current_thought = "barbara_thought_pr_37"
            jack angry "(This is bullshit - what was wrong with that argument?!)" 
            jack angry "(I’d better rewind her mind and try something different.)"
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
    jack thinking "(Well obviously.[wait_1] The faster I drink it, the faster I’ll get drunk.)"
    $ current_thought = "barbara_thought_pr_46"
    jack smug "Well, it wasn’t bad.[wait_1] But I think I’d probably have a better opinion if I could have a follow-up...?"
    bartender "Heh, nice try, but one freebie’s all that I can give you."
    bartender "Technically I shouldn’t have even done that, but I doubt it’ll make that much difference in the long run."
    jack angry "(Bloody typical - you ask for one small favour and they act like you’re asking for the world.[wait_1] Only out for herself, just like everybody else.)"
    $ current_thought = "barbara_thought_pr_47"
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
    $ rewind_point = "prologue_montage_rewind"
    
    $ current_thought = "barbara_thought_pr_38"
    jack smug "Tell me - how would you feel about a bit of an exchange?[wait_1] A free drink, and in return I’ll make sure to write a good review."
    jack smug "(Just one more drink, that’s all.[wait_1] Get a nice buzz going, and then I’ll be on my way.)"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(5, 2, 1.15) with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_41"
    bartender "Is it - are you sure that it’s alright, though?"
    jack smug "Are you alright with getting more customers?[wait_1] Because if so, then you’d better get pouring!"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(10, 4, 1.15) with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_48"
    bartender "Is it - are you sure that it’s alright, though?"
    jack smug "Only if you’re -[wait_05] if you’re -[wait_05] if you want lots of customers here![wait_1] It’s -[wait_05] it’s a good bar, isn’t it?"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(15, 6, 1.15) with quick_dissolve
    $ swap_sprites("barbara_thinking", quick_dissolve)
    $ current_thought = "barbara_thought_pr_49"
    bartender "Is it - are you sure that it’s alright, though?"
    $ current_thought = "barbara_thought_pr_50"
    jack smug "Yeah![wait_1] I -[wait_05] I like -[wait_05] this bar is great![wait_1] Even if you do water down the drinks!"
    $ swap_sprites("barbara_angry")
    bartender "What?"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(20, 8, 1.25) with quick_dissolve
    $ swap_sprites("barbara_angry", quick_dissolve)
    $ current_thought = "barbara_thought_pr_51"
    $ play_music("tense_1")
    bartender "I’m sorry, but - no, I can’t do that."
    bartender "You’re quite clearly drunk, and it wouldn’t be responsible of me to serve you any alcohol in your state."
    $ current_thought = "barbara_thought_pr_52"
    jack smug "What?[wait_1] But I -[wait_05] I can review you![wait_1] You -[wait_05] you normally like that!"
    $ current_thought = "barbara_thought_pr_53"
    bartender "I’d rather give up the most positive review in the world than give alcohol to somebody so obviously drunk."
    bartender "Sorry, but I’m going to have to ask you to leave."
    jack angry "(Oh, screw you![wait_1] I’ll -[wait_05] let’s see how drunk you think I am after this)"
    $ rewind_point = "prologue_10"
    hide screen conversation_history
    call screen psychic_powers

label prologue_10:
    show screen conversation_history
    show screen psychic_powers
    $ current_thought = "barbara_thought_pr_54"
    bartender "Are you trying to do something?"
    jack angry "(Dammit...[wait_05]she -[wait_05] she must have put something in the drinks...[wait_05]it’s affected my powers!)"
    $ current_thought = "barbara_thought_pr_55"
    jack worried "How -[wait_05] how did you know?[wait_1] You -[wait_05] you shouldn’t know...[wait_05]you couldn’t know..."
    bartender "I have no clue what you’re talking about, but that’s enough.[wait_1] Get out of my bar."
    scene black_bg with quick_dissolve

label prologue_11:
    hide screen psychic_powers
    $ _history_list = []
    $ play_music("ambient_1")
    jack angry "(Whaddo I care about what she thinks anyway...[wait_1]she’s not even that good a bartender!)"
    jack angry "(Anyway, there’s better places to go to around here...I bet it’ll be easier to get free shit there, too.)"
    hide screen conversation_history
    call screen modal_popup("You have enough time to visit one more location before the night is over.", ["OK"], [Return()])
    call screen map_navigation(find_locations([1, 2]))

label prologue_music_venue:
    $ scene_setup(33, "Monday", True, 2, 2, True, True)
    $ play_music("neutral_2")
    $ location = "music_venue"
    scene black_bg with slow_dissolve
    jack smug "(Right...[wait_05]I - I know what I’ve gotta do.)"
    jack smug "(I’ll just - just go up to the door, and then I’ll make ‘em - I’ll make the door person forget that I haven’t paid the fee.)"
    jack smug "(Then I can - I’ll go inside, and I’ll - I’ll get stuff for free.)"
    jack smug "(Yeah...[wait_05]yeah, that’s a good idea! I like this plan!)"
    jack worried "(God, my head is pounding...[wait_05]but it’s still not as - as bad as how it felt when my powers first emerged.)"
    jack worried "(I - I still don’t know why I got them, or how, but I’m glad that I’ve got - that I have them.)"
    jack smug "(I’ve got big plans in the future...[wait_05]just need s’more money...)"
    scene venue_exterior at drunk_cycle(5, 0, 1.0) with slow_dissolve
    jack angry "(There’s the door guy...[wait_05]why couldn’t it be a sexy woman on the door?[wait_1] Give us something to - to look at while we’re going in...)"
    jack angry "(Y’know, if I was a doorman, I’d let anybody in for free.[wait_1] It’s not fair how we have to -)"
    call prologue_precognition from prologue_music
    scene venue_exterior at drunk_cycle(5, 0, 1.0) with quick_dissolve
    jump prologue_end

label prologue_restaurant:
    $ scene_setup(33, "Monday", True, 2, 2, True, True)
    $ play_music("neutral_2")
    scene black_bg with slow_dissolve
    $ location = "restaurant"
    jack worried "(I feel kind of dizzy, and - and the street is moving too much, but it’s not that far from here.)"
    jack worried "(I can definitely make - make it there.)"
    jack thinking "(I - I hope that my powers are working when I get there...[wait_1]I need them so I can get those chips.)"
    jack thinking "(They should - they should lower their prices anyway, cos chips are - chips are - they’re too expensive. But they don’t wanna do that, cos they - they just wanna make money.)"
    jack thinking "(All they care about is themselves, and - and their profits and stuff...[wait_1]they’re just like that bartender.[wait_1] Everybody only cares about themselves.)"
    jack worried "(Anyway, I’d - I’d pay for stuff if I had the money, but I don’t, since I had to - I gave all that I had to that guy.)"
    jack worried "(He’s soooo expensive...[wait_1]got the info I wanted, but did he - did he have to cost so much?)"
    scene restaurant_night at drunk_cycle(5, 0, 1.0) with slow_dissolve
    jack worried "(They’d better have some tables left inside...[wait_1]it’s so cold out here...)"
    jack smug "(Although if they don’t, I can - I can make somebody go outside.[wait_1] They wouldn’t know that I -)"
    call prologue_precognition from prologue_restaurant_
    scene restaurant_night at drunk_cycle(5, 0, 1.0) with slow_dissolve
    jump prologue_end

label prologue_precognition:
    scene black_bg
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
    jack thinking "(No...[wait_05]it’s -[wait_05] whatever’s happened, it’s -[wait_05] it hasn’t happened yet.)"
    jack thinking "(It’s my -[wait_05] it’s my precog-[wait_05] precog-[wait_05] my future sight.)"
    jack thinking "(I -[wait_05] if I go in that building then it’ll...[wait_05]it’ll happen and I’ll...[wait_05]the vision will come true.)"
    jack worried "(Somebody will shoot me and -[wait_05] god, why did I drink so -[wait_05] so much?)"
    jack worried "(I -[wait_05] I can’t -[wait_05] I don’t want to die![wait_1] Can I even -[wait_05] is it even possible for me to get away?)"
    jack worried "(I don’t have control over the -[wait_05] over my future sight, so I can’t see if there’s a way that I survive.)"
    jack thinking "(I...[wait_05]I need to calm down.[wait_1] I can do this.)"
    jack thinking "(I just need to -[wait_05] I need to not go into that building, and then I’ll -[wait_05] yeah, I’ll be fine.)"
    jack thinking "(If I just keep moving then I’ll -[wait_05] I can get away.)"
    scene black_bg with quick_dissolve
    $ play_sound("gunshot.mp3", transition=white_flash)
    jack worried "(Argh![wait_1] I’m -[wait_05] I got the vision again!)"
    jack worried "(My gut hurts so much, and I don’t think -[wait_05] no![wait_1] I -[wait_05] I can get away![wait_1] I can!)"
    $ play_sound("gunshot.mp3", transition=white_flash)
    jack worried "(No...[wait_05]not here!)"
    jack worried "(Maybe...[wait_05]if I turn around...)"
    $ play_sound("gunshot.mp3", transition=white_flash)
    jack worried "(No...[wait_05]no...[wait_05]where can I go...?)"
    jack worried "(Everywhere I go I get the sensation -[wait_05] the -[wait_05] the gunshot...)"
    jack worried "(But there’s got to be a way out...[wait_05]there’s got to be!)"
    $ scene_setup(10, "Monday", True, 2, 2, True, True)
    scene street at drunk_cycle(5, 0, 1.1) with slow_dissolve
    jack worried "(Have I -[wait_05] have I been here before?[wait_1] I don’t -[wait_05] everything’s mixing together.)"
    jack thinking "(Why are they -[wait_05] who would want to hurt me?[wait_1] I -[wait_05] I’ve never even hurt a fly!)"
    $ rewind_point = "prologue_docherty_wipe"
    $ swap_sprites("docherty_neutral", quick_dissolve)
    show screen psychic_powers
    $ current_thought = "docherty_thought_pr_1"
    jack worried "You...[wait_05]can you -[wait_05] can you help me?[wait_1] Please!"
    jack worried "There’s -[wait_05] somebody’s after me, and they’re -[wait_05] I -[wait_05] I don’t know if I can get away without some help."
    jack worried "Do you -[wait_05] do you have a car, or...?"
    docherty "I apologise for this, young man, but you are in the way of my plan."
    jack angry "What do you -"
    hide screen calendar
    hide screen conversation_history
    hide screen psychic_powers
    $ play_sound("gunshot.mp3", transition=white_flash)
    scene cg1_placeholder with slow_dissolve
    $ unlock_cg(0, 1)
    jack worried "(No...[wait_05]no!)"
    jack worried "(I -[wait_05] I can't die!)"
    jack worried "(I just wanted to -[wait_05] please, somebody...[wait_05]help me...)"
    scene black_bg with slow_dissolve

    $ MainMenu(confirm=False)()