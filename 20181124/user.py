class SampleUser:
    def __init__(self, name, age, pref):
        self.name = name
        self.age = age
        self.pref = pref

    def showProfile(self):
        print(self.name+ "'s profile")
        print(self.name+ " is " + str(self.age) + "years old")
        print(self.name+ " is from " + self.pref)
