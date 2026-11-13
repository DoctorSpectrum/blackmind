label graves_investigation:
    $ current_thought_block = "mind_read_graves"
    if (branch == "a" and day == 1):
        jump graves_a_1
    elif (branch == "a" and day == 2):
        jump graves_a_2
    elif (branch == "a" and day == 3):
        jump graves_a_3
    elif (branch == "a" and day == 4):
        jump graves_a_4
    elif (branch == "b"):
        jump graves_b_4
    elif (branch == "c" and day == 2):
        jump graves_c_2
    elif (branch == "c" and day == 3):
        jump graves_c_3
    
    return

label graves_a_1:
    scene black_bg with quick_dissolve
    lloyd_narrating neutral "I’ve never had to hire, or even interact with, a private investigator. I chose this one because he’s not too far from my apartment – if I’m going to be seeing him often, I might as well make sure that it’s a short journey."
    lloyd_narrating neutral "It’s just crossing a few busy intersections, then pressing the intercom for the fourth floor of an office building."
    #SFX door reception buzz
    unknown "Whaddya want?"
    lloyd neutral "I’ve got someone that needs investigating.[wait_1] I hear that your office has the best people around for that kind of job."
    lloyd_narrating neutral "It’s a lie that I’m willing to tell.[wait_1] It never hurts to butter up the people you’ll be owing money to."
    lloyd_narrating neutral "The door unlocks a few seconds later, accompanied by the same voice as before."
    unknown "Come on in, kid."
    lloyd_narrating neutral "I do as the voice says and enter the building.[wait_1] The elevator claims to be out of order, so I climb the flight of aging stairs up to the fourth floor."
    scene detective_office with slow_dissolve
    lloyd_narrating neutral "It’s hardly the whiskey-soaked, chiaroscuro-styled office that Raymond Chandler would have you believe detectives work out of."
    lloyd_narrating neutral "It’s fairly small, and looks like it was only moved into a few hours ago."
    lloyd_narrating neutral "Much of the equipment is new, and there’s a very sterile smell in the air, as though the furniture’s only just come out of the box."
    $ swap_sprites("graves_intimidating", slow_dissolve)
    $ current_thought = "graves_thought_01"
    show screen psychic_powers
    detective "You’re the guy who called through?"
    lloyd_narrating neutral "The accent matches the person who responded on the intercom."
    lloyd_narrating neutral "I’m insulted by his prior referral to me as “kid” – he looks like he’s straight out of high school."
    $ current_thought = "graves_thought_02"
    lloyd neutral "Correct.[wait_1] Lloyd Chen, mister...?"
    lloyd_narrating neutral "I reach out a hand, and he warmly embraces it with one of his own."
    lloyd_narrating neutral "His hands aren’t overly hairy and his palm isn’t callused – he’s definitely younger than he’s acting."
    $ current_thought = "graves_thought_03"
    detective "Graves."
    lloyd_thinking neutral "Graves...?"
    $ current_thought = "graves_thought_04"
    graves "Yeah.[wait_1] They call me that because of how many friends I’ve had to bury."
    lloyd_narrating neutral "For a second he stares daggers at me, as though this fact is my fault."
    lloyd_narrating neutral "Then he bursts out laughing."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_05"
    graves "Ha ha ha![wait_1] Just kidding, mate –[wait_05] actually, my name is –[wait_05] my last name is Gravdahl."
    graves "But it makes for a nice – it’s not a bad nickname, right?"
    lloyd_narrating neutral "It’s an odd way to introduce yourself, and I wonder whether Gravdahl – Graves – is just a child playing at being an adult."
    lloyd_narrating neutral "Acting the way he thinks he should instead of the way he wants to.[wait_1] For a second I consider leaving."
    lloyd_narrating neutral "But I’m already here, and I might as well give him my pitch."
    $ current_thought = "graves_thought_06"
    lloyd neutral "It really isn’t.[wait_1] Mister Gravdahl –"
    graves "Graves, please![wait_1] It took me a long time to come up with such a great nickname!"
    $ current_thought = "graves_thought_07"
    lloyd neutral "Mister...[wait_05]Graves, shall we discuss the case I’ve come here for?"
    graves "Of course!"
    graves "Feel free to sit down at that desk.[wait_1] I’ve got a partner that –[wait_05] my partner is, um, out on a case, and so it’s –[wait_05] the seat there is free."
    lloyd_narrating neutral "I do as he suggests, adjust the height of the chair, and begin."
    $ current_thought = "graves_thought_08"
    lloyd neutral "I’ll put it to you simply, Mister Graves:[wait_05] there’s somebody in this city that I’m looking for."
    lloyd neutral "I’m not sure where exactly they are, but they’re here somewhere.[wait_1] I would like to find this person as quickly as possible."
    $ swap_sprites("graves_thinking")
    $ current_thought = "graves_thought_09"
    graves "Understood.[wait_1] May I enquire why exactly you’d like to – what the nature of your relationship with this individual is?"
    $ current_thought = "graves_thought_10"
    lloyd neutral "I’d rather keep that to myself."
    graves "Hmm.[wait_1] If you want it that way, then sure."
    $ current_thought = "graves_thought_11"
    lloyd neutral "If I were to hire you to find this individual, then how long do you anticipate it would take you to find them?"
    $ current_thought = "graves_thought_12"
    lloyd neutral "That depends.[wait_1] Can I get this person’s name, or is that also something that you’d – that you want to keep to yourself?"
    lloyd_thinking neutral "I have no idea what the man in black’s name is.[wait_1] If I explain that no doubt he’ll find it odd."
    lloyd_thinking neutral "I’m going to play my cards to my chest for now."
    $ current_thought = "graves_thought_13"
    lloyd neutral "I’d also rather keep that to myself."
    $ current_thought = "graves_thought_14"
    graves "Well, that complicates things.[wait_1] Do you have a picture?[wait_1] Or any other identifying information?"
    $ current_thought = "graves_thought_15"
    lloyd neutral "I can give you a physical description.[wait_1] A sketch, too, if you don’t mind an amateur’s hand."
    $ swap_sprites("graves_intimidating")
    graves "Is this some sort of –[wait_05] is this a joke?"
    graves "Or do you think that private investigators are –[wait_05] are magicians of some kind?"
    $ current_thought = "graves_thought_16"
    lloyd neutral "If I knew how to find this man beyond the...[wait_05]photo that I’ve been shown, I’d take care of this myself."
    graves "Fine then.[wait_1] Give me what you’ve got."
    $ swap_sprites("graves_thinking")
    lloyd_narrating neutral "I describe what I could see of the man in black during my vision to Graves."
    lloyd_narrating neutral "I tell him the exact tone of the man’s skin.[wait_1] I tell him about the shape of the man’s chin, and the angle of his cheekbones."
    lloyd_narrating neutral "I describe irrelevant details, such as the expression on his face and the clothes he was wearing."
    lloyd_narrating neutral "Throughout it all, Graves merely responds with a nod and a grunt from time to time."
    lloyd_narrating neutral "He isn’t taking any notes or recording any of what I’m saying, and my confidence in him is waning."
    lloyd_narrating neutral "I finally finish my description and wait for his response."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_17"
    graves "Alright then...[wait_05]I’ll tell you what, buddy: it’s a bit vague, but I’ll do what I can."
    graves "Of course, I’m in the middle of another case at the moment, so I’ve got a bit of work to do for that too."
    graves "So...[wait_05]realistically I can probably open up a file for you for now, and I’ll let you know how things are going after a few days."
    graves "How does that sound?"
    lloyd thinking "A few days isn’t fast enough![wait_1] The man in black could be killing again tonight – I need faster results!" 
    lloyd thinking "How can I get him to work faster?"
    menu:
        "Insist that he prioritise it":
            $ current_thought = "graves_thought_18"
            lloyd neutral "I’m going to need you to prioritise this.[wait_1] I can’t tell you why, but finding this man is incredibly important."
            $ current_thought = "graves_thought_19"
            graves "Like I said, I’ll do what I can, but at the same time –[wait_05] first come first serve."
            graves "If I get any opportunities, I’ll start on –[wait_05] I’ll do what I can for you, but you can’t blame me for wanting to finish off my existing case, right?"
            lloyd_thinking neutral "He’s got a point.[wait_1] I’m already committed now; I might as well wait and see what he turns up."
        "Call him out on his lie" (locked=not check_boolean("graves_no_cases"), message="You have not read the related thought"):
            lloyd_thinking neutral "I read his mind when I first came in, and he thought to himself that he didn’t have a case at the moment."
            lloyd_thinking neutral "He’s lying to me."
            lloyd_thinking neutral "I’m going to put some pressure on him and see how he reacts."
            $ current_thought = "graves_thought_20"
            lloyd neutral "You're lying."
            $ swap_sprites("graves_shocked")
            graves "What?![wait_1] What makes you –[wait_05] why would you say that?!"
            $ current_thought = "graves_thought_21"
            lloyd neutral "You don’t have another case to work on at the moment."
            lloyd neutral "There’s nothing stopping you from starting work on this today."
            graves "I –[wait_05] alright, I don’t know how you found that out, but it’s true."
            $ swap_sprites("graves_sad")
            $ current_thought = "graves_thought_22"
            graves "We’re –[wait_05] my partner and I, we’re still pretty new to this –[wait_05] to this work."
            graves "We’ve picked up a few cases here and there, but we –[wait_05] they’re not coming in as heavily as I –[wait_05] as we thought they would."
            graves "So I thought that if I –[wait_05] if I made out that I had a heavy workload, that this would take a few days, you’d be really impressed if I came back with something tomorrow, and –[wait_05] and maybe spread the word a bit."
            lloyd_thinking neutral "It’s a stupid business tactic.[wait_1] How many people might be turned off by lies like that?"
            $ current_thought = "graves_thought_23"
            graves "I’ll –[wait_05] I’ll start working on this once you leave."
            graves "I can’t guarantee that it’ll get very far along by the end of today, but I’ll at least get some momentum going."
            $ swap_sprites("graves_smiling")
            $ add_boolean("identify_graves_lie")
    $ current_thought = "graves_thought_24"
    graves "If you do want to come by later tonight, I can show you where things are sitting at the end of the day."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    lloyd_narrating neutral "I accept what he says and then spend some time filling out paperwork before leaving the office."
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Graves didn’t provide me with any guarantees, but he’s at least willing to be transparent about where he’s at by the end of the day."
    lloyd_narrating neutral "If I come by, I might be able to help steer him in the right direction, and he’ll hopefully have a better sense of how long things will take."

    $ visit_person("graves", "a", 0)
    return

label graves_a_2:
    scene black_bg with quick_dissolve
    if (not person_visited("graves", "a", 0)):
        lloyd_narrating neutral "Private investigators are frequently hired to find missing information, people, or objects by the people who desperately need them."
        lloyd_narrating neutral "Will this one be able to find my missing memories and fill in the gaps of last night?"
        lloyd_narrating neutral "I won’t find out unless I ask."
        lloyd_narrating neutral "I make my way through a few busy intersections and towards a tall building."
        lloyd_narrating neutral "I don’t recognise any of the businesses listed on the sign outside it, which tells me that the offices for lease likely aren’t very expensive."
        lloyd_narrating neutral "I press the intercom for the fourth floor."
        # SFX door reception buzz
        unknown "What izzit?"
        lloyd neutral "I’m hoping to hire one of your detectives.[wait_1] Is now inconvenient?"
        lloyd_narrating neutral "There’s a few moments of silence before the voice responds."
        unknown "Yeah, come on up."
        lloyd_narrating neutral "The promise of a new client tends to be a good incentive."
        lloyd_narrating neutral "The door clicks open and I step inside."
        scene detective_office with slow_dissolve
        lloyd_narrating neutral "The room is far from the stereotypical image of a detective’s place of business."
        lloyd_narrating neutral "No half-slitted blinds, wooden furniture, or deep shadows."
        lloyd_narrating neutral "If I didn’t know what the office was for I would have guessed that an IT company had just started up here."
        $ swap_sprites("graves_intimidating", slow_dissolve)
        $ current_thought = "graves_thought_34"
        show screen psychic_powers
        detective "So, you’re looking for some investigating?"
        lloyd_narrating neutral "There’s only one person in the office, although the second desk tells me that he’s probably not the only employee here."
        lloyd_narrating neutral "His voice comes out in a growl, but I suspect that he’s exaggerating it –[wait_05] he looks as though he’s barely graduated from high school."
        lloyd neutral "Correct, Mister...?"
        $ current_thought = "graves_thought_35"
        detective "Graves.[wait_1] You don’t need to tell me what’s on your mind –[wait_05] “why do they call him Graves?”"
        lloyd_narrating neutral "The thought wasn’t on my mind at all."
        graves "It’s because of how much time I spend among them."
        lloyd_narrating neutral "I stare at him, unsure how to react.[wait_1] It almost sounds like a joke."
        lloyd_narrating neutral "A moment later he confirms that it is."
        $ swap_sprites("graves_smiling")
        $ current_thought = "graves_thought_36"
        graves "Ha, the look on your face![wait_1] I really had you going, didn’t I?"
        lloyd_narrating neutral "He really didn’t."
        graves "It’s a nickname I picked up a little while back that stuck –[wait_05] long story."
        $ current_thought = "graves_thought_37"
        graves "But enough about me –[wait_05] what’s your name, mate?"
        lloyd neutral "Lloyd Chen."
        $ current_thought = "graves_thought_38"
        graves "Nice to meet you, Lloyd."
        graves "So tell me –[wait_05] what sort of investigating, exactly, are we talking about?"
    else:
        lloyd_narrating neutral "I wasn’t overly impressed with Graves when we met yesterday, but I can’t fault his confidence in himself."
        lloyd_narrating neutral "If I explain what I know of last night and share all relevant information with him he may have some answers."
        lloyd_narrating neutral "Even if all that he can do is give me some direction to look in, that’s more than I currently have."
        lloyd_narrating neutral "I make my way towards the office building that he works out of."
        lloyd_narrating neutral "The light for a pedestrian crossing turns red just as I reach it which leaves me standing at the crossing for a good minute or so, freezing in the wind as I wait."
        lloyd_narrating neutral "Eventually it returns to green and I continue to the office, making a decent enough pace that I warm myself up simply through the exercise."
        scene detective_office with slow_dissolve
        $ swap_sprites("graves_smiling", slow_dissolve)
        $ current_thought = "graves_thought_39"
        show screen psychic_powers
        lloyd_narrating neutral "Graves is leaning against a desk as I enter the office, patiently waiting for me."
        lloyd_narrating neutral "If I’ve interrupted any other work of his it’s not immediately apparent – there are no scattered papers on the desk or files brought up on his computer."
        lloyd_narrating neutral "Did he put things away as I made my way up the stairs?[wait_1] Or does he have no work beyond what I’ve given him?"
        graves "Lloyd![wait_1] Great to see you again, mate!"
        lloyd neutral "The feeling’s mutual."
        lloyd_narrating neutral "I narrowly avoid a hug from him, but only by giving a handshake."
        $ current_thought = "graves_thought_40"
        graves "Unfortunately, I can’t say that I’ve got very good news for you on the investigation so far."
        graves "I thought that I had a –[wait_05] there was a lead that looked pretty promising, but when I kept looking into it I –[wait_05] it turned out to be a dead end."
        lloyd_thinking thinking "That isn’t good to hear."
        $ current_thought = "graves_thought_41"
        lloyd neutral "That’s fine, I wasn’t expecting something so quickly."
        lloyd neutral "I’m here today to ask you to look into something else."
        graves "Oh?[wait_1] Let’s hear it then."
    $ current_thought = "graves_thought_42"
    lloyd neutral "This may sound strange, but I’d like you to find out what I was doing last night."
    $ swap_sprites("graves_thinking")
    graves "This isn’t some sort of –[wait_05] this isn’t a logic deduction puzzle or something like that, is it?"
    graves "You’re not –[wait_05] this is something that you’re actually wanting me to do?"
    lloyd neutral "I suppose that I’m more looking to hear your opinion on things than do serious detective work."
    lloyd neutral "But if you think it warrants an investigation I’ll trust your judgement."
    $ current_thought = "graves_thought_43"
    graves "What exactly has –[wait_05] what are you asking for?[wait_1] What’s happened?"
    lloyd neutral "Last evening I went to bed as per usual.[wait_1] There was nothing different about it from any other night, and I fell asleep before too long."
    graves "Alright..."
    lloyd neutral "A few hours later I woke up.[wait_1] I was in a bar with a drink in my hand and several more in my stomach."
    lloyd neutral "From the bartender’s reaction it was clear that I’d simply been drinking, like any other patron."
    $ current_thought = "graves_thought_44"
    graves "But you don’t remember any of it."
    lloyd neutral "Correct.[wait_1] My decision to visit a bar and drink so heavily is strange enough on its own, but the blank space of memory muddles things further."
    graves "Do you remember the name of the bar?"
    $ current_thought = "graves_thought_45"
    lloyd neutral "Icarus."
    graves "Icarus...[wait_05]that bar..."
    lloyd neutral "Yes?"
    graves "It’s...[wait_05]a name that means nothing to me."
    lloyd neutral "Oh."
    $ current_thought = "graves_thought_46"
    graves "Regarding your statement: you said that you woke up a few hours after going to bed.[wait_1] What exactly do you mean by that?"
    graves "As in, you –[wait_05] do you mean that you think you were unconscious and came to; you were lying down when you woke up?"
    graves "Or do you mean that you –[wait_05] do you mean that you sort of...[wait_05]realised what was going on, as a sort of –[wait_05] as though you’d been having an out-of-body experience?"
    lloyd neutral "The latter more so than the former."
    $ current_thought = "graves_thought_47"
    graves "Right.[wait_1] And have you –[wait_05] have you visited this bar again today to see whether they can tell you anything about what happened?"
    graves "You’re –[wait_05] I think that they’re probably going to be your best bet in discovering what went on.[wait_1] Assuming that they’re open during the day, that is."
    $ current_thought = "graves_thought_48"
    lloyd neutral "Are you saying that you can’t help me?"
    $ swap_sprites("graves_intimidating")
    graves "What exactly do you think I can –[wait_05] do you want me to do?"
    graves "I don’t know what you got up to after you went to bed."
    graves "I didn’t go to the –[wait_05] I wasn’t in the bar myself, so I don’t know what you were up to before you regained your –[wait_05] before you came to."
    graves "My honest opinion?"
    graves "You probably couldn’t sleep, so you decided to go out for a drink to relax, and then you had enough to forget things."
    graves "It’s a bit –[wait_05] it’s kind of weird, but stranger things have happened, you know?"
    lloyd_narrating neutral "He has a point.[wait_1] What exactly was I expecting to happen?"
    lloyd_narrating neutral "For Graves to interrogate every person in-between my apartment and the bar who might have an idea of what happened?[wait_1] He’s only human."
    lloyd_narrating neutral "He doesn’t know about my psychic powers.[wait_1] The answer is more likely to be related to them."
    lloyd_thinking neutral "But even if my psychic powers were responsible for my memories being wiped, that still doesn’t explain the initial impetus that had me visiting the bar."
    lloyd_thinking neutral "Was I contacted by someone and told to go there?"
    lloyd_thinking neutral "Did I have a breakthrough and realise that something important had happened at the bar?"
    lloyd_thinking neutral "Or...[wait_05]was going to?"
    $ current_thought = "graves_thought_49"
    lloyd neutral "You make a valid point, Graves, but I’m suspicious even so."
    lloyd neutral "Visiting a bar isn’t my usual idea of a relaxing time."
    $ swap_sprites("graves_thinking")
    graves "So there was some other reason that you visited it, and the alcohol was enough for you to forget it."
    $ current_thought = "graves_thought_50"
    lloyd neutral "But what was that initial reason?[wait_1] I must have been at that bar for a reason."
    $ swap_sprites("graves_intimidating")
    graves "I couldn’t tell you.[wait_1] You’d be better off returning there and asking around yourself."
    if (person_visited("barbara", "a", 1)):
        $ current_thought = "graves_thought_51"
        lloyd neutral "I’ve already done so.[wait_1] I didn’t find any answers, but maybe you could."
        $ swap_sprites("graves_thinking")
        graves "Ah.[wait_1] So you want me to investigate this bar?"
        graves "Icarus, you said it was called?"
        lloyd neutral "It couldn’t hurt."
        if (not person_visited("cat", "a", 1) and len(days["a"][1]) < 2):
            lloyd_thinking thinking "And while he does that, I could look into my psychic powers."
        elif (not person_visited("cat", "a", 1) and len(days["a"][1]) >= 2):
            lloyd_thinking thinking "If I’d thought about it, I could have done some research into my psychic powers while he investigates it."
    else:
        lloyd_thinking thinking "He’s got a valid point.[wait_1] It may be a lengthy train ride away, but I should have prioritised visiting the bar before coming here."
        if (len(days["a"][1]) < 2):
            lloyd_thinking thinking "I still have time to investigate it myself, but he might uncover information that I can’t find if he looks into it."
        else:
            lloyd_thinking thinking "I’ll have to get Graves to investigate it –[wait_05] there’s not enough time in the day for me to."
        $ current_thought = "graves_thought_51"
        lloyd neutral "Even so, would you be willing to investigate the bar and see whether you can uncover anything?[wait_1] It’s more your forte than mine."
    graves "...Fine.[wait_1] I’ll see what I can do, but you shouldn’t expect much."
    graves "What you get up to in the evening is more your business than mine."
    lloyd neutral "Thank you, I appreciate it."
    $ current_thought = "graves_thought_52"
    graves "Any other chores that I can take care of while I’m –[wait_05] anything else that you need me to do?"
    lloyd neutral "Nothing that I can think of."
    lloyd_thinking thinking "Best to just ignore the sarcasm.[wait_1] He won’t be complaining when he sends me the bill."
    $ current_thought = "graves_thought_53"
    graves "Alright.[wait_1] I’ll let you know what I come up with, and whether I can find anything about it that would have –[wait_05] that had you thinking it was worth visiting last night."
    lloyd neutral "Thank you, Graves."
    $ swap_sprites("graves_smiling")
    graves "No thanks needed.[wait_1] It comes with the job."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I decide to leave before the tension mounts any further."
    lloyd_narrating neutral "Graves may not be happy about the job, but I’m confident that he’ll discover more about the bar than I can."

    $ visit_person("graves", "a", 1)
    return

label graves_a_3:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "The man with the white streak was a victim of the man in black.[wait_1] The reason that he was targeted wasn’t immediately apparent to me, but it must exist regardless."
    lloyd_narrating neutral "If I can discover that reason then I can identify the man in black’s next target."
    if (person_visited("graves", "a", 0) or person_visited("graves", "a", 1)):
        lloyd_narrating neutral "I’m going to trust Graves to identify the man with the white streak, his past, and the reason that he was targeted by the man in black."
        lloyd_narrating neutral "All of this information is hidden somewhere, waiting to be uncovered, and I trust Graves to find it."
        lloyd_narrating neutral "Whatever he can discover will be more than I currently know."
        lloyd_thinking thinking "I can also check in on how Graves is going with his other tasks."
    else:
        lloyd_narrating neutral "I’m going to visit a nearby detective and have them identify the man with the white streak, his past, and the reason that he was targeted by the man in black."
        lloyd_narrating neutral "All of the information will be hidden somewhere, waiting to be uncovered, and a detective will be the person to find it."
        lloyd_narrating neutral "Whatever they can discover will be more than I currently know."
        lloyd_thinking thinking "This will also be a good test to see how effective this detective is."
        lloyd_thinking thinking "If they’re competent then I could ask them to investigate some other things."
    lloyd_narrating neutral "I make my way on foot along a few different streets and cross several intersections."
    lloyd_narrating neutral "The traffic is relentless, and the lights seem to take forever to turn red."
    lloyd_narrating neutral "Everybody is in such a rush to get to their destination, taking no time to slow down and relax."
    lloyd_narrating neutral "Then again, I’m no better."
    if (person_visited("graves", "a", 0) or person_visited("graves", "a", 1)):
        lloyd_narrating neutral "I buzz the intercom at Graves’ office building and enter."
        lloyd_narrating neutral "By the time I’ve climbed the stairs and reached Graves’ office, I’m feeling sweaty and uncomfortable."
        lloyd_narrating neutral "I enter his office."
    else:
        lloyd_narrating neutral "I double-check that the address I found online is the one in front of me."
        lloyd_narrating neutral "It’s a large building which purports to hold a multitude of offices, none of which are for businesses that I’ve ever heard of."
        lloyd_narrating neutral "I press the intercom for the fourth floor."
        # SFX door reception buzz
        unknown "Izzet important?"
        lloyd neutral "If it wasn’t, then I wouldn’t be here."
        unknown "...Ya make a good point.[wait_1] Come on up."
        lloyd_narrating neutral "The door unlocks and I enter the building."
        lloyd_narrating neutral "A sign claims that the elevator is undergoing repairs, forcing me to climb the stairs up to the detective’s office."
        lloyd_narrating neutral "I’m feeling a little sweaty and uncomfortable as I enter it."
    scene detective_office with slow_dissolve
    lloyd_narrating neutral "A dull drone confirms that an ancient air conditioning unit is on in the office today, struggling to do its duty."
    if (person_visited("graves", "a", 0) or person_visited("graves", "a", 1)):
        lloyd_narrating neutral "Otherwise, everything is as it was the last time that I was here."
        lloyd_narrating neutral "If Graves has been doing any work, the state of the office doesn’t make it apparent."
    else:
        lloyd_narrating neutral "It’s a reminder that the stereotypical offices of detectives are a thing of the past."
        lloyd_narrating neutral "There’s no heavy wooden furniture, glasses of whiskey, or dramatic lighting to be found here."
        lloyd_narrating neutral "Before me I see a fairly modern office, with two desks and computers."
        lloyd_narrating neutral "It could just as easily be used by lawyers, accountants, or any other job less dramatic than private investigator."
    $ swap_sprites("graves_intimidating", slow_dissolve)
    show screen psychic_powers
    if (person_visited("graves", "a", 0) or person_visited("graves", "a", 1)):
        $ current_thought = "graves_thought_54"
        lloyd_narrating neutral "Graves himself is leaning against the desk in a pose that makes me wonder whether he’s trying to make himself look cool."
        lloyd_narrating neutral "If so then it isn’t working –[wait_05] he looks more melodramatic than anything."
        lloyd_narrating neutral "As I enter he relaxes a little and smiles."
        $ swap_sprites("graves_smiling")
        graves "Ah, Lloyd.[wait_1] I knew that I’d be seeing you soon."
        lloyd_thinking thinking "My talking over the intercom was probably a big tip-off."
        $ current_thought = "graves_thought_55"
        graves "I’m guessing that you want an update on the current investigation?"
        $ current_thought = "graves_thought_56"
        lloyd neutral "As a matter of fact, I have another job for you.[wait_1] But an update would be appreciated."
        graves "More work?[wait_1] Lucky me."
        $ swap_sprites("graves_thinking")
        if (person_visited("graves", "a", 1)):
            $ current_thought = "graves_thought_57"
            graves "The bar that you asked me to look into –[wait_05] the place where you said you came to in, with no memory of how you got there.[wait_1] Icarus."
            lloyd neutral "Yes."
            $ current_thought = "graves_thought_58"
            graves "I’ve found out some interesting information about both the bar itself and its current owner, but no smoking gun that points to why you would have visited it."
            graves "You’re not an –[wait_05] you haven’t invested any money in it or –[wait_05] you haven’t done anything like that, right?"
            lloyd neutral "I hadn’t even heard of the bar before two days ago.[wait_1] Why?"
            graves "Oh, it wouldn’t be relevant to you then."
        else:
            $ current_thought = "graves_thought_59"
            graves "But anyway, this guy that you asked me to –[wait_05] the man in black."
            graves "I had a promising lead that I was looking into, but it turned out to be a dead end.[wait_1] Almost literally."
            lloyd neutral "What do you mean by that?"
            graves "Just that it didn’t pan out, and I realised that I was barking up the wrong tree."
            graves "But I’ve put a few other feelers out, and I’m hoping that one of them will bite."
            lloyd_thinking thinking "That’s an awful mixing of metaphors."
        $ swap_sprites("graves_smiling")
        $ current_thought = "graves_thought_60"
        graves "Do you want me to keep looking into it, and see what I can dig up?[wait_1] Or do you want me to prioritise this new job?"
        lloyd neutral "All of it’s relevant, but I’d like you to at least put some time into investigating this new matter for me."
        graves "And that is...?"
    else:
        $ current_thought = "graves_thought_61"
        lloyd_narrating neutral "A man that I assume is one of the detectives that works here is leaning against a desk."
        lloyd_narrating neutral "The pose looks forced, and I genuinely wonder whether he’s trying to make himself look cool for a new client."
        lloyd_narrating neutral "The first words out of his mouth don’t help matters."
        detective "So, you’re the new client."
        lloyd_thinking thinking "If I want to hire you."
        lloyd neutral "The name’s Lloyd."
        $ current_thought = "graves_thought_62"
        detective "They call me Graves...[wait_1]because I climbed out of one."
        lloyd_thinking thinking "Is a line like that supposed to impress me?"
        graves "Right.[wait_1] And your actual name is...?"
        $ current_thought = "graves_thought_63"
        graves "I don’t need any name other than that."
        lloyd_narrating neutral "The more that I study him the more apparent it becomes that Graves is younger than he’s projecting.[wait_1] He’s probably barely out of university, if not high school."
        lloyd_narrating neutral "It occurs to me what a mistake it was to prioritise the closest agency that I could find."
        $ current_thought = "graves_thought_64"
        lloyd neutral "Understood.[wait_1] Well, I believe that I’ve made a mistake, so I’ll be –"
        $ swap_sprites("graves_shocked")
        graves "W-wait![wait_1] I –[wait_05] can you at least tell me about the case?"
        graves "I’ll –[wait_05] I can give you a good price, I promise!"
        lloyd_narrating neutral "His voice is less gravelly than it was before, confirming my suspicions about his age."
        lloyd_narrating neutral "I look him over.[wait_1] He really is just a kid, probably with barely any experience under his belt. "
        $ current_thought = "graves_thought_65"
        lloyd neutral "Alright, sure."
        lloyd_thinking thinking "I know what it’s like to be starving for work.[wait_1] I’ll throw him this bone."
        $ swap_sprites("graves_smiling")
        graves "Great![wait_1] What needs to be investigated?[wait_1] Give me all the details!"
    $ current_thought = "graves_thought_66"
    lloyd neutral "There’s someone that I’d like you to look into."
    lloyd neutral "Find out his background, his personal history, and whatever else you can about him."
    graves "Sounds doable.[wait_1] Do you have a name for this person?"
    lloyd neutral "I don’t."
    $ swap_sprites("graves_thinking")
    graves "How about a photo?[wait_1] Or some information about where they work, or live?"
    $ current_thought = "graves_thought_67"
    lloyd neutral "I can give you a physical description."
    if (person_visited("graves", "a", 0)):
        $ swap_sprites("graves_smiling")
        graves "Ah, the Lloyd special."
    else:
        graves "Better than nothing, I guess."
    graves "What does this person look like, then?"
    $ current_thought = "graves_thought_68"
    lloyd neutral "He’s a young adult male, perhaps a little younger than me.[wait_1] He has a small soul patch and a gap in his teeth."
    lloyd neutral "His most prominent feature, however, is a streak of white in his hair, which is otherwise brown."
    lloyd_narrating neutral "He was also coated in blood and dying when I saw him last.[wait_1] But I’d rather not share that information with Graves."
    lloyd_narrating neutral "If he finds out that this is related to a murder case he might be scared away from investigating."
    $ swap_sprites("graves_thinking")
    $ current_thought = "graves_thought_69"
    graves "A white streak of hair, huh?[wait_1] That’s not something that you see every day."
    graves "That’s pretty much all the information that you have, yeah?[wait_1] Or is there anything else?"
    menu:
        "Mention Usbourne" (locked=not check_boolean("graves_recognises_jack"), message="You have not read the related thought"):
            $ current_thought = "graves_thought_70"
            lloyd neutral "Sorry, I actually misspoke before.[wait_1] I said that I didn’t have a name for this person, but I was only thinking of given names."
            graves "Oh, so you’ve got a surname?"
            $ current_thought = "graves_thought_71"
            lloyd neutral "Yes.[wait_1] It’s Usbourne."
            graves "Usbourne, huh?[wait_1] That’ll definitely make things easier –[wait_05] I can probably have something for you by this evening, if that works for you."
            lloyd neutral "I may be able to visit you then.[wait_1] Thank you."
            lloyd_thinking thinking "He seems fairly confident that he can find the information I’m looking for."
            lloyd_thinking thinking "It sounds as though he already knows the man with the white streak.[wait_1] But what’s the connection?"
            $ add_boolean("graves_mentioned_jack")
        "Nothing else":
            $ current_thought = "graves_thought_72"
            lloyd neutral "Unfortunately not.[wait_1] A description is all that I can give you."
            $ swap_sprites("graves_thinking")
            graves "Mmm.[wait_1] That’ll make things a bit more difficult then...[wait_05]can you give me a day or two to try and find out about this person?"
            graves "With just a description it can take a while to get started."
            lloyd "Of course."
            lloyd_thinking thinking "There’s no point in coming here later tonight then.[wait_1] I should give Graves the time he’s asked for."
    $ current_thought = "graves_thought_73"
    graves "Anyway, I’ll do what I can to find out about this guy."
    graves "Tell me, though –[wait_05] why exactly are you –[wait_05] what exactly do you want to know about this guy for?"
    lloyd_narrating neutral "I’ve already decided to keep the man with the white streak’s death, and the related murders, from Graves."
    lloyd_narrating neutral "I hold up my camera."
    $ current_thought = "graves_thought_74"
    lloyd_narrating neutral "I’m hoping to ask him to do some modelling for me.[wait_1] He’s a –[wait_05] I think that he would make a good model."
    $ swap_sprites("graves_intimidating")
    graves "You want him to be a model, but you’re asking me to look into his past?"
    lloyd neutral "I...[wait_05]yes, it’s always good to do a background check for this sort of thing."
    lloyd neutral "He might have had a –[wait_05] he might have a bad reputation in the industry if he’s done modelling before, or he might –[wait_05] sometimes it’s good to know exactly what a person is like before you hire them for a high-profile role such as modelling."
    lloyd neutral "I wouldn’t want him to say things that cause issues for any brands."
    $ current_thought = "graves_thought_75"
    $ swap_sprites("graves_smiling")
    graves "Ah, yeah, when you put it that way, it makes perfect sense![wait_1] Well, I’d be more than happy to help."
    lloyd_thinking thinking "He has to know that I’m lying.[wait_1] Why isn’t he throwing accusations at me?"
    lloyd neutral "Thank you, Graves.[wait_1] I’m looking forward to what you discover."
    $ current_thought = "graves_thought_76"
    graves "No worries.[wait_1] Well, if there isn’t anything else then?"
    lloyd neutral "No, nothing else."
    graves "I’d better get to work then!"
    lloyd neutral "Of course.[wait_1] I’ll see you at a later date, Graves."
    graves "See you then!"
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_thinking thinking "Why did Graves go along with my lie?[wait_1] What does he gain from it?"
    lloyd_narrating neutral "Whatever the reason Graves has for trusting me, it’s to my benefit.[wait_1] He’s said that he’ll investigate the man with the white streak’s past."
    lloyd_narrating neutral "I’ll return to his office in the future and see what he manages to uncover."

    $ visit_person("graves", "a", 2)
    return

label graves_a_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Once again it’s been a long day."
    lloyd_narrating neutral "I haven’t discovered any new information about Jack Usbourne that would have motivated the man in black to kill him."
    lloyd_narrating neutral "I still don’t even know who the man in black is."
    lloyd_narrating neutral "Just like yesterday, I’m relying on Graves to reveal the missing pieces of the puzzle to me.[wait_1] Any scrap of information will be more than I currently have."
    lloyd_narrating neutral "I skip dinner and instead prioritise making my way to Graves’ office.[wait_1] The sooner that I get in touch with him the better."
    lloyd_narrating neutral "Beyond my vision of the man in black and a little bit of Jack’s past, I haven’t gained anything particularly insightful from this whole affair."
    lloyd_narrating neutral "I’m relying on Graves to salvage this investigation and give me some progress.[wait_1] I don’t want to think about the alternative."
    scene detective_office with slow_dissolve
    $ swap_sprites("graves_intimidating", slow_dissolve)
    $ current_thought = "graves_thought_99"
    show screen psychic_powers
    lloyd_narrating neutral "There’s a weariness to Graves’ body language as I enter the office."
    lloyd_narrating neutral "It’s impossible to discern its origin –[wait_05] has he been working himself to the bone and the fatigue is wearing him down?[wait_1] Or is it a side effect of the disappointment that comes with no meaningful progress?"
    lloyd neutral "Good evening, Graves.[wait_1] How has your day been?"
    lloyd_narrating neutral "For the brief instant before he begins speaking his expression is a grimace."
    lloyd_narrating neutral "In that moment I know the answer to my question, and it’s not a good one."
    $ current_thought = "graves_thought_100"
    graves "Not great, I’m afraid.[wait_1] Lloyd...[wait_05]I’ve got some bad news for you."
    lloyd neutral "You weren’t able to discover anything about Jack."
    graves "That depends upon your definition of discovering things."
    graves "I found out plenty about him –[wait_05] some odd jobs he’s held, old social media posts, more information on his days in court."
    $ swap_sprites("graves_sad")
    $ current_thought = "graves_thought_101"
    graves "But there’s no –[wait_05] I didn’t find the smoking gun that points to why someone would kill him."
    graves "I even looked up those other two victims to see whether I could find anything in –[wait_05] any commonalities that they had, but there’s nothing."
    lloyd_narrating neutral "It was stupid of me to expect anything more."
    lloyd_narrating neutral "Graves is a professional –[wait_05] in spite of his youth –[wait_05] but he can’t work miracles.[wait_1] He’d need days to investigate everything."
    lloyd_narrating neutral "To find out whether Jack overheard something he shouldn’t have in a bar, or if the murders are for something far in the past."
    lloyd_narrating neutral "Or maybe we’re both deluding ourselves."
    lloyd_narrating neutral "Maybe it really is as I previously considered and Jack is simply a victim of a random act of violence."
    lloyd_narrating neutral "Maybe I’m just fooling myself into thinking that I can discover something the authorities can’t."
    lloyd_narrating neutral "Maybe I’ve just been wasting my time all along."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_102"
    graves "Hey, Lloyd –[wait_05] are you alright?"
    graves "You’re pretty –[wait_05] I think I’ve seen statues that are more talkative than you are right now, you know?"
    lloyd neutral "Sorry.[wait_1] I’m just realising that we –[wait_05] that this is probably a fool’s task."
    lloyd neutral "And with that realisation I’m thinking that I’ve probably been wasting my time.[wait_1] Yours too."
    $ swap_sprites("graves_thinking")
    $ current_thought = "graves_thought_103"
    graves "Well...[wait_05]not that I’m –[wait_05] I’m not particularly happy about that, I won’t lie."
    graves "But can I ask what you –[wait_05] why exactly you’re concerning yourself with this?"
    graves "You did previously say that you’re –[wait_05] that Jack died in front of you, and that you feel that you owe him, yeah."
    graves "But –[wait_05] correct me if I’m wrong, but you’re not really a cop or anything, right?"
    $ current_thought = "graves_thought_104"
    lloyd neutral "Correct.[wait_1] Would you believe that I’m a photographer?[wait_1] Or rather, I used to be one."
    $ swap_sprites("graves_smiling")
    graves "Given that I’ve never seen you without that camera, I’m not particularly surprised."
    graves "What type of photographer?[wait_1] Weddings, nature..?"
    $ current_thought = "graves_thought_105"
    lloyd neutral "I worked for a newspaper, until...[wait_05]well, that’s in the past now."
    lloyd neutral "But ideally I’d like to be a professional artist."
    graves "Right, I imagine that’d be a lot more fulfilling.[wait_1] Probably more fun, too."
    $ swap_sprites("graves_thinking")
    $ current_thought = "graves_thought_106"
    graves "But with that in mind, you –[wait_05] I don’t get why you’re investigating Jack’s death so much."
    graves "I was thinking about what you –[wait_05] about what you said yesterday, and I –[wait_05] yeah, he died in front of you, I get it."
    graves "But I’d have thought that most people in that situation would –[wait_05] that they’d go and talk to their therapist about it."
    graves "You have a therapist, right?[wait_1] I think that everybody should have one; you’d be amazed at the difference they make."
    lloyd_thinking thinking "I don’t need a therapist."
    graves "So anyway, I’m wondering –[wait_05] why exactly are you looking into this so much?"
    $ current_thought = "graves_thought_107"
    lloyd neutral "I thought that I could make a difference.[wait_1] That I could do some good with myself and help out."
    lloyd neutral "I thought that I had advantages the authorities didn’t."
    lloyd_thinking thinking "Namely, the precognitive vision of the killer."
    lloyd neutral "I’m realising now that I wasn’t thinking clearly.[wait_1] I didn’t realise what the reality would be like."
    $ current_thought = "graves_thought_108"
    graves "Do you wish that you hadn’t bothered, then?"
    lloyd_narrating neutral "It’s an interesting question.[wait_1] Should I have kept to myself and pretended that I hadn’t had my vision?"
    lloyd_narrating neutral "I would have liked to have been more productive over the last few days."
    lloyd neutral "...No, I don’t."
    lloyd neutral "If nothing else I would have felt bad if I’d turned a blind eye to the situation."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_109"
    graves "And that’s how you know that it’s worth doing."
    graves "Not that –[wait_05] not that we should have guilt motivating us a lot of the time, but if we –[wait_05] if you know that something’s the right thing to do, then why shouldn’t you –[wait_05] why not do it?"
    lloyd_narrating neutral "Graves leans against his desk as though a weight has come off his shoulders.[wait_1] For the first time since I’ve met him, he removes his sunglasses."
    scene cg4_0 with slow_dissolve
    $ current_thought = "graves_thought_110"
    graves "In this job I sometimes –[wait_05] there’s a lot of pressure, a lot of the time, to make progress and find stuff out."
    graves "Sometimes I get really stressed out, and I often feel that I’m not –[wait_05] that I should be doing things differently, or that I’m not getting things done as efficiently as I should."
    graves "It’s not always a great feeling."
    graves "But the thing I’ve also realised, is that –[wait_05] it’s that if I didn’t do it right –[wait_05] if I just did a half-assed job of everything, then that’d be really shitty of me."
    graves "If all that I ever did was what I wanted, then I –[wait_05] yeah, there’d be no pressure, but I wouldn’t really be a good person."
    graves "And I want to be a good person.[wait_1] Don’t you?"
    graves "The pressure, or the guilt, or the –[wait_05] whatever it is, it might not be fun to deal with, but it’s better to have it there and know that you’re doing the right thing, than to just –[wait_05] I don’t know, be selfish, and only think about yourself."
    scene detective_office with quick_dissolve
    $ swap_sprites("graves_smiling", quick_dissolve)
    $ current_thought = "graves_thought_111"
    lloyd neutral "So you think that it’s a good thing that I’ve been looking into Jack’s death?"
    graves "I –[wait_05] it’s possibly a bit quixotic, but I think that as long as you aren’t doing anything stupid, and you’re doing it for the right reasons, yeah."
    graves "It’s good that you want to help out and do some good."
    lloyd_thinking thinking "Maybe he’s right.[wait_1] Just because I –[wait_05] we –[wait_05] haven’t found anything yet, it doesn’t mean that stopping the killer is worthless."
    $ current_thought = "graves_thought_112"
    lloyd neutral "I’m going to be honest, Graves:[wait_05] I initially thought that you were a bit young for this job."
    lloyd neutral "I was a bit underwhelmed by our first meeting and thought that I might be wasting my time.[wait_1] But you’re surprisingly knowledgeable."
    graves "Heh, thanks.[wait_1] I guess I had to grow up pretty fast in high school."
    $ current_thought = "graves_thought_113"
    lloyd neutral "What do you mean by that?"
    $ swap_sprites("graves_sad")
    graves "I...[wait_1]one of my friends got pretty sick."
    graves "They –[wait_05] they didn’t get any better, and before long, they...[wait_05]it was all over."
    $ current_thought = "graves_thought_114"
    lloyd neutral "I’m sorry for your loss."
    $ swap_sprites("graves_smiling")
    graves "Don’t worry about it."
    graves "It was a while back, and things –[wait_05] they got pretty messy after they died, but they –[wait_05] we got through it in the end."
    graves "I guess it was that which really taught me –[wait_05] which showed me how important both giving and receiving support is."
    $ current_thought = "graves_thought_115"
    lloyd neutral "With that in mind, do you want to continue looking into Jack’s death with me?[wait_1] Even though you think that it’s quixotic?"
    graves "As long as you can afford the bill, sure."
    graves "But you shouldn’t expect results to just –[wait_05] to come out of nowhere."
    lloyd neutral "That’s fine.[wait_1] As you’ve said:[wait_05] it isn’t easy, but it is the right thing to do."
    lloyd_thinking thinking "And if I can get a benefit out of it, there’s all the more reason to stop the killer."
    $ current_thought = "graves_thought_116"
    graves "Great.[wait_1] Well then, do you want to meet again at this time tomorrow?"
    lloyd neutral "That sounds good to me.[wait_1] Thank you, Graves."
    graves "No problem, Lloyd.[wait_1] See you then."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve

    $ visit_person("graves", "a", 3)
    jump branch_a_b_4_4

label graves_b_4:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "The man in black is killing people with psychic abilities."
    lloyd_narrating neutral "The man with the white streak wasn’t his first victim, and I doubt he’s intended to be the last."
    lloyd_narrating neutral "I need to find the others with psychic abilities so that I can warn them of him."
    if (person_visited("graves", "a", 0) or person_visited("graves", "a", 1) or person_visited("graves", "a", 2)):
        lloyd_narrating neutral "Graves hasn’t achieved much in the time that I’ve worked with him.[wait_1] But I’m going to trust him with this."
        lloyd_narrating neutral "If he can identify and track down even one other person with my abilities then they may be a gateway into an entire community of psychics."
    else:
        lloyd_narrating neutral "I haven’t worked with any of the detectives at this agency before.[wait_1] But I’m going to trust them with this."
        lloyd_narrating neutral "If they can identify and track down even one other person with my abilities then I may have a gateway into an entire community of psychics."
    lloyd_narrating neutral "I can warn them about the man in black and the threat he poses."
    lloyd_narrating neutral "I have a bit of a journey to make before I reach the detectives’ office."
    lloyd_narrating neutral "I pass a multitude of people as I walk through the street towards it."
    if (person_visited("graves", "a", 0) or person_visited("graves", "a", 1) or person_visited("graves", "a", 2)):
        lloyd_narrating neutral "I wonder whether any of them have visited Graves before, or been the target of one of his investigations."
        lloyd_narrating neutral "Are they an open book to him?[wait_1] Does he know all of their secrets?"
        lloyd_narrating neutral "However much work he’s had to put into it, I could replicate in seconds with careful use of my abilities."
        lloyd_narrating neutral "It’s a little unsettling to think of the power contained in my mind."
        lloyd_narrating neutral "I reach Graves’ building and press the intercom button."
        lloyd_narrating neutral "Graves lets me in and I make my way up the stairs.[wait_1] There’s no sign of progress on the elevator."
        scene detective_office with slow_dissolve
        $ swap_sprites("graves_smiling", slow_dissolve)
        $ current_thought = "graves_thought_117"
        show screen psychic_powers
        lloyd_narrating neutral "Graves is looking as casual as ever.[wait_1] He’s leaning back in his chair and writing something on a notepad."
        lloyd_narrating neutral "Now that I think about it, I’m unsure that I’ve ever seen him do work."
        graves "Hey, Lloyd."
        if (person_visited("graves", "a", 2)):
            $ current_thought = "graves_thought_118"
            graves "Is everything alright?[wait_1] You didn’t come by last night."
            lloyd neutral "My apologies.[wait_1] I had another lead which I decided to prioritise."
            $ current_thought = "graves_thought_119"
            graves "You weren’t in any danger?[wait_1] Nothing bad happened to you?"
            lloyd neutral "No danger."
            $ swap_sprites("graves_intimidating")
            graves "Hmm.[wait_1] Would have been nice if you’d let me know."
            $ swap_sprites("graves_thinking")
            $ current_thought = "graves_thought_120"
            graves "Still, though –[wait_05] I guess it worked out in the end."
            graves "I had a bit of thinking about the guy you asked me about.[wait_05] The one with the white streak."
            lloyd_thinking thinking "I’ve already found the information I need thanks to Barbara."
            lloyd_thinking thinking "The man with the white streak was a psychic, and that’s why the man in black wanted to kill him."
            lloyd_thinking thinking "I doubt that Graves can give me anything more important than that."
            graves "You see, he’s actually a former client of mine.[wait_1] I realised it shortly after –[wait_05] as you were describing him to me."
            lloyd_thinking thinking "Graves knew the man with the white streak?"
            lloyd_thinking thinking "Then he may know about his social network.[wait_1] There may be other psychics among them."
            $ current_thought = "graves_thought_121"
            lloyd neutral "Do you know any of his friends?[wait_1] Or associates?"
            lloyd neutral "The information I found from my other lead has me wanting to find people who knew him."
            $ swap_sprites("graves_intimidating")
            graves "Well, here’s the thing I decided:[wait_05] I’m going to give you his contact details."
            graves "You can talk to him yourself, and he can decide whether or not to –[wait_05] he can work out how much he wants to share with you."
            lloyd_thinking thinking "Of course.[wait_1] Graves doesn’t know."
            $ current_thought = "graves_thought_122"
            lloyd neutral "His contact information won’t do me any good.[wait_1] He’s dead."
            $ swap_sprites("graves_shocked")
            graves "Dead?!"
            lloyd neutral "I should have told you sooner.[wait_1] It’s related to why I’ve been looking into him."
            $ swap_sprites("graves_sad")
            $ current_thought = "graves_thought_81"
            graves "Man...[wait_05]I wish I’d known that sooner.[wait_1] I –[wait_05] shit."
            lloyd_narrating neutral "I give him some time to process his thoughts."
            lloyd_narrating neutral "When I feel it’s been long enough I speak up."
            lloyd neutral "Do you have any information about his associates that you can share with me?"
            $ swap_sprites("graves_thinking")
            $ current_thought = "graves_thought_123"
            graves "I don’t.[wait_1] I could look into him further and –[wait_05] I could see what I can find out about him, but I don’t have anything for you right away."
            graves "Why?"
            lloyd neutral "It’s related to a new investigation I’d like you to begin."
            graves "What’s it involve?"
        elif (person_visited("graves", "a", 1)):
            $ current_thought = "graves_thought_58"
            graves "How are you doing?[wait_1] Were you able to find anything out about your evening?"
            graves "I wasn’t able to find out much about that bar, unfortunately."
            $ current_thought = "graves_thought_124"
            lloyd neutral "Don’t worry about it.[wait_1] There are more important things happening."
            $ swap_sprites("graves_thinking")
            graves "Oh?[wait_1] Do tell."
        elif (person_visited("graves", "a", 0)):
            $ current_thought = "graves_thought_125"
            graves "It’s been a few days since we talked."
            lloyd_thinking thinking "I had forgotten that I asked him to look into the man in black.[wait_1] I should have come by sooner."
            lloyd neutral "What did you find?"
            $ swap_sprites("graves_thinking")
            $ current_thought = "graves_thought_126"
            graves "Nothing so far, I’m afraid."
            graves "There was one particular lead that –[wait_05] I thought I had something going with one thing, but it ended up being a dead end."
            $ current_thought = "graves_thought_127"
            lloyd neutral "And you’ve found nothing promising since then?"
            graves "Sorry, I’m still looking."
            $ current_thought = "graves_thought_41"
            lloyd neutral "That’s fine.[wait_1] I have more important things to talk to you about."
            graves "Yeah?[wait_1] What sort of things?"
    else:
        lloyd_narrating neutral "I wonder whether any of them have visited the detectives before, or been the target of one of their investigations."
        lloyd_narrating neutral "Are they open books to them?[wait_1] Do they know all of their secrets?"
        lloyd_narrating neutral "However much work they’ve had to put into it, I could replicate in seconds with careful use of my abilities." 
        lloyd_narrating neutral "It’s a little unsettling to think of the power contained in my mind."
        lloyd_narrating neutral "I reach the building that the detectives’ office is located at.[wait_1] It looks fairly nondescript and unassuming."
        lloyd_narrating neutral "Will the private investigators be good enough to find other psychics for me?"
        lloyd_narrating neutral "I reach out and press the intercom button."
        # SFX door reception buzz
        unknown "Yeah?"
        lloyd_narrating neutral "The voice that comes through the speaker is as rough as gravel."
        lloyd neutral "I have a case for your office.[wait_1] Are you interested?"
        lloyd_narrating neutral "Silence for several seconds.[wait_1] And then –"
        unknown "Alright, come on up."
        lloyd_narrating neutral "The door clicks open and I make my way inside.[wait_1] I climb a stairwell up to the fourth floor and enter a door with the agency’s logo on it."
        scene detective_office with slow_dissolve
        lloyd_narrating neutral "The office I step into is as nondescript as the building.[wait_1] It feels more suited to bookkeepers or accountants than private investigators."
        $ swap_sprites("graves_intimidating", slow_dissolve)
        $ current_thought = "graves_thought_128"
        show screen psychic_powers
        lloyd_narrating neutral "The man in the office, by contrast, is a little more of what I’ve been expecting."
        detective "So, you say you’ve got a case for us?"
        lloyd neutral "I do.[wait_1] You are...?"
        detective "Call me Graves.[wait_1] I usually find myself surrounded by them these days."
        lloyd_thinking thinking "Is that supposed to be a joke?"
        lloyd_narrating neutral "Now that I’m hearing his voice in person rather than over an intercom, it’s obvious that his tone is forced."
        lloyd_narrating neutral "He’s also much younger than I expected; in his early twenties at most."
        $ current_thought = "graves_thought_129"
        lloyd neutral "I’m Lloyd." 
        lloyd neutral "You said “us”.[wait_1] Is your partner around?"
        lloyd_thinking thinking "Are they more mature than you are?"
        graves "Working a case at the moment."
        graves "But I can –[wait_05] if you give me the details, I’ll pass them on and we’ll work out shifts together."
        lloyd_narrating neutral "I’m unsure that I trust him.[wait_1] The sense that I’m getting is that he’s acting the way he thinks a private investigator should."
        lloyd_narrating neutral "But I’m already here and may as well continue."
    $ current_thought = "graves_thought_130"
    lloyd neutral "Do you know of any people with special abilities?[wait_1] I’m currently trying to find some."
    $ swap_sprites("graves_thinking")
    graves "Special abilities?"
    graves "Sorry, I don’t really know what you mean by that.[wait_1] Could you clarify?"
    if (not person_visited("graves", "a", 0) and not person_visited("graves", "a", 1) and not person_visited("graves", "a", 2)):
        lloyd_thinking thinking "His demeanour changed once we began talking."
        lloyd_thinking thinking " It looks like the tough personality is just an act for the clients.[wait_1] One that he’s not very good at keeping up."
    $ current_thought = "graves_thought_131"
    lloyd neutral "Have you ever heard of people who can dig up any type of information, no matter how private it may be?"
    graves "I’m sorry, I still don’t know what you’re talking about.[wait_1] Do you want to hire a different detective?"
    if (not person_visited("graves", "a", 0) and not person_visited("graves", "a", 1) and not person_visited("graves", "a", 2)):
        graves "You’ve –[wait_05] you literally just walked through the door!"
    $ current_thought = "graves_thought_132"
    lloyd neutral "No, that’s not what I’m talking about."
    lloyd neutral "How about...[wait_05]have you ever encountered somebody who knows what you’re going to say before you say it?"
    graves "You want somebody who’s good at reading people?"
    lloyd neutral "In a sense.[wait_1] But one who is also surrounded by strange phenomena."
    $ current_thought = "graves_thought_133"
    graves "...[wait_05]Is this, like...[wait_05]a sex thing?"
    lloyd_thinking thinking "Alright, the time for subtlety is over."
    $ current_thought = "graves_thought_134"
    lloyd neutral "Psychic powers, Graves.[wait_1] Extrasensory perception."
    lloyd neutral "Have you ever heard of people who exhibit them?"
    $ swap_sprites("graves_smiling")
    graves "Sorry, is this a joke?[wait_1] You’re looking for people who can –[wait_05] people that can read minds, bend spoons, that sort of thing?"
    lloyd neutral "It isn’t a joke.[wait_1] I have good reason to believe that there are people with abilities here, in the city."
    $ current_thought = "graves_thought_135"
    graves "Come on, Lloyd.[wait_1] Whatever’s set you on this path –[wait_05] whoever’s given you this idea –[wait_05] I can guarantee that you’re going to wind up at a dead end."
    graves "Why would you think that psychic powers are real?"
    lloyd neutral "I’ve seen footage.[wait_1] I know that it’s real."
    $ swap_sprites("graves_intimidating")
    graves "Because no footage has ever been faked.[wait_1] Everything recorded on cameras is definitely real, and it –[wait_05] there’s no such thing as video editing."
    lloyd_thinking thinking "I can see where he’s coming from.[wait_1] If I didn’t have abilities myself I would likely be just as sceptical."
    lloyd_thinking thinking "But there’s no reason for Barbara to have lied to me, and the man with the white streak having passed his powers to me makes sense."
    lloyd_thinking thinking "How can I convince him?"
    $ current_thought = "graves_thought_136"
    lloyd neutral "I can understand your scepticism, Graves.[wait_1] But the footage I saw is genuine."
    lloyd neutral "Is it really that impossible that something thought fictional is simply rare?"
    lloyd_thinking thinking "It’s a weak argument.[wait_1] I have no proof, and I can’t get him any without revealing my powers."
    $ swap_sprites("graves_thinking")
    graves "..."
    graves "You make a good point, Lloyd.[wait_1] If you say that psychic powers are real, then they are."
    graves "I should have known better."
    $ current_thought = "graves_thought_137"
    lloyd neutral "I’m surprised that you changed your opinion so quickly."
    $ swap_sprites("graves_smiling")
    graves "Well, for a start, I think that it’s good to be open to new ideas."
    graves "Have you ever heard about the first time a platypus was discovered and sent for dissection?[wait_1] The lab initially thought that it was a practical joke."
    graves "But when they couldn’t find any stitches or anything, they realised that they were wrong.[wait_1] They should have trusted their colleagues, and they should have been open to the idea of such a weird animal existing."
    graves "Sticking to their rigid old views wouldn’t have done them, or science, any good."
    lloyd_thinking thinking "It’s a similar story with Steve Sasson.[wait_1] If he hadn’t experimented with a charge-coupled device we wouldn’t be where we are today."
    $ current_thought = "graves_thought_138"
    graves "On top of that, there’s been a few things I’ve encountered that I initially thought were just fictional, but turned out to be real."
    lloyd neutral "Such as?"
    $ current_thought = "graves_thought_139"
    graves "Ha, I’ll be keeping that to myself.[wait_1] I don’t want you to have any nightmares."
    lloyd_thinking thinking "Odd response."
    $ current_thought = "graves_thought_140"
    lloyd neutral "Does this mean that you will investigate them, then?[wait_1] People with psychic powers?"
    $ swap_sprites("graves_thinking")
    graves "Well...[wait_05]I’d be lying if I said that I knew where –[wait_05] if I had any idea where I should start investigating."
    graves "This isn’t something that I’ve ever really –[wait_05] I don’t really know how you’re supposed to find people with psychic abilities."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_141"
    graves "Still, first time for everything, right?[wait_1] I’ll see how I go and let you know what I discover."
    lloyd neutral "Thank you.[wait_1] I realise that this is an odd request."
    $ current_thought = "graves_thought_142"
    graves "Honestly, I’ve had weirder.[wait_1] If I didn’t believe in client confidentiality I could literally talk for hours."
    $ current_thought = "graves_thought_143"
    graves "Anything else that I can help you with, or is that all you want from me today?"
    lloyd neutral "I don’t believe so.[wait_1] I’ll return when I’m able to."
    graves "Sounds good to me.[wait_1] I’ll see you then."
    lloyd neutral "Best of luck."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_thinking thinking "I was hoping that he would know somebody with psychic abilities.[wait_1] But an investigation into them is progress regardless."
    lloyd_narrating neutral "There’s nothing else for me to do here.[wait_1] I walk out of the office and begin thinking about my next destination."

    $ visit_person("graves", "b", 0)
    return

label graves_c_2:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I’m making progress.[wait_1] I’ve seen who the killer’s next victim is going to be, and I can save him."
    lloyd_narrating neutral "I just need to find and warn him about the killer and then he’ll be able to anticipate the attack."
    lloyd_narrating neutral "These are the thoughts that I need to reinforce.[wait_1] The thoughts that I need to remind myself of."
    lloyd_narrating neutral "I need to remind myself that I have learned new information and that my goal of stopping the killer is still viable."
    lloyd_narrating neutral "Because in truth I don’t feel that I’ve made progress.[wait_1] I don’t feel that I know what I’m doing."
    lloyd_narrating neutral "Besides discovering the killer’s next victim, a man who is a complete unknown to me, all that I’ve learned is that the man in black, Allan Docherty, is dead.[wait_1] It’s made me doubt both my visions and myself."
    lloyd_narrating neutral "I can’t let this setback stop me."
    lloyd_narrating neutral "Knowing the next victim is still sufficient knowledge for me to warn them, and if a new wrench is thrown in the works –[wait_05] should the victim have been killed weeks ago, for instance –[wait_05] that will still give me new information about how my psychic abilities work."
    lloyd_narrating neutral "But to gain that knowledge I need to find the victim.[wait_1] For that, a visit to the detectives’ agency is in hand."
    lloyd_narrating neutral "The day is cold as I travel towards the agency, walking from block to block."
    lloyd_narrating neutral "Besides the overcast sky, a further contributor to the low temperature is a consistent wind which started blowing as I began walking."
    lloyd_narrating neutral "It’s bad enough that it sends my hair flying chaotically, but things are made worse when it blows my jacket open and sends it billowing out behind me.[wait_1] For the moment I zip it up further before I continue to the detectives’ agency."
    if (person_visited("graves", "a", 0)):
        scene detective_office with slow_dissolve
        $ swap_sprites("graves_smiling", slow_dissolve)
        $ current_thought = "graves_thought_144"
        show screen psychic_powers
        lloyd_narrating neutral "As I enter the office Graves is writing something on a notepad.[wait_1] My curiosity gets the better of me and I try to read what I can of it."
        lloyd_narrating neutral "All that I manage to parse is what looks like a list of blood types before he realises what I’m doing and hides it."
        $ current_thought = "graves_thought_145"
        graves "Hi, Lloyd.[wait_1] Sorry –[wait_05] had a thought and I wanted to make some notes before it left me."
        graves "How’s it going?"
        $ current_thought = "graves_thought_146"
        lloyd neutral "Hello, Graves.[wait_1] I’m alright."
        $ current_thought = "graves_thought_40"
        graves "Regarding the stuff you asked me about yesterday –[wait_05] I thought that I’d found a solid lead, but it ended up being a dead end."
        graves "But I’ll keep looking, I promise."
        $ current_thought = "graves_thought_147"
        lloyd neutral "That’s fine.[wait_1] Actually, I’d like you to look into somebody else who’s related to the case."
    else:
        lloyd_narrating neutral "The building that the detectives’ agency is situated in is fairly small."
        lloyd_narrating neutral "I don’t recognise any of the company logos on the directory, telling me that office spaces are likely cheap to rent."
        lloyd_narrating neutral "I press the intercom for the fourth floor."
        # SFX door reception buzz
        unknown "Graves here."
        lloyd_thinking thinking "Graves?"
        lloyd neutral "Could I please come in?[wait_1] I have a case that I’d like to hire you for."
        unknown "Sure thing.[wait_1] C’mon up, kid."
        lloyd_narrating neutral "The door unlocks and I enter the building.[wait_1] A sign tells me that the elevator is out of order so I climb the stairs upwards."
        scene detective_office with slow_dissolve
        lloyd_narrating neutral "The detectives’ office has more plastic and metal than the stereotypical image would have you expect."
        lloyd_narrating neutral "There are more computers, too, in lieu of heavy oak desks and worn down leather couches."
        $ swap_sprites("graves_intimidating", slow_dissolve)
        $ current_thought = "graves_thought_148"
        show screen psychic_powers
        lloyd_narrating neutral "Although there are two desks there’s only one occupant of the room."
        lloyd_narrating neutral "He looks frustrated enough that I wonder whether I’ve interrupted him in the middle of something important."
        lloyd neutral "Hi, I’m Lloyd."
        graves "Graves.[wait_1] They call me that because I’m as tough as a gravestone."
        lloyd_narrating neutral "Bereft of the aged intercom, his voice sounds much younger.[wait_1] In fact, the more that I look at him the more apparent it becomes that he’s not as old as he’s projecting himself to be."
        $ current_thought = "graves_thought_149"
        lloyd neutral "Right.[wait_1] Are you free to discuss my case?"
        graves "I don’t know.[wait_1] Are you ready to have it blown wide open?"
        lloyd neutral "You don’t even know what it’s about yet."
        graves "I –[wait_05] yes, but I can –[wait_05] I’ll find out whatever you want me to."
        graves "I’ll solve the myste-[wait_05] myste-"
        lloyd_narrating neutral "Graves starts coughing violently.[wait_1] I debate giving him a solid thump on the back but before I can do so he lets out one final hack, ending the fit."
        $ swap_sprites("graves_smiling")
        $ current_thought = "graves_thought_150"
        graves "Well, so much for the grizzled investigator persona.[wait_1] Let’s try this again."
        graves "What’s your case about, Lloyd?"
        lloyd neutral "I was hoping that you’d be able to find somebody for me.[wait_1] There’s a man that I want to find."
    $ current_thought = "graves_thought_151"
    lloyd neutral "I can’t give you his name –[wait_05] I don’t know it –[wait_05] but I can describe him for you.[wait_1] The most notable thing about him is the suit that he wears.[wait_1] It’s quite expensive but has a somewhat eccentric design –[wait_05] a dazzling black and white striped pattern."
    lloyd neutral "Below it he’s fairly bulky and well-muscled.[wait_1] He’s slightly taller than me."
    $ current_thought = "graves_thought_152"
    graves "Any idea of his age?"
    lloyd neutral "Probably somewhere in his 40s.[wait_1] His hair is jet black and slicked back by some sort of tonic or product."
    lloyd neutral "He also has a moustache."
    graves "What type?[wait_1] If you had to –[wait_05] would you describe it as being closer to a walrus, in terms of thickness, or more along the lines of an english?"
    lloyd neutral "I don’t know.[wait_1] It’s not particularly thick, and it’s in two halves."
    $ current_thought = "graves_thought_153"
    graves "Ah, I see.[wait_1] And what else?"
    $ current_thought = "graves_thought_154"
    lloyd neutral "That’s about it.[wait_1] That’s all that I –[wait_05] I don’t have any more details than that."
    lloyd neutral "Will that be enough?"
    $ swap_sprites("graves_smiling")
    graves "That’ll be plenty, Lloyd."
    $ current_thought = "graves_thought_155"
    lloyd neutral "Are you sure?"
    if (person_visited("graves", "a", 0)):
        lloyd neutral "I was only able to give you a description yesterday, and you haven’t made much progress on that front."
        graves "But I did make progress, didn’t I?"
    $ current_thought = "graves_thought_156"
    graves "Let me tell you a little story, Lloyd."
    graves "There was this one time that we –[wait_05] my partner and I –[wait_05] were in a similar situation.[wait_1] We were asked to find somebody’s daughter that had run away from home, and were given a picture of her."
    graves "You’d think that since the mother –[wait_05] let’s call her Client X –[wait_05] knew her daughter, she’d tell us her name, right?"
    lloyd_thinking thinking "Why Client X for the alias?"
    graves "Of course she didn’t want to do that.[wait_1] She was worried about a scandal leaking out if we knew who her daughter was."
    graves "We have confidentiality agreements that makes all of that moot, but for whatever reason, she didn’t trust them.[wait_1] Thought that we might sell the information for money, or that our servers would get hacked, maybe."
    graves "On top of that, it all ended up being a –[wait_05] it was pretty stupid of her in the end, since neither she nor her daughter ended up being anybody important."
    graves "I guess she was worried about her reputation amongst her friends, maybe?[wait_1] It was a weird and unnecessary handicap that we got, anyway."
    $ current_thought = "graves_thought_157"
    lloyd neutral "I take it that you wouldn’t be telling me this story if you hadn’t found the daughter?"
    graves "Correct![wait_1] Even though we could have used a bit of extra information, we were able to find the target."
    graves "Let’s call her Daughter X."
    lloyd_thinking thinking "Why Daughter X for the alias?"
    graves "It all comes down to deductive reasoning."
    graves "In this case, we knew that she had run away from home, so we looked into places that a young twentysomething would be able to hide in easily, and would feel comfortable in."
    graves "We looked at where she’d come from to narrow down the location, asked around at a few places we knew, and we were able to –[wait_05] we found Daughter X in the end."
    graves "I’ll admit that we got lucky in that she was at one of the initial places we’d shortlisted, but if she hadn’t been we would have –[wait_05] we’d have looked at what we known and considered some alternatives."
    graves "So don’t worry –[wait_05] we’ll get your guy."
    $ current_thought = "graves_thought_158"
    lloyd neutral "Even though you know far less than you did with the daughter?"
    graves "You’ve still given me more than you can know."
    $ swap_sprites("graves_thinking")
    graves "Although, if you can, uh –[wait_1] you don’t have a name, do you?"
    graves "Because if you did, that would help me a lot."
    lloyd neutral "I don’t, sorry."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_159"
    graves "All good then.[wait_1] Come back when you’re ready and I’ll let you know if I find anything."
    lloyd neutral "Thank you, Graves."
    lloyd_thinking thinking "All that I can do from here is trust in him."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I leave Graves’ office and walk down the stairs, back to the street."
    lloyd_narrating neutral "I start thinking about where to go next..."

    $ visit_person("graves", "c", 0)
    return

label graves_c_3:
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "I’ve discovered who the man in the loud suit was.[wait_1] I’ve confirmed that parts of my vision were accurate."
    lloyd_narrating neutral "I know that the killer will strike again.[wait_1] But the cost to discover it all was too great."
    lloyd_narrating neutral "Sergei Maskelyne is dead because I couldn’t get to him in time."
    lloyd_narrating neutral "My precognitive vision feels less like an advantage I have and more akin to something from a Greek tragedy, showing me scenes that I can’t change."
    lloyd_narrating neutral "If I can’t benefit from the vision, then what was the point of it?"
    lloyd_thinking thinking "It’s alright.[wait_1] I will move past this."
    lloyd_narrating neutral "Sergei may be dead but confirming my vision was accurate does give me a new angle to explore."
    lloyd_narrating neutral "If I can find out who Sergei was then I can identify why the killer targeted him."
    lloyd_narrating neutral "If I can identify why the killer targeted him then I can potentially find his next intended victim."
    lloyd_thinking thinking "I can’t fail them.[wait_1] I have to save the next target."
    lloyd_narrating neutral "My next logical place to visit is the detectives’ agency.[wait_1] The rays of the sun are warm on my face as I walk towards the agency."
    lloyd_narrating neutral "In a more relaxed environment –[wait_05] lying on the grass, or sitting on a comfortable seat –[wait_05] I could picture myself dozing off from their influence."
    lloyd_narrating neutral "But I can’t afford to relax.[wait_1] I need to make up for my error and learn who Sergei was."
    if (person_visited("graves", "c", 0)):
        lloyd_narrating neutral "I press the intercom outside the building and connect to the fourth floor.[wait_1] Graves unlocks the door for me and lets me in."
        scene detective_office with slow_dissolve
        $ swap_sprites("graves_smiling", slow_dissolve)
        $ current_thought = "graves_thought_164"
        show screen psychic_powers
        lloyd_narrating neutral "Graves is casually leaning against his desk as I enter the office, as though he’s got nothing better to do today other than wait for me to visit."
        lloyd_narrating neutral "Unlike when I arrived yesterday, his desk is completely bare."
        lloyd_thinking thinking "Did he intentionally hide his notes so that I wouldn’t read any of them again?"
        $ current_thought = "graves_thought_165"
        graves "Hi, Lloyd.[wait_1] What brings you to my office today?"
        lloyd neutral "It’s regarding the man I was talking to you about yesterday.[wait_1] The one in the loud suit."
        graves "Oh yes?[wait_1] What’s new there?"
        lloyd neutral "I’d like you to investigate his background."
    elif (person_visited("graves", "a", 0)):
        lloyd_narrating neutral "When I press the intercom button for Graves, he’s initially as gruff and grizzled as when I first met him."
        lloyd_narrating neutral "Upon explaining who it is, his demeanour changes completely and he lets me in."
        scene detective_office with slow_dissolve
        $ swap_sprites("graves_smiling", slow_dissolve)
        $ current_thought = "graves_thought_166"
        show screen psychic_powers
        lloyd_narrating neutral "Graves looks completely at ease as I enter his office."
        lloyd_narrating neutral "I can almost understand why he wanted to present a more hard-boiled persona to me when we first met; he’s not far off appearing too inexperienced and naïve."
        graves "Hi, Lloyd.[wait_1] You want an update on the case?"
        $ current_thought = "graves_thought_40"
        graves "If so, I don’t have any good news for you.[wait_1] I thought that I had something, but when I looked further into it the main –[wait_05] it turned out to be a dead end."
        $ current_thought = "graves_thought_41"
        lloyd neutral "That’s fine.[wait_1] There’s somebody else that I’d like you to look into."
        graves "Sure, just give me the details."
    else:
        lloyd_narrating neutral "The building that the detective agency is located in isn’t very large."
        lloyd_narrating neutral "I can’t comment on the inside yet, but the outside it looks as though it’s seen better days."
        lloyd_narrating neutral "I press the intercom button for the fourth floor."
        # SFX door reception buzz
        unknown "Yeah?"
        lloyd neutral "This is the detective agency?"
        unknown "Yeah."
        lloyd neutral "May I be let in?"
        unknown "...Yeah."
        lloyd_narrating neutral "The door unlocks with a loud click and I enter the building."
        scene detective_office with slow_dissolve
        lloyd_narrating neutral "I initially think that I’ve walked into the wrong office before I realise that I’m letting my prejudices affect me."
        lloyd_narrating neutral "It looks more like the office of a small IT company than that of a detective agency."
        lloyd_narrating neutral "But there’s no real reason for private investigators to match the stereotype of a shadowy office filled with alcohol and bullet holes."
        $ swap_sprites("graves_intimidating", slow_dissolve)
        $ current_thought = "graves_thought_167"
        show screen psychic_powers
        lloyd_narrating neutral "Despite the presence of two desks only a single person is present.[wait_1] He’s leaning against a desk, clearly waiting for me."
        detective "Hey."
        lloyd_narrating neutral "His voice is less gravelly than it sounded over the intercom, and I suspect that he’s inflecting to make it sound deeper."
        lloyd_narrating neutral "He’s much younger than I anticipated –[wait_05] likely straight out of university, if not high school."
        lloyd neutral "Hello.[wait_1] I’m Lloyd."
        detective "Graves."
        lloyd_thinking thinking "Is that his name?"
        $ current_thought = "graves_thought_168"
        graves "Because I have one."
        $ current_thought = "graves_thought_169"
        lloyd neutral "One what?"
        graves "I have a grave.[wait_1] Bought it for when this job gets the better of me and I wind up six feet under."
        $ current_thought = "graves_thought_170"
        lloyd neutral "Then why is your nickname Graves plural?"
        graves "Because I...[wait_05] They were..."
        $ swap_sprites("graves_smiling")
        $ current_thought = "graves_thought_171"
        graves "Ah, screw it –[wait_05] I hate doing the whole growly edgy persona thing."
        graves "How can I help you, Lloyd?"
        lloyd neutral "There’s somebody that I’d like you to investigate for me."
    $ current_thought = "graves_thought_172"
    lloyd neutral "His name is Sergei Maskelyne."
    lloyd neutral "I can tell you that he did some work as a stage magician, as well as the address of the venue where he performed some of his act last night.[wait_1] Beyond that he’s a complete unknown to me."
    lloyd neutral "I need to know who exactly he was.[wait_1] Where he was born, how old he was, what his job history consisted of."
    lloyd neutral "What his favourite food was, his favourite sports team, whether he was left or right-handed."
    lloyd_thinking thinking "I need to find out why the killer targeted him.[wait_1] There are too many unknowns at present."
    lloyd neutral "In short, I need to know this man down to the last molecule.[wait_1] No detail is too minor to know."
    $ swap_sprites("graves_thinking")
    $ current_thought = "graves_thought_173"
    graves "A top-to-bottom investigation, huh?[wait_1] I’ll find out as much as I can, but can you tell me why?"
    $ current_thought = "graves_thought_174"
    lloyd neutral "Well, when I said that his name is Sergei Maskelyne...[wait_05]it would have been more appropriate to say that that was his name."
    graves "“That was...”[wait_1] I’m guessing that this isn’t going to be a situation where he –[wait_05] you’re not going to tell me that he legally changed his name, are you?"
    graves "You’re saying his name in the past tense because...[wait_05]well..."
    lloyd neutral "Yes.[wait_1] He died."
    lloyd neutral "He was killed by somebody –[wait_05] I don’t know who yet.[wait_1] But I’m trying to find out."
    if (person_visited("graves", "a", 0)):
        lloyd_thinking thinking "Should I tell Graves that this is related to why I initially came to him?"
        lloyd_thinking thinking "...No, I’ll keep that to myself for now."
        lloyd_thinking thinking "He might be intimidated if he realises who I’ve had him looking into."
    $ current_thought = "graves_thought_175"
    graves "You’re trying to find a killer?[wait_1] There’s more to you than meets the eye, isn’t there, Lloyd?"
    lloyd neutral "You could say the same of virtually anyone, couldn’t you?[wait_1] People are rarely what they present themselves as."
    $ swap_sprites("graves_smiling")
    $ current_thought = "graves_thought_176"
    graves "Well said.[wait_1] On that note, what do you see when you look at me?"
    $ graves_c_3_opinion = None
    menu:
        "A child pretending to be a man":
            $ current_thought = "graves_thought_177"
            lloyd neutral "A child pretending to be a man."
            $ swap_sprites("graves_shocked")
            graves "Ouch!"
            lloyd neutral "You asked me, and I gave you the truth."
            lloyd neutral "You’re mature for your age, Graves, but there’s some things that only age can teach you."
            $ swap_sprites("graves_smiling")
            $ current_thought = "graves_thought_178"
            graves "Fair point.[wait_1] But you’re the one that said people aren’t what they appear to be –[wait_05] so what does that actually make me?"
            $ graves_c_3_opinion = "child"
        "A competent detective":
            $ current_thought = "graves_thought_179"
            lloyd neutral "A competent detective.[wait_1] You know what you’re doing."
            graves "That’s what you see, huh?[wait_1] And do you think that you see that because it’s what I am, or because it’s what I want you to see?"
            $ current_thought = "graves_thought_180"
            lloyd neutral "Provided that you do what I ask of you, it’s irrelevant."
            graves "So you think that the destination matters more than the journey."
        "I don't know you well enough":
            $ current_thought = "graves_thought_181"
            lloyd neutral "I don’t know you well enough.[wait_1] I’d rather not make an assessment until I’ve scratched below the surface a little."
            graves "That’s probably wise.[wait_1] But time waits for no one, and sometimes we have to make a judgement call based on limited knowledge."
    $ current_thought = "graves_thought_182"
    graves "Anyway, that aside –[wait_05] what you’re doing sounds like it’s dangerous, not to mention that it’s –[wait_05] that you probably don’t have all of the answers."
    if (graves_c_3_opinion == "child"):
        lloyd_narrating neutral "I’ve just told him that I think of him as a child.[wait_1] And it’s true."
        lloyd_narrating neutral "The omnipresent sunglasses, the tight leather jacket, the poses and stances...[wait_05]all of it feels as though he’s acting the way that he thinks he should, rather than the way he actually wants to."
        lloyd_narrating neutral "That’s before considering the atrocious persona he presented at the beginning; a hollow imitation of a dated archetype."
        lloyd_narrating neutral "Graves is good enough to help gather information for me, but I doubt that his usefulness will stay consistent."
    else:
        lloyd_narrating neutral "I trust Graves to know more than I do on certain topics, and I trust him to have more time available than I do."
        lloyd_narrating neutral "If neither were true, I wouldn’t have come to him in the first place."
        lloyd_narrating neutral "But what happens as I share information on the investigation with him?[wait_1] How do I tell him about my precognitive visions, or the other psychic abilities that I control?"
        lloyd_narrating neutral "I trust him to help me out, but not enough to share that side of myself with him yet."
    lloyd neutral "Thank you, Graves, but this is something that I have to do on my own."
    $ current_thought = "graves_thought_183"
    graves "I won’t push you on that.[wait_1] But if you do want assistance –[wait_05] if you do want another set of eyes to –[wait_05] do you get what I mean if I say double-check your work?"
    graves "I can help you out, is the point."
    $ current_thought = "graves_thought_184"
    lloyd neutral "At present all that I need from you is an investigation into Sergei’s background."
    $ swap_sprites("graves_thinking")
    graves "And you’ll get that from me."
    graves "Consider this to be a fair warning, though –[wait_05] doing a big investigation will take me a fair bit of –[wait_05] it’ll take me a while."
    graves "And I’d rather do it that way than give you small updates and –[wait_05] and tell you bit by bit what I’ve found out.[wait_1] I could find out that I had the wrong context on something, and mislead you a bit."
    graves "If this is as important as you say it is, I reckon you probably don’t want that."
    $ current_thought = "graves_thought_185"
    lloyd neutral "You’re not incorrect.[wait_1] How long would you expect the investigation to take?"
    graves "At least a week."
    lloyd_thinking scared "A week...![wait_1] The killer could strike multiple times by then!"
    $ current_thought = "graves_thought_186"
    graves "I know what you’re thinking, though –[wait_05] it’s too long for you, right?"
    graves "Here’s my advice:[wait_05] you said that Sergei did his show at a venue last night, right?"
    lloyd neutral "Yes."
    graves "Why don’t you go there and ask them a bit about him?"
    graves "They’re probably not going to be able to give you everything that you want to know about him, but I imagine they would –[wait_05] if he’s done other performances there in the past, they probably know a little bit about him."
    graves "They might even know some of his friends or family, people who attend the show regularly, who can tell you more about Sergei."
    graves "Going there is worth a shot, isn’t it?"
    $ current_thought = "graves_thought_187"
    lloyd neutral "You make a good point, Graves.[wait_1] I’ll consider it."
    $ swap_sprites("graves_smiling")
    graves "Happy to help.[wait_1] Otherwise, I should probably get the ball rolling."
    lloyd neutral "I’ll stay out of your way then.[wait_1] If I need to visit you, I may still come by, though."
    graves "Sure, but just remember:[wait_05] whenever I’m talking to you, I’m not working."
    lloyd neutral "Of course.[wait_1] Goodbye, Graves."
    graves "See ya."
    hide graves_smiling with quick_dissolve
    hide screen psychic_powers
    scene black_bg with slow_dissolve
    lloyd_narrating neutral "Graves’ suggestion of visiting the venue may have some merit."
    lloyd_narrating neutral "As I exit the building and return to the street, I begin thinking about my next destination."

    $ visit_person("graves", "c", 1)
    return