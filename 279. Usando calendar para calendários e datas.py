import calendar

print(calendar.calendar(2023))
print(calendar.month(2023, 8))
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 8)
print(list(enumerate(calendar.day_name)))
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2023, 8, ultimo_dia)])
for week in calendar.monthcalendar(2023, 8):
    for day in week:
        if day == 0:
            continue
        print(day)