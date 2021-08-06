def add_time(start, duration, day=None):
    hours = []
    minutes = []
    days = []
    new_time = ''
    weekdays = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    start = start.split()
    dn = str(start[1])

    start = start[0].split(':')
    hours.append(int(start[0]))
    minutes.append(int(start[1]))

    duration = duration.split(':')
    hours.append(int(duration[0]))
    minutes.append(int(duration[1]))

    if minutes[0] + minutes[1] >= 60:
        hours[1] += 1
        minutes[0] = str((minutes[0] + minutes[1]) - 60)

    if len(minutes[0]) == 1:
        minutes[0] = '0' + minutes[0]

    hours.append(hours[0] + hours[1])
    shift = 0

    while hours[2] - 12 > 12:
        hours[2] = hours[2] - 12
        shift += 1

    if hours[2] > 12:
        hours[2] = hours[2] - 12

    if shift == 0:
        new_time = str(hours[2]) + ':' + minutes[0] + ' ' + dn.upper()
    elif shift % 2 != 0:
        new_time = str(hours[2]) + ':' + minutes[0] + ' ' + "PM"
    else:
        new_time = str(hours[2]) + ':' + minutes[0] + ' ' + "AM"

    return new_time
