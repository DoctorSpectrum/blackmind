label barbara_investigation:
    $ current_thought_block = "mind_read_barbara"
    if (branch == "a"):
        if (day == 1):
            jump barbara_a_1
        elif (day == 2):
            jump barbara_a_2
        elif (day == 3):
            jump barbara_a_3
        elif (day == 4):
            jump barbara_a_4
    elif (branch == "b"):
        jump barbara_b_4
    
    return

label barbara_a_1:
    scene black_bg with quick_dissolve
    #sfx of train noises
    lloyd_narrating neutral "The bar I’ve identified is called Icarus."
    lloyd_narrating neutral "The easiest way to get to it is by heading downwards below the streets, then taking a train across the city to a nearby station."
    lloyd_narrating neutral "From there, it’s just a short walk through a few streets, and then I’m at the door."
    lloyd_narrating neutral "I’m sure that any drunks appreciate the proximity to the station and how much easier that makes returning home at night."
    #sfx of creaking door
    lloyd_narrating thinking "I wasn’t expecting too much at this hour – maybe a contact number for the owner, something that I couldn’t find online – but to my surprise, the door gently creaks open when I knock on it."
    lloyd_narrating thinking "A forgetful owner?[wait_1] Or a sign of a break-in?"
    lloyd_narrating thinking "I slowly enter the building and make my way in, trying not to make too much noise."
    scene bar with slow_dissolve
    lloyd_narrating neutral "It’s rare for me to drink, but I can’t say that this would be a bad place to do it in."
    lloyd_narrating neutral "The atmosphere seems pleasant enough, and they look to have a good variety of drinks on the shelves."
    lloyd_narrating neutral "There are no immediate signs of a break-in, or anything else illegal having happened, so I let myself relax a little."
    lloyd_narrating neutral "Just as I do so, a door swings open."
    $ swap_sprites("barbara_thinking", slow_dissolve)
    $ current_thought = "barbara_thought_01"
    show screen psychic_powers
    bartender "Um...[wait_05]hello.[wait_1] Are you –[wait_05] can I help you?"
    lloyd_narrating neutral "She looks to be about my age.[wait_1] She’s holding a screwdriver in one hand, and despite her obvious surprise, is holding herself casually enough."
    lloyd_narrating neutral "I haven’t considered how I’d like to play this interaction, but I quickly decide to go with friendly and honest.[wait_1] She shouldn’t have any reason to be hostile."
    $ current_thought = "barbara_thought_02"
    lloyd friendly "Good day.[wait_1] The name’s Lloyd.[wait_1] Do you have the time to answer a few questions?"
    $ current_thought = "barbara_thought_03"
    bartender "Hey, I’m Barbara.[wait_1] I should have a bit of time, but can I ask what this is about?[wait_1] Are you a reporter?"
    lloyd neutral "What makes you think that?"
    barbara "Well, the camera’s a bit of a giveaway."
    $ current_thought = "barbara_thought_04"
    lloyd neutral "Ah, that.[wait_1] I’m...[wait_05]not a reporter, no."
    lloyd_thinking neutral "I’d better change the topic.[wait_1] There’s no easy way to describe what I’m doing."
    $ current_thought = "barbara_thought_05"
    lloyd neutral "I’m surprised that you’re open at this hour –[wait_05] I was under the impression that the drinks didn’t start flowing until the evening."
    $ current_thought = "barbara_thought_06"
    barbara "Oh, they don’t –[wait_05] but I’ve got a few things to deal with after an incident last night."
    $ current_thought = "barbara_thought_07"
    barbara "You probably came in because the door was unlocked, right?[wait_1] I’m heading in and out a bit at the moment; it’s easier to keep it that way rather than constantly fumbling for keys."
    lloyd_thinking thinking "An incident last night?[wait_1] That could be related to the man in black...[wait_05]I should investigate this further."
    menu:
        "What was the incident?":
            $ current_thought = "barbara_thought_08"
            lloyd neutral "Could I ask you to clarify what you mean by an incident last night?"
            $ swap_sprites("barbara_angry")
            barbara "It’s nothing that you need to concern yourself with.[wait_1] Just usual bar stuff."
            $ swap_sprites("barbara_smiling")
        "Ask about the door" (locked=not check_boolean("barbara_broken_door"), message="You have not read the related thought"):
            lloyd_thinking thinking "If there’s a broken door, that could be indicative of someone breaking in.[wait_1] I’d better handle this carefully."
            $ current_thought = "barbara_thought_09"
            lloyd friendly "An incident last night, huh?[wait_1] I hope that you’re alright now!"
            barbara "Oh, of course![wait_1] It’s nothing too serious - just that I got a report from a patron that the door to one of the bathroom stalls was a bit unstable, so I’m going to replace the hinges."
            lloyd_thinking neutral "Alright, it’s not related to the man in black then.[wait_1] At least I solved the mystery."
    $ current_thought = "barbara_thought_10"
    barbara "Anyway, you said something about wanting me to answer a few questions?[wait_1] What exactly do you need from me?"
    $ current_thought = "barbara_thought_11"
    lloyd neutral "I’m currently trying to find a certain person."
    lloyd neutral "I don’t know where they are at present, but they were in this area last night."
    lloyd neutral "I was hoping to find out whether you or any of your staff had heard or seen anything that could help me."
    $ swap_sprites("barbara_thinking")
    barbara "That depends.[wait_1] Do you know this person’s name?[wait_1] Do you have a photo of them?"
    $ current_thought = "barbara_thought_12"
    lloyd neutral "Not exactly."
    lloyd_narrating neutral "I describe the man to Barbara as best as I can."
    lloyd_narrating neutral "Even though it’s been hours since I had the vision, I can still picture the man in black perfectly."
    lloyd_narrating neutral "His features – and what little I could make out of the scene – have been burned into my mind with perfect clarity.[wait_1] I couldn’t forget a detail if I tried."
    lloyd_narrating neutral "Her response isn’t overly positive, however."
    barbara "Sorry...[wait_05]I don’t think that I’ve seen anybody that matches that description."
    barbara "I was in the bar for –[wait_05] most evenings I’m working here, so unless he dropped by, I wouldn’t have run into him."
    lloyd_thinking thinking "That’s not overly helpful, but it does give me a little to work with."
    lloyd_thinking thinking "The man in black isn’t a patron of this bar –[wait_05] it could mean that he’s not from the area."
    lloyd_thinking thinking "It would be good to get confirmation of that fact."
    $ current_thought = "barbara_thought_13"
    lloyd neutral "Thanks anyway."
    lloyd neutral "Do you know any of the other shop owners around here?[wait_1] Could you ask them if they remember him?"
    $ swap_sprites("barbara_angry")
    barbara "I know them, sure, but I can’t afford to just go around and pester them."
    barbara "I’ve got work to do, buddy![wait_1] If you want their information, then you can go ask them yourself!"

    if (len(days["a"][0]) >= 1):
        lloyd_thinking neutral "I might be able to tomorrow, but I definitely don’t have any more time today."
    else:
        lloyd_thinking neutral "I’ve got much more promising places on my list – I need to prioritise visiting them."
    
    lloyd_thinking neutral "It would be much more convenient if Barbara spoke to the other shopowners for me."

    menu:
        "I don't have the time to talk to them":
            $ current_thought = "barbara_thought_14"
            lloyd neutral "I don’t have the time to talk to them today.[wait_1] Are you certain that you can’t work something out?"
            $ swap_sprites("barbara_smiling")
            barbara "I...[wait_1]look, I might be able to do something."
            barbara "I’m not sure, it’ll depend upon how long my tasks today take.[wait_1] I {i}have{/i} to prioritise them."
            lloyd_thinking thinking "That’s not what I wanted to hear.[wait_1] But I don’t know what else I could say to convince her."
            lloyd neutral "If you do get the opportunity, please do.[wait_1] It would really be appreciated."
        "They might respond better to a member of the community" (locked=not check_boolean("barbara_family_community"), message="You have not read the related thought"):
            lloyd_thinking thinking "Barbara seemed fairly proud of her family’s history in the area."
            lloyd_thinking thinking "If I appeal to that, her pride might not let her ignore it."
            $ current_thought = "barbara_thought_15"
            lloyd friendly "Oh, sorry.[wait_1] I just thought that they would be a bit more willing to divulge information to someone who’s already a part of the community."
            $ swap_sprites("barbara_smiling")
            barbara "Well, if nothing else, it would sound better if somebody they knew asked them whether they’d seen this guy, yeah."
            $ current_thought = "barbara_thought_16"
            lloyd neutral "So they’d mostly help you out just because you know them, then?"
            $ swap_sprites("barbara_angry")
            barbara "Of course not![wait_1] I’ve been a –[wait_05] my family’s been in these parts for decades now!"
            barbara "They’d help me out because this community supports one another!"
            $ current_thought = "barbara_thought_17"
            lloyd neutral "Are you certain?"
            barbara "I’ll prove it –[wait_1] I’ll ask around right away, and see if anyone’s heard anything about this guy you’re looking for!"
            barbara "Whatever information people have, I’ll find it out!"
            $ add_boolean("barbara_convinced_investigate")
    
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_18"
    barbara "What’s so important about this guy, anyway?[wait_1] Does he owe you money or something?"
    lloyd_thinking thinking "Is there anything that I could tell her that would show her the importance of finding the man in black?"
    lloyd_thinking thinking "If I tell her that he’s going to commit a murder, she might get scared off."
    $ current_thought = "barbara_thought_19"
    lloyd neutral "It’s...[wait_05]important.[wait_1] I can’t go into details, sorry."
    $ swap_sprites("barbara_angry")
    barbara "Right."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_20"
    barbara "Anyway, if you want to come over later tonight, I might have something for you by then."
    barbara "And if you can’t make it, feel free to come over any time during the next few days and ring the doorbell."
    $ current_thought = "barbara_thought_21"
    lloyd neutral "You’ll be here during the day then, too?"
    barbara "There’s always work to be done – marketing, restocking, paperwork...[wait_05]If I didn’t get it done during the day, I sure as heck wouldn’t have the time to do it in the evenings!"
    $ current_thought = "barbara_thought_22"
    lloyd friendly "Understood.[wait_1] Thank you for your assistance, Barbara – it’s appreciated."
    barbara "No prob![wait_1] Good luck finding this guy!"
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I say my goodbyes and leave the bar."
    lloyd_narrating neutral "It wasn’t anything particularly concrete, but I know that the man in black was in this area last night."
    lloyd_narrating neutral "One of Barbara’s neighbours might have seen or heard something...[wait_05]but is returning here tonight the best use of my time?"
    
    $ visit_person("barbara", "a", 0)
    return

label barbara_a_2:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "Last night I was in a bar."
    lloyd_narrating neutral "I had at least a few alcoholic drinks, to judge by the sensation I had, and had likely been there for a decent amount of time."
    lloyd_narrating neutral "I don’t know why I went there or what I got up to.[wait_1] The events leading up to my waking are a mystery to me."
    lloyd_narrating neutral "Returning to the bar should provide answers to some of the questions, but I’m all too aware that they won’t come as easily as I’d like."
    lloyd_narrating neutral "I make my way below the ground and to the nearest train station."
    lloyd_narrating neutral "The long-promised upgrades haven’t been started yet, preserving the station in a dated aesthetic."
    lloyd_narrating neutral "While I wait for my train to arrive I take several wide-angle shots with my camera, preserving the aesthetic further."
    lloyd_narrating neutral "One day this might all be gone, but my photos will serve as a reminder of what it once was."
    lloyd_narrating neutral "Eventually my train arrives.[wait_1] The journey is uneventful, the only notable thing being how long it takes to get to my destination."
    lloyd_narrating neutral "From there it’s a short walk to Icarus."
    if (person_visited("barbara", "a", 0)):
        lloyd_narrating neutral "The door is closed today, but I knock on it loudly.[wait_1] Barbara arrives before long and lets me in."
    else:
        lloyd_narrating neutral "The door is closed. I knock on it loudly, and to my surprise, the bartender from last night arrives and lets me in.[wait_1] I follow her inside."
    
    scene bar with slow_dissolve
    lloyd_narrating neutral "The bar is as I remember it from last night."
    lloyd_narrating neutral "The lights gleam off the surface of the tables, which look clean and presentable."
    lloyd_narrating neutral "The sound of air rushing through some vents explains the comfortable warmth in the room, enough to tempt me to take off my jacket."
    lloyd_narrating neutral "There’s just one difference: the strong smell of cleaning products."
    $ swap_sprites("barbara_angry", slow_dissolve)
    $ current_thought = "barbara_thought_40"
    show screen psychic_powers
    if (person_visited("barbara", "a", 0)):
        lloyd_narrating neutral "Barbara hasn’t said anything since she let me into the building.[wait_1] She’s simply returned to scrubbing the tables."
        lloyd_narrating neutral "They’re clean enough that it seems unnecessary to me, but then I suppose that I don’t work in a bar."
        $ current_thought = "barbara_thought_41"
        lloyd neutral "Hi, Barbara."
        lloyd neutral "I’m...[wait_1]thank you for letting me in."
        barbara "It’s fine.[wait_1] I said that you could come in during the day, and I stick to my word."
    else:
        lloyd_narrating neutral "The bartender hasn’t said anything since she let me into the building.[wait_1] She’s simply resumed scrubbing the tables."
        lloyd_narrating neutral "They’re clean enough that it seems unnecessary to me, but then I suppose that I don’t work in a bar."
        $ current_thought = "barbara_thought_42"
        lloyd neutral "Thank you for letting me in.[wait_1] I’m Lloyd."
        bartender "I’m Barbara."
        lloyd_narrating neutral "She’s focusing far more on her work than me.[wait_1] It occurs to me how disruptive I’m being."
        $ current_thought = "barbara_thought_43"
        lloyd neutral "Are you particularly busy today?"
        barbara "After I’m done with the cleaning, there’s just paperwork, restocking products, marketing...[wait_05]there’s always more things to do."
        barbara "It comes with running a business."
        lloyd_thinking thinking "It sounds like I can visit during the daytime on other days."
    $ current_thought = "barbara_thought_44"
    lloyd neutral "I’ll try not to take up too much of your time, Barbara."
    lloyd neutral "I have a few questions to ask you, but before I do I owe you an apology.[wait_1] Last night I –[wait_05] I obviously had more alcohol than I should have."
    barbara "You can say that again!"
    $ current_thought = "barbara_thought_45"
    lloyd neutral "I can’t really explain why I had so many, but I –[wait_05] it won’t happen again.[wait_1] I promise you."
    lloyd_narrating neutral "Barbara sighs deeply.[wait_1] I’m prepared for her to tell me that she doesn’t care, that actions speak louder than words, or something along those lines."
    $ swap_sprites("barbara_smiling")
    barbara "Well...[wait_05]I’d be lying if I said that I wasn’t angry, but truth be told, I’ve dealt with a lot worse in a lot more heated situations."
    barbara "And you taking the time to come here and apologise does help a lot."
    barbara "So...[wait_05]thank you, Lloyd, for that."
    $ swap_sprites("barbara_angry")
    $ current_thought = "barbara_thought_46"
    barbara "You lie to me, though, and you will regret it."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_47"
    barbara "Now, you said that you had some questions for me?"
    lloyd neutral "I do.[wait_1] They might sound like questions that I could answer on my own, but I wouldn’t be asking them if I already knew the answers."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_48"
    barbara "Alright...[wait_05]go ahead, then."
    $ current_thought = "barbara_thought_49"
    lloyd neutral "When I was here last night, did I say anything about why I’d visited?"
    barbara "I don’t think so.[wait_1] You seemed fairly happy to just order drinks, having them on your own in the corner."
    barbara "I assumed that you just wanted to have an evening to yourself."
    lloyd_thinking neutral "Drinking by myself...[wait_05]so I wasn’t meeting anybody here."
    lloyd_thinking neutral "Or was I waiting for somebody to show up?[wait_1] And if so, was it an arranged meeting, or was I ambushing them?"
    $ current_thought = "barbara_thought_50"
    lloyd thinking "How was I acting?[wait_1] Did I seem impatient, or to be looking around for anybody?"
    barbara "Honestly?[wait_1] I couldn’t tell you."
    barbara "Unless it’s a particularly quiet night, I’ve usually got enough to handle up at the bar to pay that much attention to individual patrons."
    barbara "Most of the time I can spare some attention to see whether anybody needs more drinks, or their glasses taken away, but otherwise I’ve got plenty of other things keeping me busy."
    $ current_thought = "barbara_thought_51"
    lloyd neutral "And when I was at the bar?"
    barbara "I guess...[wait_05]I think you were fairly boisterous?"
    barbara "You seemed pretty pleased with yourself.[wait_1] I do remember asking you what had put you in a good mood, and you said that it was too complicated to explain."
    lloyd_thinking thinking "Was my good mood to do with my psychic powers, then?[wait_1] They would be something that I wouldn’t want to explain."
    lloyd_thinking thinking "But what could they have done, or could I have learned through them?"
    $ current_thought = "barbara_thought_52"
    lloyd neutral "There was nothing else to the evening beyond that?[wait_1] I came in and ordered drinks, and kept to myself the entire night?"
    barbara "Pretty much, yeah."
    barbara "I was kind of surprised that you were so confused when you came up to the bar, to be honest – you hadn’t had that many drinks, and I’d like to think that I would have noticed if they’d affected you significantly earlier in the night."
    $ swap_sprites("barbara_angry")
    $ current_thought = "barbara_thought_53"
    barbara "You didn’t smuggle in your own alcohol, right?[wait_1] You weren’t spiking your own drinks?"
    lloyd neutral "Of course not."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_54"
    barbara "Sorry.[wait_1] Had to check."
    lloyd_thinking thinking "All that I did was have some drinks and keep to myself...[wait_05]but why was I here?"
    lloyd_thinking thinking "It doesn’t sound like I was meeting somebody, and I wasn’t waiting for somebody to arrive."
    lloyd_thinking thinking "I just...[wait_05]wanted to drink some alcohol in a social environment."
    $ current_thought = "barbara_thought_55"
    lloyd_narrating thinking "It sounds benign on the surface."
    lloyd_narrating thinking "But it requires willing ignorance of several facts –[wait_05] that I’d gone to bed already.[wait_1] That I rarely drink alcohol.[wait_1] And that all of my memories were missing."
    lloyd_narrating thinking "Even if the latter could be explained away by an aspect of my psychic powers, the first two didn’t have adequate explanations."
    lloyd_thinking thinking "I won’t find the answers here.[wait_1] Barbara’s already told me all that she knows."
    $ current_thought = "barbara_thought_56"
    lloyd friendly "I believe that answers all of my questions, Barbara.[wait_1] Thank you."
    lloyd friendly "If there’s ever anything that I can do to repay you, I –"
    barbara "Well, since you brought it up...[wait_05]there actually is something that you could help me with."
    lloyd friendly "Of course."
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "Barbara directs me to the bathroom."
    barbara "I doubt that you’re the one responsible for all of this, but...[wait_05]well, you did offer to help..."
    lloyd_thinking neutral "The smell...[wait_05]the texture...[wait_05]dear god..."
    lloyd_thinking scared "N-no problem, Barbara."
    barbara "Thanks, Lloyd![wait_1] You’re a real champion!"
    lloyd_narrating neutral "I spend the next thirty minutes cleaning up vomit."
    lloyd_narrating neutral "I spend the next thirty minutes after that wishing that I could lose some of my memories again."

    $ visit_person("barbara", "a", 1)
    return

label barbara_a_3:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I’m trying to discover why the man with the white streak was killed by the man in black."
    lloyd_narrating neutral "There must be something that he has in common with the man in black’s other victims; something that painted targets on their backs."
    lloyd_narrating neutral "Finding that commonality will make it easier to identify the man in black’s next target, and I might finally be able to do some good with my psychic powers."
    lloyd_narrating neutral "I encountered the man with the white streak a few streets away from Icarus."
    lloyd_narrating neutral "I’m not going to get my hopes up but it’s possible that he’s a regular at the bar, or in the area."
    lloyd_narrating neutral "If he is then I may finally learn something about him.[wait_1] If not then at least I’ve eliminated one of the more likely leads."
    lloyd_narrating neutral "I walk to the nearest train station, moving at a casual pace."
    lloyd_narrating neutral "The next train won’t be arriving for nearly ten minutes, and I can afford to spare the time."
    lloyd_narrating neutral "The temperature in the station is a strong contrast to the air above the ground; it’s chilly enough for me to zip my jacket up part of the way."
    lloyd_narrating neutral "Once the train finally arrives I enter it and take it to my destination."
    if (person_visited("barbara", "a", 0) or person_visited("barbara", "a", 1)):
        lloyd_narrating neutral "I knock on the door of Icarus.[wait_1] I don’t have long to wait before Barbara arrives and lets me in, leading me further inside."
    else:
        lloyd_narrating neutral "I’m not surprised to find that the bar is closed, but I knock on the door regardless, hoping that somebody may be inside."
        lloyd_narrating neutral "My hunch is correct, and the owner comes to the door."
        lloyd_narrating neutral "I tell her that I’ve got some questions to ask and she leads me inside."
    
    scene bar with slow_dissolve
    lloyd_narrating neutral "To my surprise I find that the bar feels warm and welcoming, even though it hasn’t been fully set up for when it opens tonight."
    lloyd_narrating neutral "The temperature feels comfortable in spite of my jacket, smooth jazz is playing from some hidden speakers, and the smell of alcohol is being blocked by some type of air freshener."
    lloyd_narrating neutral "It almost makes me wish that I was more of a drinker so that I could order something and drink it in alongside the atmosphere."
    $ swap_sprites("barbara_smiling", slow_dissolve)
    show screen psychic_powers

    if (person_visited("barbara", "a", 1)):
        $ current_thought = "barbara_thought_59"
        lloyd_narrating neutral "Barbara seems to be in a good mood.[wait_1] It likely helps that –[wait_05] as far as I know –[wait_05] she didn’t have to deal with any drunkards last night."
        barbara "So, you decided to pay me another visit, did you?"
        $ current_thought = "barbara_thought_60"
        lloyd neutral "Is there somewhere else that you’d rather I be?[wait_1] Am I interrupting anything?"
        barbara "Oh, nothing that I can’t put off for a little bit."
        barbara "As a matter of fact, it’s nice to have an excuse to take a break."
        barbara "You know when you look at a word for so long that it loses all meaning?[wait_1] That’s how I feel right now, except instead of a word it’s numbers."
        $ current_thought = "barbara_thought_47"
        lloyd neutral "I hope that I don’t add more mental fatigue to your head, then:[wait_05] I have some questions to ask you."
        barbara "And here I was hoping you were finally interested in ordering a drink."
        barbara "But sure, I’ll bite: how can my bar and I help you, Lloyd?"
    else:
        if (not person_visited("barbara", "a", 0) and not person_visited("barbara", "a", 1)):
            $ current_thought = "barbara_thought_42"
            lloyd_narrating neutral "I’m unsure whether the bartender recognises me from two nights ago."
            lloyd_narrating neutral "If she does then she seems willing to put the incident behind her."
        elif (person_visited("barbara", "a", 0)):
            $ current_thought = "barbara_thought_41"
            lloyd_narrating neutral "Barbara seems to be in a good mood.[wait_1] I wonder whether she’s forgotten about my visit here on Tuesday evening."
        $ swap_sprites("barbara_angry")
        bartender "So, you decided to return to the scene of the crime, did you?"
        lloyd_narrating neutral "Or not."
        if (not person_visited("barbara", "a", 0) and not person_visited("barbara", "a", 1)):
            lloyd neutral "I apologise for the other night, miss...?"
            bartender "Just Barbara is fine.[wait_1] I don’t need to feel any older than I already am."
            $ current_thought = "barbara_thought_44"
            lloyd neutral "I apologise for the other night, Barbara.[wait_1] As much as I’d like to provide you with an explanation, the truth is that simply that I lost track of how much I’d been drinking."
        elif (person_visited("barbara", "a", 0)):
            lloyd neutral "I’m sorry for how I was the other night, Barbara."
            lloyd neutral "As much as I’d like to provide you with an explanation, the truth is that simply that I lost track of how much I’d been drinking."
        lloyd_narrating neutral "It’s far from the truth.[wait_1] But it’s easier than telling her that my psychic powers wiped most of my memories of that night."
        $ current_thought = "barbara_thought_57"
        barbara "That’s all that you have to say for yourself?[wait_1] That you lost track of your drinks?"
        lloyd neutral "Yes."
        $ swap_sprites("barbara_smiling")
        $ current_thought = "barbara_thought_58"
        barbara "Eh, I’ve heard worse excuses, and seen worse cases."
        lloyd neutral "You’re willing to forgive me, just like that?"
        barbara "Life’s too short to hold grudges, and if I held one against everybody who came in here and drank more than they should, I probably wouldn’t have many returning customers."
        barbara "Just to be clear –[wait_05] that’s a joke, but the principle still applies."
        lloyd neutral "Right."
        $ current_thought = "barbara_thought_47"
        if (not person_visited("barbara", "a", 0) and not person_visited("barbara", "a", 1)):
            barbara "Anyway, you said that you had a few questions for me.[wait_1] How can I help you, mister...?"
            lloyd neutral "Just Lloyd is fine.[wait_1] I don’t think we need to make this any more formal than is necessary."
            barbara "Sounds good to me![wait_1] So, tell me: how can my bar and I help you?"
        elif (person_visited("barbara", "a", 0)):
            barbara "Anyway, you said that you had a few questions for me."
            barbara "How can my bar and I help you, Lloyd?"
    $ current_thought = "barbara_thought_61"
    lloyd neutral "This may sound odd, but I’m currently trying to find out a bit of information about somebody."
    lloyd neutral "I know that they were in the area several nights ago, and it’s possible that they might have visited your bar."
    $ swap_sprites("barbara_thinking")
    barbara "When you say several nights ago, when exactly are you talking about?"
    $ current_thought = "barbara_thought_62"
    lloyd neutral "Three nights ago.[wait_1] Monday."
    barbara "Mondays tend to be my worst night for customers, sorry."
    barbara "Keep going, just –[wait_05] don’t get your hopes up too much."
    lloyd_thinking thinking "That’s disappointing, but not too surprising."
    $ current_thought = "barbara_thought_63"
    lloyd neutral "The person that I’m looking into is a white male."
    lloyd neutral "He looks a little younger than me, and has a soul patch, and a gap in-between his teeth."
    lloyd neutral "His most distinguishing feature, however, is a white streak through his hair, which is otherwise brown."
    lloyd_narrating neutral "I’m not expecting much from her."
    lloyd_narrating neutral "But as I describe the man with the white streak, Barbara nods thoughtfully several times."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_64"
    barbara "Yep, I’ve seen him.[wait_1] Only the once, but he was in here on Monday, as you said."
    lloyd neutral "Really?"
    barbara "Yeah.[wait_1] He wasn’t in here for long –[wait_05] I actually threw him out after talking to him for a bit; I realised that he was pretty drunk and wasn’t in a state where he should have more alcohol."
    barbara "What did you want to know about him?"
    lloyd_narrating neutral "My excitement fades.[wait_1] It sounds as though the man with the white streak is as much a stranger to Barbara as he is to me."
    lloyd_narrating neutral "Visiting the bar doesn’t mean that Barbara knows that much about him."
    lloyd_thinking thinking "I may as well find out what she does know about him."
    $ current_thought = "barbara_thought_65"
    lloyd neutral "Do you know what his name is?[wait_1] Or what he does for a living?"
    $ swap_sprites("barbara_angry")
    barbara "Tch.[wait_1] I can tell you what he doesn’t do –[wait_05] he’s not a reviewer, and he definitely doesn’t deserve any free drinks."
    lloyd neutral "What do you mean?"
    $ current_thought = "barbara_thought_66"
    barbara "Oh, just that he claimed that he could give me a good review if I gave him a drink for free."
    barbara "I almost fell for it, but then I noticed his body language, and the tone of his voice, and it was obvious that he was just an addict looking for a free handout."
    lloyd_narrating neutral "The mention of the man with the white streak’s body language gives me an idea."
    $ current_thought = "barbara_thought_67"
    lloyd neutral "Do you have any security footage of your interaction?"
    lloyd_thinking thinking "I’m not expecting to hear their conversation.[wait_1] But if I review the footage of him I might discover some clues that I’ve missed."
    $ swap_sprites("barbara_thinking")
    barbara "Um...[wait_05]no offence, but I don’t think that I should –[wait_05] I don’t really want to share the footage with you."
    barbara "Not that there’s anything on there that you shouldn’t see, but I –[wait_05] it is footage of {i}my{/i} bar, if that makes sense?"

    menu:
        "Offer a bribe" (locked=not check_boolean("barbara_offer_bribe"), message="You have not read the related thought"):
            lloyd_thinking thinking "Barbara was thinking earlier about how her profits need to be higher."
            lloyd_thinking thinking "Let’s see how she responds to a monetary offer."
            $ current_thought = "barbara_thought_68"
            lloyd neutral "I’ll give you two hundred dollars if you let me see the footage."
            barbara "Two hundred dollars?!"
            barbara "...[wait_05]That’s hard to say no to."
            barbara "I can’t show you the footage right now –[wait_05] I’ll need to dig through the archives a bit, and I’ve got other things to prioritise."
            barbara "Can you swing by later tonight?"
            $ current_thought = "barbara_thought_69"
            lloyd neutral "I might be able to."
            $ swap_sprites("barbara_smiling")
            barbara "Great...![wait_1] If I see you later, then I’ll show you what I’ve got."
            $ add_boolean("barbara_retrieves_footage")
        "Insist on it":
            $ current_thought = "barbara_thought_70"
            lloyd neutral "You’re being selfish, Barbara.[wait_1] I need to see that footage."
            lloyd neutral "Can you just show me?"
            $ swap_sprites("barbara_angry")
            barbara "Hey, I’m allowed to do what I want with my own footage."
            barbara "If you think that being forceful is going to have me folding immediately, then you’ve got another thing coming."
            lloyd_thinking thinking "She’s right...[wait_05]I was too blunt."
            lloyd_thinking thinking "I think I’ve soured her opinion on me too much.[wait_1] What could I have said to convince her?"
        "Politely accept":
            $ current_thought = "barbara_thought_71"
            lloyd friendly "Of course.[wait_1] It was selfish of me to ask for it."
            $ swap_sprites("barbara_smiling")
            barbara "Thanks for understanding, Lloyd."
            lloyd_thinking thinking "I was hoping that acquiescing to her request would change her mind, but it seems I was wrong."
            lloyd_thinking thinking "What could have convinced her that I need the footage?"
    $ current_thought = "barbara_thought_72"
    barbara "The footage aside, is there anything else that I can help you with?"
    $ current_thought = "barbara_thought_73"
    lloyd neutral "You’ve said that you know that the man with the white streak isn’t a reviewer."
    lloyd neutral "Is there anything else that you can tell me about him?[wait_1] You didn’t learn his name, did you?"
    $ swap_sprites("barbara_thinking")
    barbara "No...[wait_05]he mostly asked me some questions about the bar and if we had any deals."
    barbara "If he’d actually stayed and asked some questions I could have given him something, but –[wait_05] no, I don’t know anything about the guy."
    if (check_boolean("barbara_retrieves_footage")):
        lloyd_thinking thinking "The only information I’ll learn from here will be from the security footage."
        lloyd_thinking thinking "I don’t think that there’s any reason to stay here for any longer."
    else:
        lloyd_thinking thinking "Despite a promising start I don’t think that I’ll learn anything from here."
        lloyd_thinking thinking "There’s no reason to stay here for any longer."
    $ current_thought = "barbara_thought_74"
    lloyd neutral "Thank you for what information you did give me.[wait_1] I’d best go then."
    $ swap_sprites("barbara_smiling")
    barbara "Sure you don’t want something to wet your whistle before you go?[wait_1] We’re technically closed right now, but I won’t tell anyone if you don’t!"
    lloyd neutral "Thank you, but I have other things to do."
    barbara "Alright.[wait_1] Well, see you, Lloyd!"
    lloyd neutral "Farewell, Barbara."
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I exit the bar, the door locking itself behind me."
    lloyd_narrating neutral "For now I should head elsewhere."

    $ visit_person("barbara", "a", 2)
    return

label barbara_a_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Jack Usbourne’s name may now be known to me, but his past and connection to the victims of the man in black are still complete unknowns."
    lloyd_narrating neutral "I still can’t identify why he was killed or what traits a future victim might have.[wait_1] I need to."
    if (person_visited("barbara", "a", 2)):
        lloyd_narrating neutral "Yesterday Barbara said that Jack had visited Icarus on Monday, and that she had security footage of him."
        lloyd_narrating neutral "I wasn’t able to view it, but I may be able to if I return to the bar now."
        lloyd_narrating neutral "I may be barking up the wrong tree, but it’s possible that there will be a clue in the footage of him at the bar."
    else:
        lloyd_narrating neutral "Jack died only a few streets away from Icarus."
        lloyd_narrating neutral "It’s possible that he was a regular at the bar and that I can find out something of his past by asking around."
        lloyd_narrating neutral "Even if I don’t learn specifically about his past, it’s not impossible that I could be pointed to somebody in the area who did know him."
    lloyd_narrating neutral "I take some steps down below the ground and make my way to the nearest train station."
    lloyd_narrating neutral "The angle of the staircase is steep and I wonder how often people slip on them and injure themselves when they’re sufficiently wet."
    lloyd_narrating neutral "I wouldn’t be surprised to hear that several people die each year from such a cause."
    lloyd_narrating neutral "At the station platform, I wait for what feels like eternity before my train arrives and takes me to my destination."
    lloyd_narrating neutral "It’s easy enough to get to the bar from there that I don’t need to use an app."
    if (person_visited("barbara", "a", 0) or person_visited("barbara", "a", 1) or person_visited("barbara", "a", 2)):
        lloyd_narrating neutral "When Barbara answers the door and sees who it is she stifles a giggle, as though we’re children meeting at a secret clubhouse."
        lloyd_narrating neutral "I can’t help but smile myself."
        lloyd_narrating neutral "There is a certain degree of fun, of exclusivity, to being let into the establishment and seeing what it’s like after hours."
    else:
        lloyd_narrating neutral "The door to the bar is locked, something that I hadn’t considered."
        lloyd_narrating neutral "I choose to knock on it rather than give up immediately, and I’m surprised when it’s opened."
        lloyd_narrating neutral "When I tell the bartender that I have some questions for her she’s accommodating, offering to let me into the bar."
    scene bar with slow_dissolve
    lloyd_narrating neutral "I seat myself at a barstool, wishing that I had an option with better back support but not wanting to openly critique."
    lloyd_narrating neutral "Once I’ve confirmed that the bar isn’t wet I take off my camera and place it away from the edge."
    lloyd_narrating neutral "Its weight is familiar enough for me to forget about it at times, and I don’t want to lean forwards without thinking and crack the lens."
    $ swap_sprites("barbara_smiling", slow_dissolve)
    show screen psychic_powers
    if (person_visited("barbara", "a", 0) or person_visited("barbara", "a", 1) or person_visited("barbara", "a", 2)):
        $ current_thought = "barbara_thought_75"
        lloyd_narrating neutral "Barbara is looking to be in a good mood.[wait_1] A slight odour of perfume is wafting around her, and I wonder why she’s wearing some during what should be an ordinary work day."
        lloyd_narrating neutral "Am I interrupting some plans of hers?"
        $ current_thought = "barbara_thought_76"
        lloyd_narrating neutral "Hi, Barbara.[wait_1] Thanks once again for letting me in."
        barbara "No worries, Lloyd –[wait_05] I’m always happy to see you."
        barbara "What can I help you with today?[wait_1] You’re not looking for a drink, are you?"
        $ current_thought = "barbara_thought_77"
        lloyd neutral "Sorry, Barbara –[wait_05] I’m here once again to ask you some questions."
        barbara "Can’t say that’s a surprise.[wait_1] Shoot."
    else:
        $ current_thought = "barbara_thought_78"
        lloyd_narrating neutral "The bartender looks to be in a much better mood than when I saw her the other night."
        lloyd_narrating neutral "I’m hoping that she’ll stay that way and listen to what I have to say."
        lloyd neutral "Thank you for letting me in.[wait_1] The name’s Lloyd."
        bartender "Hey Lloyd –[wait_05] nice to meet you.[wait_1] I’m Barbara."
        barbara "Not to sound like a clichè, but have we met before?[wait_1] Your face is familiar."
        lloyd_thinking thinking "Here we go."
        $ current_thought = "barbara_thought_79"
        lloyd neutral "We have met before.[wait_1] I was here a few nights ago, drinking."
        $ swap_sprites("barbara_angry")
        barbara "Oh.[wait_1] You."
        $ current_thought = "barbara_thought_80"
        lloyd neutral "I know that I should have done this earlier in the week, but I –[wait_05] I’d like to apologise to you for my actions that night."
        lloyd neutral "I’d like to say that I had a good reason, but the truth is quite simply that I didn’t even know that I had drunk as much as I had."
        lloyd_thinking thinking "I’m not lying to her.[wait_1] She’s just misinterpreting my words."
        barbara "Mmm.[wait_1] You’re not here because you’re looking for a second round, are you?"
        barbara "We don’t open until the evening."
        $ current_thought = "barbara_thought_81"
        lloyd neutral "It couldn’t be further from my mind.[wait_1] I’d just like to apologise, ask you some questions, and then I’ll be on my way."
        $ swap_sprites("barbara_smiling")
        $ current_thought = "barbara_thought_82"
        barbara "Hey –[wait_05] no need to be so penitent."
        barbara "Thank you for the apology –[wait_05] you’re far from the worst person that’s stepped through these doors."
        lloyd_thinking thinking "That was surprisingly easy."
        barbara "So tell me –[wait_05] what are these questions that you have for me?"
    if (person_visited("barbara", "a", 2)):
        $ current_thought = "barbara_thought_83"
        lloyd neutral "Yesterday I was asking you about the man with the white streak."
        lloyd neutral "I managed to find out a little bit about him from somebody else who had dealt with him in the past."
        lloyd neutral "If I told you that his name is Jack Usbourne, does that ring any bells for you?[wait_1] Have you ever heard of anything involving someone with that name?"
        $ swap_sprites("barbara_thinking")
        barbara "Jack Usbourne...[wait_1]no, not that I can think of."
        barbara "Since I don’t recognise the name I can say that he probably doesn’t live around here, but otherwise –[wait_05] no."
        lloyd_thinking thinking "Nothing new from yesterday.[wait_1] I was hoping that the name would be useful."
        if (check_boolean("barbara_retrieves_footage")):
            $ swap_sprites("barbara_angry")
            $ current_thought = "barbara_thought_84"
            barbara "But hey, now that I’ve answered your question, I’ve got one of my own:[wait_05] why didn’t you come by in the evening?"
            barbara "I had the footage ready and everything."
            lloyd neutral "Sorry.[wait_1] I wanted to, but couldn’t be in two places at once."
            barbara "Well, whatever your other appointment was, I doubt it was as useful or important as what I found when I reviewed the footage."
        else:
            $ current_thought = "barbara_thought_85"
            barbara "But hey, speaking of this guy –[wait_05] I was reviewing some security footage yesterday and ended up watching his interaction in the bar again."
            barbara "What I saw there was pretty weird."
    else:
        $ current_thought = "barbara_thought_86"
        lloyd neutral "Have you ever heard the name Jack Usbourne?"
        $ swap_sprites("barbara_thinking")
        barbara "Can’t say that I have, or if I have it was just in passing."
        barbara "You don’t have a picture, do you?"
        $ current_thought = "barbara_thought_87"
        lloyd neutral "I can give you a description."
        lloyd_narrating neutral "I describe all of Jack’s features, emphasising the gap in his teeth and white streak in his hair.[wait_1] The image is familiar to her."
        $ swap_sprites("barbara_smiling")
        $ current_thought = "barbara_thought_88"
        barbara "No way![wait_1] He was here just a few nights ago!"
        lloyd_thinking thinking "My guess was right.[wait_1] He did visit this bar before dying."
        barbara "I’d almost forgotten about him, because he was only in for a few minutes."
        barbara "At least, that’s what I initially thought."
        $ current_thought = "barbara_thought_89"
        lloyd neutral "What do you mean?"
        $ swap_sprites("barbara_thinking")
        barbara "I was reviewing some security footage last night and I ended up re-watching his interaction in the bar."
        barbara "It was...[wait_05]pretty weird."
    lloyd neutral "How so?"
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_90"
    barbara "Long story short:[wait_05] the footage doesn’t match up with what I thought happened that night."
    barbara "He stole a whole heap of drinks –[wait_05] and therefore money –[wait_05] from me."
    lloyd_thinking thinking "Could this be why the man in black killed Jack?[wait_1] He was some sort of vigilante who thought that the world was better off without a thief like Jack?"
    $ swap_sprites("barbara_angry")
    $ current_thought = "barbara_thought_91"
    barbara "For his sake he’d better not come back here again!"
    barbara "I don’t care what sort of story he tries spinning next time –[wait_05] his ass is going right back out onto the street, and I’ll make him wish he was dead!"
    $ current_thought = "barbara_thought_92"
    lloyd neutral "Somebody’s beaten you to it.[wait_1] Jack is already dead."
    $ swap_sprites("barbara_sad")
    barbara "He’s...[wait_05]what?"
    lloyd_narrating neutral "I’ve said it without thinking."
    if (max_rewinds == None or minds_rewound < max_rewinds):
        lloyd_narrating neutral "For a moment I’m tempted to rewind her mind and make her forget about what I’ve said."
        lloyd_narrating neutral "But is it really worth it?"
    else:
        lloyd_narrating neutral "If I wasn’t so drained I’d be tempted to rewind her mind and make her forget about what I’ve said."
        lloyd_narrating neutral "But I doubt that it would be worth it."
    lloyd_narrating neutral "She was getting fairly worked up about Jack."
    lloyd_narrating neutral "It’s probably better to let her know the truth so that she can let go of her anger."
    $ current_thought = "barbara_thought_93"
    lloyd neutral "I don’t know what time he came to your bar, but it was likely shortly after that."
    lloyd neutral "He was –[wait_05] I found him dead several streets away from here.[wait_1] A gunshot wound."
    $ current_thought = "barbara_thought_94"
    barbara "I...[wait_05]oh my god."
    barbara "I –[wait_05] I didn’t like him, but I –[wait_05] I didn’t want him to die.[wait_1] I –[wait_05] I’m not that selfish."
    lloyd neutral "I know, Barbara.[wait_1] I wouldn’t have thought that you did."
    $ current_thought = "barbara_thought_95"
    barbara "Is the –[wait_05] do you know when the funeral is?"
    lloyd_narrating neutral "I haven’t even considered it.[wait_1] I’ve been trying to find Jack’s killer but I never gave a thought to Jack himself."
    lloyd neutral "I’m unsure.[wait_1] I can’t imagine that it’s already occurred, though."
    $ current_thought = "barbara_thought_96"
    barbara "Yeah, not if he was just alive the other day."
    barbara "I –[wait_05] I don’t know the guy –[wait_05] and I thought he was an asshole, but even so I –[wait_05] do you think that I should go to his funeral?"
    barbara "I –[wait_05] I was probably one of the last people to see him alive."
    lloyd_narrating neutral "Before I can give a response, she’s already resumed talking."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_97"
    barbara "Then again, it’s not like I really knew him."
    barbara "He’s –[wait_05] there’ll probably be a lot of his friends and family there, and I –[wait_05] what would I say to them?"
    barbara "“Hi, I’m Barbara.[wait_1] Jack tried to trick me into giving him free alcohol before he died, and I said no because I thought he was a drunkard.[wait_1] Beyond that, I didn’t know him.”"
    barbara "It doesn’t –[wait_05] it’s not really something that you want to hear about when you’re remembering someone, is it?"
    lloyd_narrating neutral "I think that Barbara’s mistaken in her belief."
    lloyd_narrating neutral "Graves told me that Jack had never met his father, and there was no mention of any siblings.[wait_1] I doubt that many family members will attend the funeral."
    lloyd_narrating neutral "Graves also mentioned that Jack had been to court and had committed petty crimes.[wait_1] I can’t be certain, but I wouldn’t be surprised if a lifestyle like that creates few friendships."
    lloyd_narrating neutral "His funeral will likely be fairly desolate."
    $ current_thought = "barbara_thought_98"
    lloyd neutral "You make a valid point, Barbara.[wait_1] Attending Jack’s funeral likely would be uncomfortable and a bit of an intrusion."
    $ swap_sprites("barbara_smiling")
    barbara "Right?[wait_1] The guy’s died –[wait_05] whoever’s there will probably be emotional enough."
    barbara "I don’t need to make things worse."
    lloyd_narrating neutral "I might be doing the wrong thing by lying to her.[wait_1] It feels disrespectful to Jack."
    lloyd_narrating neutral "But it’s clear that not attending the funeral will make Barbara more comfortable, and I don’t see why she should feel obliged to attend it."
    $ current_thouhgt = "barbara_thought_99"
    lloyd neutral "Best to just focus on your business and yourself.[wait_1] I’m sure that you have enough to worry about without adding a funeral into the mix."
    $ current_thought = "barbara_thought_100"
    barbara "You make a good point, Lloyd.[wait_1] But hey, maybe you could attend in my stead."
    barbara "You said that you wanted to know more about Jack, right?[wait_1] I’m sure that some of the others there can give you some information about him."
    lloyd_narrating neutral "I hadn’t considered that.[wait_1] It’s a good point that she makes."
    lloyd_narrating neutral "If even one person who knew Jack attends, I can ask them about him."
    lloyd neutral "That’s a good idea, Barbara.[wait_1] Thank you for the suggestion."
    $ current_thought = "barbara_thought_101"
    barbara "You’re welcome![wait_1] What else can I help you with?"
    lloyd_narrating neutral "There probably isn’t much more reason to stay here."
    if (len(days["a"][3]) < 2):
        lloyd_narrating neutral "Even with the funeral as a source of information, I should continue investigating Jack’s background."
        lloyd_narrating neutral "The more that I can find out about him the better."
    else:
        lloyd_narrating neutral "I’m meeting with Graves soon, and don’t want to be late."
    $ current_thought = "barbara_thought_102"
    lloyd neutral "Nothing at present, Barbara.[wait_1] I’ll be sure to visit as soon as I can, though."
    barbara "Okay![wait_1] In that case, I’ll catch you whenever that is, Lloyd!"
    lloyd neutral "See you."
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I return to the train station and wait for a train.[wait_1] I still have things to do today."

    $ visit_person("barbara", "a", 3)
    return 

label barbara_b_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "It’s the end of the day.[wait_1] I haven’t learned of any other psychic in the city.[wait_1] I’ve gained nothing from the day’s investigations."
    lloyd_narrating neutral "All that I can do is trust in Barbara to have security footage as useful as she shared with me yesterday."
    lloyd_thinking thinking "But first, a meal."
    scene restaurant_night with slow_dissolve
    lloyd_narrating neutral "I make my way to my favourite restaurant and order a meal."
    lloyd_narrating neutral "It’s a soothing presence after the trials of the day."
    lloyd_narrating neutral "I can admit that I’ve gotten slack over the past few days and fallen into the habit of eating here by default rather than cooking something at home."
    lloyd_narrating neutral "In my defence it’s been an exhausting week.[wait_1] Tracking down a serial killer is tiring work."
    lloyd_narrating neutral "Once I’ve finished my meal I head towards the train station and make my way towards Icarus."
    scene bar with slow_dissolve
    lloyd_narrating neutral "Icarus is even busier tonight than it was the previous night."
    lloyd_narrating neutral "I find Barbara working the bar, but she tells me that I’ll have to wait until another one of her employees shows up before she can talk to me."
    lloyd_narrating neutral "I sit down at the only free seat I can find and wait.[wait_1] It’s over an hour before Barbara is finally available."
    $ swap_sprites("barbara_smiling", slow_dissolve)
    $ current_thought = "barbara_thought_124"
    show screen psychic_powers
    barbara "Heya, Lloyd!" 
    barbara "Sorry about the delay –[wait_05] I should have told you to come by earlier; I ended up having an hour or so free before we opened."
    lloyd neutral "Better late than never, as they say."
    lloyd neutral "How did it go?[wait_1] Were you able to discover any more strange footage?"
    lloyd_narrating neutral "It’s the only lead I have at the moment for finding other psychics."
    lloyd_narrating neutral "If she doesn’t have anything then I’ve hit a dead end."
    $ swap_sprites("barbara_sad")
    $ current_thought = "barbara_thought_125"
    barbara "No such luck, Lloyd.[wait_1] Whoever this group of people that you’re building a case against are, none of the others have been here."
    lloyd neutral "Are you sure of that?"
    $ current_thought = "barbara_thought_126"
    barbara "There’s only enough space on the drive for about two weeks or so of footage at a time."
    barbara "I went through everything that I had and didn’t see anyone else suspicious."
    lloyd_narrating neutral "It’s the worst-case scenario.[wait_1] I have no idea how to find any other psychics."
    lloyd_narrating neutral "How can I find the man in black’s next target now?"
    $ current_thought = "barbara_thought_127"
    lloyd neutral "Oh.[wait_1] That’s a pity."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_128"
    barbara "...Tell me, Lloyd:[wait_05] if I had found footage of somebody else stealing drinks, what would you have done with it?"
    lloyd neutral "I would have tried to track down the person in the footage.[wait_1] I’d have questions for them."
    barbara "And would you be asking those questions because you want to help me out?[wait_1] Or would they be to help yourself?"
    lloyd_narrating neutral "It’s obvious what to say here.[wait_1] I should tell her that I’m trying to help her out."
    lloyd_narrating neutral "The more that she believes I’m doing this for her sake, the more willing she’ll be to assist me."
    $ current_thought = "barbara_thought_129"
    lloyd neutral "I...[wait_05]I was doing it for my own sake."
    lloyd neutral "There’s some information that I want from this group, and it –[wait_05] it doesn’t have anything to do with them conning you."
    $ swap_sprites("barbara_sad")
    barbara "Yeah.[wait_1] That’s what I thought."
    barbara "You’ve been using me, haven’t you?"
    $ current_thought = "barbara_thought_130"
    lloyd neutral "How did you work it out?"
    $ swap_sprites("barbara_smiling")
    barbara "Well, you weren’t exactly subtle about it."
    if (person_visited("barbara", "a", 0) or person_visited("barbara", "a", 1)):
        barbara "Whenever you come in here, you end up asking me to do something for you."
        barbara "The more I thought about it, the more I realised how odd it was that you were being so...[wait_05]altruistic."
    else:
        barbara "You went from asking me all these –[wait_05] asking all of these questions to suddenly talking about how you could help me and get me some compensation."
    barbara "I probably should have realised your motivations earlier, but I...[wait_05]I liked helping you."
    barbara "And I thought that you were being genuine...[wait_05]I guess I was pretty blind to what sort of person you are."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_131"
    barbara "One thing that I would like to know, however...[wait_05]what exactly is your job?"
    barbara "I don’t know what you would have gotten out of it if I had found somebody stealing from me."
    $ current_thought = "barbara_thought_132"
    lloyd neutral "I’m between jobs at present."
    lloyd neutral "I should have one –[wait_05] I moved here, to this city, because I received an offer –[wait_05] but it didn’t pan out."
    lloyd neutral "I’m living off my savings at the moment."
    $ swap_sprites("barbara_sad")
    barbara "Oof, that’s no good.[wait_1] What exactly happened?"
    lloyd neutral "I’m normally a photographer."
    lloyd neutral "A magazine headhunted me –[wait_05] they said that they liked my existing work –[wait_05] but when I went through the interview process they said that they’d be using AI to touch up my work before it went to print."
    lloyd neutral "I didn’t like that."
    $ current_thought = "barbara_thought_133"
    barbara "Yeah, it’s ruining a lot of jobs now, huh?"
    barbara "I barely have to deal with it –[wait_05] I get some prompts in some of my bookkeeping software telling me to use the AI features –[wait_05] but even that’s too much."
    barbara "I can’t imagine how bad being in a creative industry that’s pushing for it must be."
    $ current_thought = "barbara_thought_134"
    barbara "Anyway, I guess that if you’re a photographer, there was never really a chance of you helping me with my problems, was there?"
    lloyd neutral "You mean catching the person who stole those drinks from you?"
    $ current_thought = "barbara_thought_135"
    barbara "That’s part of it, yeah.[wait_1] But just –[wait_05] can I tell you something, Lloyd?"
    barbara "I’m the third generation of my family to run this bar."
    barbara "The building was bought by Grandma decades ago, and she was determined to make it work."
    barbara "Everybody around her said that she didn’t know what she was doing, that she couldn’t compete with the other bars in the area."
    barbara "She didn’t care.[wait_1] She had an idea and wanted to stick with it."
    barbara "That’s why it’s called Icarus –[wait_05] she said that she’d rather fly close to the sun and fall than stay on the ground and never try."
    barbara "Anyway, I don’t know if you’ve noticed this, but there aren’t a lot of other bars in the immediate area."
    barbara "They all shut down over the years for one reason or another, but Icarus kept flying high."
    barbara " Because Grandma knew what people wanted from their locals.[wait_1] Because she listened to people, and because she had good business sense."
    barbara "She made the bar work, when everybody else said that it was going to fail."
    $ current_thought = "barbara_thought_136"
    barbara "Sorry, I’m rambling, aren’t I?[wait_1] I’ll –[wait_05] bear with me, I’m getting to the point."
    barbara "When it was time for her to retire Grandma passed the bar down to Mum, who took it over and ran it for decades."
    barbara "A few months ago, Mum decided that she was getting old enough to retire herself, and asked if I wanted to take over."
    barbara "I said yes, of course.[wait_1] I’d decided a long time ago that I wanted to take over, and put my own mark on the family legacy."
    barbara "Only...[wait_05]here’s the thing.[wait_1] It’s been losing money since I took over."
    barbara "The bar is still profitable, and it’s not like I’m going to run out of money in the next week or anything, but I can’t run it indefinitely at this rate."
    barbara "I’ve –[wait_05] I thought that I had prepared myself for this."
    barbara "I helped out here as soon as I was able to, I went to business school, but I –[wait_05] none of it prepares you for the reality."
    barbara "I don’t even know why the numbers are down."
    barbara "Is it the economy, and I’m just getting screwed over by things out of my control?"
    barbara "Am I reaching less people online, and the profitability of my business is entirely affected by the search algorithms?"
    barbara "Or am I just doing something wrong?"
    $ current_thought = "barbara_thought_137"
    barbara "So...[wait_05]getting to the point, when I found the footage of that guy getting all of those drinks for free, I thought, “Great![wait_1] This is it![wait_1] This is why I’m not making as much profit!”"
    barbara "“People are stealing from me, and I’m ordering more often than I realised![wait_1] Once Lloyd catches them, the numbers will go up again!”"
    barbara "Before that, I’d been seriously wondering how I could turn things around."
    barbara "I’d been thinking I might need to raise prices, or start cutting employees’ shifts."
    barbara "I didn’t want to do any of it, but I needed to think in the long term."
    barbara "So now that I know that you aren’t able to help me, that guys like this aren’t to blame for falling profits, I have to consider what’s best for the business."
    barbara "I just want to run a place that supports the community and is properly affordable, but I don’t think that it’s viable."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_138"
    barbara "Anyway, sorry for dumping all of that on you.[wait_1] I didn’t realise that would get so long-winded, I just..."
    $ swap_sprites("barbara_sad")
    barbara "I’ve got a lot of emotions around this place, and what the future of it looks like."
    $ current_thought = "barbara_thought_139"
    lloyd neutral "Barbara...[wait_05]there’s a reason that I lied to you."
    lloyd neutral "It wasn’t something that I was doing for fun.[wait_1] I was doing it because I thought that the ends justified the means."
    lloyd neutral "I thought that if you got me what I wanted then that would make the lie worth it."
    lloyd neutral "With that in mind, I think that you should keep running the bar the way you currently are."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_140"
    barbara "Sorry?"
    lloyd neutral "If you raise prices, or drop your employees’ shifts, you’ll tell yourself that it’s alright for now.[wait_1] You’ll say that it’s because you need to look at the long-term picture."
    lloyd neutral "But if you embrace a small justification now you’ll find it easier to adopt the next change, and the one after that."
    lloyd neutral "You’ll find it easier to be selfish, and to think of what your business needs, rather than what your customers need."
    lloyd neutral "It will sound like a reasonable argument in your mind, but it won’t be."
    $ current_thought = "barbara_thought_141"
    barbara "...I’m not entirely sure what the right thing to do is, then."
    $ swap_sprites("barbara_smiling")
    $ current_thought = "barbara_thought_142"
    barbara "But I do see your point, Lloyd."
    barbara "Thanks.[wait_1] And I’m sorry if I was a bit harsh towards you."
    lloyd neutral "Don’t be.[wait_1] You were right to criticise my actions."
    lloyd neutral "I lied to you and used you; that was selfish of me."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_143"
    barbara "Why were you so set on lying to me, anyway?"
    barbara "You said that photography’s your thing –[wait_05] so why are you trying to find the guy with the white streak, and his friends, anyway?"
    lloyd_narrating neutral "My instinct is to lie to her once again.[wait_1] To make up some plausible excuse."
    lloyd_narrating neutral "But I’ve lied enough to Barbara.[wait_1] She’s opened up to me; the least that I can do is be honest with her."
    $ current_thought = "barbara_thought_144"
    lloyd neutral "This may sound crazy, but the man with the white streak –[wait_05] I believe he has psychic powers."
    lloyd neutral "I think that there are others like him, and that a serial killer is picking them off.[wait_1] I’d like to warn them."
    $ swap_sprites("barbara_smiling")
    barbara "Psychic powers?[wait_1] Like –[wait_05] reading minds, telekinesis, that sort of thing?"
    lloyd neutral "Yes."
    $ swap_sprites("barbara_thinking")
    $ current_thought = "barbara_thought_145"
    barbara "Huh.[wait_1] You know, somehow I believe you."
    $ swap_sprites("barbara_smiling")
    barbara "I don’t suppose you’re influencing me with your own psychic powers, are you?"
    lloyd neutral "Of course not."
    lloyd_thinking thinking "There’s no need to tell her about the powers that I do have.[wait_1] I don’t know how she would react."
    $ current_thought = "barbara_thought_146"
    barbara "Good, because I’m going to need control of all my mental faculties if we’re going to stop this killer!"
    lloyd neutral "“We’re” going to stop this killer?"
    barbara "What, you think I’m not good enough to help?"
    barbara "I’ve already found things out for you –[wait_05] we might as well make it official!"
    $ current_thought = "barbara_thought_147"
    lloyd neutral "Well...[wait_05]only if you agree to let me help with Icarus."
    lloyd neutral "I can take much better publicity photos than the ones you currently have."
    barbara "No complaints from me, Lloyd."
    barbara "You know, I think this is the start of a beautiful relationship."
    lloyd neutral "I can’t disagree with that."
    hide barbara_smiling with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "Barbara soon realises that the bar requires her attention and excuses herself."
    lloyd_narrating neutral "I’m glad to see her go –[wait_05] I don’t want her prioritising my needs over her own."
    lloyd_narrating neutral "For the first time since I began this investigation, I have an ally on my side who understands the scope of what I’m undertaking, and who is willing to help."
    lloyd_narrating neutral "I make my way to the bar, telling Barbara that we should meet up again tomorrow, when things are less chaotic here."
    lloyd_narrating neutral "She agrees with me, and I prepare to leave."
    lloyd_narrating friendly "But not before purchasing a pint of pilsner." 
    lloyd_narrating friendly "After all, it’s good to support your local."

    $ visit_person("barbara", "b", 0)
    jump branch_a_b_4_4