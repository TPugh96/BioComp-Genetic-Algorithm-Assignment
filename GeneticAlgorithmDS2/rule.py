numberOfRules = 10


class Rule:
    numberOfConditions = 7
    conditions = []
    output = 0

    def __init__(self):
        self.numberOfConditions = 7
        self.conditions = []
        self.output = 0


def check_rules_match(current_data, current_rule):
    for a, b in list(zip(current_data, current_rule)):
        if a != b and b != 2:
            return False
    return True
