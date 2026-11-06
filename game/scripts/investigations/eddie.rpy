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
            jump eddie_a_4
    
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
    $ visit_person("eddie", "a", 2)
    return

label eddie_a_4:
    $ visit_person("eddie", "a", 3)
    return 