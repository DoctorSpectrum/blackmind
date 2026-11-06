label branch_a_1_0:
    $ branch = "a"
    $ day = 1
    call screen chapter_breaks("TUESDAY", "There are millions of residents in the city, comprising a diverse range of ages, genders, and jobs.\n\nThat means that there are millions of potential victims.")
    scene apartment_day with slow_dissolve
    lloyd_narrating neutral "It’s taken me a bit of time to research, but I’ve found four potential places to visit today that can hopefully help me out."
    lloyd_narrating neutral "I’m not sure that I’ll have time for all of them, though, so I’ll need to prioritise carefully."
    call screen modal_popup("You are now ready to begin the main game of BLACKMIND: Psychic Social Simulator. As Lloyd, you’re going to try and track down Jack’s killer and find a way to stop him – but as you uncover new information, you might find your priorities and goals changing.")
    call screen modal_popup("Lloyd isn’t as experienced with using psychic powers as Jack was, and so there are a few things to note when playing as him:\n\n{font=DejaVuSans.ttf}•{/font} You can only use your Mind Read ability 3 times per conversation.\n\n{font=DejaVuSans.ttf}•{/font} You can only use your Mind Rewind ability 1 time per conversation.\n\nRemember to make use of the History log to carefully review conversations, and determine where the best place to use your psychic abilities is.\n\nIn addition, you only have enough time each day to visit three locations. Choose which locations you want to visit carefully. You can only visit a location once per day.\n\nThis information, and more, can be reviewed in the Help section of the pause menu.", short=False)
    call screen map_navigation(find_locations([1, 2]))

label branch_a_1_4:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "The sun is starting to set, the day coming to a close."
    lloyd_narrating neutral "I’ve travelled all across the city today but still haven’t found anything solid about the identity of the man in black."
    lloyd_narrating neutral "It’s frustrating, but I’m pleased that I managed to establish some contacts who I can work with to stop him."
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "I head to my favourite restaurant for some dinner."
    lloyd_narrating neutral "It’s a fairly popular franchise, with branches all across the city in as similar a layout as possible."
    lloyd_narrating neutral "I’ve barely had any time for food today and it’s good to stop and slow down for a bit."
    lloyd_thinking neutral "What am I in the mood for today...?"

    menu:
        "Kung Pao Chicken":
            lloyd_narrating neutral "The server spoons kung pao chicken from a tray onto a plate until it’s sufficiently full then passes it over to me."
            lloyd_narrating neutral "I sit down at my table and begin eating it."
            lloyd_narrating neutral "It’s authentically made, with enough spice to cause a tingling feeling in my mouth but not so much that I’m uncomfortable."
            lloyd_narrating neutral "The chicken has been cooked perfectly, being chewy and not too dry."
        "Sweet and Sour Pork":
            lloyd_narrating neutral "The server spoons sweet and sour pork from a tray onto my plate before passing it over to me."
            lloyd_narrating neutral "I make my way to an empty table and begin eating it."
            lloyd_narrating neutral "The dish has been prepared perfectly, with the sweetness and texture of the pineapple contrasting well against the crunch of the pork."
        "Dumplings":
            lloyd_narrating neutral "I order ten pork and chive dumplings which are placed onto a plate and passed over to me."
            lloyd_narrating neutral "They’ve been sitting in the bain marie for long enough that they’re not as crunchy or as hot as I’d like, but each one is delicious nevertheless."
    
    lloyd_narrating neutral "As I make my way through the meal I go over what I’ve accomplished today."
    lloyd_narrating neutral "I have to think carefully about what to do next.[wait_1] With the remaining time in the day I can only visit one of my contacts."
    lloyd_narrating neutral "The most promising one was..."
    
    menu:
        "Barbara" (locked=not person_visited("barbara", "a", 0), message="You did not visit the bar today"):
            jump branch_a_1_4_barbara
        "Cat" (locked=not person_visited("cat", "a", 0) or not check_boolean("cat_name_discovered"), message=("You did not visit the library today" if not person_visited("cat", "a", 0) else "You did not convince the librarian to investigate the man in black")):
            jump branch_a_1_4_cat
        "Eddie" (locked=not person_visited("eddie", "a", 0) or not check_boolean("eddie_investigates_docherty"), message=("You did not visit the newspaper today" if not person_visited("eddie", "a", 0) else "You did not convince Eddie to investigate the man in black")):
            jump branch_c_1_4
        "Graves" (locked=not person_visited("graves", "a", 0), message="You did not visit the detective agency today"):
            jump branch_a_1_4_graves

label branch_a_1_4_barbara:
    lloyd_thinking neutral "There are only three known facts about the man in black."
    lloyd_thinking neutral "His appearance.[wait_1] His plan to commit murder." 
    lloyd_thinking neutral "And that he was somewhere around Icarus last night when he killed the man with the white streak of hair."
    lloyd_thinking neutral "Barbara – or her neighbours – are the strongest lead I have.[wait_1] I’ll check in and find out what she’s discovered."
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I return to Icarus, the walk from the station already feeling more familiar."
    lloyd_narrating neutral "The bar is open to the public at this hour, but it’s quiet anyway, with only a few patrons huddled away in the corner."
    
    scene bar with slow_dissolve
    $ current_thought_block = "mind_read_barbara"
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_23"
    show screen psychic_powers
    lloyd neutral "Hello, Barbara."
    $ current_thought = "barbara_thought_24"
    barbara "Oh hey![wait_1] It’s –[wait_05] um, don’t tell me...[wait_05]Linus?"
    barbara "No –[wait_05] Lloyd![wait_1] It is Lloyd, isn’t it?"
    $ current_thought = "barbara_thought_25"
    lloyd neutral "Correct."
    $ current_thought = "barbara_thought_26"
    barbara "What can I do for you?[wait_1] If you need a recommendation, I’ve got a really nice pilsner from a local brewery."
    $ current_thought = "barbara_thought_27"
    lloyd neutral "Sorry, but I’m not here for business.[wait_1] What did you discover from your neighbours?"
    $ swap_sprites("barbara_thinking")

    if (check_boolean("barbara_convinced_investigate")):
        $ current_thought = "barbara_thought_28"
        barbara "Sorry, Lloyd –[wait_05] I asked a few of them, but nothing that’ll help you."
        barbara "None of them saw anyone like the guy you described around here –[wait_05] not too surprising when you consider that they were all closed."
        lloyd_thinking neutral "She’s got a point.[wait_1] I was too optimistic in hoping that they were here and paying attention to what was happening in the street."
        lloyd neutral "Thank you for asking anyway."
    else:
        $ current_thought = "barbara_thought_29"
        barbara "I’ll be honest with you:[wait_05] I didn’t get the opportunity to talk to any of them."
        barbara "I know that this is important to you, but managing my business is important to me, and I just didn’t get the time for it."
        lloyd_thinking neutral "I can’t fault her for that.[wait_1] Perhaps it was a mistake to expect too much of her."
        lloyd neutral "Thank you for your honesty."

    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_30"
    barbara "Now, do you want to try some of that pilsner?"
    lloyd_narrating neutral "I’m tempted for a moment despite my aversion to drinking."
    lloyd_narrating neutral "It would be nice to sit down and simply relax."
    lloyd_narrating neutral "But it’s been a long day and I’m feeling quite drained."
    lloyd_narrating neutral "If I can’t find any answers to the mystery of the man in black then I should get some rest."
    $ current_thought = "barbara_thought_31"
    lloyd neutral "Thank you, but I should be going."
    $ swap_sprites("barbara_sad")
    barbara "Oh, okay."
    hide screen psychic_powers
    hide barbara_sad with quick_dissolve
    scene black_bg with slow_dissolve
    lloyd_narrating "The wait for a train takes a while and any ideas about visiting another contact disappear by the time I’m finally seated and moving."
    lloyd_narrating "I’m tired and feel like the day has gone poorly."
    lloyd_narrating "All that I want to do now is rest up before looking further into the man in black tomorrow."
    lloyd_narrating "I just hope that I’m not mistaken in leaving the bar, and that he won’t strike again tonight."
    jump branch_a_1_4_bar

label branch_a_1_4_cat:
    lloyd_thinking neutral "The only things I know for certain about the man in black are his features and that he’s going to murder again."
    lloyd_thinking neutral "The information I have on him is too tenuous at present and I won’t be able to find him fast enough at the pace I’m going."
    lloyd_thinking neutral "The better move is to visit the library and see what that woman, Cat, will let me access."
    lloyd_thinking neutral "I know from her thoughts that the books aren’t in the library, yet she said that she could let me look at some of them if I returned tonight."
    lloyd_thinking neutral "What’s she planning?[wait_1] Is she actually going to let me see the books, or will she devise some excuse to cancel the meeting?"
    lloyd_thinking neutral "The only way I’ll find out is if I make the journey."
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I travel through the park once more to reach the library."
    lloyd_narrating neutral "The moon is one day away from being full, and in the darkness the park feels more ominous and dangerous than it did during the day."
    lloyd_narrating neutral "There are no more laughing families – just silence and shadows."

    scene library_night with slow_dissolve
    $ current_thought_block = "mind_read_cat"
    lloyd_narrating neutral "The library is popular enough to justify staying open late."
    lloyd_narrating neutral "Despite this it’s mostly empty."
    lloyd_narrating neutral "Some people are quietly studying with laptops or reading in armchairs but they’re few and far between."
    lloyd_narrating neutral "It doesn’t take me long to notice Cat, standing closely to the entrance."
    $ swap_sprites("cat_neutral", slow_dissolve)
    lloyd_narrating neutral "I stride towards her confidently.[wait_1] The next few seconds will determine whether I’ve wasted my time here or not."
    $ current_thought = "cat_thought_20"
    show screen psychic_powers
    lloyd neutral "Did you bring one of the books?"
    $ current_thought = "cat_thought_21"
    cat "I’ve been thinking...[wait_1]are you sure you need to look at them?"
    cat "They’re...[wait_1]nothing special."
    $ current_thought = "cat_thought_22"
    lloyd neutral "I’ll be the judge of that.[wait_1] If you have one I’ll be seeing it."
    lloyd_narrating neutral "Her face is a solid mask, betraying none of her emotions.[wait_1] She doesn’t react at first."
    lloyd_narrating neutral "Then she reaches into her bag and brings out a thin book."
    $ current_thought = "cat_thought_23"
    cat "Here you are.[wait_1] I’ll give you five minutes with it...[wait_1]then it needs to be taken back."
    lloyd_narrating neutral "{i}Opening Your Third Eye{/i}. It’s one of the less promising titles but I can’t fault Cat for bringing it."
    lloyd_narrating neutral "I didn’t specify what I wanted to see."
    $ current_thought = "cat_thought_24"
    lloyd_narrating neutral "I quickly skim the foreword of the book and find it wanting."
    lloyd_narrating neutral "The author claims that everybody has the potential for psychic powers within them."
    lloyd_narrating neutral "They say that it’s simply about finding the right trigger for unlocking them – whether that’s unblocking your chakra, being in a dangerous situation, or aligning your energy with someone who has unlocked theirs."
    $ current_thought = "cat_thought_25"
    cat "Are you done yet?"
    lloyd_narrating neutral "I pass the book back.[wait_1] If the answers to my abilities exist in a book, they won’t be found in this one."
    $ current_thought = "cat_thought_26"
    lloyd neutral "Give me the next book."
    cat "No...[wait_1]you already saw one of them.[wait_1] The others...[wait_1]aren’t for you."
    $ current_thought = "cat_thought_27"
    lloyd neutral "And if I ask one of your coworkers for assistance?"
    cat "Maybe they’ll refuse to help you."
    lloyd neutral "Maybe I should ask them for help regardless."
    $ current_thought = "cat_thought_28"
    cat "...[wait_1]Come by tomorrow...[wait_1]I might be able to get you another book then."
    lloyd_narrating neutral "Without waiting for a confirmation from me, she leaves."
    hide screen psychic_powers
    hide cat_neutral with quick_dissolve
    lloyd_thinking neutral "The books aren’t here at the library, but she was able to bring one of them anyway."
    lloyd_thinking neutral "She’s probably keeping them at her house."
    lloyd_thinking neutral "But why are they there?[wait_1] And why is she so hostile to me reading them?"
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "The day has taken a lot out of me."
    lloyd_narrating neutral "I can feel my eyelids growing heavier and heavier as I walk back through the park."
    lloyd_narrating neutral "Any ideas I had about visiting another contact fade away as I grow closer and closer to my apartment."
    lloyd_narrating neutral "For now all that I want to do is rest.[wait_1] I can look further into the mystery of the man in black and my new abilities tomorrow."
    jump branch_a_1_4_bar

label branch_a_1_4_graves:
    lloyd_thinking neutral "I know that the man in black is going to murder again but not when or where."
    lloyd_thinking neutral "I can’t work on that information so the only other option is to try and identify him through his appearance."
    lloyd_thinking neutral "As a detective I’m hoping that Graves has done this before, and has some information by now."
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I make my way over to the office building that Graves is in, ignoring the busy crowds around me."
    lloyd_narrating neutral "It’s getting late and I’m unsure whether he’ll still be working."
    lloyd_narrating neutral "If he isn’t there then I won’t be able to contact him until tomorrow."
    lloyd_narrating neutral "It’s not unlikely that things will be too late by then.[wait_1] The man in black might commit murder night after night until he’s stopped."
    lloyd_narrating neutral "As I approach Graves’ building I spot a light on the fourth floor."
    lloyd_narrating neutral "He’s still in and that means that there’s still hope."
    lloyd_narrating neutral "I take a quick shot of the building, regretting that I didn’t bring a more powerful flash, and then press the intercom button."
    # SFX door reception buzz
    graves "What kinda time do ya think this is, wiseguy?"
    lloyd neutral "It’s me, Graves.[wait_1] Lloyd."
    graves "Oh, of course![wait_1] That’s –[wait_05] excellent, come on up!"
    lloyd_narrating neutral "The door unlocks with a loud click and I step inside."
    lloyd_narrating neutral "I’m eager to hear what Graves has managed to uncover."
    
    scene detective_office with slow_dissolve
    $ swap_sprites("graves_smiling", slow_dissolve)
    $ current_thought_block = "mind_read_graves"
    $ current_thought = "graves_thought_25"
    show screen psychic_powers
    lloyd_narrating neutral "Graves greets me with a friendly handshake that I suspect he wants to turn into a hug, and then offers me some green tea.[wait_1] I decline."
    $ current_thought = "graves_thought_26"
    lloyd neutral "Thank you, but I’m more interested in how the case is progressing."
    lloyd neutral "Where are things standing at present?"
    graves "Like I told you earlier today –[wait_05] I’ve opened up a file for your case; to find this –[wait_05] to find the man in black."
    if (days["a"][0][2] == "graves"):
        graves "Unfortunately, you visited fairly late in the day, so I haven’t managed to do much more than put some feelers out."
        graves "I’ve contacted a few people I know, placed a few –[wait_05] I’ve made some, um, calls, but I haven’t heard back from any –[wait_05] from anybody just yet."
    else:
        graves "I’ve reached out to a few of my people, made a few –[wait_05] I’ve called up some people and made them aware of the –[wait_05] of what the case entails, but I haven’t heard back from any of them yet."
        graves "Things are still all a bit –[wait_05] it’s a bit up in the air at the moment."
    $ current_thought = "graves_thought_27"
    lloyd neutral "In other words, you have nothing."
    $ swap_sprites("graves_intimidating")
    if (check_boolean("identify_graves_lie")):
        $ current_thought = "graves_thought_28"
        graves "Hey, do you remember what I –[wait_05] what I told you?"
        graves "I told you that I couldn’t guarantee that things would –[wait_05] that they’d get very far along."
        lloyd neutral "As I recall, you also said that you planned to have some results by tomorrow which you could impress me with."
        $ current_thought = "graves_thought_29"
        graves "Yeah, well, my clients normally give me a bit more than a vague description to work with."
        graves "If you, um, want faster results, you’ll need to help me narrow things down a bit."
        graves "Got anything else you want to –[wait_05] that I can work with?"
    else:
        $ current_thought = "graves_thought_28"
        graves "Hey, I did warn you that I was in the middle of –[wait_05] that I had another case that I was working on."
        graves "Is this really that surprising?"
        lloyd neutral "...I suppose not."
        $ current_thought = "graves_thought_29"
        graves "I can also speed things up a bit more if you give me a bit more information on this – on the guy you want found."
        graves "Do you have anything else that you can – that you’re able to share?"
    $ current_thought = "graves_thought_30"
    lloyd neutral "...Not at present."
    $ current_thought = "graves_thought_31"
    graves "Then I guess I’m not the only one affecting the progress of the case."
    $ current_thought = "graves_thought_32"
    lloyd neutral "...Fine.[wait_1] I might be back tomorrow."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_33"
    graves "Cool.[wait_1] I’ll hopefully see you then, mate."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve 
    lloyd_narrating neutral "I shouldn’t have been too disappointed, but I nevertheless am."
    lloyd_narrating neutral "I’d convinced myself that Graves was a miracle worker."
    lloyd_narrating neutral "I’d expected results within a few short hours."
    lloyd_narrating neutral "But in the process I’d forgotten that he was younger than me."
    lloyd_narrating neutral "Had I made a mistake in going to him in the first place?"
    lloyd_narrating neutral "For now I would wait and see whether this tree bore any fruit."
    lloyd_narrating neutral "I take the stairs back down and return to my apartment."
    lloyd_narrating neutral "I start planning out which of my other contacts I have the time to meet with tonight, but before I know it my eyelids start growing heavy."
    lloyd_narrating neutral "The day has taken more out of me than I anticipated."
    lloyd_narrating neutral "Eventually I decide that the wiser move is to rest. Finding the man in black can continue tomorrow."
    
    jump branch_a_1_4_bar

label branch_a_1_4_bar:
    mental_jack "Alright...[wait_05]now let’s have a little fun."
    call screen chapter_breaks("HOURS LATER", "Lloyd went to bed with the expectation that when he woke up he would be in a better state for finding the man in black.\n\nHe isn't.")

    scene black_bg with quick_dissolve
    lloyd_thinking neutral "What the...[wait_05]what’s that...[wait_05]noise?[wait_1] And...[wait_05]feeling?"
    lloyd_narrating neutral "My head is pounding once more, and the initial thought is that I’m about to have another vision of the future."
    lloyd_narrating neutral "But there are other sensations mixed in with it this time, too."
    lloyd_narrating neutral "A slight dizziness in my head.[wait_1] A taste of something that’s both smokey and sweet in my mouth.[wait_1] A mild nausea in my stomach."
    lloyd_narrating neutral "And the realisation that I’m no longer in my apartment."
    scene bar with slow_dissolve
    if (person_visited("barbara", "a", 0)):
        lloyd_narrating neutral "It takes me a minute to realise where I am.[wait_1] Icarus, the bar that Barbara owns."
    else:
        lloyd_narrating neutral "It takes me a minute to realise what sort of place I’m in.[wait_1] It looks like some kind of drinking establishment."
    lloyd_narrating neutral "How I got here is a mystery to me.[wait_1] The last thing that I recall is getting into bed and falling asleep."
    lloyd_narrating neutral "I go to the bar in the hope of finding some answers."
    $ swap_sprites("barbara_smiling")
    $ current_thought_block = "mind_read_barbara"
    show screen psychic_powers
    if (person_visited("barbara", "a", 0)):
        $ current_thought = "barbara_thought_32"
        barbara "Finished that drink already?"
        $ current_thought = "barbara_thought_33"
        lloyd neutral "No, I...[wait_1]Barbara, how did I –[wait_05] what’s happened?[wait_1] How did I get here?"
    else:
        $ current_thought = "barbara_thought_34"
        bartender "Finished that drink already?"
        $ current_thought = "barbara_thought_35"
        lloyd neutral "No, I...[wait_1]sorry, how did I –[wait_05] what’s happened?[wait_1] How did I get here?"
    lloyd_narrating neutral "As I speak the words they come out slightly slurred from a tongue that feels too fuzzy." 
    lloyd_narrating neutral "I’m also swaying slightly; unable to stay completely upright."
    
    if (person_visited("barbara", "a", 0)):
        barbara "You walked through the front door, same as everybody else does."
        $ swap_sprites("barbara_angry")
        $ current_thought = "barbara_thought_36"
        barbara "But if you’ve already forgotten that, then I think we’ll have to call that your last drink of the evening."
        lloyd neutral "That’s –[wait_05] I don’t care."
        lloyd neutral "I –[wait_05] what I want to know is –[wait_05] why –[wait_05] why am I here?"
        barbara "Apparently, to drink more than you’re capable of handling."
        $ current_thought = "barbara_thought_37"
    else:
        bartender "You walked through the front door, same as everybody else does."
        $ swap_sprites("barbara_angry")
        $ current_thought = "barbara_thought_38"
        bartender "But if you’ve already forgotten that, then I think we’ll have to call that your last drink of the evening."
        lloyd neutral "That’s –[wait_05] I don’t care."
        lloyd neutral "I –[wait_05] what I want to know is –[wait_05] why –[wait_05] why am I here?"
        bartender "Apparently, to drink more than you’re capable of handling."
        $ current_thought = "barbara_thought_39"
    lloyd neutral "I –[wait_05] okay.[wait_1] I’m –[wait_05] I’m going home..."
    lloyd neutral "I...[wait_05]sorry if I caused any trouble."
    lloyd_narrating neutral "There might be answers to this mystery if I stay here and look for them."
    lloyd_narrating neutral "But I feel exhausted and just want to get back to sleep.[wait_1] It’s far too late to be doing anything else, and there will be time tomorrow for questions."
    hide barbara_angry with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I exit the bar and make my way to the nearest train station."
    if (not person_visited("barbara", "a", 0)):
        lloyd_narrating neutral "Before I get too far from the bar I take note of its name."
        lloyd_narrating neutral "Icarus.[wait_1] An interesting name."
        lloyd_narrating neutral "It rings a bell but I can’t make the connection.[wait_1] I shrug it off and continue to the train."
    lloyd_narrating neutral "It’s far too late by the time I finally reach home and go to bed."
    
label branch_a_2_0:
    # Power upgrade
    $ branch = "a"
    $ day = 2
    call screen chapter_breaks("WEDNESDAY", "It’s now been more than twenty-four hours since Lloyd vowed to find and stop the man in black.\n\nHe has not made any progress in discovering who the man’s identity or what his aims are.")
    scene apartment_day with slow_dissolve
    lloyd_narrating neutral "I wake up in bed wondering whether my memory of last night was a bad dream."
    if (person_visited("barbara", "a", 0)):
        lloyd_narrating neutral "I remember something about being in Icarus and a cold train ride, but it’s indistinct enough that my mind could be playing tricks."
    else:
        lloyd_narrating neutral "I remember something about being in a bar and a cold train ride, but it’s indistinct enough that my mind could be playing tricks."
    lloyd_narrating neutral "Then the sensation of a head full of cotton wool and a full bladder kicks in."
    lloyd_narrating neutral "The bright light of day feels far more intense than it should, and when I shamble my way out of bed my stomach hurts enough to force me into a ball."
    lloyd_narrating neutral "Last night was definitely not a dream.[wait_1] The hangover confirms what memories deny."
    lloyd_narrating neutral "I went out to a bar and got roaring drunk but don’t remember why."
    lloyd_thinking neutral "Did I go out to celebrate something and then drink so much that I forgot why I went out?"
    lloyd_thinking neutral "Or was there some other reason that I visited the bar?[wait_1] Was it to do with the man in black?"
    lloyd_thinking neutral "My powers only let me read the future...[wait_1]it’s a pity that they won’t let me read the p–"
    lloyd_narrating neutral "Thinking about my psychic abilities makes me realise what possibly happened."
    lloyd_thinking neutral "Could my psychic abilities have been responsible for my memories disappearing?"
    lloyd_thinking neutral "Did they somehow backfire on me and cause me to forget the start of my night out?"
    lloyd_narrating neutral "The more that I think about it the more it makes sense."
    lloyd_narrating neutral "My psychic powers affect peoples’ minds, and I’ve forgotten most of my night out."
    lloyd_narrating neutral "That solves that mystery, but not why I went to the bar in the first place."
    lloyd_thinking neutral "Nothing on my phone gives me a conclusive answer."
    lloyd_thinking neutral "It’s a little tenuous but I’d like to talk to some of the contacts I made yesterday and see whether any of them know anything."
    lloyd_thinking neutral "Maybe one of them will know what happened"
    
    call screen map_navigation(find_locations([]))

label branch_a_2_4:
    call screen mobile_articles