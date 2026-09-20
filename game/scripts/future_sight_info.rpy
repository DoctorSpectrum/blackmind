init python:
    def get_future_sight_info(id=None):
        global day, branch, person
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
                "day": 0,
                "picture": "barbara_smiling.png",
                "title": "BARTENDER",
                "description": "Jack is trying to get a free drink from the bartender",
                "current": [
                    {
                        "keyword": "ALCOHOL",
                        "discovered": check_boolean("prologue_bar_interested")
                    }
                ],
                "general": []
            }, {
                "person": "barbara_prologue_02",
                "branch": None,
                "day": 0,
                "picture": "barbara_smiling.png",
                "title": "BARTENDER",
                "description": "Jack is trying to get a free drink from the bartender",
                "current": [
                    {
                        "keyword": "EMPLOYER",
                        "discovered": check_boolean("prologue_bar_history")
                    },
                    {
                        "keyword": "IMPROVEMENTS",
                        "discovered": check_boolean("prologue_drink_policies")
                    },
                    {
                        "keyword": "CHEAPER",
                        "discovered": check_boolean("prologue_drink_discounts")
                    },
                    {
                        "keyword": "INCORRECT",
                        "discovered": check_boolean("prologue_drink_review")
                    }
                ],
                "general": [{
                        "keyword": "LEGACY",
                        "discovered": check_boolean("prologue_barbara_history_1")
                    },
                    {
                        "keyword": "QUALITY",
                        "discovered": check_boolean("prologue_barbara_history_2")
                    },
                ]
            }, {
                "person": "docherty_prologue",
                "branch": None,
                "day": 0,
                "picture": "docherty_neutral.png",
                "title": "???",
                "description": "",
                "current": [],
                "general": []
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
            "person": "barbara_prologue_02",
            "history": [
                {
                    "history": "The bar has been in the bartender's family for three generations. Profitability has been down lately.",
                    "unlocked": check_boolean("prologue_barbara_history_1")
                },
                {
                    "history": "The bartender has attended business school.",
                    "unlocked": check_boolean("prologue_barbara_history_2")
                }
            ]
        }, {
            "person": "docherty_prologue",
            "history": []
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
                history_string += h["history"] + "\r\n\r\n"

        return history_string if len(history_string) > 0 else "You have not discovered anything about this character yet."
