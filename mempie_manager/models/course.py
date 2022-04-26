class Course:
    def __init__(self, name, date, times, duration, age_range, capacity, location, description, peak_off_peak, id=None):
        self.name = name
        self.date = date
        self.times = times
        self.duration = duration
        self.age_range = age_range
        self.capacity = capacity
        self.location = location
        self.description = description
        self.peak_off_peak = peak_off_peak
        self.id = id