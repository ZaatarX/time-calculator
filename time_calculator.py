def add_time(start, duration, day=None):
    hours = []
    minutes = []
    if day:
        day = str(day)
        weekdays = {
            0: 'Sunday',
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday'
        }
        for key, value in weekdays.items():
            if value == day.capitalize():
                day = key
                break
    else:
        day = ''

    # breaking down the string into usable data

    # extracting if am or pm
    start = start.split()
    dn = str(start[1])
    if dn == 'AM':
        flag = 0
    else:
        flag = 1

    # extracting hours and minutes from start time
    start = start[0].split(':')
    hours.append(int(start[0]))
    minutes.append(int(start[1]))

    # extracting hours and minutes from duration time
    duration = duration.split(':')
    hours.append(int(duration[0]))
    minutes.append(int(duration[1]))

    # normalizing minutes and adding an hour if necessary
    if minutes[0] + minutes[1] >= 60:
        hours[1] += 1
        minutes[0] = str((minutes[0] + minutes[1]) - 60)
    else:
        minutes[0] += minutes[1]

    if int(minutes[0]) < 10:
        temp = str(minutes[0])
        minutes[0] = '0' + temp

    # adding to get total hours and calculate passage of time
    hours.append(hours[0] + hours[1])
    shift = 0

    # to each loop a shift is added meaning it went from AM to PM and vice-versa
    while hours[2] >= 12:
        hours[2] -= 12
        shift += 1
        if flag == 0:
            flag = 1
        else:
            flag = 0

    # time to build the string
    if hours[2] == 0:
        hours[2] = 12

    hour = str(hours[2])
    minute = str(minutes[0])

    if flag == 0:
        dn = 'AM'
    else:
        dn = 'PM'

    # no shift difference
    if shift == 0 or (shift == 1 and flag == 1):
        if day != '':
            day = f', {weekdays[day]}'
        return f'{hour}:{minute} {dn}{day}'
    # next day shifts
    elif shift <= 2:
        if day != '':
            if day >= 6:
                day %= 6
                day = f', {weekdays[day]}'
            else:
                day = f', {weekdays[day]}'
        return f'{hour}:{minute} {dn}{day} (next day)'

    later = round(hours[1] / 24) + 1

    if day != '':
        day += later
        if day > 6:
            day %= 7
            day = f', {weekdays[day]}'
        else:
            day = f', {weekdays[day]}'

    if flag + (round(shift / 2) + 1) % 2 == 0:
        return f'{hour}:{minute} PM{day} ({later} days later)'
    else:
        return f'{hour}:{minute} AM{day} ({later} days later)'
