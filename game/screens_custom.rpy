screen debug():
    
    vbox:
        xalign 0.5
        yalign 0.2

        textbutton _("Test Mind Reading"):
            action [
                Hide("debug"),
                Call("test_mind_reading", from_current=True)
            ]

        textbutton _("Test Conversation Rewind"):
            action NullAction()

        textbutton _("Test Conversation Progress"):
            action NullAction()

        textbutton _("Test Map Jump"):
            action NullAction()

        textbutton _("Test Money"):
            action NullAction()

        textbutton _("Test Locking Choices"):
            action NullAction()

        textbutton _("Test Upgrading Psychic Abilities"):
            action NullAction()

        textbutton _("Test Timeline"):
            action NullAction()

screen psychic_powers():
    frame:
        xalign 1.0
        yalign 0.0
        background Solid("#ffea00")
        padding (5, 5, 5, 5)
        
        vbox:
            if (current_thought is not None):
                textbutton _("Read Mind" if minds_read < 3 else "Power Exhausted"):
                    text_color "#000"
                    action [
                        SetVariable("minds_read", (minds_read + 1 if minds_read < 3 else 3)),
                        (Call(current_thought, from_current=True) if minds_read < 3 else NullAction())
                    ]