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
    
    # C-2
    elif (current_thought == "cat_thought_90"):
        librarian_thoughts "It’s him...[wait_1]how can I get rid of him today?"
    elif (current_thought == "cat_thought_91"):
        cat_thoughts "I’ll play dumb...[wait_1]maybe he’ll get frustrated and leave..."
    elif (current_thought == "cat_thought_92"):
        cat_thoughts "Hehehe."
    elif (current_thought == "cat_thought_93"):
        cat_thoughts "I wish I could tell him...[wait_1]but I can’t trust him."
    elif (current_thought == "cat_thought_94"):
        librarian_thoughts "{i}Riddley Walker{/i}...[wait_1]this one is definitely going in the pile that’s getting burned."
    elif (current_thought == "cat_thought_95"):
        librarian_thoughts "This list...[wait_1]why is he looking into these books?[wait_1] Does he know what’s happened?"
    elif (current_thought == "cat_thought_96"):
        librarian_thoughts "...I didn’t ask."
    elif (current_thought == "cat_thought_97"):
        cat_thoughts "Well, it’s not like you’d be looking for somebody unimportant..."
    elif (current_thought == "cat_thought_98"):
        cat_thoughts "I doubt that he’s really looking for someone...[wait_1]but I’ll pretend to help him anyway..."
    elif (current_thought == "cat_thought_99"):
        cat_thoughts "Did I make a mistake...?[wait_1] Is he actually looking for someone?"
    elif (current_thought == "cat_thought_100"):
        cat_thoughts "I don’t know enough about Asian names to know if that’s a real name or not..."
    elif (current_thought == "cat_thought_101"):
        cat_thoughts "I’d better check...[wait_1]just in case I misspelled it and this person does exist..."
    elif (current_thought == "cat_thought_102"):
        cat_thoughts "What does Jīngshén Tángláng mean, then?"
    elif (current_thought == "cat_thought_103"):
        cat_thoughts "He’s probably still lying to me.[wait_1] I don’t know why he thinks that this will convince me to give him the books."
    elif (current_thought == "cat_thought_104"):
        cat_thoughts "He’s being intentionally vague.[wait_1] He must be trying to trick me."
    elif (current_thought == "cat_thought_105"):
        cat_thoughts "He isn’t asking about the books any more...[wait_1]maybe he’s forgotten about them..."
    elif (current_thought == "cat_thought_106"):
        cat_thoughts "That description...[wait_1]it sounds exactly like Sergei![wait_1] What’s his interest with him?"
        $ add_boolean("sergei_name_mentioned")
    elif (current_thought == "cat_thought_107"):
        cat_thoughts "No...[wait_1]I reacted too strongly![wait_1] Have to downplay it!"
    elif (current_thought == "cat_thought_108"):
        cat_thoughts "He even knows Sergei’s name.[wait_1] He {i}has{/i} been spying on us!"
    elif (current_thought == "cat_thought_109"):
        cat_thoughts "I need to get away from this guy and warn him!"
    elif (current_thought == "cat_thought_110"):
        cat_thoughts "Finally...[wait_1]he’s leaving."
    elif (current_thought == "cat_thought_111"):
        cat_thoughts "I think I convinced him...[wait_1]or that his way of dropping a threat?"
    
    # C-2-4
    elif (current_thought == "cat_thought_112"):
        cat_thoughts "What’s he doing here?"
    elif (current_thought == "cat_thought_113"):
        librarian_thoughts "Sergei...[wait_1]please be alright..."
    elif (current_thought == "cat_thought_114"):
        librarian_thoughts "I don’t like being called “you”."
    elif (current_thought == "cat_thought_115"):
        librarian_thoughts "He’d better not try and make conversation."
    elif (current_thought == "cat_thought_116"):
        unknown_thoughts "Whatever he wants...[wait_1]it had better be quick."
    elif (current_thought == "cat_thought_117"):
        cat_thoughts "Why is he asking me...?[wait_1] There are plenty of others to talk to..."
    elif (current_thought == "cat_thought_118"):
        cat_thoughts "I thought it was something falling...[wait_1]but it could have been a gun..."
    elif (current_thought == "cat_thought_119"):
        cat_thoughts "If it was a gun...[wait_1]does that mean this was murder?"
    elif (current_thought == "cat_thought_120"):
        cat_thoughts "Lloyd is pretty suspicious...[wait_1]he came from nowhere...[wait_1]he’s asking questions..."
    elif (current_thought == "cat_thought_121"):
        cat_thoughts "Go talk to someone else...[wait_1]please..."

    # C-3
    elif (current_thought == "cat_thought_122"):
        cat_thoughts "It’s him![wait_1] Can I get out of here before he sees me?"
    elif (current_thought == "cat_thought_123"):
        cat_thoughts "He was at the venue last night...[wait_1]asking me those questions.[wait_1] Could he be...?"
    elif (current_thought == "cat_thought_124"):
        cat_thoughts "I should talk to him now.[wait_1] He’ll get suspicious if I try to leave."
    elif (current_thought == "cat_thought_125"):
        cat_thoughts "I can’t let him know about Sergei and I."
        $ add_boolean("cat_knows_sergei")
    elif (current_thought == "cat_thought_126"):
        cat_thoughts "What does he want?[wait_1] I didn’t see anything."
    elif (current_thought == "cat_thought_127"):
        cat_thoughts "No...[wait_05]he knows too much.[wait_1] How do I get him to leave?"
    elif (current_thought == "cat_thought_128"):
        cat_thoughts "I can’t trust him.[wait_1] I can only trust Sergei’s allies...[wait_1]the others in the community..."
        $ add_boolean("cat_references_community")
    elif (current_thought == "cat_thought_129"):
        cat_thoughts "He’s not going to give up.[wait_1] I need to get him to leave."
    elif (current_thought == "cat_thought_130"):
        cat_thoughts "This is going to be a lie.[wait_1] I just know that it is."
    elif (current_thought == "cat_thought_131"):
        cat_thoughts "Either he’s telling the truth, or he’s found out about Sergei’s allies.[wait_1] Whichever it is...[wait_1]I’d better use the shielding technique."
    elif (current_thought == "cat_thought_132"):
        cat_thoughts "..."
        lloyd_thinking thinking "I can’t read her thoughts...[wait_05]but I could before.[wait_1] What’s going on here?"
    elif (current_thought == "cat_thought_133"):
        cat_thoughts "He’s clearly lying.[wait_1] He doesn’t work for the venue."
    elif (current_thought == "cat_thought_134"):
        cat_thoughts "Is he going to retaliate?[wait_1] I have to intimidate him."

    # C-3-4
    elif (current_thought == "cat_thought_135"):
        cat_thoughts "He did arrive...[wait_1]good.[wait_1] That means...[wait_1]the plan can proceed."
    elif (current_thought == "cat_thought_136"):
        cat_thoughts "It also has...[wait_1]a little surprise for you.[wait_1] I hope he reads it soon."
    elif (current_thought == "cat_thought_137"):
        cat_thoughts "I took them from his computer...[wait_1]obviously..."
    elif (current_thought == "cat_thought_138"):
        cat_thoughts "Does he suspect something...?[wait_1] That I want his guard lowered for tomorrow...?"
        $ add_boolean("cat_preparing_trap")
    elif (current_thought == "cat_thought_139"):
        cat_thoughts "Finally...[wait_1]what’s got him so cautious...?"
    elif (current_thought == "cat_thought_140"):
        cat_thoughts "Now...[wait_1]to work on the next few steps..."
    
    # C-4
    elif (current_thought == "cat_thought_141"):
        cat_thoughts "..."
        lloyd_thinking thinking "I can’t read her thoughts.[wait_1] She’s blocking me somehow."
    elif (current_thought == "cat_thought_142"):
        cat_thoughts "I think that he’s being honest...[wait_1]what have I been chasing after all this time?"
    elif (current_thought == "cat_thought_143"):
        cat_thoughts "I might be wrong...[wait_1]but if I am, at least I’ll be with Sergei."
    elif (current_thought == "cat_thought_144"):
        cat_thoughts "Why am I so...[wait_1]broken?[wait_1] Why aren’t I like other people?"
    elif (current_thought == "cat_thought_145"):
        cat_thoughts "He thinks that he’s like me...[wait_1]but he’s not."
    elif (current_thought == "cat_thought_146"):
        cat_thoughts "I don’t think he’s that bad a person...[wait_1]I think I should make up for my mistake..."
    elif (current_thought == "cat_thought_147"):
        cat_thoughts "I suppose he can have this."
    elif (current_thought == "cat_thought_148"):
        cat_thoughts "What’s he hoping to get out of this?"
    elif (current_thought == "cat_thought_149"):
        cat_thoughts "I hope he finds what he’s looking for.[wait_1] He deserves it."
    
    # D-3
    elif (current_thought == "cat_thought_150"):
        if (check_boolean("cat_name_discovered")):
            cat_thoughts "It’s him...[wait_1]My wait is over."
        else:
            librarian_thoughts "It’s him...[wait_1]My wait is over."
    elif (current_thought == "cat_thought_151"):
        cat_thoughts "Where do I begin...?[wait_1] Do I tell him about Sergei...?"
    elif (current_thought == "cat_thought_152"):
        cat_thoughts "I’ll set the scene first...[wait_1]then I’ll explain about Sergei..."
    elif (current_thought == "cat_thought_153"):
        cat_thoughts "How could I have done any different...?"
    elif (current_thought == "cat_thought_154"):
        cat_thoughts "It was so positive to see someone volunteering...[wait_1]to see some fresh blood..."
    elif (current_thought == "cat_thought_155"):
        cat_thoughts "If only I had known what would happen...[wait_1]if only I could have seen it coming..."
    elif (current_thought == "cat_thought_156"):
        cat_thoughts "You tried...[wait_1]but you didn’t do enough..."
    elif (current_thought == "cat_thought_157"):
        cat_thoughts "There are some coincidences...[wait_1]but I shouldn’t hold a grudge.[wait_1] He didn’t do anything wrong..."
    elif (current_thought == "cat_thought_158"):
        cat_thoughts "Why didn’t you act sooner...?[wait_1] Why didn’t you at least stop the killer...?"
    elif (current_thought == "cat_thought_159"):
        cat_thoughts "He doesn’t need to know...[wait_1]Nobody will ever find out..."
    elif (current_thought == "cat_thought_160"):
        cat_thoughts "Just to be sure..."
    elif (current_thought == "cat_thought_161"):
        cat_thoughts "Is it really a coincidence...?[wait_1] I feel like he’s hiding something..."
    elif (current_thought == "cat_thought_162"):
        cat_thoughts "I was wrong...[wait_1]why do I always overthink things...?"
    elif (current_thought == "cat_thought_163"):
        cat_thoughts "He won’t understand.[wait_1] How do I tell him?"
    elif (current_thought == "cat_thought_164"):
        cat_thoughts "My words are insufficient...[wait_1]if only he could read my thoughts, and feel the emotions that I felt for Sergei."
    elif (current_thought == "cat_thought_165"):
        cat_thoughts "Whoever he has lost...[wait_1]they can’t compare to Sergei..."
    elif (current_thought == "cat_thought_166"):
        cat_thoughts "If he has overdue fees...[wait_1]I’ll clear them..."
    elif (current_thought == "cat_thought_167"):
        cat_thoughts "Why would he want a stranger to find them...?[wait_1] This is strange..."
    elif (current_thought == "cat_thought_168"):
        cat_thoughts "Lloyd tried to help Sergei...[wait_1]I shouldn’t be so suspicious of him..."
    elif (current_thought == "cat_thought_169"):
        cat_thoughts "He never mentioned a Jack to me...[wait_1]so why would he tell Lloyd the name?"
    
    # D-4
    elif (current_thought == "cat_thought_170"):
        cat_thoughts "It’s him...[wait_1]I’ll have to tell him."
    elif (current_thought == "cat_thought_171"):
        cat_thoughts "If he read Lloyd’s mind, he might have found something and thought that Lloyd’s name was Jack..."
        lloyd_thinking thinking "Interesting idea.[wait_1] But what could Sergei have read in my mind to think that I identified as someone called Jack?"
    elif (current_thought == "cat_thought_172"):
        cat_thoughts "He didn’t refer to Lloyd as Jack...[wait_1]the request was to find Jack.[wait_1] The theory doesn’t work."
    elif (current_thought == "cat_thought_173"):
        cat_thoughts "Does he realise what he’s done...?"
    elif (current_thought == "cat_thought_174"):
        cat_thoughts "He had nothing to gain from it...[wait_1]no ulterior motive...[wait_1]he was just trying to help."
    elif (current_thought == "cat_thought_175"):
        cat_thoughts "Then...[wait_1]all of my preparation...[wait_1]it was all for nothing..."
    elif (current_thought == "cat_thought_176"):
        cat_thoughts "Maybe...[wait_1]there’s a chance..."
    elif (current_thought == "cat_thought_177"):
        cat_thoughts "I shouldn’t get my hopes up...[wait_1]but maybe..."
    elif (current_thought == "cat_thought_178"):
        cat_thoughts "I’ll have to fill in the pit...[wait_1]but at least he’s gone..."
    elif (current_thought == "cat_thought_179"):
        cat_thoughts "Should I tell the long version or the short version...?[wait_1] I’ll stick with the short version..."
    elif (current_thought == "cat_thought_180"):
        cat_thoughts "I’d better be careful with my words...[wait_1]I can’t have Lloyd guess the real reason why he was researching it..."
    elif (current_thought == "cat_thought_181"):
        cat_thoughts "If only I could go back to those days...[wait_1]if only Sergei hadn’t died..."
    elif (current_thought == "cat_thought_182"):
        cat_thoughts "Bones and Flowers...by The Screaming Tribesmen..."
    elif (current_thought == "cat_thought_183"):
        cat_thoughts "Why is this such a rare trait in people...?[wait_1] Why can’t people think of others more, rather than themselves...?"
    elif (current_thought == "cat_thought_184"):
        cat_thoughts "What’s wrong with liking black clothing?[wait_1] What’s wrong with liking tattoos or piercings?"
    elif (current_thought == "cat_thought_185"):
        cat_thoughts "Lloyd might sympathise...[wait_1]but he’ll never understand what it’s like to be a woman."
    elif (current_thought == "cat_thought_186"):
        cat_thoughts "Maybe I’ll get a new tattoo...[wait_1]one of the ones that Sergei said he was thinking of getting..."
    elif (current_thought == "cat_thought_187"):
        cat_thoughts "Do I have to answer this question...?[wait_1] I don’t know..."
    elif (current_thought == "cat_thought_188"):
        cat_thoughts "He doesn’t understand...[wait_1]work is the one easy thing at the moment, because it’s the one thing I know how to do..."
    elif (current_thought == "cat_thought_189"):
        cat_thoughts "Lloyd really does think about other people a lot...[wait_1]he’s a good person."
    
    # E-4
    elif (current_thought == "cat_thought_190"):
        hot_librarian_thoughts "It’s him...[wait_1]I need to talk to him..."
    elif (current_thought == "cat_thought_191"):
        hot_librarian_thoughts "I really owe Lloyd...he’s such a good person."
        $ add_boolean("cat_sympathetic")
        if ((check_boolean("barbara_sympathetic") and check_boolean("eddie_sympathetic")) or (check_boolean("barbara_sympathetic") and check_boolean("graves_sympathetic")) or (check_boolean("eddie_sympathetic") and check_boolean("graves_sympathetic"))):
            jack_possessing_thinking angry "She’s another person that Lloyd matters to...[wait_05]what does he have that I don’t?!"
        elif (check_boolean("barbara_sympathetic") or check_boolean("eddie_sympathetic") or check_boolean("graves_sympathetic")):
            jack_possessing_thinking angry "Why does she think so highly of Lloyd?[wait_1] What’s he done for her lately?"
        else:
            jack_possessing_thinking smug "If I’m such a good person...[wait_05]how will you show me your appreciation?[wait_1] Heh heh."
    elif (current_thought == "cat_thought_192"):
        hot_librarian_thoughts "So then he was trying to occupy me...[wait_1]but why?"
    elif (current_thought == "cat_thought_193"):
        hot_librarian_thoughts "I need to be on guard...[wait_1]this might be another attempt to distract me..."
    elif (current_thought == "cat_thought_194"):
        hot_librarian_thoughts "I have to tell him..."
    elif (current_thought == "cat_thought_195"):
        hot_librarian_thoughts "It was so thoughtful of him...[wait_1]he’s such a good person..."
        $ add_boolean("cat_sympathetic")
        if ((check_boolean("barbara_sympathetic") and check_boolean("eddie_sympathetic")) or (check_boolean("barbara_sympathetic") and check_boolean("graves_sympathetic")) or (check_boolean("eddie_sympathetic") and check_boolean("graves_sympathetic"))):
            jack_possessing_thinking angry "She’s another person that Lloyd matters to...[wait_05]what does he have that I don’t?!"
        elif (check_boolean("barbara_sympathetic") or check_boolean("eddie_sympathetic") or check_boolean("graves_sympathetic")):
            jack_possessing_thinking angry "Why does she think so highly of Lloyd?[wait_1] What’s he done for her lately?"
        else:
            jack_possessing_thinking smug "If I’m such a good person...[wait_05]how will you show me your appreciation?[wait_1] Heh heh."
    elif (current_thought == "cat_thought_196"):
        hot_librarian_thoughts "Was he running from the murderer?[wait_1] Did he never intend to help Sergei?"
    elif (current_thought == "cat_thought_197"):
        hot_librarian_thoughts "A hero would have saved Sergei..."
    elif (current_thought == "cat_thought_198"):
        hot_librarian_thoughts "Not a difficult request to fulfill..."
    elif (current_thought == "cat_thought_199"):
        hot_librarian_thoughts "Is he...[wait_1]hitting on me?"
    elif (current_thought == "cat_thought_200"):
        hot_librarian_thoughts "I suppose that I can recommend some classics..."
    elif (current_thought == "cat_thought_201"):
        hot_librarian_thoughts "He seems easily distracted...[wait_1]but I think he could manage it."
    elif (current_thought == "cat_thought_202"):
        hot_librarian_thoughts "I think he might have only seen an adaptation of Dracula...[wait_1]possibly a porn version..."
    elif (current_thought == "cat_thought_203"):
        hot_librarian_thoughts "I’ll test him...[wait_1]see whether he has read it or not..."
    elif (current_thougt == "cat_thought_204"):
        hot_librarian_thoughts "I’ll try one more time...[wait_1]this isn’t as enjoyable as I thought it would be."
    elif (current_thought == "cat_thought_205"):
        hot_librarian_thoughts "He probably thinks that Frankenstein is the name of the creature..."
    elif (current_thought == "cat_thought_206"):
        hot_librarian_thoughts "I hate when people just watch the movie instead of reading the book...[wait_1]why are so many people against reading these days?"
    elif (current_thought == "cat_thought_207"):
        hot_librarian_thoughts "And just like that...[wait_1]he’s completely missed the point."
    elif (current_thought == "cat_thought_208"):
        hot_librarian_thoughts "This should be entertaining...[wait_1]will it be by Dr. Seuss?[wait_1] Or more along the lines of Mr. Nice?"
    elif (current_thought == "cat_thought_209"):
        hot_librarian_thoughts "It’s Carrie.[wait_1] He’s talking about Carrie."
    elif (current_thought == "cat_thought_210"):
        hot_librarian_thoughts "How few books has he read...[wait_1]if he thinks that Carrie is obscure?"
    elif (current_thought == "cat_thought_211"):
        hot_librarian_thoughts "Will he mention anything beyond the prom scene?"
    elif (current_thought == "cat_thought_212"):
        hot_librarian_thoughts "I feel like he hasn’t actually read it...[wait_1]but it is a good book."
    elif (current_thought == "cat_thought_213"):
        hot_librarian_thoughts "Does he think I don’t have access to any books...?"
    elif (current_thought == "cat_thought_214"):
        hot_librarian_thoughts "I’ll try to let him down gently...[wait_1]he hasn’t been very enjoyable to talk to but his nerves might have gotten the better of him."
    elif (current_thought == "cat_thought_215"):
        hot_librarian_thoughts "I...[wait_1]don’t think that I want him to return.[wait_1] He was very off-putting."
        

    $ ignore_thoughts_length()
    return