class WaitingList:
    def __init__(self, member, course, child_first_name, child_last_name, child_age, special_requirements=None, id=None):
        self.member = member
        self.course = course
        self.child_first_name = child_first_name
        self.child_last_name = child_last_name
        self.child_age = child_age
        self.special_requirements = special_requirements
        self.id = id