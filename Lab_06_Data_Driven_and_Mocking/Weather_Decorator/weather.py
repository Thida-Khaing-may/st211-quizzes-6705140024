def get_temperature():
    return 20
def describe_weather():
    if get_temperature() >= 15:
        return "Pleasant"
    return "Cold"