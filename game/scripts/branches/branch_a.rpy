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
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "The sun is setting on another day.[wait_1] Inversely proportional to its position in the sky is my frustration."
    lloyd_narrating neutral "I’ve spent the entire day trying to discover what exactly happened last night but haven’t made any progress."
    lloyd_narrating neutral "None of my contacts have any clue why I would have gone to the bar and I don’t know how to reverse the damage my psychic powers did to my memories."
    lloyd_narrating neutral "I’ve returned to my favourite restaurant to eat dinner while I think things over."
    lloyd_thinking thinking "What am I in the mood for today...?"
    menu:
        "Chow mein":
            lloyd_narrating neutral "I order the chow mein and am given a generous serving which I take over to my table."
            lloyd_narrating neutral "The noodles are steaming hot and I have to blow on them to cool them down, but the dish is fantastic nevertheless."
            lloyd_narrating neutral "The sauce provides a pleasant sour flavour that complements the vegetables, and whenever I discover a piece of chicken the taste sensation is immediately enhanced."
        "Yangzhou fried rice":
            lloyd_narrating neutral "I order some Yangzhou fried rice, knowing that the rice will help sate my hunger after a day with little food."
            lloyd_narrating neutral "The rice has cooled down since it was cooked and is more lukewarm than anything, but the mixture of its texture with the vegetables and meat is just as delicious as always."
        "Char siu with rice":
            lloyd_narrating neutral "I order the char siu with rice, and am slightly disappointed when I see how little of the actual meat is on the plate by the time I’m served."
            lloyd_narrating neutral "My disappointment vanishes as I begin eating it, however, the umami flavour of the sauce and the texture of the meat impressing me despite the small amount I’ve been given."
    
    lloyd_narrating neutral "As I eat my meal I try and think about what to do next, but the solutions aren’t coming to me."
    lloyd_thinking neutral "It’s been a complete waste of a day."
    lloyd_thinking neutral "I haven’t learned anything new about the man in black and I haven’t reclaimed my missing memories."
    lloyd_thinking neutral "What do I do now?"

    if (not check_boolean("cat_investigates_murders")):
        lloyd_narrating neutral "The answer is obvious."
        lloyd_narrating neutral "There’s nothing else that I can do."
        lloyd_narrating neutral "I’m lacking the information I need to find the man in black."
        lloyd_narrating neutral "Nobody in the city can tell me about my missing memories or how my psychic abilities backfired."
        lloyd_narrating neutral "Any attempts to uncover the information will get me nowhere."
        lloyd_thinking thinking "I was hoping to get something out of this investigation...[wait_05]and to save some lives."
        lloyd_thinking thinking "But there’s wisdom in knowing when to abandon a project."
        lloyd_narrating neutral "I open up my phone and browse some galleries by some of my favourite photographers."
        lloyd_narrating neutral "I continue scrolling through them as I finish my meal, making a point to not think about the man in black or anything that I’ve done over the past two days."
        lloyd_narrating neutral "By the time I’m done at the restaurant I’m feeling good."
        lloyd_narrating neutral "Focusing on my interests instead of a fruitless cause has loosened a knot of tension in my chest which I hadn’t realised was there."
        scene black_bg with slow_dissolve
        lloyd_narrating neutral "I return home, certain that I’m done with the case.[wait_1] And I am."
        lloyd_narrating neutral "There’s no more investigating, and I turn my focus in the next few days to some personal matters."
        lloyd_narrating neutral "What I don’t anticipate is that the case isn’t done with me."
        lloyd_narrating neutral "But without the information I could have discovered, there’s no way for me to avoid my fate."
        narrator "GAME OVER"
        $ MainMenu(confirm=False)()
    
    lloyd_narrating neutral "The answer is decided for me as my phone receives a notification."
    # SFX Phone vibrating
    lloyd_thinking thinking "“This should be of interest to you”...?"
    lloyd_narrating neutral "The message is from an unknown number, and I’m hesitant to click on the links included with it."
    lloyd_narrating neutral "My curiosity wins out in the end though."
    call screen mobile_articles
    lloyd_narrating neutral "The links take me to two separate articles, each one being news reports about two recent deaths in the city.[wait_1] Both victims died of bullet wounds."
    lloyd_narrating neutral "Neither article says anything about suspects or motivation, and while a comparison is made between the victims, there’s no known connection or commonalities between them."
    lloyd_thinking thinking "The message must be from Cat.[wait_1] She’s done good work to find these articles...[wait_05]although they don’t give me much."
    lloyd_narrating neutral "Why did the man in black kill these two?[wait_1] Who could his next victim be?"
    lloyd_narrating neutral "There’s no connection between them, and it doesn’t sound as though either of them are related to the man with the white streak."
    lloyd_narrating neutral "Or do they?[wait_1] What do I really know about the man with the white streak?"
    lloyd_narrating neutral "Nothing, really.[wait_1] I don’t even know his name."
    lloyd_thinking thinking "Could he be the missing link between the other victims?"
    lloyd_narrating neutral "There’s only one way to find out.[wait_1] Tomorrow I’ll focus on the man in black’s most recent victim, and see what I can discover about him."
    lloyd_narrating neutral "If I can find out who exactly he is then I’ll begin to unravel the method to the man in black’s madness."
    lloyd_narrating neutral "I send Cat a text thanking her and then finish my meal." 
    lloyd_narrating neutral "I may not have made significant progress today, but I’m feeling more confident about tomorrow."
    scene black_bg with slow_dissolve

label branch_a_3_0:
    # Power upgrade
    $ branch = "a"
    $ day = 3
    call screen chapter_breaks("THURSDAY", "After two days of investigating Lloyd hasn’t discovered anything about the man in black. He has no idea of his motivation or who he’s targeted.\n\nToday is the day that changes.")
    scene apartment_day with slow_dissolve
    lloyd_thinking thinking "Investigating the man in black didn’t turn up any information.[wait_1] I have to change things around and look at things from a different angle."
    lloyd_thinking thinking "Namely, who was his victim and why was he killed?"
    lloyd_narrating neutral "The police will be doing the same as I am but they’re missing an essential tool:[wait_05] my psychic powers."
    lloyd_narrating neutral "I should be able to discover information that they can’t."
    lloyd_thinking thinking "The police might already have some information which could help me but I can’t get it from them."
    lloyd_thinking thinking "I’d need to question them about the victim and what they know in order to read their thoughts about him, which will make me look suspicious."
    lloyd_thinking thinking "Now, who would be the best person to help me discover who the man with the white streak is?"
    call screen map_navigation(find_locations([]))

label branch_a_3_4:
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "It’s been a long day of asking questions and I’m ready to take a break."
    lloyd_narrating neutral "Just as I’ve done the past two days I travel to my favourite restaurant and order a meal while I think it over."
    lloyd_thinking thinking "Tonight, I’ll order some..."
    menu:
        "Twice-cooked pork":
            lloyd_narrating neutral "The twice-cooked pork served at the restaurant is one of the reasons that it’s my favourite place to eat at."
            lloyd_narrating neutral "It’s got chilli bean paste included in its sauce, adding a kick of heat to the meal and enhancing the flavour further."
            lloyd_narrating neutral "The serving I’m given is clearly fresh out of the wok, still steaming from the plate."
        "Lemon chicken":
            lloyd_narrating neutral "The lemon chicken served by the restaurant isn’t anything particularly complicated, but that doesn’t mean that it isn’t tasty."
            lloyd_narrating neutral "I receive a plate of it from my server and sit down at my table. I have no regrets as I bite into it."
            lloyd_narrating neutral "The texture of the chicken is perfect, a crumbed exterior which gives way to a soft interior."
            lloyd_narrating neutral "The sauce has been made well, adding a tang to the meal without overwhelming it, while also creating a new texture in the process."
        "Zhajiangmian":
            lloyd_narrating neutral "The zhajiangmian is served into a bowl and passed over to me."
            lloyd_narrating neutral "The restaurant makes it Beijing-style, with diced pork used instead of minced meat."
            lloyd_narrating neutral "Multiple vegetables included with it add a delicious crunchy texture to the meal, and help contrast the softness of the noodles."
    lloyd_narrating neutral "As I eat my meal, I think about what to do next."
    lloyd_narrating neutral "I want to know who the man with the white streak –[wait_05] the victim of the man in black –[wait_05] is."
    lloyd_narrating neutral "If I can work out who he is and why he was killed then I can discover who the man in black’s next potential victim will be."
    lloyd_narrating neutral "After everything that I did today it’s obvious what I should do."
    menu:
        "Check in with Graves" (locked=not person_visited("graves", "a", 2) or not check_boolean("graves_mentioned_jack"), message=("You did not visit the detective today" if not person_visited("graves", "a", 2) else "You did not give Graves a name to investigate")):
            $ current_thought_block = "mind_read_graves"
            lloyd_thinking thinking "Graves apparently knows the man with the white streak as somebody named Usbourne."
            lloyd_thinking thinking "I’ll find out what he knows and discover the connection between all of the man in black’s victims."
            lloyd_narrating neutral "With that information I’ll be able to discover who his next target is and warn them before he can strike."
            lloyd_narrating neutral "Or report what’s going on to the authorities.[wait_1] Or set an ambush for him."
            lloyd_narrating neutral "The possibilities are wide, but I can’t do anything before seeing Graves."
            lloyd_narrating neutral "I finish my meal and then make my way back to his office building.[wait_1] I’m closing in on the man in black."
            lloyd_narrating neutral "I just need a little more time and information."
            scene detective_office with slow_dissolve
            $ swap_sprites("graves_smiling", slow_dissolve)
            lloyd_narrating neutral "Graves is as jovial as ever."
            lloyd_narrating neutral "Is this all a game to him?[wait_1] Or does he just need to stay positive so as to forget some of the horrors he no doubt sees in his line of work?"
            $ current_thought = "graves_thought_77"
            show screen psychic_powers
            lloyd_narrating neutral "Tell me, Graves:[wait_05] have you managed to discover anything about the man that I described to you?[wait_1] The one with the white streak of hair?"
            $ current_thought = "graves_thought_78"
            graves "I’ll put my cards on the table, Lloyd:[wait_05] I was fairly certain that I knew who you were talking about as soon as you described him."
            graves "The only reason I didn’t tell you what I knew at the time is that I –[wait_05] I wasn’t certain how much would be reasonable to tell you."
            lloyd neutral "What do you mean?"
            graves "The man with the white streak that you asked about is a –[wait_05] he’s a former client of mine, and I wasn’t sure whether giving you information about him would be a breach of client confidentiality."
            graves "After spending some time today thinking about it, I came to a decision:[wait_05] I’ll give you something on him if you tell me why exactly you want to know about him."
            $ swap_sprites("graves_intimidating")
            $ current_thought = "graves_thought_79"
            graves "And please, don’t give me some bullshit about wanting him as a model, again."
            graves "It wasn’t exactly convincing the first time."
            lloyd_thinking thinking "I knew it.[wait_1] He did see through the lie."
            lloyd neutral "Why did you pretend that you were convinced, then?"
            graves "I needed some time to think things over and wasn’t sure how you’d –[wait_05] I didn’t know how you’d react if I called you out on the lie."
            graves "So if you tell me the truth now about what your interest in him is, and I’m convinced that you don’t mean him any harm, I’ll give you his name and a number you can use to contact him."
            graves "Then he can decide what information to share with you himself."
            $ current_thought = "graves_thought_80"
            lloyd neutral "I wouldn’t be able to harm him if I wanted to.[wait_1] He’s dead."
            $ swap_sprites("graves_shocked")
            graves "He’s what?!"
            $ current_thought = "graves_thought_81"
            lloyd neutral "He died a few days ago.[wait_1] Killed on the street."
            lloyd neutral "I’m trying to find out what the connection between him and some other victims is."
            $ swap_sprites("graves_sad")
            graves "Bloody hell...[wait_1]killed on the street, huh?"
            lloyd_narrating neutral "He presses his fingers to his temple and concentrates for several moments.[wait_1] He sighs as he lowers them."
            $ current_thought = "graves_thought_82"
            graves "I wish you’d told me that little fact earlier today –[wait_05] I could have done some serious research into Jack."
            graves "As it is, all that I can tell you is what I –[wait_05] what we discovered while working for him."
            lloyd neutral "I take it that you don’t mind sharing that information?"
            graves "It’s not like the poor bastard can object, can he?"
            $ swap_sprites("graves_thinking")
            $ current_thought = "graves_thought_83"
            graves "Jack came to my partner and I a few weeks ago."
            graves "He hired us to find out about –[wait_05] he wanted us to look into his father."
            lloyd neutral "What for?"
            graves "He’s never met him.[wait_1] His parents split up when he was a baby, and so he –[wait_05] he wanted to find where his father was so that he could arrange a meeting."
            graves "We were able to do that and gave him the address where his father lives, along with a phone number."
            $ current_thought = "graves_thought_84"
            lloyd neutral "If his father was gone, who raised Jack?"
            graves "From what he said, it sounds like it was his mother, by herself."
            graves "She didn’t have a lot of money, though –[wait_05] I’m not sure why, but she didn’t get any child support from her former partner."
            graves "Because of that Jack grew up without too many –[wait_05] he didn’t have many luxuries as a child."
            $ current_thought = "graves_thought_85"
            lloyd neutral "Beyond his parents separating, is there anything else notable in his past?"
            graves "It didn’t sound like it.[wait_1] Nothing too notable in his present, either."
            $ current_thought = "graves_thought_86"
            lloyd neutral "How do you know that?"
            graves "We do background checks on our clients when we take on a job –[wait_05] particularly when they pay in cash, as Jack did."
            graves " It means that we’re not going to, say, find a victim for their abuser."
            lloyd neutral "What did your background check on me uncover?"
            $ current_thought = "graves_thought_87"
            graves "In Jack’s case, there were no –[wait_05] we didn’t find any particularly egregious red flags."
            graves "He’d been arrested for some petty crimes, and there were some things here and there that he’d been taken to court over but found innocent of, but nothing that –[wait_05] he wasn’t connected to any serious criminal groups or –[wait_05] or anything like that."
            $ current_thought = "graves_thought_88"
            lloyd neutral "You’re certain of that?"
            graves "Well, like I said earlier –[wait_05] if you’d told me earlier why you were looking into this I could have done some more in-depth research."
            graves "But from our general background check –[wait_05] no, there’s nothing serious there. Nothing too notable about him, like I said."
            $ current_thought = "graves_thought_89"
            lloyd neutral "Damn...[wait_05]there’s absolutely nothing?[wait_1] He’s completely unremarkable?"
            graves "From what I can tell, yeah."
            $ current_thought = "graves_thought_90"
            lloyd_thinking thinking "Then why did the killer target him?[wait_1] What’s Graves missing?"
            lloyd_thinking thinking "Or...[wait_05]maybe I’m the one missing something."
            lloyd_thinking thinking "What if there was no reason for the killer to target Jack, or his other two victims?"
            lloyd_thinking thinking "What if it was just a crime of passion –[wait_05] he shot the first people he encountered on the street who were by themselves?"
            $ swap_sprites("graves_smiling")
            $ current_thought = "graves_thought_91"
            graves "Hey, are you alright?[wait_1] You look kind of –[wait_05] you look a bit distressed."
            $ current_thought = "graves_thought_92"
            lloyd neutral "I’m fine.[wait_1] I just –[wait_05] I realised that I’ve probably been looking at this the wrong way."
            lloyd neutral "I’ve been assuming that Jack was killed for a reason, but there’s no real evidence for it."
            lloyd neutral "It’s more likely that he was just a victim of random violence.[wait_1] Whoever the killer is, there’s probably not a lot of method to their madness."
            $ current_thought = "graves_thought_93"
            graves "Mmm.[wait_1] I’m not saying that that’s –[wait_05] that it’s impossible, but I don’t really like the idea of that."
            graves "I think that people tend to be fairly rational –[wait_05] even if emotion sometimes does cloud their judgements."
            $ current_thought = "graves_thought_94"
            lloyd neutral "What are you saying?[wait_1] That there {i}is{/i} a reason why Jack was killed?"
            $ swap_sprites("graves_thinking")
            graves "I couldn’t say for sure, but I’d like to investigate both his past and present more thoroughly."
            graves "Do you want to come by here tomorrow evening and I’ll let you know what I –[wait_05] whatever I discover?"
            lloyd_thinking thinking "Tomorrow evening is too long to wait...[wait_05]but is there any alternative?"
            lloyd neutral "Certainly."
            $ swap_sprites("graves_smiling")
            $ current_thought = "graves_thought_95"
            graves "Great.[wait_1] Now then, there’s just one more thing..."
            $ swap_sprites("graves_intimidating")
            graves "Why exactly are you looking into these deaths?[wait_1] What’s your motivation?"
            $ current_thought = "graves_thought_96"
            graves "I don’t think that the police have that much interest in the case, and I –[wait_05] the reason that I knew that Jack was dead is because I ran into him on the street."
            graves "He died in front of me, so...[wait_05]I suppose I feel as though I owe it to him to do something."
            $ swap_sprites("graves_shocked")
            graves "Bloody hell![wait_1] I –"
            $ swap_sprites("graves_thinking")
            graves "– yeah, I can see why you’d feel a bit responsible for him."
            $ current_thought = "graves_thought_97"
            graves "Well, that’s good to hear."
            graves "Not the –[wait_05] not him dying in front of you, of course, but the –[wait_05] I’m glad to hear that you want to help out.[wait_1] Not a lot of people would do that."
            lloyd_thinking thinking "I’m just glad that he’s not questioning that any further."
            $ current_thought = "graves_thought_98"
            lloyd neutral "I’ll see whether I can find out anything else about him on my end tomorrow, and then I’ll meet you here in the evening, as discussed."
            graves "Sounds like a plan to me.[wait_1] See you, Lloyd."
            hide graves_thinking with quick_dissolve
            hide screen psychic_powers
            scene black_bg with quick_dissolve
            scene apartment_night with slow_dissolve
            lloyd_narrating neutral "I return to my apartment and think about tomorrow.[wait_1] I’ve learned a little about Jack, but it’s not enough."
            lloyd_narrating neutral "Graves had better come through tomorrow."
            return
        "Travel to Icarus" (locked=not person_visited("barbara", "a", 2) or not check_boolean("barbara_retrieves_footage"), message=("You did not visit the bar today" if not person_visited("barbara", "a", 2) else "You did not convince Barbara to give you the footage")):
            jump branch_b_3_4
        "Return home":
            lloyd_narrating neutral "I’ve been travelling all around the city today in search of answers and have hit a wall."
            lloyd_narrating neutral "I’m no closer to discovering the identity of the man with the white streak than I am the identity of the man in black."
            lloyd_thinking thinking "I’m not going to discover anything new tonight."
            lloyd_thinking thinking "The best way to progress in the investigation is to get a full night of rest so that I can keep going tomorrow."
            lloyd_narrating neutral "While eating my meal I’ve worked out what to do tomorrow."
            lloyd_narrating neutral "I was reluctant to approach the police and find out what they know but it’s clear now that it’s the only path forward."
            lloyd_narrating neutral "They will have begun their own investigation into the victim and will have more information than me."
            lloyd_narrating neutral "If I word my questions carefully and use my powers tactically I can learn everything that I need to know about the man with the white streak."
            lloyd_thinking thinking "It was a mistake not to go to the police in the first place.[wait_1] They’ll have everything that I need to know."
            scene black_bg with slow_dissolve
            lloyd_narrating neutral "That’s what I genuinely believe when I go to sleep that night."
            lloyd_narrating neutral "But when I visit a police station the next day I’m instantly proven wrong."
            lloyd_narrating neutral "My questions aren’t as subtle as I think they are and I’m soon dismissed as a nuisance."
            lloyd_narrating neutral "Reading the mind of the officer I’m questioning doesn’t give me anything useful, and things go awry when I push a bit harder."
            lloyd_narrating neutral "It doesn’t take long for me to be arrested and placed in a holding cell."
            lloyd_narrating neutral "My investigation is over for good.[wait_1] I won’t be able to stop the man in black or save any of his future victims."
            narrator "GAME OVER"
            $ MainMenu(confirm=False)()

label branch_a_4_0:
    # Power upgrade
    $ branch = "a"
    $ day = 4
    call screen chapter_breaks("FRIDAY", "Lloyd has found out who the man with the white streak, Jack Usbourne, is, but knows little more than that. He’s going to research Jack further today.\n\nHe has no backup plan for if this plan fails.")
    scene apartment_day with slow_dissolve
    lloyd_thinking thinking "Jack Usbourne.[wait_1] The man with the white streak."
    lloyd_thinking thinking "Graves said that there was nothing particularly remarkable about him...[wait_05]was his death random?"
    lloyd_thinking thinking "Or are we just lacking the information to see why he was targeted?"
    lloyd_thinking thinking "Graves is going to dig up what information he can, meaning that I have the entire day to myself."
    lloyd_thinking thinking "Should I visit any of my other contacts?"

    call screen map_navigation(find_locations([]))