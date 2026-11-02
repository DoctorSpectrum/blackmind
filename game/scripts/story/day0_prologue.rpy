label prologue_01:
    $ quick_menu = False

    $ renpy.music.stop()
    scene black_bg
    show cg1_0 at cg_1_teaser
    $ unlock_cg(0, 0)
    $ docherty_partial("calm_01")
    docherty "I apologise for this, young man, but you are in the way of my plan." (name="???")
    hide cg1_0
    show cg1_1
    $ play_sound("gunshot.mp3", pause=0.75, transition=white_flash)
    $ unlock_cg(0, 1)
    hide cg1_1 with quick_dissolve
    call screen chapter_breaks("PROLOGUE", "A young man has just been released from police custody. He is trying to work out where best to use his psychic powers.\n\nElsewhere, another man is loading bullets into a gun.")
    $ quick_menu = True

    $ play_music("neutral_1")
    scene street with slow_dissolve
    $ scene_setup(16, "Monday", True, 1, 2, True, True)
    $ current_thought_block = "mind_read_prologue"

    $ jack_partial("irritated_01")
    jack angry "(God, it took the cops long enough to let me go.)"
    jack angry "(Absolutely no evidence at all that I stole those wallets, but they still managed to draw it out into hours of questioning.)"
    $ jack_partial("dismissive_02")
    jack angry "(What’s the big deal, anyway?)"
    jack angry "(Pickpocketing’s considered a petty crime.[wait_1] That basically means that they shouldn’t be wasting any time on it, especially when they’ve got no evidence.)"
    $ jack_partial("cocky_01")
    jack smug "(Anyway, how much cash was I able to get from those suckers before the cops spotted me?)"
    $ jack_partial("irritated_02")
    jack thinking "(Damn, practically nothing...it'd be easier if I could take plastic, but it’s just too easy to trace or be blocked.)"
    $ jack_partial("dismissive_01")
    jack smug "(Well, whatever.[wait_1] Not like I need any of it to get myself a whiskey.)"
    scene black_bg with quick_dissolve
    
    scene bar with slow_dissolve
    $ jack_partial("confused_01")
    jack thinking "(Is there no bartender here?[wait_1] And...also no customers?)"
    $ jack_partial("friendly_01")
    jack thinking "Hello![wait_1] Anybody home?"
    jack smug "(I’ll give it thirty seconds, then I’m grabbing all the bottles I can hold.)"
    jack smug "(They probably want people to do that anyway.[wait_1] You wouldn’t just leave things unattended and then be annoyed that they’re missing; you know what you’re getting in for.)"
    $ swap_sprites("barbara_smiling", slow_dissolve)
    $ current_thought = "barbara_thought_pr_01"
    $ barbara_partial("apologetic_01")
    bartender "Sorry![wait_1] I was out back, changing over a keg."
    $ barbara_partial("friendly_01") 
    bartender "How are you doing?" 
    $ jack_partial("friendly_01")
    jack smug "Not too bad, although I’d definitely be doing better if I had a drink...[wait_05]or two!"
    $ jack_partial("cocky_01")
    jack smug "(God I'm funny!)"
    $ barbara_partial("friendly_02")
    bartender "I can help you out with that.[wait_1] What exactly were you hoping for?"

label prologue_02:
    $ hide_history()
    if (history_expanded):
        $ renpy.notify("history expanded")
    menu:
        "Whiskey":
            $ show_history()
            $ jack_partial("dismissive_02")
            jack worried "(There’s no point in looking at the prices she’s got - it’ll all be overpriced, just like every other bloody place.)"
            $ jack_partial("irritated_01")
            jack worried "(Who’s out there making things affordable for the little guy?[wait_1] Nobody, that’s who.)"
            jack thinking "(So when you think about it, is it really an issue if I use my abilities and trick her into giving me a drink for free?[wait_1] Obviously not.)"
            $ jack_partial("dismissive_02")
            jack thinking "(She’ll definitely make all that money back when the first fat cat of the night steps in {size=-10}maybe{/size}.)"
            $ jack_partial("analytical_01")
            jack smug "(I’ll just need to convince her that she’ll benefit from pouring me that drink.)"
            jack smug "(What’s she thinking about right now?)"

            hide screen say
            $ hide_history()
            $ add_boolean("psychic_powers_available")
            if (current_input == "KB"):
                call screen modal_popup("{image=gui/icons/mind_read_icon_idle.png}\r\n\r\nClick on the Read Mind button in the top right-hand corner, or press the 1 key, to read the bartender’s mind.")
            elif (current_input == "GP"):
                call screen modal_popup("{image=gui/icons/mind_read_icon_idle.png}\r\n\r\nClick on the Read Mind button in the top right-hand corner, or press left on the D-Pad, to read the bartender’s mind.")
            else:
                call screen modal_popup("{image=gui/icons/mind_read_icon_idle.png}\r\n\r\nClick on the Read Mind button in the top right-hand corner, or press the 1 key/left on the D-Pad, to read the bartender’s mind.")
            call screen psychic_powers

        "Lemonade":
            $ show_history()
            $ jack_partial("cocky_01")
            jack smug "(Ha ha ha.)"
            $ jack_partial("irritated_02")
            jack angry "(No.)"
            jump prologue_02
        "Whiskey" (locked=True, message="You cannot legally afford this drink"):
            jump prologue_02

label prologue_03:
    if (check_boolean("reread_thought_tutorial") == False):
        $ add_boolean("reread_thought_tutorial")
        call screen modal_popup("{image=gui/icons/mind_read_icon_idle.png}\r\n\r\nThe Read Mind icon will appear in the text box to indicate when you have read the current thought. You can click on the button to re-read that thought.")
    $ jack_partial("cheerful_01")
    jack thinking "(She’s happy to give me what I want?[wait_1] This bar is fucking amazing!)"
    $ current_thought = "barbara_thought_pr_02"
    $ jack_partial("friendly_01")
    jack thinking "You’re good to give me a glass of whiskey, yeah?"
    $ barbara_partial("friendly_02")
    bartender "And coke?[wait_1] Sure thing - just tap your card when you’re ready and I’ll be right with you." 
    $ current_thought = "barbara_thought_pr_03"
    $ jack_partial("irritated_01")
    jack angry "Tap my - what do you mean?[wait_1] I thought you were going to give me it for free!"
    $ swap_sprites("barbara_angry")
    $ barbara_partial("angry_02")
    bartender "And why the hell would I do that?" 
    $ current_thought = "barbara_thought_pr_04"
    $ jack_partial("angry_01")
    jack angry "You thought it![wait_1] Don’t try and deny it, I know you did!"
    $ barbara_partial("angry_01")
    bartender "What the hell?![wait_1] Just - who the hell are you?" 
    $ jack_partial("scared_01")
    jack worried "(Shit![wait_05] I shouldn’t have said that - I’d better wipe that from her memory!)"
    hide screen say
    $ hide_history()
    $ rewind_point = "prologue_04"
    $ add_boolean("mind_wipe_available")
    if (current_input == "KB"):
        call screen modal_popup("{image=gui/icons/mind_wipe_icon_idle.png}\r\n\r\nClick on the Rewind Mind button, or press the 2 key, to make the bartender forget the last few minutes of conversation.")
    elif (current_input == "GP"):
        call screen modal_popup("{image=gui/icons/mind_wipe_icon_idle.png}\r\n\r\nClick on the Rewind Mind button, or press up on the D-Pad, to make the bartender forget the last few minutes of conversation.")
    else:
        call screen modal_popup("{image=gui/icons/mind_wipe_icon_idle.png}\r\n\r\nClick on the Rewind Mind button, or press the 2 key/up on the D-Pad, to make the bartender forget the last few minutes of conversation.")
    call screen psychic_powers

label prologue_04:
    show screen psychic_powers
    if (renpy.music.get_playing() != "audio/music/bourbon_mood.mp3"):
        $ play_music("neutral_1")

    $ remove_boolean("prologue_interior_designing_2")
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_pr_05"
    $ barbara_partial("dazed_01")
    bartender "Urgh...[wait_05]my head..."
    $ barbara_partial("confused_01") 
    bartender "I - sorry mate, I was out back, changing over a keg.[wait_1] At least...[wait_05]that’s what I thought I was doing." 
    $ current_thought = "barbara_thought_pr_06"
    $ swap_sprites("barbara_smiling")
    $ barbara_partial("friendly_01")
    bartender "How are you doing?" 
    if (check_boolean("jack_tutorial_psychic_explanation") == False):
        $ jack_partial("cocky_01")
        jack thinking "(If I use my psychic abilities correctly, I can definitely trick her into giving me something for free.)"
        $ jack_partial("analytical_01")
        jack thinking "(The best way to do that is by using my precog – my precon – my future vision to see what I need to focus on.)"
        $ add_boolean("jack_tutorial_psychic_explanation")
    if (current_input == "KB"):
        call screen modal_popup("{image=gui/icons/future_sight_icon_idle.png}\r\n\r\nClick on the Future Sight button, or press the 3 key, to activate your future sight.")
    elif (current_input == "GP"):
        call screen modal_popup("{image=gui/icons/future_sight_icon_idle.png}\r\n\r\nClick on the Future Sight button, or press right on the D-Pad, to activate your future sight.")
    else:
        call screen modal_popup("{image=gui/icons/future_sight_icon_idle.png}\r\n\r\nClick on the Future Sight button, or press the 3 key/right on the D-Pad, to activate your future sight.")
    $ add_boolean("future_sight_available")
    call screen psychic_powers

    jack thinking "(My future sight showed me the word {b}ALCOHOL{/b}. If I focus on comments related to that, I should make some progress.)"
    $ rewind_point = "prologue_05"

label prologue_05:
    show screen psychic_powers
    $ current_thought = "barbara_thought_pr_07"
    bartender "You still with me, mate?[wait_1] You’ve gone kind of quiet."
    $ current_thought = "barbara_thought_pr_08"
    bartender "Do you know what you want to have to drink?"
    $ current_thought = "barbara_thought_pr_09"
    bartender "If not, I can come back once you’ve decided."

    menu:
        "I want a whiskey":
            jack smug "‘Course I know what I want:[wait_05] a whiskey!"
            $ current_thought = "barbara_thought_pr_10"
            bartender "Sure thing![wait_1] Just tap your card while I get it ready!"
            jack worried "(Wait...the whole point of this was to trick her into giving me a drink for free.[wait_1] Just asking for one won’t do it.)"
            jack worried "(I need to make her forget this, then use my future vision. [wait_1]That’ll help get me to where I want.)"
            call screen psychic_powers
        "Talk about the bar" (locked=not check_boolean("prologue_bar_interested"), message="Read the thought related to alcohol to unlock this option"):
            $ person = "barbara_prologue_02"
            $ add_boolean("call_future_sight")
            $ add_boolean("future_sight_types")
            call screen modal_popup("You’ve managed to move a little further to your goal, but Jack won’t be getting a free drink just yet. Use your future vision again to see what keywords will help you proceed.")
            call screen psychic_powers

label prologue_06:
    show screen psychic_powers
    $ rewind_point = "prologue_06"
    $ current_thought = "barbara_thought_pr_11"
    $ jack_partial("cheerful_01")
    jack smug "You know, your boss has done a really nice job with the place."
    $ current_thought = "barbara_thought_pr_12"
    jack smug "In particular, he’s really good at hiring staff."
    $ swap_sprites("barbara_angry")
    $ current_thought = "barbara_thought_pr_13"
    $ barbara_partial("irritated_01")
    bartender "As a matter of fact, I’m the owner."
    $ current_thought = "barbara_thought_pr_14"
    $ jack_partial("cocky_03")
    jack smug "Oh, really?[wait_05] Like I said, you’ve done a great job with it - I love the aesthetic you’ve got going."
    $ jack_partial("confused_02")
    jack worried "(What the hell is the name of this style?[wait_1] The only one I know is gothic, and it definitely isn’t that.)"
    $ current_thought = "barbara_thought_pr_15"
    jack smug "It's a very...[wait_05] ...[wait_05] ...gothic style, if I'm not mistaken?"
    $ barbara_partial("irritated_02")
    bartender "You are mistaken, but that’s neither here nor there."
    bartender "Anyway, did you want a drink?" 

label prologue_07:
    $ hide_history()
    menu:
        "No":
            $ show_history()
            $ current_thought = "barbara_thought_pr_16"
            $ play_music("tense_1")
            $ jack_partial("dismissive_01")
            jack angry "At the prices you’re offering?[wait_1] No thanks."
            $ barbara_partial("angry_02")
            bartender "Then what are you even doing here?!" 
            $ jack_partial("confused_02")
            jack worried "Um..."
            jack worried "(What, exactly, was I thinking with that, again?)"
            $ current_thought = "barbara_thought_pr_17"
            $ barbara_partial("irritated_03")
            bartender "If you’re not ordering, then please leave.[wait_1] I’ve got better things to do than entertain beggars." 
            $ jack_partial("analytical_03")
            jack thinking "(Okay, so I’ll need to read more of her thoughts so that I can work out what she might want to talk about, to get her to like me more.)"
            jack thinking "(First of all I’ll need to rewind her mind, though.)"
            $ hide_history()
            call screen psychic_powers
        "Talk about the history of the bar" (locked=not check_boolean("prologue_bar_history"), message="You have not read this information in the bartender's mind"):
            $ show_history()
            $ jack_partial("dismissive_01")
            jack smug "Oh, of course, of course."
            jump prologue_08
        "Talk about interior design" (locked=not check_boolean("prologue_interior_designing"), message="You have not read this information in the bartender's mind"):
            $ show_history()
            $ current_thought = "barbara_thought_pr_18"
            $ jack_partial("cocky_03")
            jack smug "What I really wanted was to talk about interior design."
            jack smug "I think that your work is...[wait_1]beautiful, really.[wait_1] Really beautiful, yeah."
            if (check_boolean("prologue_interior_designing_2") == False):
                $ swap_sprites("barbara_smiling")
                $ barbara_partial("proud_01")
                bartender "Oh, thank you![wait_1] But it’s not actually my work - I just hired an interior designer for it." 
                $ current_thought = "barbara_thought_pr_19"
                $ jack_partial("confused_02")
                jack thinking "What?[wait_05] But you wanted to teach me a lesson or two about it.[wait_05] That’s what you thought before."
                $ swap_sprites("barbara_thinking")
                $ current_thought = "barbara_thought_pr_20"
                $ barbara_partial("confused_01")
                bartender "I’m...[wait_05]not sure what exactly to tell you.[wait_1] My job is running a bar, not doing interior design." 
                $ swap_sprites("barbara_smiling")
                $ barbara_partial("friendly_02")
                bartender "And on that note - you never answered me when I asked before."
                bartender "Did you want a drink?" 
                $ add_boolean("prologue_interior_designing_2")
                jump prologue_07
            else:
                $ swap_sprites("barbara_smiling")
                $ barbara_partial("cheerful_02")
                bartender "Yes, I heard you the first time."
                $ barbara_partial("friendly_01") 
                bartender "But you still haven’t answered my question - do you want a drink?" 
                jump prologue_07

label prologue_08:
    show screen psychic_powers
    $ rewind_point = "prologue_08"
    $ current_thought = "barbara_thought_pr_21"
    if (renpy.music.get_playing() != "audio/music/bourbon_mood.mp3"):
        $ play_music("neutral_1")
    
    $ jack_partial("cocky_02")
    jack smug "How could I be in such a...[wait_05]historic place and not want to have a drink?"
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_pr_22"
    $ barbara_partial("cheerful_01")
    bartender "You’ve heard of our bar before, then?" 
    $ current_thought = "barbara_thought_pr_23"
    $ jack_partial("confused_02")
    jack worried "\"Our\" bar?"
    $ current_thought = "barbara_thought_pr_24"
    $ barbara_partial("proud_01")
    bartender "Oh, this bar has been in my family for three generations now." 
    $ barbara_partial("cheerful_01")
    bartender "Although I’ve only been running it for the last...[wait_05]I want to say eight months?" 
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_pr_25"
    $ barbara_partial("proud_01")
    bartender "Which doesn’t sound like a lot, but I’ve got a lot of good ideas about how to make it even better!"
    bartender "Before you know it, this will be your favourite bar in the area - no, in the city!" 
    $ current_thought = "barbara_thought_pr_26"
    $ barbara_partial("friendly_02")
    bartender "In fact, I can start out by showing you how good our drinks are - what exactly did you want to drink, again?" 

    $ hide_history()
    menu:
        "Nothing":
            $ show_history()
            $ play_music("tense_1")
            $ current_thought = "barbara_thought_pr_27"
            $ jack_partial("dismissive_02")
            jack smug "Oh, no need to worry about it.[wait_1] I’m not looking to drink anything."
            $ swap_sprites("barbara_angry")
            $ barbara_partial("irritated_03")
            bartender "Then why, exactly, did you come in here?" 
            $ current_thought = "barbara_thought_pr_28"
            $ jack_partial("confused_02")
            jack worried "Uh..."
            jack worried "(I had something I wanted to say here...[wait_05]didn’t I?)"
            $ current_thought = "barbara_thought_pr_29"
            $ jack_partial("confused_01")
            jack worried "To...[wait_05]talk to you?"
            $ barbara_partial("irritated_02")
            bartender "I’m flattered, but please - just leave." 
            $ jack_partial("analytical_03")
            jack thinking "(I’ll wipe her memory of this part of the conversation, and try this again...)"
            jack thinking "(I need to start nudging her towards the idea of free drinks, or I’ll never get anywhere.)"
            $ hide_history()
            call screen psychic_powers
        "That depends upon your drinks policies" (locked=not check_boolean("prologue_drink_policies"), message="You have not read information about the bar's drinks policies in her mind"):
            jump prologue_09

label prologue_09:
    $ show_history()
    show screen psychic_powers
    $ rewind_point = "prologue_09"
    if (renpy.music.get_playing() != "audio/music/bourbon_mood.mp3"):
        $ play_music("neutral_1")

    $ current_thought = "barbara_thought_pr_30"
    $ jack_partial("cocky_03")
    jack smug "I'd like to know a bit about your drink policies first."
    $ current_thought = "barbara_thought_pr_31"
    jack smug "Got any happy hour specials, or other discounts for me?"
    $ current_thought = "barbara_thought_pr_32"
    $ barbara_partial("apologetic_01")
    bartender "Happy hour ended at six o’clock, sorry." 
    $ barbara_partial("friendly_02")
    $ current_thought = "barbara_thought_pr_33"
    bartender "So with that in mind, how can I help you?" 
    $ hide_history()

    menu:
        "Give me a whiskey":
            $ show_history()
            $ jack_partial("analytical_02")
            jack smug "(It sounds like she’s pretty keen to give me it for cheaper - I knew that listening to her bang on about all that boring stuff would be worth it.)"
            $ current_thought = "barbara_thought_pr_34"
            $ jack_partial("friendly_01")
            jack smug "Can I have a whiskey? With all of the discounts applied, of course."
            $ swap_sprites("barbara_smiling")
            $ barbara_partial("cheerful_02")
            bartender "Sure! Just so you know, there aren’t any discounts for it, so that’ll be $14." 
            $ current_thought = "barbara_thought_pr_35"
            $ play_music("tense_1")
            $ jack_partial("angry_01")
            jack angry "What?![wait_1] This is bullshit, you’re not willing to give me even a little bit off the top?"
            $ swap_sprites("barbara_angry")
            $ current_thought = "barbara_thought_pr_36"
            $ barbara_partial("angry_02")
            bartender "What for?[wait_1] If that’s going to be the way you want it, then I’ll do you one better and ask you to get out - right now."
            $ jack_partial("disappointed_01")
            jack thinking "(If I do that, then I won’t get any of that lovely booze...)"
            $ jack_partial("analytical_03")
            jack thinking "(I guess I’ll need a good reason why she should give me a discount, since apparently I’m not good enough for her.)"
            jack thinking "(Let’s rewind her mind and try again.)"
            $ hide_history()
            call screen psychic_powers
        "How about you give me a discount since I’m a regular?" (locked=not check_boolean("prologue_drink_discounts"), message="You have not read information about discounts in the bartender's mind"):
            $ show_history()
            $ jack_partial("cocky_01")
            jack smug "(Alright, there’s no way that this can go wrong.[wait_1] That drink is as good as mine.)"
            $ current_thought = "barbara_thought_pr_37"
            $ jack_partial("cocky_03")
            jack smug "How about you give me a drink with a bit of a discount?[wait_1] As a bit of a treat, for one of your regulars?"
            $ current_thought = "barbara_thought_pr_38"
            $ swap_sprites("barbara_angry")
            $ play_music("tense_1")
            $ barbara_partial("irritated_02")
            bartender "Interesting idea, although that’s not actually a policy that I run here." 
            $ current_thought = "barbara_thought_pr_39"
            $ jack_partial("cocky_02")
            jack smug "Oh come now - you don’t want to reward your loyal customers?[wait_1] The people who are basically paying your wages for you?"
            $ current_thought = "barbara_thought_pr_40"
            $ barbara_partial("irritated_02")
            bartender "Sorry, but it doesn’t work that way."
            bartender "So are you going to order a drink - at its full price - or not?" 
            $ current_thought = "barbara_thought_pr_41"
            $ jack_partial("irritated_02")
            jack angry "(This is bullshit - what was wrong with that argument?!)" 
            $ jack_partial("analytical_01")
            jack angry "(I’d better rewind her mind and try something different.)"
            $ hide_history()
            call screen psychic_powers
        "I’ll write a good review if you give me a free drink" (locked=not check_boolean("prologue_drink_review"), message="You have not read information about the bar's publicity in the bartender's mind"):
            $ show_history()
            $ current_thought = "barbara_thought_pr_42"
            $ jack_partial("cocky_01")
            jack smug "Tell me - how would you feel about a bit of an exchange?[wait_1] A free drink, and in return I’ll make sure to write a good review."
            $ swap_sprites("barbara_thinking")
            $ current_thought = "barbara_thought_pr_43"
            $ barbara_partial("confused_02")
            bartender "You mean...[wait_05]for a blog or something, right?[wait_1] Or a - a Google review?" 
            $ jack_partial("cocky_03")
            jack smug "Let me put it this way:[wait_05] I’m not supposed to name any names, but I’m thinking of a magazine right now, and it’s definitely one that you’ve heard before."
            jack thinking "(That’s not a lie.[wait_05] I’m thinking of a magazine, but I never explicitly said that I worked for them.)"
            $ jack_partial("dismissive_02")
            jack thinking "(It’s not my fault if she misinterprets that.)"
            $ swap_sprites("barbara_smiling")
            $ current_thought = "barbara_thought_pr_44"
            $ barbara_partial("excited_01")
            bartender "Well I - if you really are working for someone big, then I - yeah, I - a review would be - yes please!" 
            $ current_thought = "barbara_thought_pr_45"
            bartender "Is it - are you sure that it’s alright, though?" 
            $ jack_partial("cocky_01")
            jack smug "Only if you’re alright with getting flooded with customers after they hear what I have to say about this place.[wait_1] Ha!"
            $ jack_partial("dismissive_02")
            jack smug "(It’s fine.[wait_05] I’ll just get her to give me a single free drink, then I’ll definitely be heading off.)"
            jack smug "(It’s not like I’m going to exploit this or anything.)"
            $ current_thought = "barbara_thought_pr_46"
            $ barbara_partial("friendly_01")
            bartender "Well in that case - what exactly can I get you?" 
            $ current_thought = "barbara_thought_pr_47"
            $ jack_partial("cocky_03")
            jack smug "How about a whiskey and coke?[wait_1] That'd really wet my whistle."
            $ barbara_partial("friendly_02")
            bartender "Coming right up!"

label prologue_10:
    scene black_bg with quick_dissolve
    $ play_sound("ice_cube_clink.mp3")
    $ current_thought = "barbara_thought_pr_48"
    $ jack_partial("irritated_01")
    jack thinking "(I’ve definitely had better, and I bet she’s probably watered this down, just like every other bloody bar.)"
    $ jack_partial("dismissive_01")
    jack thinking "(But I guess if I was a reviewer, I’d pretend to like it.)"
    scene bar with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_49"
    $ barbara_partial("friendly_01")
    bartender "How was it?[wait_05] You certainly looked like you enjoyed it; you drank it quickly enough!"
    $ jack_partial("irritated_01")
    jack thinking "(Well obviously.[wait_1] The faster I drink it, the faster I’ll get drunk.)"
    $ current_thought = "barbara_thought_pr_50"
    $ jack_partial("cocky_02")
    jack smug "Well, it wasn’t bad.[wait_1] But I think I’d probably have a better opinion if I could have a follow-up...?"
    $ barbara_partial("amused_01")
    bartender "Heh, nice try, but one freebie’s all that I can give you."
    $ barbara_partial("apologetic_01")
    bartender "Technically I shouldn’t have even done that, but I doubt it’ll make that much difference in the long run."
    $ jack_partial("irritated_01")
    jack angry "(Bloody typical - you ask for one small favour and they act like you’re asking for the world.[wait_1] Only out for herself, just like everybody else.)"
    $ current_thought = "barbara_thought_pr_51"
    $ jack_partial("analytical_01")
    jack smug "(Well, luckily for me, I have a nice solution for that...)"
    $ rewind_point = "prologue_11"
    $ hide_history()
    call screen psychic_powers

label prologue_montage_rewind:
    $ jack_partial("analytical_01")
    jack smug "(No need to do that quite yet - I haven’t gotten the next drink yet!)"
    return

label prologue_11:
    $ show_history()
    show screen psychic_powers
    $ rewind_point = "prologue_montage_rewind"
    
    $ current_thought = "barbara_thought_pr_42"
    $ jack_partial("cocky_01")
    jack smug "Tell me - how would you feel about a bit of an exchange?[wait_1] A free drink, and in return I’ll make sure to write a good review."
    jack smug "(Just one more drink, that’s all.[wait_1] Get a nice buzz going, and then I’ll be on my way.)"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(5, 2, 1.15) with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_45"
    $ barbara_partial("excited_02")
    bartender "Is it - are you sure that it’s alright, though?"
    $ jack_partial("friendly_01")
    jack smug "Are you alright with getting more customers?[wait_1] Because if so, then you’d better get pouring!"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(10, 4, 1.15) with quick_dissolve
    $ swap_sprites("barbara_smiling", quick_dissolve)
    $ current_thought = "barbara_thought_pr_52"
    $ barbara_partial("excited_02")
    bartender "Is it - are you sure that it’s alright, though?"
    $ jack_partial("cocky_01")
    jack smug "Only if you’re -[wait_05] if you’re -[wait_05] if you want lots of customers here![wait_1] It’s -[wait_05] it’s a good bar, isn’t it?"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(15, 6, 1.25) with quick_dissolve
    $ swap_sprites("barbara_thinking", quick_dissolve)
    $ current_thought = "barbara_thought_pr_53"
    $ barbara_partial("excited_02")
    bartender "Is it - are you sure that it’s alright, though?"
    $ current_thought = "barbara_thought_pr_54"
    $ jack_partial("cocky_02")
    jack smug "Yeah![wait_1] I -[wait_05] I like -[wait_05] this bar is great![wait_1] Even if you do water down the drinks!"
    $ swap_sprites("barbara_angry")
    $ barbara_partial("irritated_03")
    bartender "What?"
    scene black_bg with quick_dissolve
    scene bar at drunk_cycle(20, 8, 1.25) with quick_dissolve
    $ swap_sprites("barbara_angry", quick_dissolve)
    $ current_thought = "barbara_thought_pr_55"
    $ play_music("tense_1")
    $ barbara_partial("irritated_02")
    bartender "I’m sorry, but - no, I can’t do that."
    bartender "You’re quite clearly drunk, and it wouldn’t be responsible of me to serve you any alcohol in your state."
    $ current_thought = "barbara_thought_pr_56"
    $ jack_partial("confused_02")
    jack smug "What?[wait_1] But I -[wait_05] I can review you![wait_1] You -[wait_05] you normally like that!"
    $ current_thought = "barbara_thought_pr_57"
    $ barbara_partial("irritated_02")
    bartender "I’d rather give up the most positive review in the world than give alcohol to somebody so obviously drunk."
    bartender "Sorry, but I’m going to have to ask you to leave."
    $ jack_partial("angry_01")
    jack angry "(Oh, screw you![wait_1] I’ll -[wait_05] let’s see how drunk you think I am after this)"
    $ rewind_point = "prologue_12"
    $ hide_history()
    call screen psychic_powers

label prologue_12:
    $ show_history()
    show screen psychic_powers
    $ current_thought = "barbara_thought_pr_58"
    $ barbara_partial("angry_02")
    bartender "Are you trying to do something?"
    $ jack_partial("irritated_02")
    jack angry "(Dammit...[wait_05]she -[wait_05] she must have put something in the drinks...[wait_05]it’s affected my powers!)"
    $ current_thought = "barbara_thought_pr_59"
    $ jack_partial("confused_01")
    jack worried "How -[wait_05] how did you know?[wait_1] You -[wait_05] you shouldn’t know...[wait_05]you couldn’t know..."
    $ barbara_partial("angry_01")
    bartender "I have no clue what you’re talking about, but that’s enough.[wait_1] Get out of my bar."
    scene black_bg with quick_dissolve

label prologue_13:
    hide screen psychic_powers
    $ _history_list = []
    $ play_music("ambient_1")
    $ jack_partial("dismissive_02")
    $ person = "docherty_prologue"
    jack angry "(Whaddo I care about what she thinks anyway...[wait_1]she’s not even that good a bartender!)"
    jack angry "(Anyway, there’s better places to go to around here...I bet it’ll be easier to get free shit there, too.)"
    $ hide_history()
    $ renpy.choice_for_skipping()
    call screen modal_popup("You have enough time to visit one more location before the night is over.")
    call screen map_navigation(find_locations([1, 2]))

label prologue_music_venue:
    $ scene_setup(33, "Monday", True, 2, 2, True, True)
    $ play_music("neutral_1")
    $ location = "music_venue"
    scene black_bg with slow_dissolve
    $ jack_partial("analytical_01")
    jack smug "(Right...[wait_05]I - I know what I’ve gotta do.)"
    jack smug "(I’ll just - just go up to the door, and then I’ll make ‘em - I’ll make the door person forget that I haven’t paid the fee.)"
    jack smug "(Then I can - I’ll go inside, and I’ll - I’ll get stuff for free.)"
    $ jack_partial("cocky_02")
    jack smug "(Yeah...[wait_05]yeah, that’s a good idea! I like this plan!)"
    $ jack_partial("analytical_02")
    jack worried "(God, my head is pounding...[wait_05]but it’s still not as - as bad as how it felt when my powers first emerged.)"
    $ jack_partial("confused_01")
    jack worried "(I - I still don’t know why I got them, or how, but I’m glad that I’ve got - that I have them.)"
    $ jack_partial("cocky_01")
    jack smug "(I’ve got big plans for the future...[wait_05]just need to work out when to do the confrontation...[wait_05]get my revenge...)"
    scene venue_exterior at drunk_cycle(5, 0, 1.0) with slow_dissolve
    $ jack_partial("irritated_02")
    jack angry "(There’s the door guy...[wait_05]why couldn’t it be a sexy woman on the door?[wait_1] Give us something to - to look at while we’re going in...)"
    jack angry "(Y’know, if I was a doorman, I’d let anybody in for free.[wait_1] It’s not fair how we have to -)"
    call prologue_precognition from prologue_music
    scene venue_exterior at drunk_cycle(5, 0, 1.0) with quick_dissolve
    jump prologue_end

label prologue_restaurant:
    $ scene_setup(33, "Monday", True, 2, 2, True, True)
    $ play_music("neutral_1")
    scene black_bg with slow_dissolve
    $ location = "restaurant"
    $ jack_partial("irritated_01")
    jack worried "(I feel kind of dizzy, and - and the street is moving too much, but it’s not that far from here.)"
    jack worried "(I can definitely make - make it there.)"
    $ jack_partial("scared_01")
    jack thinking "(I - I hope that my powers are working when I get there...[wait_1]I need them so I can get those chips.)"
    $ jack_partial("irritated_01")
    jack thinking "(They should - they should lower their prices anyway, cos chips are - chips are - they’re too expensive. But they don’t wanna do that, cos they - they just wanna make money.)"
    jack thinking "(All they care about is themselves, and - and their profits and stuff...[wait_1]they’re just like that bartender.[wait_1] Everybody only cares about themselves.)"
    jack worried "(Anyway, I’d - I’d pay for stuff if I had the money, but I don’t, since I had to - I gave all that I had to that guy, Graves.)"
    $ jack_partial("disappointed_01")
    jack worried "(He’s soooo expensive...[wait_1]got the info I wanted, but did he - did he have to cost so much?)"
    scene restaurant_night at drunk_cycle(5, 0, 1.0), restaurant with slow_dissolve
    $ jack_partial("analytical_03")
    jack worried "(They’d better have some tables left inside...[wait_1]it’s so cold out here...)"
    $ jack_partial("cocky_01")
    jack smug "(Although if they don’t, I can - I can make somebody go outside.[wait_1] They wouldn’t know that I -)"
    call prologue_precognition from prologue_restaurant_
    scene restaurant_night at drunk_cycle(5, 0, 1.0), restaurant with slow_dissolve
    jump prologue_14

label prologue_precognition:
    scene black_bg
    $ hide_history()
    $ play_music("tense_2")
    $ play_sound("gunshot.mp3", pause=2.0, transition=white_flash)
    show screen calendar("Monday", 2, 2)
    $ show_history()
    return

label prologue_14:
    show red_pulse
    $ jack_partial("scared_01")
    jack worried "(My -[wait_05] my stomach, I -[wait_05] what’s happened?!)"
    jack worried "(It feels so -[wait_05] so sharp, and, and -[wait_05] god, breathing is -[wait_05] I -[wait_05] I can feel it with every breath.)"
    jack worried "(I -[wait_05] I -[wait_05] oh god, I -[wait_05] I’m dying!)"
    $ jack_partial("scared_02")
    jack worried "(I...[wait_05]{size=-8}Mum.[wait_1] Mum, please come and - and help me!{/size})"
    jack worried "{size=-8}(I -[wait_05] I’m sorry Mum, I -[wait_05] please make it go away!){/size}"
    jack worried "{size=-8}(I -[wait_05] I don’t want to die...[wait_05]why isn’t anybody helping me?){/size}"
    $ jack_partial("disappointed_01")
    jack worried "{size=-8}(Nobody cares about me...[wait_05]nobody wants me...){/size}"
    jack worried "...[wait_05] ..."
    hide red_pulse
    $ jack_partial("confused_02")
    jack thinking "(No...[wait_05]it’s -[wait_05] whatever’s happened, it’s -[wait_05] it hasn’t happened yet.)"
    $ jack_partial("analytical_02")
    jack thinking "(It’s my –[wait_05] my future sight –[wait_05] it’s kicked in harder than usual.)"
    jack thinking "(I -[wait_05] if I go in that building then it’ll...[wait_05]it’ll happen and I’ll...[wait_05]the vision will come true.)"
    $ jack_partial("scared_01")
    jack worried "(Somebody will shoot me and -[wait_05] god, why did I drink so -[wait_05] so much?)"
    jack worried "(I -[wait_05] I can’t -[wait_05] I don’t want to die![wait_1] Can I even -[wait_05] is it even possible for me to get away?)"
    jack worried "(I don’t have control over the -[wait_05] over my future sight, so I can’t see if there’s a way that I survive.)"
    $ jack_partial("scared_01")
    jack thinking "(I...[wait_05]I need to calm down.[wait_1] I can do this.)"
    $ jack_partial("analytical_01")
    jack thinking "(I just need to -[wait_05] I need to not go into that building, and then I’ll -[wait_05] yeah, I’ll be fine.)"
    jack thinking "(If I just keep moving then I’ll -[wait_05] I can get away.)"
    scene black_bg with quick_dissolve
    $ play_sound("gunshot.mp3", transition=white_flash)
    $ jack_partial("scared_01")
    jack worried "(Argh![wait_1] I’m -[wait_05] I got the vision again!)"
    jack worried "(My gut hurts so much, and I don’t think -[wait_05] no![wait_1] I -[wait_05] I can get away![wait_1] I can!)"
    $ play_sound("gunshot.mp3", transition=white_flash)
    $ jack_partial("scared_02")
    jack worried "(No...[wait_05]not here!)"
    jack worried "(Maybe...[wait_05]if I turn around...)"
    $ play_sound("gunshot.mp3", transition=white_flash)
    $ jack_partial("scared_01")
    jack worried "(No...[wait_05]no...[wait_05]where can I go...?)"
    jack worried "(Everywhere I go I get the sensation -[wait_05] the -[wait_05] the gunshot...)"
    jack worried "(But there’s got to be a way out...[wait_05]there’s got to be!)"
    $ scene_setup(10, "Monday", True, 2, 2, True, True)
    scene street at drunk_cycle(5, 0, 1.16) with slow_dissolve
    $ jack_partial("scared_01")
    jack worried "(Have I -[wait_05] have I been here before?[wait_1] I don’t -[wait_05] everything’s mixing together.)"
    jack thinking "(Why are they -[wait_05] who would want to hurt me?[wait_1] I -[wait_05] I’ve never even hurt a fly!)"
    $ rewind_point = "prologue_docherty_wipe"
    $ swap_sprites("docherty_neutral", quick_dissolve)
    show screen psychic_powers
    $ current_thought = "docherty_thought_pr_1"
    $ jack_partial("scared_02")
    jack worried "You...[wait_05]can you -[wait_05] can you help me?[wait_1] Please!"
    jack worried "There’s -[wait_05] somebody’s after me, and they’re -[wait_05] I -[wait_05] I don’t know if I can get away without some help."
    jack worried "Do you -[wait_05] do you have a car, or...?"
    $ docherty_partial("calm_01")
    docherty "I apologise for this, young man, but you are in the way of my plan."
    $ jack_partial("confused_02")
    jack angry "What do you -"
    hide screen calendar
    $ hide_history()
    hide screen psychic_powers
    scene cg1_2 at cg_1_reveal
    $ play_sound("gunshot.mp3", transition=white_flash)
    $ unlock_cg(0, 2)
    $ jack_partial("scared_01")
    jack worried "(No...[wait_05]no!)"
    $ jack_partial("scared_02")
    jack worried "(I -[wait_05] I can't die!)"
    $ jack_partial("scared_01")
    jack worried "(I just wanted to -[wait_05] please, somebody...[wait_05]help me...)"
    scene black_bg with slow_dissolve
    $ renpy.choice_for_skipping()

    #$ play_music("neutral_2")
    #call screen cta with slow_dissolve

label prologue_15:
    call screen chapter_breaks("EARLIER...", "Losing two or more litres of blood is usually fatal.\n\nIf the victim is brought to a hospital fast enough, though, they might just be able to be saved.")

    scene street with slow_dissolve
    lloyd_narrating neutral "I’ve been standing in the alley for about five minutes now, trying to find the right angle for the shot."
    lloyd_narrating neutral "But no matter where I stand, or how I try and frame it, I just can’t make it work.[wait_1] The lighting’s all wrong, and I don’t have the space to set up my tripod properly."
    lloyd_narrating neutral "Finally, I decide to lower the camera and place the cover over its lens.[wait_1] I’ll have to find a different angle to shoot the building from, although I doubt that I’ll find one as powerful as this one."
    lloyd_thinking neutral "What’s another aspect of it that I could focus on?[wait_1] Maybe if I was on its eastern side, the lighting there could –"
    $ play_sound("gunshot.mp3", transition=white_flash)    
    lloyd_narrating scared "A loud bang, coming from perhaps a block away, startles me and interrupts my train of thought."
    lloyd_narrating scared "Instinctively I grab my camera: firstly, to protect it from whatever has made the noise, and then, after realising that there’s no immediate danger, to examine it and confirm that it hasn’t been damaged."
    lloyd_thinking neutral "It seems fine, but I’d better keep the cover on."
    lloyd_thinking neutral "What caused the noise, though?[wait_1] A car backfiring?[wait_1] Someone letting off a firecracker?"
    lloyd_thinking thinking "...[wait_1]You never know, there could be a photo opportunity there.[wait_1] It’s not every day that you hear a noise like that."
    lloyd_thinking thinking "And if there is something...[wait_1]that’s a potential bargaining chip."
    lloyd_narrating thinking "I put my camera into its bag to protect it, and then exit the alleyway."
    scene black_bg with slow_dissolve
    lloyd_narrating thinking "The noise was loud and sudden, so it’s difficult to pinpoint where it came from.[wait_1] But it’s easy enough to circle this block and the adjacent ones, to see whether I can find the source of it."
    lloyd_narrating thinking "After a few minutes, I’m losing hope of finding whatever caused the loud bang."
    lloyd_narrating thinking "But then...[wait_1]I find him."
    scene cg2_0 at slow_dissolve
    lloyd scared "What –[wait_05] what happened here?!"
    lloyd_narrating scared "It’s the most violent and bloody scene I’ve ever encountered in my life."
    lloyd_narrating scared "A white man is lying on the street, along with what looks like most of the blood in his body." 
    lloyd_narrating scared "There’s an awful bubbling noise whenever he weakly breathes in, and beneath the usual scent of the city I can vaguely detect something metallic."
    scene black with quick_dissolve
    lloyd_narrating thinking "It’s too awful.[wait_1] I close my eyes and stop staring at it, before the nausea overtakes me."
    lloyd_narrating thinking "There’s –[wait_05] I’ve never had to deal with something like this."
    lloyd_thinking thinking "I...[wait_1]I don’t know what to do."
    lloyd_thinking thinking "I don’t know whether an ambulance can get here in time, and I –[wait_05] can I even help him?[wait_1] Would it do any good?"
    
    menu:
        "Help him":
            lloyd_thinking thinking "I could try and help him...but I’m not sure whether it would do any good."
            lloyd_thinking thinking "He –[wait_05] he’s lost so much blood, and I don’t think that there are any hospitals nearby."
            lloyd_thinking thinking "Whatever I try to do might actually make things worse.[wait_1] Is helping him really the right decision?"
            menu:
                "Help him":
                    lloyd_narrating thinking "I look over the scene again." 
                    lloyd_narrating thinking "It’s obvious now that the noise I heard was a gunshot, and this poor man was the recipient of the bullet."
                    lloyd_thinking thinking "The police are inevitably going to get involved with this, sooner or later."
                    lloyd_thinking thinking "I don’t know anything about what happened, but they might not believe me – I could end up being interrogated for answers that I don’t have."
                    lloyd_thinking thinking "Is helping him really the right decision?"
                    menu:
                        "Help him":
                            jump prologue_help_jack
                        "Leave him":
                            jump prologue_leave_jack
                "Leave him":
                    jump prologue_leave_jack
        "Leave him":
            jump prologue_leave_jack

label prologue_leave_jack:
    lloyd_thinking thinking "Whoever you are, I’m sorry, but –[wait_05] I can’t help you, and I can’t afford the complication that dealing with you will create."
    lloyd_thinking thinking "If I could have gotten here sooner, then I –[wait_05] I might have been able to do something, but...[wait_05]it’s just too late now, and it’s not going to do either of us any good."
    lloyd_thinking thinking "I'm sorry."
    scene street with slow_dissolve
    lloyd_narrating neutral "Before the dying man can realise that somebody has approached him, I turn around and walk away, trying not to appear unnatural."
    lloyd_narrating neutral "His voice croaks out once or twice into the darkness, but I refuse to turn back around, to look at him."
    lloyd_narrating neutral "I can’t save him, and it would be foolish to try."
    lloyd_narrating neutral "I haven’t seen anybody else on the street, but I’m sure there must be some people inside the surrounding buildings who are aware of the dying man, and are also ignoring him."
    lloyd_narrating neutral "It’s more their responsibility to help him than it is mine, and so I don’t let myself feel guilty."
    lloyd_narrating neutral "No doubt the police will eventually find his body, and they can investigate what led up to his death."
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "It isn’t long before the sounds of the dying man have faded away completely."
    lloyd_narrating neutral "I spend about fifteen minutes attempting to do some photography, but I can’t concentrate clearly enough, and eventually I give up and return to my apartment."
    lloyd_narrating neutral "Every now and then a stab of shame pierces me, but I push it down.[wait_1] I couldn’t have done anything."
    lloyd_narrating neutral "He was beyond any help I could have given.[wait_1] I couldn’t have done anything."
    lloyd_narrating neutral "If any of the news covers the death the next day, I don’t see it."
    lloyd_narrating neutral "Granted, I don’t look for it, but that’s because I don’t need to know any of the details surrounding the dead man."
    lloyd_narrating neutral "I couldn’t have done anything."
    lloyd_narrating neutral "Within a few weeks I’ve mostly pushed the incident out of my mind."
    lloyd_narrating neutral "I’ve continued with my photography, and I’m expecting something big to come up soon."
    lloyd_narrating neutral "I may not have been of any help, but I’ve been able to focus on and advance my own goals.[wait_1] That’s all that matters, really."
    narrator "THE END"
    $ MainMenu(confirm=False)()

label prologue_help_jack:
    lloyd_thinking thinking "I might not be able to help this dying man."
    lloyd_thinking thinking "I might add extra complications to my life by doing this."
    lloyd_thinking thinking "But I can’t just stand back and let it be someone else’s problem – I have to try to do something."
    lloyd_narrating thinking "I open my eyes again and force myself to take in the scene."
    scene cg2_0 at slow_dissolve
    lloyd_narrating scared "It’s worse than I remember it being."
    lloyd_narrating scared "The blood is all too wet, all too real."
    lloyd_narrating scared "My camera normally puts some distance between myself and the rest of the world; this is more than I’m used to."
    lloyd_narrating scared "I can’t let any of this get to me, though.[wait_1] I have to try and help this man."
    #sfx of phone dialling
    lloyd scared "Try and stay still.[wait_1] I’m going to call for an ambulance."
    dying_jack "Th-thanks, mate.[wait_1] Do you –[wait_05] d’you know how long it’ll –[wait_05] how long – ?"
    #sfx of phone connecting
    lloyd neutral "I’m unsure.[wait_1] It’s connecting now."
    lloyd_thinking neutral "I’m trying to concentrate on what the automated voice at the other end of the line is saying, but the man keeps talking, making it hard to hear."
    lloyd_thinking neutral "My attention is divided between the two voices, and I can’t focus properly."
    dying_jack "...bald guy[wait_1]...with –[wait_1] with dark clothes –"
    phone "– not an emergency, please hang up, and dial –"
    dying_jack "...no idea why he –[wait_05] why he did it.[wait_1] I –[wait_05] I just –"
    phone "– stay on the line.[wait_1] A trained operator will be with you –"
    lloyd_narrating scared "Suddenly, I feel a weight on my leg.[wait_1] The dying man has pulled together the last of his strength to sit up and grasp his bloody hands to me."
    lloyd scared "Conserve your strength.[wait_1] I’ve nearly gotten through to someone, I just need to –"
    dying_jack "N-nah...listen, mate, I -[wait_05] I’m not going to make it."
    dying_jack "I –[wait_05] I saw this happening, and I –[wait_05] I should’ve known that I couldn’t –[wait_05] couldn’t escape it..."
    lloyd_narrating neutral "I have no idea what he’s talking about."
    lloyd_narrating neutral "Did he know the person who shot him, and anticipated this?[wait_1] Did they have some sort of falling out?"
    dying_jack "I’m done for...but you –[wait_05] you can stop him...[wait_05]please...[wait_05]for me?"
    lloyd_thinking neutral "He might not be making any sense, but his eyes are as serious as any I’ve ever seen."
    lloyd_thinking neutral "He truly believes that he’s about to die...but I’ve got to do what I can."
    lloyd_narrating neutral "I reach out my hand to his, to grasp it so that I can lower him back down to the ground, and relieve the pressure on his wound."
    lloyd_narrating neutral "But the moment my skin brushes against his..."
    lloyd scared "Argh!"
    #invert colours, or colour shift the CG, or do a pulse out or something
    lloyd_narrating scared "A spike of pain drives itself into my skull."
    lloyd_narrating scared "The worst headache I’ve ever known flares up, and a wave of vertigo rolls over my body."
    lloyd_narrating scared "I can’t see through the brutal haze of pain; I’m unable to tell which way is up and which is down."
    lloyd_narrating scared "I get an uncanny out-of-body experience for a moment, feeling as though I’m seeing myself through the eyes of the dying man, and then it’s gone."
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I can feel something cold and hard beneath my hands, legs, and cheek, and I realise that I’ve fallen down to the ground in my nausea."
    lloyd_narrating neutral "There’s still a harsh throbbing in the back of my head, but it’s bliss in comparison to what I was feeling moments ago."
    phone "–lo?[wait_1] Is anyone there?"
    lloyd_narrating neutral "At some point the phone managed to connect."
    lloyd_narrating neutral "I reach out a hand for it, trying to find where I dropped it, before a finger finally nudges an edge."
    lloyd_narrating neutral "I get a proper grip on it as I pull myself up and to my feet."
    lloyd neutral "Sorry, I –[wait_05] I was a bit –[wait_05] I felt nauseous for a moment there."
    phone "Are you alright?[wait_1] Are you in need of medical assistance?"
    lloyd neutral "I’m not, but..."
    lloyd_narrating neutral "The words die in my throat as I look down at the man."
    scene cg2_1 at slow_dissolve
    lloyd_narrating neutral "The lack of the tiny bubbling noise betrays the fact that he’s stopped breathing."
    lloyd_narrating neutral "His body is completely still, and it will never move again."
    lloyd neutral "S-sorry, I –[wait_05] I think that this man is –[wait_05] I think that he’s just –[wait_05] he looks dead."
    lloyd_narrating neutral "The operator talks me through what to do so that they can confirm the death, beginning by asking me for the address."
    lloyd_narrating neutral "I patiently follow the instructions, but I’m hardly concentrating on them at all."
    lloyd_narrating neutral "Other questions are prodding at the edge of my mind, and it’s impossible to ignore them."
    lloyd_thinking neutral "Why did he die with a smile on his face?[wait_1] He was panicking before; he was scared."
    lloyd_thinking neutral "Now he looks more...serene."
    lloyd_narrating neutral "The back of my head is still throbbing."
    
    call screen chapter_breaks("HOURS LATER", "People react to stress in different ways. Some people crumple and fold, unable to cope with excessive pressure to their systems.\n\nOthers respond by evolving.")
    scene apartment_night at slow_dissolve
    lloyd_narrating neutral "The ambulance has come and gone, confirming what I already knew:[wait_05] that the man was dead."
    lloyd_narrating neutral "Because of the nature of the wound I had to talk to some police, but they were fairly sympathetic; they know how stressful seeing that sort of thing is."
    lloyd_narrating neutral "I answered their questions as best as I could and gave them my contact details in case they have to conduct a follow-up interview."
    lloyd_narrating neutral "I’ve been home for several hours now, trying and failing to fall asleep."
    lloyd_narrating neutral "It’s not just that the image of the dying man, the smell of his blood, keeps coming into my head."
    lloyd_narrating neutral "It’s not just that my mind keeps wondering about what happened, how he ended up in the situation he found himself in."
    lloyd_narrating neutral "My head is still pounding like a jackhammer, a constant pain beating a tattoo through my skull."
    lloyd_narrating neutral "That’s bad enough on its own, but my neighbours aren’t helping."
    lloyd_narrating neutral "Despite how late it is I keep hearing whispers of conversations; fragments of sentences here and there."
    lloyd_narrating neutral "I don’t want to knock on doors and make a fuss – especially if they’re going to settle down and go to sleep eventually – but it’s disruptive nevertheless."
    lloyd_narrating neutral "Every time I feel myself starting to drift off, a new jolt of pain drives itself through my head, or I’ll hear some vaguely audible words, and I’m wide awake again."
    lloyd_narrating neutral "I’ve tried taking both aspirin and sleeping tablets, but neither of them have had any effect on me."
    lloyd_narrating neutral "If anything, my head feels even worse than before."
    lloyd_narrating neutral "I’ve already tried doing some basic meditation to try and fall asleep, but I’m determined to actually stick with it this time."
    lloyd_narrating neutral "I slow my breathing and count in time with my breaths, trying to ignore the pain in my head."
    lloyd_narrating neutral "I keep it going, pretending that the continued whispering of my neighbours isn’t getting on my nerves."
    lloyd_narrating neutral "I focus solely on my breathing and counting, imagining the air travelling in and out of my lungs as I do so."
    lloyd_narrating neutral "And then...the voices get louder."
    # Show a screen with the voices flying around the place
        # Have you ever tried washing up without using washing-up liquid?
        # ...stupid idea to invest in it, I should have known that...
        # ...did she get there? It sounded like she did, but she might have faked...
        # ...better think of a good compliment on his technique...
        # ...should be getting to bed, but if I can just play one more...
    lloyd neutral "Hello?[wait_1] Is anyone –[wait_05] are you in my apartment?"
    lloyd_narrating neutral "It’s a stupid thing to call out."
    lloyd_narrating neutral "Of course my neighbours aren’t in my apartment –[wait_05] and if they were, they wouldn’t want to answer me.[wait_1] They’d want to stay as quiet as possible."
    lloyd_thinking neutral "Somewhat ironic, then, that they’re talking so loudly about those topics."
    lloyd_thinking neutral "Some of those are fairly private thoughts to be sharing."
    lloyd_narrating neutral "It’s then that I realise what the whispers are."
    lloyd_narrating neutral "Why I’ve been able to hear my neighbours tonight, when I’m normally unable to."
    lloyd_narrating neutral "Why such private information is being shared by them."
    lloyd_narrating neutral "Why my head is hurting so much, so intensely."
    lloyd_thinking neutral "It isn’t their words that I’m hearing –[wait_05] it’s their thoughts."
    lloyd_thinking neutral "Whatever they’re currently thinking, I’m able to pick up."
    lloyd_thinking neutral "But...why?[wait_1] How is it that I’m able to do this?"
    lloyd_narrating neutral "I think about it for several moments but can’t work out what the trigger is."
    lloyd_narrating neutral "My headache started around the time I encountered the dying man, but there’s no connection that I can deduce."
    lloyd_thinking neutral "Speaking of my headache...it’s not as bad now."
    lloyd_narrating neutral "I can still hear intermittent whispers – stray thoughts – but using my newfound ability seems to have silenced them for the most part."
    lloyd_narrating neutral "There are probably limits to this power...I might not be able to use it too often in succession."
    lloyd_thinking neutral "That solves one of the issues that’s stopping me from sleeping...but I’ve still got a bit of a headache."
    lloyd_narrating neutral "The pain has receded to a dull throbbing that’s far more manageable, but it’s still less than ideal."
    lloyd_narrating neutral "I try meditating again, to will the pain away."
    lloyd_narrating neutral "I concentrate on the back of my head as I slowly inhale and exhale."
    lloyd_narrating neutral "I imagine that the pain is gradually dissipating, each throb being slightly less painful than the last."
    lloyd_narrating neutral "I pretend that there’s a lump at the back of my head, and that each time I breathe out, it grows a little smaller."
    lloyd_narrating neutral "The pain suddenly disappears – but in its place is a new sensation."
    