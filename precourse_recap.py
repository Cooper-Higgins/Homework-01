current_date = 20
operation_date = 30
patient = "Mr. Goose"

def countdown():
  days_left = operation_date - current_date
  print(f"Only {days_left} days to go until your operation!")

def get_well_soon():
  print("Get well soon " + str(patient) + "!")

countdown()
get_well_soon()