weekdays=['sun','mon','tue','wed','thu','fri','sat','sun','mon']
print(weekdays.count('mon'))
weekdays=['sun','mon','tue','wed','thu','fri','sat','sun','tue','wed']
print([[x,weekdays.count(x)]for x in set(weekdays)])