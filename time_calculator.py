def add_time(start, duration, day = None):
    
  vueltas = 0
  days_later = ""
  dias_semana = ["Monday", "Tuesday", "Wendesday", "Thursday", "Friday", "Saturday", "Sunday"]
  final_day = 0
  days_later_int = 0

  #Get starting hours and minutes and AM/PM
  start_split = start.split()
  start_time = start_split[0].split(":")
  start_hour = start_time[0]
  start_minute = start_time[1]
  start_M = start_split[1]
  M = start_M

  #Get duration hours and minutes 
  duration_time = duration.split(":")
  duration_hour = duration_time[0]
  duration_minute = duration_time[1]
    
  #sum hours and minutes
  sum_hours = int(start_hour) + int(duration_hour)
  sum_minutes =  int(start_minute) + int(duration_minute)
      
  #sumar minutos 
  if sum_minutes > 59:
      sum_minutes -= 60
      sum_hours += 1
    
  #suma horas  
  while sum_hours > 11:
      sum_hours -= 12
      vueltas += 1

  #poner 0 en minutos
  if sum_minutes < 10:
    sum_minutes = "0" + str(sum_minutes)

  #calcular next day
  if (start_M == "PM" and (vueltas == 1 or vueltas == 2)) or (start_M == "AM" and vueltas == 2):
      days_later = "next day"

  #calcular cuando las vueltas son mas de 2  
  if vueltas > 2:
    if start_M == "PM":
      days_later = str(int(vueltas/2)) + " days later"
      days_later_int = int(vueltas/2)
    elif start_M == "AM" and vueltas == 3:
      days_later = "next day"
    elif start_M == "AM":
      if vueltas%2 == 1:
        days_later = str(int(vueltas/2)) + " days later"
        days_later_int = int(vueltas/2)
      elif vueltas%2 == 0:
        days_later = str(int(vueltas/2)) + " days later"
        days_later_int = int(vueltas/2)

  #calcular AM o PM  
  while vueltas > 0:
    if M == "PM":
      M = "AM"
    elif M == "AM":
      M = "PM"
    vueltas -= 1

  #opcional dia de la semana
  if day != None:
    start_day = dias_semana.index(day)

    if days_later == "next day":
      final_day = start_day + 1
    else:
      final_day = start_day + days_later_int      

    while final_day > 6:
      final_day -= 7
    
    final_day = dias_semana[final_day]

    new_time = str(sum_hours) + ":" + str(sum_minutes) + " " + M + "," + " " + final_day + " " + "(" + days_later + ")"
  
  else:
    new_time = str(sum_hours) + ":" + str(sum_minutes) + " " + M + " " + "(" + days_later + ")"
  
  return new_time

print(add_time("8:47 PM", "200:32", "Tuesday"))
