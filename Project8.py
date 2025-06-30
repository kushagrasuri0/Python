print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")

class Time:
    def _init_(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def _str_(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def time_to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def seconds_to_time(seconds):
        hour = int(seconds // 3600)
        seconds %= 3600
        minute = int(seconds // 60)
        second = int(seconds % 60)
        return Time(hour, minute, second)

def mul_time(time: Time, number: float) -> Time:
    total_seconds = time.time_to_seconds()
    result_seconds = total_seconds * number
    return Time.seconds_to_time(result_seconds)

def pace(finish_time: Time, distance: float) -> Time:
    return mul_time(finish_time, 1 / distance)

if _name_ == "_main_":
    race_time = Time(1, 30, 0)
    distance = 13.1  

    avg_pace = pace(race_time, distance)

    print("Race Time:", race_time)
    print("Distance:", distance, "miles")
    print("Average Pace per mile:", avg_pace)
