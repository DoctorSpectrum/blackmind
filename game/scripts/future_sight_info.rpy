init python:
    def get_future_sight_info(id=None, person=None, branch=None, day=None):
        information = [{
                "person": None,
                "branch": None,
                "day": None,
                "picture": "jack_smug.png",
                "title": "UNKNOWN",
                "description": "Unknown future vision; please report this bug!",
                "current": [],
                "general": []
            }, {
                "person": "barbara_prologue",
                "branch": None,
                "day": None,
                "picture": "barbara_smiling.png",
                "title": "BARTENDER",
                "description": "This is a description of your goal and what you are seeing",
                "current": [
                    {
                        "keyword": "ALCOHOL",
                        "discovered": False
                    }
                ],
                "general": [
                    {
                        "keyword": "LONG-TERM #1",
                        "discovered": False
                    },
                    {
                        "keyword": "LONG-TERM #2",
                        "discovered": False
                    },
                    {
                        "keyword": "LONG-TERM #3",
                        "discovered": False
                    },
                    {
                        "keyword": "LONG-TERM #4",
                        "discovered": False
                    }
                ]
            }]

        if (id is not None):
            return information[id]

        for info in information:
            if (info["person"] == person and info["branch"] == branch and info["day"] == day):
                return info

        return information[0]

    def get_future_sight_history(id=None, person=None):
        history_list = [{
            "person": None,
            "history": [
                {
                    "history": "Error loading character's history",
                    "unlocked": True
                }
            ]
        }, {
            "person": "barbara_prologue",
            "history": [
                {
                    "history": "Test history",
                    "unlocked": False
                },
                {
                    "history": "Test history #2",
                    "unlocked": False
                }
            ]
        }]

        if (id is not None):
            return construct_history(history_list[id])

        for history in history_list:
            if (history["person"] == person):
                return construct_history(history)
        
        return construct_history(history_list[0])

    def construct_history(history):
        history_string = ""
        for h in history["history"]:
            if h["unlocked"] == True:
                history_string += h["history"] + "\r\n"

        return history_string if len(history_string) > 0 else "You have not discovered anything about this character yet."
