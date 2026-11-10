label mind_read_cat:
    # A-1
    if (current_thought == "cat_thought_01"):
        librarian_thoughts "I’m working right now...[wait_05]this had better be quick..."
    elif (current_thought == "cat_thought_02"):
        librarian_thoughts "Why make this my problem...?[wait_1] Look around and you’ll probably find them."
    elif (current_thought == "cat_thought_03"):
        librarian_thoughts "He shouldn’t be able to see my screen from there...[wait_1]he shouldn’t be able to see their status..."
    elif (current_thought == "cat_thought_04"):
        librarian_thoughts "Why can’t he just accept that they’re not available...[wait_1]?"
    elif (current_thought == "cat_thought_05"):
        librarian_thoughts "There...[wait_1]that should get rid of him..."
    elif (current_thought == "cat_thought_06"):
        librarian_thoughts "Why is he so insistent...?[wait_1] What does he want the books for...?"
    elif (current_thought == "cat_thought_07"):
        librarian_thoughts "He’s really starting to annoy me...[wait_1]why won’t he believe what I’m telling him?"
    elif (current_thought == "cat_thought_08"):
        librarian_thoughts "I need him to disappear before he finds out that the books aren’t here.[wait_1] He’s becoming a problem."
        $ add_boolean("cat_books_missing")
    elif (current_thought == "cat_thought_09"):
        librarian_thoughts "I’ll need to threaten him...[wait_1]if he keeps pushing this then he might make a scene."
    elif (current_thought == "cat_thought_10"):
        librarian_thoughts "This should get him to leave...[wait_1]before he finds out the truth about the books."
    elif (current_thought == "cat_thought_11"):
        librarian_thoughts "Thank goodness...[wait_1]if I’d had to explain why I needed security, they might have found out about the books."
    elif (current_thought == "cat_thought_12"):
        librarian_thoughts "Just leave...[wait_1]turn away and go..."
    elif (current_thought == "cat_thought_13"):
        librarian_thoughts "What...?[wait_1] How does he know that?[wait_1] Or...[wait_1]is he bluffing?"
    elif (current_thought == "cat_thought_14"):
        librarian_thoughts "I’ll keep intimidating him...[wait_1]have him think that his bluff failed..."
    elif (current_thought == "cat_thought_15"):
        librarian_thoughts "How should I handle this...?[wait_1] If he talks to one of them, and they check the records..."
    elif (current_thought == "cat_thought_16"):
        librarian_thoughts "If he sees one or two of them...[wait_1]it might be enough to get him to stay quiet."
    elif (current_thought == "cat_thought_17"):
        librarian_thoughts "Hopefully he’s busy...[wait_1]that will give me more time to work out what to do..."
    elif (current_thought == "cat_thought_18"):
        librarian_thoughts "He’s not giving anything away...[wait_1]Damn![wait_1] I’d better show up to be safe."
    elif (current_thought == "cat_thought_19"):
        librarian_thoughts "Please go away...[wait_1]please go away..."

    # A-1-4
    elif (current_thought == "cat_thought_20"):
        cat_thoughts "He’s here...[wait_1]and I still don’t know how to get rid of him for good"
    elif (current_thought == "cat_thought_21"):
        cat_thoughts "This probably won’t work...[wait_1]but I should try it anyway."
    elif (current_thought == "cat_thought_22"):
        cat_thoughts "I’d rather not give him it...[wait_1]but if I don’t..."
    elif (current_thought == "cat_thought_23"):
        cat_thoughts "I chose the worst-written of the books...[wait_1]hopefully he’ll think they’re all like this and stop pressuring me..."
    elif (current_thought == "cat_thought_24"):
        cat_thoughts "He’s obviously speed-reading it...[wait_1]what is he looking for?"
    elif (current_thought == "cat_thought_25"):
        cat_thoughts "The sooner we’re done here...[wait_1]the better."
    elif (current_thought == "cat_thought_26"):
        cat_thoughts "He’s so insistent...[wait_1]how do I get rid of him...?"
    elif (current_thought == "cat_thought_27"):
        cat_thoughts "If I talk to them before he can...[wait_1]then he has nothing on me.[wait_1] I just need to come up with a good lie..."
    elif (current_thought == "cat_thought_28"):
        cat_thoughts "This should buy me some time...[wait_1]I can work out how to stop him by tomorrow..."
    
    # A-2
    elif (current_thought == "cat_thought_29"):
        if (check_boolean("cat_name_discovered")):
            cat_thoughts "It’s him...[wait_1]how can I stop him from asking about those books today?"
        else:
            librarian_thoughts "It’s him...[wait_1]how can I stop him from asking about those books today?"
    elif (current_thought == "cat_thought_30"):
        if (check_boolean("cat_name_discovered")):
            cat_thoughts "It’ll be okay...[wait_1]there’s no way for him to find out where they are..."
        else:
            librarian_thoughts "It’ll be okay...[wait_1]there’s no way for him to find out where they are..."
    elif (current_thought == "cat_thought_31"):
        if (check_boolean("cat_name_discovered")):
            cat_thoughts "So much nicer...[wait_1]as a name."
        else:
            librarian_thoughts "So much nicer...[wait_1]as a name."
    elif (current_thought == "cat_thought_32"):
        cat_thoughts "I can’t let him know...[wait_1]where they are.[wait_1] I’ll have to bluff."
    elif (current_thought == "cat_thought_33"):
        cat_thoughts "Why is he...[wait_1]making such a big deal about this?[wait_1] It’s not like anybody died..."
    elif (current_thought == "cat_thought_34"):
        cat_thoughts "Is he buying it?[wait_1] He’s gone quiet..."
    elif (current_thought == "cat_thought_35"):
        cat_thoughts "He’s lying...[wait_1]he must be..."
    elif (current_thought == "cat_thought_36"):
        cat_thoughts "What?[wait_1] I need more details about this."
    elif (current_thought == "cat_thought_37"):
        cat_thoughts "A shooting?[wait_1] I should check my files...[wait_1]see whether there are any reports about it..."
    elif (current_thought == "cat_thought_38"):
        cat_thoughts "Better get all the details...[wait_1]make it easier to find the information in the files..."
    elif (current_thought == "cat_thought_39"):
        cat_thoughts "“A hunch.”[wait_1] Could he be one of Sergei’s types?"
    elif (current_thought == "cat_thought_40"):
        cat_thoughts "I need more information...[wait_1]to narrow the files down..."
    elif (current_thought == "cat_thought_41"):
        cat_thoughts "He sounds like an amateur...[wait_1]I’d better give him some advice..."
    elif (current_thought == "cat_thought_42"):
        cat_thoughts "I could use more information...[wait_1]but this should be enough to narrow down the files..."
    elif (current_thought == "cat_thought_43"):
        cat_thoughts "This sounds like a fun project to work on!"
    elif (current_thought == "cat_thought_44"):
        cat_thoughts "He’ll probably forget to tell me something...[wait_1]but that’s part of the challenge..."
    elif (current_thought == "cat_thought_45"):
        cat_thoughts "He’s forgotten about the books...[wait_1]I hope he doesn’t ask about them again..."
    elif (current_thought == "cat_thought_46"):
        cat_thoughts "Where did that come from?[wait_1] This man suddenly became interesting!"
    elif (current_thought == "cat_thought_47"):
        cat_thoughts "He probably means retrograde amnesia...[wait_1]let’s see what he says..."
    elif (current_thought == "cat_thought_48"):
        cat_thoughts "If he remembers going to bed...[wait_1]I think I know what this is..."
    elif (current_thought == "cat_thought_49"):
        cat_thoughts "If it isn’t DID...[wait_1]then I have another theory..."
    elif (current_thought == "cat_thought_50"):
        cat_thoughts "Traumatic experiences like...[wait_1]being attacked by a shark?"
    elif (current_thought == "cat_thought_51"):
        cat_thoughts "I have to direct him away from the books..."
    elif (current_thought == "cat_thought_52"):
        cat_thoughts "It didn’t work...[wait_1]he’s going to regret not listening..."
    elif (current_thought == "cat_thought_53"):
        cat_thoughts "A hunch?[wait_1] Does this mean...?"
    elif (current_thought == "cat_thought_54"):
        cat_thoughts "Finally...[wait_1]it worked..."
    
    # A-3
    elif (current_thought == "cat_thought_55"):
        cat_thoughts "No...[wait_05]why has he returned?[wait_1] I can’t talk to him..."
    elif (current_thought == "cat_thought_56"):
        cat_thoughts "I’ll just stay silent...[wait_1]he’ll leave when he realises that I’m not talking..."
    elif (current_thought == "cat_thought_57"):
        cat_thoughts "Staying silent won’t work...[wait_1]I’ll try and remove him as fast as possible..."
    elif (current_thought == "cat_thought_58"):
        cat_thoughts "Shut up![wait_1] You don’t realise how dangerous this is, do you?"
    elif (current_thought == "cat_thought_59"):
        cat_thoughts "If I’m just his sounding board then he doesn’t actually need me.[wait_1] I need this conversation to end...[wait_1]now."
    elif (current_thought == "cat_thought_60"):
        cat_thoughts "He’s talked for too long already.[wait_1] I need to end this."
    elif (current_thought == "cat_thought_61"):
        cat_thoughts "Why don’t you get the hint?[wait_1] Why don’t you leave?"
    elif (current_thought == "cat_thought_62"):
        cat_thoughts "I’ll humour him.[wait_1] Maybe then he’ll leave."
    elif (current_thought == "cat_thought_63"):
        cat_thoughts "There.[wait_1] I listened to your description.[wait_1] Now go."
    elif (current_thought == "cat_thought_64"):
        cat_thoughts "I shouldn’t talk this much.[wait_1] But he isn’t giving up and I need him to."
    elif (current_thought == "cat_thought_65"):
        cat_thoughts "If you can take a hint then why are you still here?"
    elif (current_thought == "cat_thought_66"):
        cat_thoughts "Naïve idiot.[wait_1] Let’s see how you feel when the killer targets you."
    
    # A-4
    elif (current_thought == "cat_thought_67"):
        cat_thoughts "I thought that he got the hint yesterday.[wait_1] Why is he back?"
    elif (current_thought == "cat_thought_68"):
        cat_thoughts "...Maybe he won’t be here for as long today.[wait_1] If this is quick it might be okay."
    elif (current_thought == "cat_thought_69"):
        cat_thoughts "I don’t know.[wait_1] Now leave."
    elif (current_thought == "cat_thought_70"):
        cat_thoughts "It’s too risky...[wait_1]I need him to leave..."
    elif (current_thought == "cat_thought_71"):
        cat_thoughts "It’s not that simple, Lloyd.[wait_1] Why do you think that I’m scared?"
    elif (current_thought == "cat_thought_72"):
        cat_thoughts "Do I...[wait_1]tell him?"
    elif (current_thought == "cat_thought_73"):
        cat_thoughts "Shut up![wait_1] Shut up and listen!"
    elif (current_thought == "cat_thought_74"):
        cat_thoughts "Now...[wait_1]he knows.[wait_1] Please...[wait_1]please leave me, Lloyd."
    elif (current_thought == "cat_thought_75"):
        cat_thoughts "Don’t make me relive it...[wait_1]just leave, Lloyd..."
    elif (current_thought == "cat_thought_76"):
        cat_thoughts "He’s not listening to me...[wait_1]all that he cares about is his little investigation..."
    elif (current_thought == "cat_thought_77"):
        cat_thoughts "Thank god...[wait_1]he’s finally listening..."
    
    # B-4
    elif (current_thought == "cat_thought_78"):
        cat_thoughts "Is that Lloyd...?[wait_1] Don’t look at him..."
    elif (current_thought == "cat_thought_79"):
        cat_thoughts "Damn...[wait_1]I shouldn’t have done that..."
    elif (current_thought == "cat_thought_80"):
        cat_thoughts "I hope he leaves...[wait_1]it’s not safe..."
    elif (current_thought == "cat_thought_81"):
        cat_thoughts "If they’re not here...[wait_1]he should leave...[wait_1]before it’s too late..."
    elif (current_thought == "cat_thought_82"):
        cat_thoughts "If only I could help him...[wait_1]but I can’t risk it..."
    elif (current_thought == "cat_thought_83"):
        cat_thoughts "This should keep him away from the books...[wait_1]and away from me..."
    elif (current_thought == "cat_thought_84"):
        cat_thoughts "What else can I try...?[wait_1] He’s not listening..."
    elif (current_thought == "cat_thought_85"):
        cat_thoughts "Do I tell him...?[wait_1] Or is that too much...?[wait_1] Will somebody else die...?"
    elif (current_thought == "cat_thought_86"):
        cat_thoughts "Please just listen to me...[wait_1]you’re putting me in danger..."
    elif (current_thought == "cat_thought_87"):
        cat_thoughts "Sergei’s already died...[wait_1]who will he target next?"
    elif (current_thought == "cat_thought_88"):
        cat_thoughts "If only I hadn’t helped him the other day...[wait_1]then everything would be fine..."
    elif (current_thought == "cat_thought_89"):
        cat_thoughts "He’s finally leaving...[wait_1]thank god..."
    

    $ ignore_thoughts_length()
    return