label mind_read_barbara:
    # A-1
    if (current_thought == "barbara_thought_01"):
        bartender_thoughts "Whoa, who sent this hottie here?![wait_1] If he’s looking for a drink, I’d be more than happy to help him!"
    elif (current_thought == "barbara_thought_02"):
        bartender_thoughts "Is he a cop?[wait_1] He’s dressed pretty casually for –[wait_05] oh, wait, I get it."
    elif (current_thought == "barbara_thought_03"):
        bartender_thoughts "Is he here to do a story on the bar?[wait_1] Or – shit, was that drunk guy last night legitimate?[wait_1] Did he really want to write up a review?"
    elif (current_thought == "barbara_thought_04"):
        barbara_thoughts "Does he consider being a reviewer and a reporter different jobs?[wait_1] Or...[wait_05]is he here for some other reason?"
    elif (current_thought == "barbara_thought_05"):
        barbara_thoughts "Did he just dodge the question?[wait_1] What’s he here for?"
    elif (current_thought == "barbara_thought_06"):
        barbara_thoughts "And I’d better wrap this up quickly, so that I can get back to it - that door won’t fix itself!"
        $ add_boolean("barbara_broken_door")
    elif (current_thought == "barbara_thought_07"):
        barbara_thoughts "If people can get in so quietly, though, maybe that’s a sign that I should start locking it."
    elif (current_thought == "barbara_thought_08"):
        barbara_thoughts "Sheesh, talk about nosy!"
    elif (current_thought == "barbara_thought_09"):
        barbara_thoughts "Oh, he probably thought that it was a bar fight, or something like that.[wait_1] He’s jumping to the wrong conclusion, but it’s kind of cute that he’s thinking of my safety!"
    elif (current_thought == "barbara_thought_10"):
        barbara_thoughts "Let’s see if I can get him back on topic...[wait_1]there’s something suspicious about this guy."
    elif (current_thought == "barbara_thought_11"):
        barbara_thoughts "Okay, he’s definitely a cop.[wait_1] Undercover, but not doing a very good job of it."
    elif (current_thought == "barbara_thought_12"):
        barbara_thoughts "He’s a newbie, I’m guessing?[wait_1] It’s probably his first day on the job."
    elif (current_thought == "barbara_thought_13"):
        barbara_thoughts "Of course I know the other shop owners –[wait_05] my family’s been a part of the community for decades!"
        $ add_boolean("barbara_family_community")
    elif (current_thought == "barbara_thought_14"):
        barbara_thoughts "I guess I can try and help him...[wait_05]but I probably won’t actually be able to ask around for a day or two.[wait_1] There’s just too much I have to work on here."
    elif (current_thought == "barbara_thought_15"):
        barbara_thoughts "They probably wouldn’t normally say too much, but to a guy this good-looking?[wait_1] They’d probably make an exception."
    elif (current_thought == "barbara_thought_16"):
        barbara_thoughts "They –[wait_05] I hope that it’s more than that...[wait_05]that they respect me for who I am, and how I’ve been running things.[wait_1] That it’s not just my family name."
    elif (current_thought == "barbara_thought_17"):
        barbara_thoughts "This could be a good test, actually, to see how much the other shop owners respect me."
        barbara_thoughts "Do they appreciate what I’ve been trying to do, or have they just been polite to me so far because of my family?"
    elif (current_thought == "barbara_thought_18"):
        barbara_thoughts "Before I get too far into this, I should try and work out what this guy’s deal is, anyway."
    elif (current_thought == "barbara_thought_19"):
        barbara_thoughts "So...[wait_05]he wants my information, and my connections, but he doesn’t trust me enough to tell me what’s up.[wait_1] Brilliant."
    elif (current_thought == "barbara_thought_20"):
        barbara_thoughts "I guess that I’ll still help him out, though...[wait_1]I would like to get to know him a bit better."
    elif (current_thought == "barbara_thought_21"):
        barbara_thoughts "Running a bar involves a lot more than just pouring drinks, buddy!"
    elif (current_thought == "barbara_thought_22"):
        barbara_thoughts "He seems pretty nice...[wait_05]but I’m a little wary of his interest in this mysterious man.[wait_1] I hope he’s on the up-and-up."

    # A-1-4
    elif (current_thought == "barbara_thought_23"):
        barbara_thoughts "Oh, the hottie is back!"
    elif (current_thought == "barbara_thought_24"):
        barbara_thoughts "Crap, how could I forget his name already?[wait_1] Wait...[wait_05]no, I think that’s it!"
    elif (current_thought == "barbara_thought_25"):
        barbara_thoughts "Phew!"
    elif (current_thought == "barbara_thought_26"):
        barbara_thoughts "I’ve got to get rid of this damn stock![wait_1] He’d like a beer, right?"
    elif (current_thought == "barbara_thought_27"):
        barbara_thoughts "Ah, of course...[wait_05]I should have seen that coming." 
    elif (current_thought == "barbara_thought_28"):
        barbara_thoughts "I’m kind of relieved that none of them knew anything –[wait_05] his interest in this guy is still a little suspicious."
    elif (current_thought == "barbara_thought_29"):
        barbara_thoughts "Hopefully he gets the hint that I’m not his PA."
    elif (current_thought == "barbara_thought_30"):
        barbara_thoughts "He’s still happy to spend a bit of money and chat, right?"
    elif (current_thought == "barbara_thought_31"):
        barbara_thoughts "Damn...[wait_05]I was hoping that we could have a bit more of a casual conversation."
        barbara_thoughts "And maybe I could find out a bit more about what his connection with this guy is..."
    elif (current_thought == "barbara_thought_32"):
        barbara_thoughts "That has to be, what, the fourth in the last hour?" 
        barbara_thoughts "He’s been holding them well enough, but why is he drinking so much?"
    elif (current_thought == "barbara_thought_33"):
        barbara_thoughts "He’s been holding his drinks fine before now.[wait_1] Why is he pretending to be drunk?"
    elif (current_thought == "barbara_thought_34"):
        bartender_thoughts "That has to be, what, the fourth in the last hour?" 
        bartender_thoughts "He’s been holding them well enough, but why is he drinking so much?"
    elif (current_thought == "barbara_thought_35"):
        bartender_thoughts "He’s been holding his drinks fine before now.[wait_1] Why is he pretending to be drunk?"
    elif (current_thought == "barbara_thought_36"):
        barbara_thoughts "Wait...[wait_05]is he actually drunk?[wait_1] Was he just faking his sobriety really well before?"
    elif (current_thought == "barbara_thought_37"):
        barbara_thoughts "He’s changed completely.[wait_1] This is weird."
    elif (current_thought == "barbara_thought_38"):
        bartender_thoughts "Wait...[wait_05]is he actually drunk?[wait_1] Was he just faking his sobriety really well before?"
    elif (current_thought == "barbara_thought_39"):
        bartender_thoughts "He’s changed completely.[wait_1] This is weird."

    # A-2
    elif (current_thought == "barbara_thought_40"):
        if (person_visited("barbara", "a", 0)):
            barbara_thoughts "Is he hung over?[wait_1] I’m still not sure whether he was pretending to be drunk or not last night."
        else:
            bartender_thoughts "Is he hung over?[wait_1] I’m still not sure whether he was pretending to be drunk or not last night."
    elif (current_thought == "barbara_thought_41"):
        barbara_thoughts "I feel like I’m going to regret this."
    elif (current_thought == "barbara_thought_42"):
        bartender_thoughts "I feel like I’m going to regret this."
    elif (current_thought == "barbara_thought_43"):
        barbara_thoughts "Busy enough that I’ll kick you out if this isn’t worth my time."
    elif (current_thought == "barbara_thought_44"):
        barbara_thoughts "So he wasn’t faking his drunkenness?"
    elif (current_thought == "barbara_thought_45"):
        barbara_thoughts "I wouldn’t mind it so much if he was drunk in certain circumstances.[wait_1] Like, say, during a private evening?"
    elif (current_thought == "barbara_thought_46"):
        barbara_thoughts "Not that I can do much beyond banning him from the bar."
    elif (current_thought == "barbara_thought_47"):
        barbara_thoughts "What could I help him with?[wait_1] Does he want my number?"
    elif (current_thought == "barbara_thought_48"):
        barbara_thoughts "That doesn’t sound like he wants my number...[wait_05]damn."
    elif (current_thought == "barbara_thought_49"):
        barbara_thoughts "Weird question to ask.[wait_1] Why wouldn’t you know this?"
    elif (current_thought == "barbara_thought_50"):
        barbara_thoughts "I guess he seemed kind of smug, but I assume that was the alcohol in his system."
    elif (current_thought == "barbara_thought_51"):
        barbara_thoughts "Some of the things he said were –[wait_05] he probably doesn’t want to know how he was acting.[wait_1] I’ll downplay it a bit."
    elif (current_thought == "barbara_thought_52"):
        barbara_thoughts "It sounds like he’s trying to trace his steps for the night.[wait_1] Was he out somewhere before he came here, and was directed here?"
    elif (current_thought == "barbara_thought_53"):
        barbara_thoughts "Why do I have to keep telling people not to do that?!"
    elif (current_thought == "barbara_thought_54"):
        barbara_thoughts "Okay, he’s a keeper."
    elif (current_thought == "barbara_thought_55"):
        barbara_thoughts "He’s just staring off into the distance...[wait_05]I think that he’s forgotten I’m here."
    elif (current_thought == "barbara_thought_56"):
        barbara_thoughts "I have to seize this opportunity while I can![wait_1] It might never come again!"
    
    # A-3
    elif (current_thought == "barbara_thought_57"):
        barbara_thoughts "Is there anything more to it than that? It feels pretty simple."
    elif (current_thought == "barbara_thought_58"):
        barbara_thoughts "If he wasn’t so cute, I wouldn’t let him get away with this.[wait_1] But he is, so I will!"
    elif (current_thought == "barbara_thought_59"):
        barbara_thoughts "Hey, it’s Lloyd![wait_1] I can’t afford to entertain him for too long today; I can’t take a break for too long."
    elif (current_thought == "barbara_thought_60"):
        barbara_thoughts "You’re interrupting that budgeting that I’ve been putting off, right when I’ve finally made time for it.[wait_1] But people who don’t own businesses never really get it."
    elif (current_thought == "barbara_thought_61"):
        barbara_thoughts "What am I, a private investigator?"
    elif (current_thought == "barbara_thought_62"):
        barbara_thoughts "Not much activity on Mondays.[wait_1] This might be my excuse to kick him out and get back to work."
    elif (current_thought == "barbara_thought_63"):
        barbara_thoughts "It’s that asshat who tried to score free drinks. Is Lloyd friends with him?"
    elif (current_thought == "barbara_thought_64"):
        barbara_thoughts "I’ll tell you the truth –[wait_05] but I notice you haven’t told me why you want to find out about him."
    elif (current_thought == "barbara_thought_65"):
        barbara_thoughts "I’m not going to downplay what this guy was doing.[wait_1] He deserves whatever he gets."
    elif (current_thought == "barbara_thought_66"):
        barbara_thoughts "If only he had been legitimate...[wait_05]I really need my profits to be higher."
        $ add_boolean("barbara_offer_bribe")
    elif (current_thought == "barbara_thought_67"):
        barbara_thoughts "Why is he asking me for that?[wait_1] ...[wait_05]This is still about the jerk with the white streak, right?"
    elif (current_thought == "barbara_thought_68"):
        barbara_thoughts "Why is he so desperate to see this footage?[wait_1] It’s kind of suspicious...[wait_05]but I shouldn’t look a gift horse in the mouth."
    elif (current_thought == "barbara_thought_69"):
        barbara_thoughts "Weird that he’s suddenly so noncommittal about the whole thing.[wait_1] How much does this actually matter to him?"
    elif (current_thought == "barbara_thought_70"):
        barbara_thoughts "And just like that, he turned into a dick, like so many other guys when I say no."
    elif (current_thought == "barbara_thought_71"):
        barbara_thoughts "It probably wouldn’t have hurt to show it to him.[wait_1] If he’d asked me in the right way I’d probably let him see it."
    elif (current_thought == "barbara_thought_72"):
        barbara_thoughts "I’d better change the topic, before he makes this weird."
    elif (current_thought == "barbara_thought_73"):
        barbara_thoughts "I still don’t know what Lloyd’s interest in this guy is."
    elif (current_thought == "barbara_thought_74"):
        barbara_thoughts "Thank god.[wait_1] I can finally get back to work."
    
    # A-4
    elif (current_thought == "barbara_thought_75"):
        barbara_thoughts "Alright, Barbara, stay calm.[wait_1] No need to overthink this."
    elif (current_thought == "barbara_thought_76"):
        barbara_thoughts "He seems pretty happy to see me.[wait_1] So far, so good."
    elif (current_thought == "barbara_thought_77"):
        barbara_thoughts "That’s fine.[wait_1] I’ll let him ask his questions, and once we’re done, I’ll ask mine."
    elif (current_thought == "barbara_thought_78"):
        bartender_thoughts "Damn, who’s this hottie?[wait_1] I’m happy to let him in if it means we can chat for a bit."
    elif (current_thought == "barbara_thought_79"):
        barbara_thoughts "Oh.[wait_1] The guy who was pretending to be drunk."
    elif (current_thought == "barbara_thought_80"):
        barbara_thoughts "He’s come into the bar while we’re closed just to apologise?[wait_1] I don’t buy it."
    elif (current_thought == "barbara_thought_81"):
        barbara_thoughts "So he does have a motive for being here beyond the apology.[wait_1] I’ll wait this out for now and see where he’s going with it."
    elif (current_thought == "barbara_thought_82"):
        barbara_thoughts "I’ll ease up on him a bit, make him feel a bit more relaxed, and see how things turn out."
    elif (current_thought == "barbara_thought_83"):
        barbara_thoughts "The guy who visited the bar on Monday.[wait_1] I still don’t know what Lloyd wants with him."
    elif (current_thought == "barbara_thought_84"):
        barbara_thoughts "The footage contains an absolute bombshell.[wait_1] He really should have come by."
    elif (current_thought == "barbara_thought_85"):
        barbara_thoughts "The footage contains an absolute bombshell.[wait_1] I need to tell him what I found in it."
    elif (current_thought == "barbara_thought_86"):
        barbara_thoughts "I look like a private investigator?"
    elif (current_thought == "barbara_thought_87"):
        barbara_thoughts "I asked for a picture.[wait_1] Not a description.[wait_1] Did he even hear what I said?"
    elif (current_thought == "barbara_thought_88"):
        barbara_thoughts "But what does Lloyd want with him?"
    elif (current_thought == "barbara_thought_89"):
        barbara_thoughts "I’ve got an absolute bombshell regarding this Jack guy.[wait_1] I need to tell Lloyd what I found."
    elif (current_thought == "barbara_thought_90"):
        barbara_thoughts "Did Lloyd already know this?[wait_1] Is he trying to get money of his own back from Jack?"
    elif (current_thought == "barbara_thought_91"):
        barbara_thoughts "How often has he pulled this scam here?[wait_1] The evidence has been there for months, and I never realised!"
    elif (current_thought == "barbara_thought_92"):
        barbara_thoughts "What?![wait_1] I...[wait_05]I wasn’t serious.[wait_01] I didn’t really mean it."
    elif (current_thought == "barbara_thought_93"):
        barbara_thoughts "Have there been any other deaths around here that I’m unaware of?[wait_1] Is the rest of the community safe?"
    elif (current_thought == "barbara_thought_94"):
        barbara_thoughts "What else can I say?[wait_1] What are you supposed to say, or do, when someone dies?"
    elif (current_thought == "barbara_thought_95"):
        barbara_thoughts "I...[wait_05]is this the sort of thing I should be asking?"
    elif (current_thought == "barbara_thought_96"):
        barbara_thoughts "What am I saying?[wait_1] I –[wait_05] I can’t stop now though...[wait_05]Lloyd will think I’m a jerk if I back out."
    elif (current_thought == "barbara_thought_97"):
        barbara_thoughts "No...[wait_05]no, I can’t go.[wait_1] I can’t leave the bar.[wait_1] It’s more important to me than some jerk who scammed me out of some money."
    elif (current_thought == "barbara_thought_98"):
        barbara_thoughts "Thank god.[wait_1] He’s not judging me for the decision."
    elif (current_thought == "barbara_thought_99"):
        barbara_thoughts "I don’t have to go.[wait_1] He gets it.[wait_1] He really gets it!"
    elif (current_thought == "barbara_thought_100"):
        barbara_thoughts "If I tell him to go instead of me, maybe he’ll think I’m more interested in going than I am?[wait_1] So I’ll look less selfish?"
    elif (current_thought == "barbara_thought_101"):
        barbara_thoughts "He bought it![wait_1] This is working out pretty well, honestly."
    elif (current_thought == "barbara_thought_102"):
        barbara_thoughts "I was going to ask him...[wait_05]no, now’s not the time.[wait_1] Talking about Jack’s death and the funeral kind of put a dampener on things."
    
    # B-3-4
    elif (current_thought == "barbara_thought_103"):
        barbara_thoughts "Lloyd’s shown up, just as he said he would.[wait_1] What will he make of what I found out?"
    elif (current_thought == "barbara_thought_104"):
        barbara_thoughts "What am I doing wrong?[wait_1] Why aren’t people ordering as much as they used to?"
    elif (current_thought == "barbara_thought_105"):
        barbara_thoughts "It’s not a sign that business is picking up, Lloyd..."
    elif (current_thought == "barbara_thought_106"):
        barbara_thoughts "How long can things sustain themselves like this?[wait_1] And how do I attract a larger crowd?"
    elif (current_thought == "barbara_thought_107"):
        barbara_thoughts "C’mon, Lloyd.[wait_1] Surprise me."
    elif (current_thought == "barbara_thought_108"):
        barbara_thoughts "What’s he going to think about the footage?[wait_1] It’s so weird."
    elif (current_thought == "barbara_thought_109"):
        barbara_thoughts "I did wonder whether maybe –[wait_05] no, that wouldn’t be it."
    elif (current_thought == "barbara_thought_110"):
        barbara_thoughts "I’ll share what I have with him, but why does Lloyd want to know?[wait_1] Is he asking for my benefit, or his own?"
    elif (current_thought == "barbara_thought_111"):
        barbara_thoughts "No shit, Lloyd.[wait_1] I already told you that."
    elif (current_thought == "barbara_thought_112"):
        barbara_thoughts "He goes quiet for so long sometimes, it’s like he’s forgotten that I’m here.[wait_1] But he looks so handsome when he’s brooding."
    elif (current_thought == "barbara_thought_113"):
        barbara_thoughts "That’s enough staring.[wait_1] I should remind him that I’m still here."
    elif (current_thought == "barbara_thought_114"):
        barbara_thoughts "No, he’s...[wait_05]he’s forgotten about me again."
    elif (current_thought == "barbara_thought_115"):
        barbara_thoughts "I haven’t considered it before.[wait_1] But it would explain some things..."
    elif (current_thought == "barbara_thought_116"):
        barbara_thoughts "He knows something about how this happened.[wait_1] Is he going to tell me?"
    elif (current_thought == "barbara_thought_117"):
        barbara_thoughts "Is there anything that he can actually do?[wait_1] Or does he just want an excuse to see my security footage?"
    elif (current_thought == "barbara_thought_118"):
        barbara_thoughts "Whatever this is, I just don’t feel comfortable about it.[wait_1] I want to stay as far away from it as possible."
    elif (current_thought == "barbara_thought_119"):
        barbara_thoughts "He’s going to prosecute the guy with the white streak?[wait_1] Then I –[wait_05] oh, Lloyd, I misjudged you![wait_1] I’m so sorry!"
    elif (current_thought == "barbara_thought_120"):
        barbara_thoughts "This is –[wait_05] everything’s going to be fine![wait_1] The bar is going to recover![wait_1] Everything will work out, and it’s all thanks to Lloyd!"
    elif (current_thought == "barbara_thought_121"):
        barbara_thoughts "How does Lloyd even know about this weird scam?[wait_1] It’s almost too good to be –[wait_05] no, Barbara, stop thinking like that.[wait_1] Don’t look a gift horse in the mouth."
    elif (current_thought == "barbara_thought_122"):
        barbara_thoughts "I have to start moving those pilsners.[wait_1] Nobody who’s tried them likes them."
    elif (current_thought == "barbara_thought_123"):
        barbara_thoughts "Don’t let him see how you’re really feeling, Barbara.[wait_1] Just smile and wave."
    
    # B-4
    elif (current_thought == "barbara_thought_124"):
        barbara_thoughts "He’s not going to be happy when he hears what I have for him.[wait_1] I’ll stay peppy and friendly to lighten the mood."
    elif (current_thought == "barbara_thought_125"):
        barbara_thoughts "Did he even care about the group?[wait_1] Or did he just want my footage?"
    elif (current_thought == "barbara_thought_126"):
        barbara_thoughts "He’ll probably ask why I don’t store more footage.[wait_1] If I could afford the space, buddy, I’d have it!"
    elif (current_thought == "barbara_thought_127"):
        barbara_thoughts "I don’t think he’s disappointed because I’m the one missing out on compensation."
    elif (current_thought == "barbara_thought_128"):
        barbara_thoughts "I might as well just ask him outright and see if my hunch is right."
    elif (current_thought == "barbara_thought_129"):
        barbara_thoughts "Yep.[wait_1] He’s just like all the other guys."
    elif (current_thought == "barbara_thought_130"):
        barbara_thoughts "Should I lie to him?[wait_1] ...[wait_05]Nah, he was honest with me."
    elif (current_thought == "barbara_thought_131"):
        barbara_thoughts "I was wondering whether he’s an associate of the white-streak guy...[wait_05]something about Lloyd does remind me of him."
    elif (current_thought == "barbara_thought_132"):
        barbara_thoughts "Do I ask if he has any experience bartending?[wait_1] No, Barbara![wait_1] You need to cut shifts as it is!"
    elif (current_thought == "barbara_thought_133"):
        barbara_thoughts "Any artist using AI in their workflow is a fucking disgrace to the community."
    elif (current_thought == "barbara_thought_134"):
        barbara_thoughts "I wonder how his photos compare to the guy that took the publicity photos for this place?"
    elif (current_thought == "barbara_thought_135"):
        barbara_thoughts "Do I tell him why my name is Barbara?[wait_1] No, that’s too much information.[wait_1] He doesn’t know enough family in-jokes."
    elif (current_thought == "barbara_thought_136"):
        barbara_thoughts "Got to get to the point![wait_1] He’s looking bored!"
    elif (current_thought == "barbara_thought_137"):
        barbara_thoughts "I guess I just don’t know as much as I think I do.[wait_1] It’s easy to think that you’re exceptional, that you’ll make waves...[wait_05]but I’m really just not as good at this as I thought I was."
    elif (current_thought == "barbara_thought_138"):
        barbara_thoughts "I’ve probably bored him.[wait_1] He doesn’t care."
    elif (current_thought == "barbara_thought_139"):
        barbara_thoughts "Why’d you have to get my hopes up, Lloyd?[wait_1] Why’d you have to make me think that I wasn’t to blame?"
    elif (current_thought == "barbara_thought_140"):
        barbara_thoughts "Is he just saying this to make me feel better?[wait_1] Or...[wait_05]does he really mean it?"
    elif (current_thought == "barbara_thought_141"):
        barbara_thoughts "It’s easy for him to tell me that.[wait_1] But what should I actually do?"
    elif (current_thought == "barbara_thought_142"):
        barbara_thoughts "He’s not that bad a guy.[wait_1] He might have let me down...[wait_05]but I’d still like to get to know him better."
    elif (current_thought == "barbara_thought_143"):
        barbara_thoughts "Please don’t be something weird...[wait_05]please don’t be something weird..."
    elif (current_thought == "barbara_thought_144"):
        barbara_thoughts "Psychic powers?[wait_1] Urgh, creepy![wait_1] I’d hate for someone to be reading my thoughts!"
    elif (current_thought == "barbara_thought_145"):
        barbara_thoughts "If this is just a really shitty lie, I’ll probably find out soon enough."
    elif (current_thought == "barbara_thought_146"):
        barbara_thoughts "I’ve made up my mind.[wait_1] I want to help Lloyd!" 
        barbara_thoughts "{size=-8}Plus it’s a good excuse to spend time with him.{/size}"
    elif (current_thought == "barbara_thought_147"):
        barbara_thoughts "I knew it![wait_1] That other photographer did do a shitty job!"
    

    $ ignore_thoughts_length()
    return