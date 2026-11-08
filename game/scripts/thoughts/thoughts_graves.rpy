label mind_read_graves:
    # A-1
    if (current_thought == "graves_thought_01"):
        detective_thoughts "Thank goodness he did come up...[wait_05]I’ve been itching to start a new case ever since the previous one finished."
        $ add_boolean("graves_no_cases")
    elif (current_thought == "graves_thought_02"):
        detective_thoughts "He’s not too bad-looking...[wait_05]he seems to be in fairly good shape, if nothing else."
    elif (current_thought == "graves_thought_03"):
        detective_thoughts "He’s probably expecting a grizzled, hard-boiled detective – I’ll try to meet his expectations."
    elif (current_thought == "graves_thought_04"):
        graves_thoughts "One is more than most people have to."
    elif (current_thought == "graves_thought_05"):
        graves_thoughts "He’s very quiet – better try and get him a bit more relaxed! I don’t want him thinking that I’m {i}too{/i} grizzled!"
    elif (current_thought == "graves_thought_06"):
        graves_thoughts "C’mon, mate, at least try and stick with it!"
    elif (current_thought == "graves_thought_07"):
        graves_thoughts "Hopefully this is interesting.[wait_1] Let’s see what he’s got for me."
    elif (current_thought == "graves_thought_08"):
        graves_thoughts "What’s his relationship with this person, I wonder?[wait_1] A distant relative?[wait_1] An old lover?"
    elif (current_thought == "graves_thought_09"):
        graves_thoughts "Better sort this out quickly – I don’t want to wind up helping with something illegal."
    elif (current_thought == "graves_thought_10"):
        graves_thoughts "Very evasive...[wait_05]let’s see where exactly he’s going with this."
    elif (current_thought == "graves_thought_11"):
        graves_thoughts "If he gives me more information then I’ll be able to actually answer that..."
    elif (current_thought == "graves_thought_12"):
        graves_thoughts "He’s got to have a name, right?"
    elif (current_thought == "graves_thought_13"):
        graves_thoughts "Okay, that’s very interesting.[wait_1] If I knew this person’s name, and looked them up, I wonder what I’d find?"
    elif (current_thought == "graves_thought_14"):
        graves_thoughts "I might be able to do a reverse image search...[wait_1]I’m really damn curious about who this person is, now."
    elif (current_thought == "graves_thought_15"):
        graves_thoughts "At least when Usbourne hired us, he gave us a name."
    elif (current_thought == "graves_thought_16"):
        graves_thoughts "I guess this does make sense...[wait_05]but I’m still not sure why he wants me to find this guy."
    elif (current_thought == "graves_thought_17"):
        graves_thoughts "I’ll probably need a few days, so I’ll start by tempering his expectations a bit."
    elif (current_thought == "graves_thought_18"):
        graves_thoughts "What {i}is{/i} this guy’s relationship?[wait_1] Is he a spy trying to catch a terrorist?[wait_1] A gangster trying to find someone who squealed?"
    elif (current_thought == "graves_thought_19"):
        graves_thoughts "He’ll just have to wait for a bit.[wait_1] He’ll have to be patient, like everybody else."
    elif (current_thought == "graves_thought_20"):
        graves_thoughts "Shit, what does he –[wait_05] how does he know that?![wait_1] What did I say to him earlier?"
    elif (current_thought == "graves_thought_21"):
        graves_thoughts "I should just bluff and tell him he’s wrong, but –[wait_05] no, he’d be able to tell that it’s a lie.[wait_1] I reacted too strongly."
    elif (current_thought == "graves_thought_22"):
        graves_thoughts "Nothing to do now but tell the truth...[wait_05]well, most of it, at least."
    elif (current_thought == "graves_thought_23"):
        graves_thoughts "At least this doesn’t change any of my current plans."
    elif (current_thought == "graves_thought_24"):
        graves_thoughts "Not that I’m expecting them to be much, but if I can show him that I’ve started, that’ll hopefully give him some confidence in me."
    
    # A-1-4
    elif (current_thought == "graves_thought_25"):
        graves_thoughts "Argh, another person who doesn’t understand the benefits of green tea!"
    elif (current_thought == "graves_thought_26"):
        graves_thoughts "He’s not expecting things to be too far along, surely?"
    elif (current_thought == "graves_thought_27"):
        graves_thoughts "...Apparently he is."
    elif (current_thought == "graves_thought_28"):
        graves_thoughts "You set the expectation for the clients, and then they go and ignore it anyway."
    elif (current_thought == "graves_thought_29"):
        graves_thoughts "Is he willing to give me some more information now that he can see how it’s hampering the case?"
    elif (current_thought == "graves_thought_30"):
        graves_thoughts "I’m not angry, I’m just disappointed."
    elif (current_thought == "graves_thought_31"):
        graves_thoughts "Does he see how hypocritical he’s being?[wait_1] How selfish?"
    elif (current_thought == "graves_thought_32"):
        graves_thoughts "Thank god.[wait_1] I can finally finish up here and head back home."
    elif (current_thought == "graves_thought_33"):
        graves_thoughts "I get that he’s frustrated that I haven’t made solid progress, but I hope that he’s a bit more reasonable tomorrow."
    
    # A-2
    elif (current_thought == "graves_thought_34"):
        detective_thoughts "Gotta be careful with the image.[wait_1] Not too rough, but not as young as I am."
    elif (current_thought == "graves_thought_35"):
        detective_thoughts "He hasn’t laughed![wait_1] We’re off to a good start!"
    elif (current_thought == "graves_thought_36"):
        graves_thoughts "Nope, too serious.[wait_1] He thinks I’m weird."
    elif (current_thought == "graves_thought_37"):
        graves_thoughts "I wonder whether this’ll match up with what we find out during the background check?"
    elif (current_thought == "graves_thought_38"):
        graves_thoughts "How much are you going to lie to me, Lloyd?"
    elif (current_thought == "graves_thought_39"):
        graves_thoughts "Nice to see Lloyd again.[wait_1] His background check was pretty clean."
    elif (current_thought == "graves_thought_40"):
        graves_thoughts "I doubt that Docherty is who Lloyd is looking for, given everything he said about his mystery person."
    elif (current_thought == "graves_thought_41"):
        graves_thoughts "Shit, what do I do in terms of paperwork?[wait_1] Bill additional hours, or open up a separate case?"
    elif (current_thought == "graves_thought_42"):
        graves_thoughts "Odd request.[wait_1] Is he trying to keep me busy or distract me from something?"
    elif (current_thought == "graves_thought_43"):
        graves_thoughts "Most people wouldn’t go to a detective for this sort of thing.[wait_1] Why has he come to me?"
    elif (current_thought == "graves_thought_44"):
        graves_thoughts "This almost sounds like possession.[wait_1] But only temporary?"
    elif (current_thought == "graves_thought_45"):
        graves_thoughts "Icarus is famous for hubris.[wait_1] Why would you give something that name?"
    elif (current_thought == "graves_thought_46"):
        graves_thoughts "I’d like a bit more information.[wait_1] What is he hoping to get from me?"
    elif (current_thought == "graves_thought_47"):
        graves_thoughts "If he hasn’t gone there yet it’s a bit suspicious.[wait_1] Why wouldn’t you make it your first destination?"
    elif (current_thought == "graves_thought_48"):
        graves_thoughts "Why would I even want to help somebody with an attitude like this?[wait_1] ...Because he’s asking you to, of course."
    elif (current_thought == "graves_thought_49"):
        graves_thoughts "I think that he’s lying to me.[wait_1] I think he remembers why he went there, but doesn’t want to tell me."
    elif (current_thought == "graves_thought_50"):
        graves_thoughts "What sort of answer is he hoping I’ll give him?[wait_1] He wants me to tell him something specific, but I don’t know what, or why."
    elif (current_thought == "graves_thought_51"):
        graves_thoughts "This must be what he’s been building to.[wait_1] Is there something else at the bar that he wants me to find?"
    elif (current_thought == "graves_thought_52"):
        graves_thought "I feel like this is going to be a waste of my time.[wait_1] But as long as he pays me it should be fine.[wait_1] It’s not like I’ll be in danger if I investigate the bar."
    elif (current_thought == "graves_thought_53"):
        graves_thought "If I’d known that this was what he wanted from me I would have pretended to be out.[wait_1] I’d rather do work on some of our other cases."
    
    # A-3
    elif (current_thought == "graves_thought_54"):
        graves_thought "Do I look casual enough?"
    elif (current_thought == "graves_thought_55"):
        graves_thought "He’s probably going to be disappointed.[wait_1] I haven’t discovered anything."
    elif (current_thought == "graves_thought_56"):
        graves_thought "Another job?[wait_1] He can’t be that interested in the previous one then."
    elif (current_thought == "graves_thought_57"):
        graves_thought "I still haven’t found out why it’s called that."
    elif (current_thought == "graves_thought_58"):
        graves_thought "He probably doesn’t need to know that the bar’s original owner borrowed money from the mob for the initial payment, right?"
    elif (current_thought == "graves_thought_59"):
        graves_thought "Since discovering what happened to Docherty I haven’t learned anything else promising.[wait_1] Is it possible that Docherty {i}is{/i} the person he wanted me to find?"
    elif (current_thought == "graves_thought_60"):
        graves_thought "I hope that he gives me more information for this new job than the old one.[wait_1] Lloyd’s a bit of an expert at being vague."
    elif (current_thought == "graves_thought_61"):
        detective_thoughts "He probably thinks that I look pretty cool.[wait_1] This should make for a good first impression."
    elif (current_thought == "graves_thought_62"):
        detective_thoughts "Too edgy?[wait_1] Or just edgy enough?"
    elif (current_thought == "graves_thought_63"):
        graves_thoughts "Got to keep up the tough guy look.[wait_1] I need him to treat me seriously."
    elif (current_thought == "graves_thought_64"):
        graves_thoughts "...Shit.[wait_1] Too much tough guy, not enough genuine guy."
    elif (current_thought == "graves_thought_65"):
        graves_thoughts "Thank god![wait_1] Now –[wait_05] just don’t screw it up again!"
    elif (current_thought == "graves_thought_66"):
        graves_thoughts "Not too unusual a request.[wait_1] But I’d love to know what Lloyd wants with this guy."
    elif (current_thought == "graves_thought_67"):
        graves_thoughts "Is this somebody that he’s stalking?[wait_1] Not having any of this information feels suspicious..."
    elif (current_thought == "graves_thought_68"):
        graves_thoughts "Sounds kind of like he’s describing Usbourne.[wait_1] Could that be the person he’s looking for?"
        $ add_boolean("graves_recognises_jack")
    elif (current_thought == "graves_thought_69"):
        graves_thoughts "There could be plenty of people with a white streak of hair.[wait_1] He’s not necessarily looking for Usbourne."
        $ add_boolean("graves_recognises_jack")
    elif (current_thought == "graves_thought_70"):
        graves_thoughts "I don’t buy that he misspoke.[wait_1] He decided he didn’t want to keep this to himself."
    elif (current_thought == "graves_thought_71"):
        graves_thoughts "It {i}is{/i} Usbourne![wait_1] But why didn’t he initially want me to know?"   
    elif (current_thought == "graves_thought_72"):
        graves_thoughts "I can’t confirm that it’s Usbourne, but I’d bet money that it is."
        $ add_boolean("graves_recognises_jack")
    elif (current_thought == "graves_thought_73"):
        graves_thoughts "How much are you going to lie to me, Lloyd?"
    elif (current_thought == "graves_thought_74"):
        graves_thoughts "I don’t believe him one bit. He’s lying."
    elif (current_thought == "graves_thought_75"):
        graves_thoughts "I’ll pretend to buy his lie for now."
    elif (current_thought == "graves_thought_76"):
        graves_thoughts "I almost hope that he doesn’t visit me later.[wait_1] I’ve got to think about this pretty carefully."
    
    # A-3-4
    elif (current_thought == "graves_thought_77"):
        graves_thoughts "Of course I have.[wait_1] But can I trust Lloyd with it?"
    elif (current_thought == "graves_thought_78"):
        graves_thoughts "Lloyd’s still being kind of suspicious.[wait_1] I don’t know what his endgame is."
    elif (current_thought == "graves_thought_79"):
        graves_thoughts "If he lies again, I’ll have to enact the backup plan."
    elif (current_thought == "graves_thought_80"):
        graves_thoughts "Is he lying again?[wait_1] I don’t think he is."
    elif (current_thought == "graves_thought_81"):
        graves_thoughts "Damn...[wait_05]now he’ll never pay off that last invoice we charged him."
    elif (current_thought == "graves_thought_82"):
        graves_thoughts "I won’t tell him everything that I know.[wait_1] I still don’t know whether he’s being genuine.[wait_1] For now I’ll just keep it to the safe stuff."
    elif (current_thought == "graves_thought_83"):
        graves_thoughts "We probably shouldn’t have given him such a steep discount for it, but I’m a bit of a sucker for helping with this sort of thing."
    elif (current_thought == "graves_thought_84"):
        graves_thoughts "Is this relevant to know?[wait_1] I’ll just tell him enough to satisfy his curiosity."
    elif (current_thought == "graves_thought_85"):
        graves_thoughts "Is he looking for something in particular?[wait_1] Did I miss something important?"
    elif (current_thought == "graves_thought_86"):
        graves_thoughts "He’s determined to find something.[wait_1] We must have missed something."
    elif (current_thought == "graves_thought_87"):
        graves_thoughts "He never did anything as serious as murder.[wait_1] That’s more than I can say."
    elif (current_thought == "graves_thought_88"):
        graves_thoughts "He’s definitely looking for something in particular.[wait_1] If I find it, how will I know what it is?[wait_1] And whether or not to trust him with it?"
    elif (current_thought == "graves_thought_89"):
        graves_thoughts "Why does he see this as an issue?[wait_1] Did I just turn this into a dead end for him?"
    elif (current_thought == "graves_thought_90"):
        graves_thoughts "He looks fairly concerned.[wait_1] What’s his next move going to be? Will he let me in on it, or doesn’t he trust me enough?"
    elif (current_thought == "graves_thought_91"):
        graves_thoughts "Better make sure he isn’t about to vomit.[wait_1] I’ve cleaned up enough of that this week."
    elif (current_thought == "graves_thought_92"):
        graves_thoughts "That’s what had him shaken?[wait_1] He’s more empathetic than I realised."
    elif (current_thought == "graves_thought_93"):
        graves_thoughts "We’re more than just reactive and thoughtless animals.[wait_1] I refuse to believe any different."
    elif (current_thought == "graves_thought_94"):
        graves_thoughts "There probably is a reason.[wait_1] More importantly, I’d like the time to work out what your stake in all of this is."
    elif (current_thought == "graves_thought_95"):
        graves_thoughts "Now to just get his statement on this, and to see how well it matches up with what I can discover."
    elif (current_thought == "graves_thought_96"):
        graves_thoughts "I don’t think that’s a lie.[wait_1] He seems fairly genuine."
    elif (current_thought == "graves_thought_97"):
        graves_thoughts "I think that I might have misjudged Lloyd a bit.[wait_1] He’s a bit secretive but does seem to be trying to help."
        graves_thoughts "I’ll still investigate him to be certain, of course."
    elif (current_thought == "graves_thought_98"):
        graves_thoughts "That will give me time to investigate both Jack and Lloyd."
    

    $ ignore_thoughts_length()
    return