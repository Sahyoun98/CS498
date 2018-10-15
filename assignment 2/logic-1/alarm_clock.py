def alarm_clock(day, vacation):
  x = 7
  if day == 0 or day == 6:
    x = x + 3
  if vacation:
    x = x + 3
  if x == 7:
    return "7:00"
  if x == 10:
    return "10:00"
  return "off"