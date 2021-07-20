"""
Implement the output of information about the time interval depending on its duration in seconds:
- up to a minute: <s> sec;
- up to an hour: <m> min <s> sec;
- up to a day: <h> hour <m> min <s> sec;
- * in other cases: <d> days <h> hour <m> min <s> sec.
                   (<d> дн <h> час <m> мин <s> сек)
"""

HOURS = 24
MINUTES = 60
SECONDS = 60

DURATION = [SECONDS, MINUTES, HOURS]
interval_name = ['дн', 'час', 'мин', 'сек']
duration_list = [53, 153, 4153, 400153, 606005, 409800308]

for duration in duration_list:
    print(f'{duration = }')

    interval_value = []
    for interval in DURATION:
        if duration:
            interval_value.insert(0, duration % interval)
            duration //= interval
    if duration:
        interval_value.insert(0, duration)

    length = len(interval_value)
    for i in range(length):
        print(f' {interval_value[i]} ', end=interval_name[4-length+i])
    print()
