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
    $ visit_person("barbara", "a", 3)
    return 