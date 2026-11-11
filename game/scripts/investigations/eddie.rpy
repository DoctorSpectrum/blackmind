label eddie_investigation:
    $ current_thought_block = "mind_read_eddie"
    if (branch == "a"):
        if (day == 1):
            jump eddie_a_1
        elif (day == 2):
            jump eddie_a_2
        elif (day == 3):
            jump eddie_a_3
        elif (day == 4):
            jump eddie_a_b_4
    elif (branch == "b"):
        jump eddie_a_b_4
    
    return

label eddie_a_1:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I travel eastwards for a quarter of an hour with mixed feelings in my stomach throughout the duration of the journey."
    lloyd_narrating neutral "Of all the places to visit today this is both the one I’m most excited for, but also looking forward to the least."
    lloyd_narrating neutral "It’s been several weeks since I was inside the office of a newspaper, and it’s sure to stir up some bittersweet emotions within me."
    # SFX: Camera shutter
    lloyd_narrating neutral "I take a photo of the building once I’m standing outside it."
    lloyd_narrating neutral "It’s nothing particularly impressive – a skyscraper similar to those in the blocks surrounding it, the large sign out front the only thing that indicates anything special about it – but it feels like an appropriate homage to pay before entering."
    lloyd_narrating neutral "I enter one of the revolving doors and already feel like I’m home."
    lloyd_narrating neutral "I’ve already called ahead and arranged to speak with somebody about a story I’ve got."
    lloyd_narrating neutral "The meeting will be a balancing act on razor’s edge."
    lloyd_narrating neutral "Too much information about the man in black and his future plans will get me directed to the police, or dismissed as a crackpot trying to get his name in the news."
    lloyd_narrating neutral "Too little information, and the story won’t have enough juice to entice the reporter."
    scene office_interview_room with slow_dissolve
    lloyd_narrating neutral "The receptionist directs me to one of the many rooms for conducting interviews, telling me that I shouldn’t have to wait long."
    lloyd_narrating neutral "Several minutes pass before the door opens."
    $ swap_sprites("eddie_smiling", slow_dissolve)
    $ current_thought = "eddie_thought_01"
    show screen psychic_powers
    employee "Sorry for the wait –[wait_05] I had to edit some –"
    $ swap_sprites("eddie_angry")
    $ current_thought = "eddie_thought_02"
    employee "Wait...[wait_05]Lloyd fucking Chen?![wait_1] You?!"
    if (check_boolean("eddie_name_learned")):
        menu:
            "I don't believe we've met":
                jump eddie_unrecognised
            "You're Eddie Thompson":
                jump eddie_recognised
    else:
        jump eddie_unrecognised

    return

label eddie_unrecognised:
    lloyd_narrating neutral "The recognition is a surprise."
    lloyd_narrating neutral "This man’s face is a complete mystery to me.[wait_1] If we’ve crossed paths before, I don’t recall when."
    $ current_thought = "eddie_thought_03"
    lloyd friendly "I don’t believe we’ve met.[wait_1] Can I ask how you know me?"
    lloyd_narrating neutral "The man has a camera on him – it’s possible that he’s familiar with my work."
    lloyd_narrating neutral "I didn’t realise that I had enough of a reputation in the industry, though."
    employee "...You’re fucking joking, right?"
    $ current_thought = "eddie_thought_04"
    lloyd friendly "I didn’t realise that my reputation preceded me.[wait_1] May I get your name?"
    employee "Take a guess."
    lloyd_thinking neutral "Is he also someone that I’m supposed to know by reputation?"
    $ current_thought = "eddie_thought_05"
    lloyd friendly "I honestly couldn’t say."
    $ current_thought = "eddie_thought_06"
    employee "You really don’t fucking remember?"
    employee "Multiple years, repeatedly screwing me over, and I’m just a footnote to you."
    employee "The surprising thing is that I can be surprised by the way you act."
    lloyd_thinking neutral "Screwing him over?[wait_1] That can’t be right."
    lloyd_thinking neutral "But I’m not here to settle an old debt.[wait_1] I need to try and calm him down a bit and focus on my goal."
    $ current_thought = "eddie_thought_07"
    lloyd friendly "I don’t recall what you’re talking about, but I’ve come here for a reason.[wait_1] I –"
    $ current_thought = "eddie_thought_08"
    employee "Yeah, good point – why don’t you tell me why you’ve organised this little meeting with me?"
    $ current_thought = "eddie_thought_09"
    lloyd_narrating neutral "I do as he asks, describing the man in black and that he’s a dangerous individual."
    lloyd_narrating neutral "As far as this man knows I’ve heard all of this from a reliable source who’s too afraid to identify themselves."
    lloyd_narrating neutral "Eventually I finish explaining what I can.[wait_1] I’ve provided the bait, now he just has to bite."
    $ current_thought = "eddie_thought_10"
    employee "Cool story.[wait_1] I don’t care."
    $ current_thought = "eddie_thought_11"
    lloyd neutral "What?[wait_1] But surely you –"
    employee "Look, I know that for someone in your position, this must seem like big news, but for someone like me, with an actual job?"
    employee "I’ve got real stories to follow.[wait_1] And I have actual deadlines so –[wait_05] see ya."
    lloyd_narrating neutral "The man stands up and begins leaving.[wait_1] I’m trying to work out what to say that will make him stay when he clears his throat."
    $ current_thought = "eddie_thought_12"
    employee "Oh, and by the way, Chen:[wait_05] I know you won’t bother to look it up, or try to remember, so out of the kindness of my heart –[wait_05] Eddie Thompson."
    $ add_boolean("eddie_name_learned")
    eddie "I also worked at {i}The Brief{/i}.[wait_1] Dick."
    lloyd_narrating neutral "With that connection made, I vaguely recall a coworker who looked like him."
    lloyd_narrating neutral "I can’t think of what our relationship was like or even what his personality was."
    lloyd_narrating neutral "But now’s not the time for that.[wait_1] Eddie is leaving the room and if I want to act, now’s the time."
    menu:
        "Please reconsider":
            $ current_thought = "eddie_thought_13"
            lloyd neutral "Eddie, I’m sorry if I hurt you in the past, but please reconsider."
            lloyd neutral "I’d really like your help with this."
            eddie "Yeah, well I really wanted someone who didn’t fuck me over all the time in the past, so consider this to be me repaying the favour."
        "What are your intentions?" (locked=not check_boolean("eddie_pretend_indifference"), message="You have not read the related thought"):
            lloyd_thinking neutral "Eddie thought to himself that he’s only pretending not to care about the story."
            lloyd_thinking neutral "So what’s he actually going to do with the information I gave him?"
            $ current_thought = "eddie_thought_14"
            lloyd neutral "What are your intentions, Eddie?[wait_1] Are you planning to follow the story?"
            eddie "None of your business, Chen."
    hide screen psychic_powers
    hide eddie_angry with quick_dissolve
    lloyd_narrating neutral "Eddie leaves the room and closes the door behind him."
    lloyd_narrating neutral "I want to go after him but the moment has passed.[wait_1] For now I’ll have to leave."
    lloyd_thinking neutral "If I come back another day, he might be in a better mood.[wait_1] For now I’d better keep moving."
    
    $ visit_person("eddie", "a", 0)
    return

label eddie_recognised:
    lloyd_thinking neutral "I know who he is this time.[wait_1] If I act friendly to him I can gain his trust and make him believe me."
    $ current_thought = "eddie_thought_15"
    lloyd friendly "Eddie?[wait_1] Eddie Thompson?![wait_1] From back at {i}The Brief{/i}?!"
    $ current_thought = "eddie_thought_16"
    eddie "You don’t have to act like you’ve ever considered me a friend, Chen.[wait_1] In fact, I’d rather you just act like your natural self."
    lloyd_thinking neutral "That didn’t work as well as I hoped it would.[wait_1] But I have to stick with it."
    $ current_thought = "eddie_thought_17"
    lloyd friendly "Hey, now, Eddie – that’s not fair.[wait_1] We had plenty of great times at {i}The Brief{/i}, didn’t we?"
    eddie "Oh, sure, there were plenty of great times."
    eddie "At least, for you there might have been.[wait_1] But for me?"
    eddie "There’s a reason that I left for greener pastures – for somewhere that I wouldn’t be repeatedly screwed over."
    $ current_thought = "eddie_thought_18"
    lloyd friendly "Well, that’s –"
    $ swap_sprites("eddie_arrogant")
    $ current_thought = "eddie_thought_19"
    eddie "But enough about my kick-ass job –[wait_05] how about you?[wait_1] What are you up to now?"
    eddie "Oh, that’s right –[wait_05] didn’t I hear something about you getting fired?"
    eddie "Something about how you haven’t gotten any work in months?"
    lloyd neutral "..."
    eddie "Word travels, Chen.[wait_1] And now that the tables have turned, you’ve come crawling to me."
    eddie "Isn’t that right?"
    $ current_thought = "eddie_thought_20"
    lloyd neutral "I didn’t know that you were here, Eddie.[wait_1] Or that you would be assigned to talk to me."
    lloyd_thinking neutral "Or who you were."
    $ current_thought = "eddie_thought_21"
    $ swap_sprites("eddie_angry")
    eddie "...Fine.[wait_1] What have you got?"
    $ current_thought = "eddie_thought_22"
    lloyd_narrating neutral "I tell him that I’ve got a source who believes there’s a killer in the city.[wait_1] I tell him that they’ve already killed at least once."
    lloyd_narrating neutral "I tell him that it’s the sort of story the public love – bloody murders, a compelling mystery, a deadly villain."
    lloyd_narrating neutral "I explain all about the man in black and how if he can be found before he kills again, not only will lives have been saved, but the story will be an exclusive scoop."
    $ current_thought = "eddie_thought_23"
    eddie "...I dunno."
    eddie "Can I talk to your source on this?[wait_1] It’s pretty vague at this point – I need something with a few less unknowns."
    $ current_thought = "eddie_thought_24"
    lloyd neutral "My source is...[wait_05]they’re uncomfortable meeting with anyone.[wait_1] They’re worried that their life is in danger."
    $ current_thought = "eddie_thought_25"
    eddie "And yet they met with you."
    $ current_thought = "eddie_thought_26"
    lloyd neutral "They had to tell someone.[wait_1] Will you look into the story or not?"
    lloyd_narrating neutral "Eddie thinks over it for a few moments.[wait_1] Despite my best efforts he hasn’t fully swallowed the bait."
    lloyd_narrating neutral "I’m starting to think that this might be going nowhere when he nods slowly."
    $ current_thought = "eddie_thought_27"
    eddie "Alright, I can do a little bit of research into this – trying to find out any details of this guy wearing black."
    eddie "Can you come back later tonight?"
    $ current_thought = "eddie_thought_28"
    lloyd neutral "Maybe.[wait_1] My schedule is erratic at the moment."
    $ current_thought = "eddie_thought_29"
    eddie "I guess when you don’t have a job, you can afford to just laze around and do whatever you want, whenever you want."
    lloyd_narrating neutral "Eddie checks the notes that he’s been taking and stands up from the table."
    lloyd_narrating neutral "He doesn’t look any more cheerful than when he first recognised me, but at least he’s on my side."
    $ current_thought = "eddie_thought_30"
    eddie "If you can’t make it, come by tomorrow, or another day.[wait_1] I’ll let you know what I’ve got."
    lloyd neutral "Understood.[wait_1] Thank you, Eddie."
    $ current_thought = "eddie_thought_18"
    eddie "Oh, and Lloyd?"
    lloyd neutral "Yes?"
    eddie "This story had better be fuckin’ worth my time."
    hide eddie_angry with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "With those words of wisdom he leaves the room."
    lloyd_narrating neutral "I have no more reason to stay in this building and exit it."
    scene black_bg with slow_dissolve
    lloyd_thinking neutral "Eddie’s contacts will hopefully be far-reaching, and able to find out information on the man in black."
    lloyd_thinking neutral "But he made it clear that he’s not happy to work with me."
    lloyd_thinking neutral "I can return here later, but will he tell me anything that I couldn’t discover on my own?"

    $ add_boolean("eddie_investigates_docherty")
    $ visit_person("eddie", "a", 0)
    return

label eddie_a_2:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Everything from last night is a blank."
    lloyd_narrating neutral "I have no memory of waking up from my sleep."
    lloyd_narrating neutral "I have no memory of deciding to visit the bar, Icarus, nor of travelling there."
    lloyd_narrating neutral "I have no memory of how my powers backfired or malfunctioned, leaving me with a giant blank spot in my evening."
    lloyd_narrating neutral "But I may be able to fix it.[wait_1] If there was any notable news which would have inspired me to travel to the bar, I would trust a newspaper to know it."
    lloyd_narrating neutral "Was something supposed to happen there later in the night and I left too early?"
    lloyd_narrating neutral "Was the man in black caught and I decided to visit a bar and celebrate?"
    lloyd_narrating neutral "Whatever the reason, I’ll trust them to discern it."
    lloyd_narrating neutral "I head eastwards, the direction of the newspaper."
    lloyd_narrating neutral "It’s overcast and windy today, and I find myself repeatedly looking up at the sky to see whether it’s started raining."
    lloyd_narrating neutral "I can put my camera in a waterproof bag if I need, but I’d feel more comfortable if it didn’t rain at all."
    lloyd_narrating neutral "The weather seems stable for now but that doesn’t mean that I trust it."
    lloyd_narrating neutral "I make it into the skyscraper which hosts the newspaper office without my camera suffering any damage."
    if (person_visited("eddie", "a", 0)):
        lloyd_narrating neutral "I speak to a receptionist on the ground floor about why I’m here."
        lloyd_narrating neutral "I lie today, saying that I’ve got a follow-up interview with Eddie."
        lloyd_narrating neutral "I’m trusting that he’ll be angry enough to see what’s going on, giving me the opportunity to talk to him."
    else:
        lloyd_narrating neutral "I speak to a receptionist on the ground floor, keeping things simple by saying that I’d like to speak to a reporter about a story that I have."
        lloyd_narrating neutral "It takes some cajoling but I’m eventually directed to an interview room and told to wait."
    
    scene office_interview_room with slow_dissolve
    lloyd_narrating neutral "The sight of the office through the glass doors is welcoming.[wait_1] Nothing looks overly restrictive or alien to me."
    lloyd_narrating neutral "I can see somebody browsing a gallery of photos from where I am, and a stab of jealousy runs through me."
    lloyd_narrating neutral "I would be quite comfortable if I were hired by this newspaper."
    lloyd_narrating neutral "I haven’t been in the room for very long before the door opens."
    if (person_visited("eddie", "a", 0)):
        $ swap_sprites("eddie_angry", slow_dissolve)
        $ current_thought = "eddie_thought_31"
        show screen psychic_powers
        lloyd_narrating neutral "Eddie’s the person who steps through it, of course.[wait_1] He looks exactly as I anticipated: angry."
        if (check_boolean("eddie_investigates_docherty")):
            eddie "You’ve got ten seconds to explain why you didn’t show up last night, apologise for wasting my time, and then fuck off outta here, Chen."
            eddie "I mean it."
            $ current_thought = "eddie_thought_32"
            lloyd neutral "I would have come if I could have, Eddie.[wait_1] But there were other matters which took priority."
            eddie "“Other matters”?"
            $ current_thought = "eddie_thought_33"
            lloyd neutral "I had some other promising leads, and I needed to follow them up."
            lloyd_narrating neutral "Eddie slams a fist onto the table.[wait_1] I’m certain that he’s imagining it hitting my face."
            eddie "You had other leads?[wait_1] You got me running errands for you, then decided that somebody else was more important?"
            eddie "Why did I even bother?"
            $ current_thought = "eddie_thought_34"
            lloyd neutral "Does this mean that you were able to find anything about the man in black?"
            eddie "After the shitty description you gave me?[wait_1] Of course not."
            eddie "But we’re not here to talk about why you sent me on a wild goose chase yesterday."
            $ current_thought = "eddie_thought_35"
        eddie "Why the hell did you say you had an interview with me?[wait_1] I’ve got enough real work to do without wasting my time with you."
    else:
        $ swap_sprites("eddie_smiling", slow_dissolve)
        $ current_thought = "eddie_thought_36"
        show screen psychic_powers
        lloyd_narrating neutral "A man wearing a cheap suit enters the room.[wait_1] I try to discern what the brand of camera he’s using is."
        lloyd_narrating neutral "Once I recognise it I have to hold back a judgemental click of the tongue."
        lloyd_narrating neutral "COEUS may make affordable cameras, but the features they offer are inferior to most of their competitors."
        $ current_thought = "eddie_thought_37"
        lloyd_narrating neutral "The man’s smile falls as he takes me in."
        $ swap_sprites("eddie_angry")
        $ current_thought = "eddie_thought_38"
        employee "Lloyd Chen?![wait_1] What the hell are you doing here?"
        lloyd neutral "I’m sorry, you must have me mistaken for somebody else.[wait_1] I don’t believe that we’ve met."
        $ current_thought = "eddie_thought_39"
        lloyd_narrating neutral "A vein throbs in his temple.[wait_1] I hear a knuckle crack as he clenches his fist tighter."
        employee "Are you fucking kidding me?[wait_1] You don’t remember me?"
        employee "Fuck, I knew that you didn’t give a shit about anybody but yourself, but I thought you at least deigned to remember the names of people around you."
        employee "But I guess you’re just too damn good for the rest of us, huh?"
        lloyd_narrating neutral "My mind races, trying to recall when I’ve seen this man before.[wait_1] I take a stab in the dark."
        $ current_thought = "eddie_thought_40"
        lloyd neutral "I do remember you.[wait_1] We both worked at {i}The Brief{/i}."
        employee "And my name is?"
        lloyd thinking "It’s...[wait_1]"
        $ current_thought = "eddie_thought_41"
        employee "Eddie Thompson.[wait_1] I’d tell you to remember it this time, but I already know that you won’t."
        lloyd_narrating neutral "He sighs and takes a seat."
        eddie "I’m already here, so you might as well get talking."
        eddie "What’s this important story that you have for me?"
    $ current_thought = "eddie_thought_42"
    lloyd neutral "I’m hoping that you can give me some ideas about what I was up to last night."
    $ swap_sprites("eddie_unimpressed")
    eddie "The hell do you mean by that?[wait_1] If you can’t keep track of how you spend your evenings, that’s your problem."
    $ current_thought = "eddie_thought_43"
    lloyd neutral "Let me explain.[wait_1] I went to bed last night shortly after I returned home."
    lloyd neutral "I had been out for the entirety of the day and was fairly tired, so I fell asleep quickly."
    lloyd_narrating neutral "Eddie looks unimpressed.[wait_1] I hasten up the story."
    $ current_thought = "eddie_thought_44"
    lloyd neutral "An unknown amount of time later I woke up.[wait_1] You’d think that I would find myself still in bed.[wait_1] But I was at a bar."
    lloyd neutral "I have no memory of how I got there or what I had been doing there.[wait_1] And so –"
    eddie "And so, what?"
    eddie "You think there’s a story in how you got so wasted that you couldn’t remember your evening?"
    eddie "You want me to write up an article about how you can’t hold your drinks?"
    eddie "Or do you want me to stop the presses, tell everybody about my exclusive news:[wait_05] “Local Man Wastes My Time.”"
    $ current_thought = "eddie_thought_45"
    lloyd neutral "I’d like to know what your thoughts are on what happened."
    lloyd neutral "Was there some notable event at that bar that inspired me to travel there?"
    if (person_visited("eddie", "a", 0)):
        lloyd neutral "Did I send you a message explaining why I was going there?"
    lloyd neutral "Did any news come in that would have made me want to celebrate?"
    $ swap_sprites("eddie_angry")
    $ current_thought = "eddie_thought_46"
    eddie "This is a fucking joke, right?"
    eddie "You think that this is –[wait_05] I’m not a mind-reader, Chen."
    eddie "I don’t know what the fuck goes on in your head, like why you’d decide to get up and go to a bar in the middle of the night."
    eddie "I can tell you why you don’t remember any of it, though –[wait_05] it’s called drinking too much."
    eddie "Try slowing down and having some water next time, you idiot."
    lloyd_thinking thinking "He’s wrong about that.[wait_1] I lost my memories because of my psychic abilities."
    lloyd_thinking thinking "But I can’t tell him that."
    $ current_thought = "eddie_thought_47"
    lloyd neutral "Even so, don’t you find it odd that I would go to that particular bar?[wait_1] It was a long distance from my apartment."
    lloyd neutral "It’s not the sort of thing you’d go to on a whim."
    $ swap_sprites("eddie_unimpressed")
    eddie "What’s the name of this bar?[wait_1] And how far away is it?"
    lloyd neutral "It’s called Icarus.[wait_1] It’s far away enough that I travelled to it by train; it would take at least an hour or more to reach it on foot."
    $ swap_sprites("eddie_smiling")
    eddie "Great![wait_1] You know where it is, and how to get to it!"
    eddie "So that means that you can go back to it, and bother whoever the fuck is working the day shift with your problems!"
    eddie "Tell them all about this shit, and we’ll see whether them telling you to drink less will actually sink in."
    $ current_thought = "eddie_thought_48"
    lloyd neutral "Are you certain that you haven’t heard of it before, Eddie?"
    lloyd neutral "You’ve never heard of the name Icarus, or a reason for me to go there?"
    $ swap_sprites("eddie_angry")
    eddie "How many times do I need to tell you?![wait_1] No!"
    eddie "I don’t know the bar, and I don’t care about it!"
    eddie "You know what your problem is, Chen?"
    lloyd_thinking thinking "I shouldn’t respond to this."
    $ current_thought = "eddie_thought_49"
    lloyd neutral "What?"
    eddie "You’re just way too fucking selfish.[wait_1] All you care about is yourself."
    eddie "Because you know what?[wait_1] I actually get it."
    eddie "From what you’ve said, it must have been pretty creepy to wake up somewhere and have no idea how you got there."
    eddie "I get why you’d want to know what happened and to get some help in finding it out.[wait_1] I get it."
    eddie "But what I don’t get is why you’ve decided to crash my day and derail my work."
    eddie "I don’t get why you think that I –[wait_05] and probably every other person in your life –[wait_05] should just drop everything that they’re doing to help you out."
    eddie "It’s just –[wait_05] what is wrong with you?"
    hide eddie_angry with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "Before I can respond, he stands up and leaves the room."
    lloyd_narrating neutral "I know that he won’t be coming back."
    lloyd_thinking neutral "...Maybe he does have a bit of a point."
    lloyd_thinking neutral "Coming here to ask Eddie for assistance with this was a waste of time."
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "With Eddie gone I’m not particularly hopeful that I’ll be able to discover the information I need at the newspaper."
    lloyd_narrating neutral "I leave the building and start thinking about my next destination."

    $ visit_person("eddie", "a", 1)
    return

label eddie_a_3:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Cat was able to find out information about the man in black’s first two victims for me, but I couldn’t find a connection between them."
    lloyd_narrating neutral "There’s no reason that I can see for why he chose to kill the two of them."
    lloyd_narrating neutral "If I can find out more about his third victim –[wait_05] the man with the white streak –[wait_05] then I should be able to discover the commonalities between them."
    lloyd_narrating neutral "With that I’ll be able to narrow down who his next target will be."
    lloyd_narrating neutral "Newspapers are excellent sources of information."
    lloyd_narrating neutral "It’s possible that there’s already a story about the man with the white streak being written by a reporter at present."
    lloyd_narrating neutral "Seeing the article in progress might give me all that I need to solve this puzzle and make more progress towards stopping the man in black."
    lloyd_narrating neutral "The weather is warm and sunny today as I make my way eastwards towards the newspaper."
    lloyd_narrating neutral "The jackhammer of a construction crew assaults my ears as I wait at an intersection."
    lloyd_narrating neutral "I briefly scan the workers but nothing about them stands out as being worthy of a photo."
    lloyd_narrating neutral "Eventually the light turns green and I continue onwards."
    if (not person_visited("eddie", "a", 0) and not person_visited("eddie", "a", 1)):
        lloyd_narrating neutral "I’ve already called ahead and made an appointment with the newspaper, saying that I’ve got a story to share with a reporter."
        lloyd_narrating neutral "On reaching the skyscraper which holds their offices a receptionist directs me to a small room for interviews."
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "It wasn’t too long ago that I was in a room similar to this at a different newspaper.[wait_1] Things didn’t work out so well then."
        lloyd_narrating neutral "I’m hoping that this will go better."
        $ swap_sprites("eddie_smiling", slow_dissolve)
        $ current_thought = "eddie_thought_36"
        show screen psychic_powers
        employee "Sorry for the wait –[wait_05] the reporters are all –"
        $ swap_sprites("eddie_angry")
        $ current_thought = "eddie_thought_37"
        employee "Chen?![wait_1] What the hell are you doing here?!"
        lloyd_thinking thinking "Have I met this man before?[wait_1] I don’t think so."
        lloyd_thinking "I’d definitely remember if I knew somebody who owned a camera with that many flaws."
        $ current_thought = "eddie_thought_39"
        lloyd neutral "My apologies, I think that you’ve mistaken me for somebody else."
        employee "As if I could ever forget you, Chen. Not after what you did to me."
        lloyd neutral "I’m sorry, but I have no idea what you’re talking about."
        employee "Of course not.[wait_1] You’d never deign to think about anybody other than yourself, would you?"
        employee "Does the name Eddie Thompson help clarify things for you?"
        $ current_thought = "eddie_thought_50"
        lloyd neutral "...Is that who you are?"
        eddie "Of course it is![wait_1] God, you’re the fucking worst!"
        lloyd_narrating neutral "Despite his issues with me he pulls out a seat and sits down."
        $ current_thought = "eddie_thought_41"
        eddie "What are you even here for, Chen?"
    elif (person_visited("eddie", "a", 1)):
        lloyd_narrating neutral "Once I reach the newspaper I’m directed to the same room which I spoke to Eddie in yesterday."
        lloyd_narrating neutral "I’m a little surprised that I’m still granted access; I half-expected Eddie to tell the receptionist not to let me in."
        lloyd_narrating neutral "Either he hasn’t thought to do so or he doesn’t have enough pull around here to do so."
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "I hear furious stomping approaching the interview room from what feels like a kilometre away."
        lloyd_narrating neutral "It’s safe to say that Eddie has been asked to talk to me again."
        $ swap_sprites("eddie_angry", slow_dissolve)
        $ current_thought = "eddie_thought_51"
        show screen psychic_powers
        eddie "I’m going to save us both some time, Chen.[wait_1] Get the hell out of here, now."
        eddie "You can ask somebody else to help find your toothbrush, or tie your shoelaces, or whatever fucking mundane task you need assistance with."
        eddie "I’m not helping you."
        lloyd neutral "Hi, Eddie.[wait_1] I think that you’ll be much more interested in why I’m here today."
        $ swap_sprites("eddie_unimpressed")
        eddie "Nope.[wait_1] Don’t care."
        eddie "You had your chance to impress me yesterday and you wasted it."
        $ current_thought = "eddie_thought_52"
        eddie "I don’t care if you’ve found a cache of gold and you want to donate it to me; I’m not listening.[wait_1] And you’re leaving.[wait_1] Now."
        menu:
            "I’ll pay you to listen" (locked=not check_boolean("eddie_bribeable"), message="You have not read the related thought"):
                $ current_thought = "eddie_thought_53"
                lloyd neutral "I’ll pay you to listen to me."
                eddie "What?"
                lloyd_narrating neutral "I take a note out from my wallet and place it on the table."
                $ current_thought = "eddie_thought_54"
                lloyd neutral "This could be yours, Eddie.[wait_1] All that you have to do is listen to me and decide whether it’s worth your time or not."
                eddie "...Fine."
                eddie "Tell me what you’re here for, Chen."
            "This assignment will impress people":
                $ current_thought = "eddie_thought_55"
                lloyd neutral "This will be worth your while, Eddie.[wait_1] It will really impress your co-workers."
                eddie "Just like yesterday’s meeting was really impressive?[wait_1] I’m not falling for this."
                eddie "Get out of here now, or I’m calling security."
                $ current_thought = "eddie_thought_56"
                lloyd neutral "There have been several dead –"
                $ swap_sprites("eddie_angry")
                eddie "Nope.[wait_1] Don’t care.[wait_1] Out with you."
                hide eddie_angry with quick_dissolve
                hide screen psychic_powers
                scene black_bg with slow_dissolve
                lloyd_narrating neutral "Eddie does everything short of physically assaulting me to get me out of my seat and subsequently out of the office."
                lloyd_narrating neutral "I take the hint and leave the building."
                lloyd_thinking thinking "That didn’t go so well.[wait_1] It might not be worth returning here tomorrow if this is how he’s feeling about me."
                $ visit_person("eddie", "a", 2)
                $ add_boolean("eddie_ejects_lloyd")
                return
    elif (person_visited("eddie", "a", 0)):
        lloyd_narrating neutral "Just like the other day, I’ve called ahead of time and made an appointment."
        lloyd_narrating neutral "The receptionist at the newspaper directs me to the same room as last time and asks me politely to wait."
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "I haven’t been in the room for very long before the door opens and a familiar face steps through."
        $ swap_sprites("eddie_angry", quick_dissolve)
        $ current_thought = "eddie_thought_31"
        show screen psychic_powers
        eddie "Chen."
        lloyd neutral "Hello, Eddie.[wait_1] How are you doing?"
        eddie "Not good, Chen.[wait_1] Not very fucking good."
        eddie "Do you want to take a guess why?"
        $ current_thouhgt = "eddie_thought_57"
        lloyd neutral "You’ve realised that you should have purchased a more reliable camera brand?"
        if (check_boolean("eddie_investigates_docherty")):
            eddie "Nice guess."
            $ current_thought = "eddie_thought_58"
            eddie "No, I’m not doing well because I just got told that the guy I went out of my way to help has shown up."
            eddie "The same guy who asked me to do research that was supposedly important, but not so important that he could be bothered to check in on me and see what I’d uncovered."
            eddie "Sound like somebody you know, Chen?"
            $ current_thought = "eddie_thought_32"
            lloyd neutral "I’m sorry, Eddie.[wait_1] There were other priorities that evening, and I –"
            eddie "Great.[wait_1] Fucking great!"
            eddie "I’m so glad to hear that there were other priorities!"
            eddie "Obviously one of them wasn’t letting me know not to hang around here for so long, but as long as you got to deal with your priorities."
            eddie "That’s the important thing, right?"
            $ current_thought = "eddie_thought_59"
            lloyd neutral "How long were you waiting for, Eddie?"
            lloyd_narrating neutral "He snorts."
            eddie "Oh, you know, just until 9 PM or so."
            eddie "I’d been thinking since around 7 that you might not show up, but I thought, “You know what? He really emphasised that this is important.”"
            eddie "“I should trust him.[wait_1] If it’s so important, he wouldn’t just leave me out to dry!”"
            lloyd neutral "Were you waiting because you did have something to tell me?[wait_1] Did you discover anything about the man in black?"
            lloyd_narrating neutral "This time Eddie scoffs before responding."
            $ current_thought = "eddie_thought_60"
            eddie "Of fucking course not."
            eddie "You think that I could find out information that quickly when all that you’ve given me is a vague description?"
            eddie "I was waiting for you so I could tell you that you needed to get more from your source."
            $ current_thought = "eddie_thought_61"
            lloyd neutral "I have good news for you then, Eddie."
            lloyd neutral "My source has given me more information."
            eddie "...Alright, let’s hear it then.[wait_1] Tell me about it."
        else:
            eddie "Very funny.[wait_1] No, I’m not doing well because I have to deal with you."
            eddie "I suppose you want to ask me to look into your weirdo in black?"
            lloyd neutral "The one who’s killed several people, yes."
    if (not person_visited("eddie", "a", 0)):
        $ current_thought = "eddie_thought_62"
        lloyd neutral "I’ve been looking into an important story recently."
        lloyd neutral "A killer, loose in the city."
        lloyd neutral "I’ve got a source who has given me some information about them, and I want to stop them."
        $ swap_sprites("eddie_unimpressed")
        eddie "You?[wait_1] Looking into a story?"
        eddie "Last I heard you were unemployed, Chen."
        eddie "Is this how you think you get back into the big leagues?[wait_1] You buy your way in with some exaggerated story about a killer?"
        eddie "Don’t let yourself react to that, Lloyd."
        $ current_thought = "eddie_thought_63"
        lloyd neutral "Are you saying that you can accept a killer on the loose, Eddie?"
        eddie "No, but it’s not my job to stop them.[wait_1] My job is taking the best photos possible for the paper."
        $ current_thought = "eddie_thought_64"
        lloyd neutral "So you’d be fine with me getting photos for this story?"
        eddie "...Go on."
    $ current_thought = "eddie_thought_65"
    lloyd neutral "My source has dug up some information on the killer’s prior victims.[wait_1] Their deaths were reported in some news articles."
    lloyd neutral "But there’s a problem:[wait_05] we don’t know why they were targeted.[wait_1] They don’t seem to have anything in common."
    eddie "So the killer’s a nutjob who’s killing for the fun of it."
    eddie "A wanna-be Jack the Ripper.[wait_1] Duh."
    $ current_thought = "eddie_thought_66"
    lloyd neutral "Maybe.[wait_1] But would you want to bet the life of their next victim on that idea?"
    lloyd neutral "Or would you rather assume that the connection between the victims is hidden?"
    eddie "...I guess that it could be something to look into, yeah."
    $ current_thought = "eddie_thought_67"
    lloyd_narrating neutral "I take out my phone and pass it to him.[wait_1] The first of the articles Cat sent me is on it."
    $ current_thought = "eddie_thought_68"
    lloyd neutral "This is the story about the first victim.[wait_1] There aren’t many –"
    eddie "You’re reading stories by {i}The DB!{/i}?[wait_1] You should know that they’re a shitty news source."
    lloyd neutral "Maybe so, but at least they’ve got a story on this."
    eddie "It’s not much.[wait_1] Might as well not have a story at all."
    $ current_thought = "eddie_thought_69"
    lloyd neutral "Exactly.[wait_1] If you could look into these victims and find out more about them than {i}The DB!{/i}..."
    eddie "...then you reckon I can find out the connection."
    eddie "Hmm.[wait_1] Not bad, Chen."
    $ current_thought = "eddie_thought_70"
    lloyd neutral "There’s something else.[wait_1] The man in black has killed another person beyond these two."
    eddie "Any articles on that victim?"
    lloyd_thinking thinking "Should I have asked Cat to look up the man with the white streak last night?"
    lloyd neutral "Not to my knowledge.[wait_1] But I know who it was."
    eddie "You do?[wait_1] What was their name?"
    $ current_thought = "eddie_thought_71"
    lloyd neutral "I don’t know."
    eddie "Jesus Christ, Chen."
    eddie "One of your fuckin’ friends gets killed and you don’t even care about them enough to remember their name?"
    eddie "Bad enough that you forgot my name, but this is another fuckin’ level.[wait_1] You’re unbelievable."
    $ current_thought = "eddie_thought_72"
    lloyd neutral "It’s not like that.[wait_1] I ran into the victim as he was bleeding out."
    lloyd neutral "It’s how I was drawn into this."
    eddie "That still doesn’t help us.[wait_1] If he’s dead, he’s dead."
    lloyd neutral "But you can research who he was, can’t you?"
    eddie "Not if you don’t know who he was."
    lloyd neutral "I may not know who he was, but I can give you a physical description of him."
    eddie "Hmm.[wait_1] Not much that I can do with that."
    eddie "But sure, give it to me anyway."
    lloyd_narrating neutral "I describe the man with the white streak in detail to Eddie."
    lloyd_narrating neutral "I describe his soul patch, the gap in his teeth, and of course the streak in his hair."
    lloyd_narrating neutral "I make sure to describe his clothes and build as well."
    lloyd_narrating neutral "(I don’t bother adding in that he’s Caucasian.[wait_1] Eddie will automatically assume that he is.)"
    lloyd_narrating neutral "When I’m done, Eddie doesn’t look any happier."
    $ current_thought = "eddie_thought_73"
    eddie "Yeah, there’s not much that I can do with that."
    eddie "Still, I’ll see what I can find out about these other victims.[wait_1] Something might come up once I do a bit of digging."
    $ current_thought = "eddie_thought_74"
    lloyd neutral "Thank you, Eddie.[wait_1] Should I return this evening?"
    if (check_boolean("eddie_investigates_docherty")):
        eddie "What, like you were going to return the other day?[wait_1] No, I’m not falling for that again."
    else:
        eddie "What, you think I can get all of this information that quickly?[wait_1] Like I need that pressure."
    lloyd neutral "Very well.[wait_1] I’ll return when I can, then."
    $ current_thought = "eddie_thought_75"
    $ swap_sprites("eddie_unimpressed")
    eddie "Wait, Chen.[wait_1] Before you go..."
    lloyd neutral "Yes?"
    if (person_visited("eddie", "a", 1)):
        lloyd_narrating neutral "Eddie’s hand reaches out and takes the note on the table."
        eddie "Don’t forget to bring more of these next time."
    elif (check_boolean("eddie_investigates_docherty")):
        eddie "My camera’s plenty reliable.[wait_1] Don’t go dismissing it just because you can’t work out all the settings."
    else:
        eddie "This story had better be worth my damn time."
    hide eddie_unimpressed with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Eddie’s been given his assignment.[wait_1] There’s nothing else for me to do here."
    lloyd_narrating neutral "I leave the building and think about what to do next."

    $ visit_person("eddie", "a", 2)
    return

label eddie_a_b_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "It’s the fourth day of my investigation and I haven’t found any information to stop the killer."
    lloyd_narrating neutral "I don’t know who his next victim will be.[wait_1] I don’t know what his name is or where he is."
    if (branch == "a"):
        lloyd_narrating neutral "I barely know anything about his previous victims, and I don’t know why he killed them."
        lloyd_narrating neutral "What I do know is the man with the white streak’s name."
        lloyd_narrating neutral "I don’t know enough about who he was as a person, but with a bit of research I can learn what sort of person he was, and then possibly why he was targeted by the man in black."
        lloyd_narrating neutral "To do that I’m going to head to the newspaper and find whatever information I can."
    elif (branch == "b"):
        lloyd_narrating neutral "I barely know anything about his previous victims."
        lloyd_narrating neutral "What I do know is why he targeted them.[wait_1] The man in black is killing people with psychic abilities."
        lloyd_narrating neutral "I need to find others with my powers, and to do that I’m going to head to the newspaper and discover what I can."
    lloyd_narrating neutral "I head eastwards towards the skyscraper that the newspaper’s offices are located in."
    lloyd_narrating neutral "It’s tall enough to be seen from multiple blocks away, looming over them like a dragon before a terrified village."
    lloyd_narrating neutral "The skyscraper was erected more than seventy years ago, and the newspaper has held offices within it for more than sixty of those years.[wait_1] In that time over a million stories have been written and published within its walls."
    lloyd_narrating neutral "Will I find the story that I’m looking for today?"
    if (not person_visited("eddie", "a", 0) and not person_visited("eddie", "a", 1) and not person_visited("eddie", "a", 2)):
        lloyd_narrating neutral "I enter the newspapers’ lobby and marvel at how modern it is."
        lloyd_narrating neutral "I’ve been thinking of seeking information here for several days but have always found other places to prioritise."
        lloyd_narrating neutral "I have a slight sense of regret at that now; it’s a nice building."
        lloyd_narrating neutral "I’ve already called ahead and said that I’d like to speak to somebody about a story.[wait_1] The receptionist directs me to a small room used for interviews, and asks me to wait patiently."
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "I don’t have to wait long before the interviewer arrives."
        $ swap_sprites("eddie_smiling", slow_dissolve)
        $ current_thought = "eddie_thought_36"
        show screen psychic_powers
        employee "Hi.[wait_1] I hear you’ve got a story?" 
        employee "I’m not a reporter, but I –"
        $ current_thought = "eddie_thought_37"
        lloyd_narrating neutral "His smile disappears as he takes me in, replaced with a look of rage."
        $ swap_sprites("eddie_angry")
        employee "Chen?![wait_1] You’re the person I have to talk to?"
        lloyd_thinking thinking "How does he know my name?[wait_1] I’ve never seen this man before in my life."
        $ current_thought = "eddie_thought_39"
        lloyd neutral "Yes, that’s correct.[wait_1] And you are?"
        lloyd_narrating neutral "I hold my hand out but he ignores it."
        employee "You don’t remember me?[wait_1] You’re fucking...[wait_05]no, of course you’re not kidding."
        employee "You’re serious, aren’t you?[wait_1] You seriously don’t remember me."
        lloyd_thinking thinking "Bad camera, cheap suit...[wait_05]where would I know him from?"
        $ current_thought = "eddie_thought_76"
        lloyd neutral "Sorry...[wait_05]were you the photographer at a wedding I attended?[wait_1] I don’t –"
        employee "I’m working at a newspaper and you think that you know me from a fucking wedding?"
        employee "You can’t comprehend anybody being even close to the pedestal you’ve placed yourself on, can you, Chen?"
        lloyd neutral "Where did we meet, then?"
        employee "Think back to your days at {i}The Brief{/i}.[wait_1] Does the name Eddie Thompson ring a bell?"
        lloyd_narrating neutral "The name is vaguely familiar.[wait_1] The face isn’t."
        $ current_thought = "eddie_thought_77"
        lloyd friendly "Of course![wait_1] Sorry, Eddie –[wait_05] it’s been so long![wait_1] I’m so sorry!"
        lloyd_narrating neutral "He grunts and sits down at the table."
        eddie "So, what do you have for me?"
    elif (person_visited("eddie", "a", 0) and not person_visited("eddie", "a", 1) and not person_visited("eddie", "a", 2)):
        lloyd_narrating neutral "I enter the building’s lobby and speak to the receptionist."
        lloyd_narrating neutral "I tell her that I’d like to speak to Eddie Thompson about something important, and I’m directed to the same room that I was in the other day."
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "I don’t hear Eddie approaching the room.[wait_1] That tells me that he hasn’t realised that I’m the person who’s arranged the meeting yet."
        $ swap_sprites("eddie_angry", slow_dissolve)
        $ current_thought = "eddie_thought_78"
        show screen psychic_powers
        eddie "Chen.[wait_1] Why am I not surprised that it’s you here?"
        lloyd_narrating neutral "Hello, Eddie.[wait_1] I apologise if I’m interrupting anything."
        if (check_boolean("eddie_investigates_docherty")):
            eddie "“If” you’re interrupting anything?[wait_1] Do you think that I spend all my time just lounging around, waiting for you to visit me?"
            eddie "Some of us have actual work to do, you know.[wait_1] We don’t sit around idling, only doing stuff when it suits us."
            eddie "We take other peoples’ schedules into account."
            lloyd neutral "Are you referring to something specific?"
            $ current_thought = "eddie_thought_59"
            eddie "Oh, you reckon, smart guy?[wait_1] Could it maybe have something to do with the other day, when I waited here for you all night?"
            lloyd neutral "I’m sorry, Eddie.[wait_1] I didn’t realise that you waited here that late."
            eddie "What did you think would happen?[wait_1] That I’d just get bored and leave at 5:30?"
            eddie "Of course I didn’t –[wait_05] I stayed here, because I’m not you."
            $ current_thought = "eddie_thought_32"
            lloyd neutral "There were other priorities that –"
            eddie "Oh, other priorities my ass."
            eddie "You just couldn’t be bothered thinking of anybody else.[wait_1] Again."
            lloyd neutral "If I’d come past would you have had information for me?[wait_1] On the man in black?"
            $ swap_sprites("eddie_unimpressed")
            $ current_thought = "eddie_thought_60"
            eddie "No, but that’s besides the point, isn’t it?[wait_1] You hung me out to dry, Chen."
            $ current_thought = "eddie_thought_79"
            lloyd neutral "Are you willing to look past that and help me out today?"
            lloyd_narrating neutral "Eddie thinks about it for several moments, then pulls out a chair and sits down."
            eddie "God knows I fucking shouldn’t.[wait_1] But I’m too damn nice."
            eddie "Tell me what you want, Chen."
        else:
            eddie "Well, the apology makes it all better then, doesn’t it?[wait_1] Justifies me putting my other work on hold and dropping everything for you."
            lloyd neutral "If you’re busy then I –"
            eddie "Oh, shut it, Chen.[wait_1] Stop pretending that you actually care; it’s a worse look on you than when you transparently use people."
            lloyd_narrating neutral "He pulls out a chair and sits down."
            eddie "Just make it fast, and let’s get through it quickly.[wait_1] You’re just lucky that my editor’s in a shitty mood with me right now."
            lloyd_thinking thinking "If his editor is responsible for this then it’s all the better for me."
            lloyd_thinking thinking "I don’t know what I would have done if he had said he was too busy and left."
        lloyd neutral "I’ve already told you that I was looking into a killer.[wait_1] But there’s something else that I haven’t told you."
    elif (person_visited("eddie", "a", 1) and not person_visited("eddie", "a", 2)):
        lloyd_narrating neutral "I enter the building’s lobby."
        lloyd_narrating neutral "I’ve already called ahead and asked whether I can speak to Eddie, and the receptionist has agreed to arrange something.[wait_1] I’m directed to the same room that I was in last time."
        scene office_interview_room with slow_dissolve
        lloyd_narrating neutral "Eddie looks furious as he approaches the room."
        lloyd_narrating neutral "I think for a moment that he’ll walk past the glass doors once he recognises me through them, ignoring me completely."
        lloyd_narrating neutral "To my surprise he opens them, albeit more forcefully than he should."
        $ swap_sprites("eddie_angry", slow_dissolve)
        $ current_thought = "eddie_thought_51"
        show screen psychic_powers
        eddie "Hey, Chen.[wait_1] You want to tell me why you’re interrupting my work day today?"
        eddie "Need a hand finding a coin that rolled under your couch?[wait_1] Or do you need me to open a jar for you?"
        lloyd neutral "I’m sorry, Eddie.[wait_1] I don’t think that this will take too long."
        eddie "Finally, something we can agree on![wait_1] I’ll give you ten seconds to leave before I call security."
        eddie "You can’t just trick people into organising meetings and expect there to be no consequences."
        lloyd neutral "What if this meeting could be beneficial to you, Eddie?"
        $ current_thought = "eddie_thought_80"
        eddie "You think I’m going to fall for that, Chen?[wait_1] I don’t care what you’re selling –[wait_05] I’m not buying it." 
        eddie "Ten."
        $ current_thought = "eddie_thought_81"
        lloyd neutral "I have a story that I need your help with, Eddie."
        eddie "Nine.[wait_1] Eight."
        $ current_thought = "eddie_thought_82"
        lloyd neutral "It could be big.[wait_1] But I’ve hit a wall."
        eddie "Seven.[wait_1] Six."
        lloyd_thinking thinking "He’s not going to listen.[wait_1] What can I say to convince him?"
        menu:
            "Have some money" (locked=not check_boolean("eddie_bribeable_2"), message="You have not read the related thought"):
                $ current_thought = "eddie_thought_83"
                lloyd neutral "I’ll pay you to listen to me.[wait_1] How does that sound?"
                lloyd_narrating neutral "Eddie pauses in his countdown, but doesn’t say anything else.[wait_1] I take a note out of my wallet and place it on the table."
                $ current_thought = "eddie_thought_84"
                lloyd neutral "How about it?"
                $ swap_sprites("eddie_unimpressed")
                eddie "...Fine.[wait_1] Tell me what you want, Chen."
            "I’ll let you take credit":
                $ current_thought = "eddie_thought_85"
                lloyd neutral "I’ll let you take credit for the story, Eddie."
                eddie "Five.[wait_1] Four."
                lloyd neutral "You can present the whole thing as yours.[wait_1] I won’t even be around when you do."
                eddie "Three.[wait_1] Two."
                lloyd_thinking thinking "He’s not listening.[wait_1] Is he actually going to call security?"
                $ current_thought = "eddie_thought_86"
                eddie "One.[wait_1] Alright, Chen, that’s –"
                lloyd scared "Wait![wait_1] I –[wait_05] alright, Eddie, you win." 
                lloyd scared "I’ll leave."
                $ swap_sprites("eddie_smiling")
                $ current_thought = "eddie_thought_87"
                eddie "Good.[wait_1] And don’t come back, Chen."
                hide eddie_smiling with quick_dissolve
                hide screen psychic_powers
                scene black_bg with slow_dissolve
                lloyd_narrating neutral "I leave the building before Eddie thinks that I’m going to try anything tricky."
                lloyd_narrating neutral "My visit here was a complete waste of time."
                $ visit_person("eddie", "a", 3)
                return
    elif (person_visited("eddie", "a", 2)):
        lloyd_narrating neutral "I enter the building’s lobby, confident that I can convince the receptionist to let me in to see Eddie once again."
        if (check_boolean("eddie_ejects_lloyd")):
            lloyd_narrating neutral "I’m subsequently surprised when I’m told that I’m not allowed in to see Eddie, or any other employees, unless I’ve been invited."
            lloyd_thinking thinking "I pushed Eddie to his limit more than I realised.[wait_1] I should have seen this coming."
            lloyd_narrating neutral "There’s nothing else for me to do here."
            lloyd_narrating neutral "I leave the building and start thinking about what to do next."
            $ visit_person("eddie", "a", 3)
            return
        else:
            lloyd_narrating neutral "I’m directed to the same room that I was in yesterday, and once again told to be patient."
            lloyd_narrating neutral "To my surprise, Eddie is already in the room when I arrive."
            scene office_interview_room with slow_dissolve
            $ swap_sprites("eddie_unimpressed", slow_dissolve)
            $ current_thought = "eddie_thought_88"
            show screen psychic_powers
            eddie "Took you long enough, Chen."
            lloyd neutral "Eddie.[wait_1] How did you know that I was coming at this time?"
            eddie "Call it a hunch, Chen.[wait_1] Or maybe you’re just predictable."
            eddie "You want to do this thing or not?"
            lloyd neutral "Of course."
            lloyd_narrating neutral "I pull out a chair and sit down.[wait_1] I notice as I do that Eddie has a manilla folder in front of him."
            $ current_thought = "eddie_thought_89"
            lloyd neutral "I take it that the information you’ve discovered is in there?"
            lloyd_narrating neutral "Eddie scoffs."
            eddie "I’ve got some stuff, but I doubt it’s anything you really care about."
            eddie "A combination of the information the cops released to the press, with a bit extra on top that I was able to find out from a mate of mine who knows a guy."
            lloyd neutral "Anything you have could be important."
            eddie "You sure?[wait_1] Because most of this is just the gory details –[wait_05] the exact injuries your two victims suffered, some stuff the coroner found."
            eddie "Before you ask –[wait_05] no, they didn’t find anything unusual during the autopsy.[wait_1] The injuries and states of the bodies were exactly what you’d expect for gunshot victims."
            lloyd_thinking thinking "It doesn’t sound as though much of that is relevant."
            lloyd neutral "How about the other person I asked about?[wait_1] The man with the white streak."
            lloyd_narrating neutral "Eddie sighs and puts the folder away."
            $ current_thought = "eddie_thought_90"
            eddie "Yeah, him.[wait_1] I couldn’t find shit on him."
            eddie "I’m gonna need more than that if you want me to start digging into him."
            lloyd neutral "I was able to find out a little more yesterday."
            eddie "You were?![wait_1] Fucking hell, Chen, don’t just sit on it." 
            eddie "What have you got?"
    if (not person_visited("eddie", "a", 0) and not person_visited("eddie", "a", 2)):
        $ current_thought = "eddie_thought_62"
        lloyd neutral "There’s something that I’ve been looking into.[wait_1] Several people have been murdered recently by an unknown killer."
        eddie "And, what, you think you can be the one to find the killer?[wait_1] You’ll be the one to write up the big story about it?"
        lloyd neutral "Call it a hunch that I can identify the killer."
        $ current_thought = "eddie_thought_63"
        eddie "Sure you fucking can.[wait_1] In your eyes you’re able to solve crimes that should be left to the cops."
        eddie "You probably think that you can take on serial killers and not only stop them, but get all of the evidence needed to put them away for good."
        eddie "Because nothing you ever do is wrong, is it, Chen?"
        lloyd neutral "I’m not infallible.[wait_1] But I do have a lead that nobody else does."
        $ current_thought = "eddie_thought_91"
        eddie "And you reckon that you can find the killer using it?"
        lloyd neutral "Maybe.[wait_1] But I’ll need your assistance."
        eddie "Hmm.[wait_1] I’d rather not give it."
        eddie "But tell me what you need."
    if (not person_visited("eddie", "a", 2)):
        $ current_thought = "eddie_thought_92"
        if (branch == "a"):
            lloyd neutral "I encountered the killer’s most recent victim before he died.[wait_1] I also recently discovered what his name is."
            eddie "So?"
            lloyd neutral "I know very little about him beyond his name and physical appearance.[wait_1] If I can find out more about him then I might be able to deduce why he was targeted."
            lloyd neutral "Therefore, the potential next target of the killer will be narrowed down."
            lloyd_narrating neutral "Eddie lets out a short, sharp bark."
            $ current_thought = "eddie_thought_93"
            eddie "What, you have some sort of magical database that’s just filled with information about all sorts of people in the city?"
            eddie "And you can just input whatever fuckin’ info you get and get a list of potential targets from that?"
            eddie "Get fuckin’ real, Chen."
            $ current_thought = "eddie_thought_94"
            lloyd neutral "The information I discover about him could make the targets more obvious.[wait_1] It’s better than nothing."
            eddie "I kinda fucking doubt that.[wait_1] I think nothing would be better in this case."
            eddie "I know you think that you can’t do any wrong, Chen, but if you don’t listen to me and stop looking into this you’ll damn well regret it."
            lloyd neutral "Even so, I’d rather do something than nothing."
            $ current_thought = "eddie_thought_95"
            lloyd_narrating neutral "Eddie closes his eyes and sighs deeply."
            eddie "Fine.[wait_1] Tell me what you want me to do."
        else:
            lloyd neutral "I encountered the killer’s most recent victim before he died."
            lloyd neutral "With the information that I’ve discovered I believe that I know what the killer’s motivation is."
            lloyd neutral "I believe I know who he’s targeting."
            eddie "You do? Tell me, then."

    if (branch == "a"):
        lloyd neutral "I have the name of the killer’s most recent victim.[wait_1] Jack Usbourne."
        lloyd neutral "Is a name sufficient for you to find information about him?"
        $ current_thought = "eddie_thought_96"
        eddie "It’s a start.[wait_1] It’s not enough to get you his entire fuckin’ family tree, or his job history, or anything like that right now."
        eddie "But give me a few minutes and I can at least look it up in the archives.[wait_1] How do you spell the surname?"
        lloyd neutral "I have no idea."
        eddie "{size=-8}Unbe-fucking-lievable...{/size}"
        hide eddie_unimpressed with quick_dissolve
        hide eddie_angry with quick_dissolve
        hide screen psychic_powers
        scene black_bg with quick_dissolve
        lloyd_narrating neutral "I don’t have to wait too long for Eddie to return."
        lloyd_narrating neutral "He’s holding several pieces of paper when he does."
        scene office_interview_room with slow_dissolve
        $ swap_sprites("eddie_unimpressed")
        show screen psychic_powers
        $ current_thought = "eddie_thought_97"
        eddie "Here you go, Chen."
        eddie "Seems this Usbourne guy got into trouble a few times and wound up in court.[wait_1] Nothing too serious –[wait_05] just some pickpocketing and simple con jobs by the look of it."
        lloyd_narrating neutral "I skim the papers Eddie hands me."
        lloyd_narrating neutral "I wouldn’t rule out one of these cases motivating the killer, but I can’t immediately see anything that would relate to the other victims that Cat found."
        $ current_thought = "eddie_thought_98"
        lloyd neutral "I already knew most of this, Eddie.[wait_1] Would you be able to –"
        $ swap_sprites("eddie_angry")
        eddie "To what, Lloyd?[wait_1] To go and put another search in for Usbourne?"
        eddie "To bend over backwards and find more information that you apparently already know?[wait_1] To research your damn story for you?"
        eddie "This is so fucking typical of you, Chen."
        lloyd_narrating neutral "Eddie’s been perpetually angry at me.[wait_1] I’ve brushed it off and tried to turn the other cheek but it’s wearing me down."
        $ current_thought = "eddie_thought_99"
        lloyd neutral "Why are you so angry at me, Eddie?[wait_1] What did I do that made you hold this grudge against me?"
        eddie "Why the hell wouldn’t I hold a grudge against you, Chen?[wait_1] You only ever think of yourself."
        eddie "You think that your shit is the most important shit in the world, and that everybody else should cater to your fuckin’ whims.[wait_1] It was exactly the same when we were both working at {i}The Brief{/i}."
        eddie "You’d always get the good assignments, and rather than asking if I wanted to work with you, or suggesting to the boss that I could do some of them, you’d just walk right out of the room and go do the assignment."
        eddie "No friendly banter, no apology, nothing.[wait_1] All that mattered was your work, and me not getting any of it meant that I never got noticed."
        lloyd_thinking thinking "Is that really how he saw it?"
        lloyd_thinking thinking "...Is that really how I acted?"
        lloyd neutral "Eddie, I –"
        $ current_thought = "eddie_thought_100"
        eddie "Oh, no you fucking don’t.[wait_1] You don’t just get to give me a fake apology and tell me that you never meant it."
        eddie "You know why?[wait_1] Because I know that seconds after giving it, you’ll just go back to asking me to do more shit for you."
        eddie "You only ever think of yourself, Chen."
        eddie "And if you want to prove me wrong, you’ll thank me, take those papers I’ve given you, and come see me again at a later date, when I’ve had the time and space to find out more information about this Usbourne guy."
        lloyd_thinking thinking "..."
        lloyd neutral "Thank you, Eddie.[wait_1] I apologise if I’ve treated you poorly."
        lloyd neutral "I’ll leave now."
        $ current_thought = "eddie_thought_101"
        eddie "Good.[wait_1] Some of us have actual work to do here."
        hide eddie_angry with quick_dissolve
        hide screen psychic_powers
        scene black_bg with slow_dissolve
        lloyd_thinking thinking "Is what Eddie said really true?[wait_1] Do I only care about myself?"
        lloyd_thinking thinking "It is true that I didn’t remember who he was..."
        lloyd_narrating neutral "I decide not to dwell on it for now.[wait_1] I still have things to do."
        lloyd_narrating neutral "Beating myself up won’t stop the man in black."
        $ visit_person("eddie", "a", 3)
    else:
        $ current_thought = "eddie_thought_102"
        lloyd neutral "How likely is it that you can find people who are...[wait_05]special?"
        $ swap_sprites("eddie_unimpressed")
        eddie "You’re going to have to be more specific, Chen."
        eddie "Special how?[wait_1] People with mental issues?[wait_1] People who break athletic records without even trying?"
        eddie "Freaks that can solve Rubiks Cubes?"
        lloyd neutral "Nothing like that.[wait_1] I’m thinking more of people who...[wait_05]know things."
        eddie "Stop beating around the fucking bush, Chen."
        eddie "Just say what you fucking mean and cut with the bullshit spy talk."
        $ current_thought = "eddie_thought_103"
        lloyd neutral "Have you ever heard about people with extrasensory perception?"
        eddie "What?"
        lloyd neutral "Psychic abilities.[wait_1] Reading minds.[wait_1] Seeing the future."
        lloyd_thinking thinking "Not to mention making people lose memories."
        $ swap_sprites("eddie_angry")
        $ current_thought = "eddie_thought_104"
        eddie "What does this have to do with the guy you encountered?[wait_1] The last known victim of the killer?"
        $ current_thought = "eddie_thought_105"
        lloyd neutral "There’s a good chance that the killer targeted him because he thought that he was psychic.[wait_1] It’s likely the same for his other victims, too."
        eddie "How do you figure that?"
        lloyd neutral "It’s complicated to explain."
        eddie "And I wouldn’t get it, right?[wait_1] Because I’m too dumb?"
        lloyd neutral "No.[wait_1] You just don’t have all of the information that I do."
        $ current_thought = "eddie_thought_106"
        eddie "And you’re not going to share that with me because...?"
        lloyd_thinking thinking "I can’t tell him that I’m psychic, or that I found reliable evidence that the man with the white streak was."
        lloyd_thinking thinking "I doubt that he would believe me even if I did tell him."
        lloyd neutral "I can’t share it with you.[wait_1] But trust that my reasoning is sound."
        lloyd_narrating neutral "Eddie is silent for several moments.[wait_1] The furrow in his brow deepens."
        $ current_thought = "eddie_thought_107"
        eddie "So you want me to help you with this shit, but you don’t trust me enough to share anything with you?"
        lloyd neutral "Well, I –"
        eddie "This is so fucking like you."
        eddie "Only you’re allowed to know about the information, because you don’t want anybody else to get the credit for it, right?[wait_1] Or is it that you don’t think highly enough of anybody else?"
        lloyd neutral "I’d tell you if I could, Eddie."
        eddie "Like hell you would.[wait_1] You’re arrogant, Chen."
        eddie "You only think about yourself, and you just treat everybody else like they’re your little tools."
        eddie "And if you think that ordering me around to do your busywork is the way to get my assistance, you’re wrong.[wait_1] I’m not helping you."
        lloyd_thinking thinking "I’m losing him.[wait_1] I need his help."
        $ current_thought = "eddie_thoughts_108"
        lloyd neutral "I lied."
        eddie "What?"
        lloyd neutral "I lied about why the killer targeted his victims."
        lloyd neutral "He knew that they were psychic.[wait_1] They had extrasensory abilities."
        lloyd neutral "I don’t know how he found out, but he did.[wait_1] That’s the information that I was keeping from you."
        lloyd_narrating neutral "Eddie is silent for several moments before answering."
        eddie "You really think that, Chen?"
        eddie "Or do you think that I’m that gullible?[wait_1] That I’ll believe a bullshit story like that?"
        $ current_thought = "eddie_thoughts_109"
        lloyd neutral "It’s the truth.[wait_1] I know that they had psychic abilities because...[wait_05]I saw it.[wait_1] In some security footage."
        lloyd_thinking thinking "Better not tell him that I’ve got powers myself just yet."
        lloyd_narrating neutral "Once again Eddie is silent."
        lloyd_narrating neutral "He studies my expression, trying to determine what I’m playing at."
        lloyd_narrating neutral "I’m trying to project earnestness.[wait_1] To look honest.[wait_1] Because I really need help to find other psychics."
        $ swap_sprites("eddie_unimpressed")
        $ current_thought = "eddie_thoughts_110"
        eddie "You’re telling the truth, aren’t you?[wait_1] These people really were psychic."
        lloyd neutral "Yes.[wait_1] The killer will eliminate more with their abilities, unless we can find them and warn them."
        eddie "I agree.[wait_1] But I’m not going to help you."
        lloyd neutral "What?"
        $ current_thought = "eddie_thoughts_111"
        eddie "If there are people out there that can read my mind –[wait_05] my private thoughts, which aren’t supposed to for anybody else –[wait_05] then why shouldn’t they be killed?"
        eddie "How can I trust them to not dig around in my head and find whatever they want?"
        lloyd neutral "We’re talking about innocent people."
        eddie "Freaks like that?[wait_1] They’re not innocent."
        eddie "If I knew about anyone with abilities like theirs, I wouldn’t hesitate to blow their heads off myself."
        eddie "I can do it, you know –[wait_05] I’ve got the means."
        lloyd_thinking thinking "I’ve lost him.[wait_1] There’s no way that he’ll help me now."
        $ swap_sprites("eddie_angry")
        $ current_thought = "eddie_thought_112"
        eddie "You don’t know where any of these people are, do you, Chen?"
        lloyd neutral "If I did, would I have come here?"
        eddie "No, I guess not."
        lloyd_thinking thinking "I’m not getting anything from him."
        $ current_thought = "eddie_thought_113"
        lloyd neutral "I think I’ll be leaving now, Eddie."
        eddie "Off to protect your invasive little friends, are you?"
        eddie "Just don’t forget that they’ll be scraping every corner of your mind like the monsters they are."
        hide eddie_angry with quick_dissolve
        hide screen psychic_powers
        scene black_bg with slow_dissolve
        lloyd_thinking thinking "That was a disaster.[wait_1] I never would have thought that Eddie would react like that."
        lloyd_thinking thinking "What does he have in his head that he’s so determined to keep private?"
        lloyd_narrating neutral "There’s no way to know.[wait_1] I leave the building and start thinking about my next destination."

        $ visit_person("eddie", "b", 0)
    return 