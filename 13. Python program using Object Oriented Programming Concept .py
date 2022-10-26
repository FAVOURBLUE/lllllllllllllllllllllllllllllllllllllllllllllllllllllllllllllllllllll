class MyTime:
 def __init__(self, hrs=0, mins=0, secs=0):
 """ Create a MyTime object initialized to hrs, mins, secs """
 self.hours = hrs
 self.minutes = mins
 self.seconds = secs
 def __str__(self):
 timeString = ""
 if self.hours < 10:
 timeString += "0"
 timeString += str(self.hours) + ":"
 if self.minutes < 10:
 timeString += "0"
 timeString += str(self.minutes) + ":"
 if self.seconds < 10:
 timeString += "0"
 timeString += str(self.seconds)
 return timeString
def add_time(t1, t2):
 h = t1.hours + t2.hours
 m = t1.minutes + t2.minutes
 s = t1.seconds + t2.seconds
 sumTime = MyTime(h, m, s)
 return sumTime
currentTime = MyTime(9, 14, 30)
breadTime = MyTime(3, 35, 0)
doneTime = add_time(currentTime, breadTime)
print(doneTime)
