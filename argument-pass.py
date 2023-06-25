import random


def time_activity(*arg, **kwargs):
    print(arg)
    print(kwargs)
    min = (sum(arg)) + random.randint(0, 12)
    # choice = random.choice(kwargs.keys())
    choice2 = random.choice(list(kwargs.keys()))
    # print(f"you have to spend {min} for  {kwargs[choice]}")
    print(f"you have to spend {min} for  {kwargs[choice2]}")

time_activity(10, 12, 23, hobby="coding", sport="football", studyhour=12)
