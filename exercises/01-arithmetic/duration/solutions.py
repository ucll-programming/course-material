def hours(duration):
    return duration // 3600


def minutes(duration):
    return (duration - hours(duration) * 3600) // 60


def seconds(duration):
    return duration - hours(duration) * 3600 - minutes(duration) * 60
