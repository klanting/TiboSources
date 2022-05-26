import time


class Timer:
    def __init__(self, **kwargs):
        self.weeks = kwargs.get("weeks", 0)
        self.days = kwargs.get("days", 0)
        self.hours = kwargs.get("hours", 0)
        self.minutes = kwargs.get("minutes", 0)
        self.seconds = kwargs.get("seconds", 0)

        self.convert_time()

    def convert_time(self):
        if self.seconds >= 60:
            self.minutes += int(self.seconds/60)
            self.seconds = self.seconds % 60
        elif self.seconds < 0:
            self.minutes -= 1
            self.seconds += 60

        if self.minutes >= 60:
            self.hours += int(self.minutes/60)
            self.minutes = self.minutes % 60
        elif self.minutes < 0:
            self.hours -= 1
            self.minutes += 60

        if self.hours >= 24:
            self.days += int(self.hours/24)
            self.hours = self.hours % 24
        elif self.hours < 0:
            self.days -= 1
            self.hours += 24

        if self.days >= 7:
            self.weeks += int(self.days/7)
            self.days = self.days % 7
        elif self.days < 0:
            self.weeks -= 1
            self.days += 7

    def add(self, **kwargs):
        self.weeks += kwargs.get("weeks", 0)
        self.days += kwargs.get("days", 0)
        self.hours += kwargs.get("hours", 0)
        self.minutes += kwargs.get("minutes", 0)
        self.seconds += kwargs.get("seconds", 0)

        self.convert_time()

    def subtract(self, **kwargs):
        self.weeks -= kwargs.get("weeks", 0)
        self.days -= kwargs.get("days", 0)
        self.hours -= kwargs.get("hours", 0)
        self.minutes -= kwargs.get("minutes", 0)
        self.seconds -= kwargs.get("seconds", 0)

        self.convert_time()

    def display(self):
        print(self.weeks, self.days, self.hours, self.minutes, self.seconds)

    def __lt__(self, other):
        value = (self.weeks*604800 + self.days*86400 + self.hours*3600 + self.minutes*60 + self.seconds)
        return value < other

    def __gt__(self, other):
        value = (self.weeks * 604800 + self.days * 86400 + self.hours * 3600 + self.minutes * 60 + self.seconds)
        return value > other


if __name__ == "__main__":
    t = Timer(seconds=(604800 + 86400 + 3600 + 60 + 1))
    while t > 0:
        time.sleep(1)
        t.subtract(seconds=1)
        t.display()
