class Course:
    def __init__(self, name, date, times, duration, age_range, location, description, id=None):
        self.name = name
        self.date = date
        self.times = times
        self.duration = duration
        self.age_range = age_range
        self.location = location
        self.description = description
        self.id = id