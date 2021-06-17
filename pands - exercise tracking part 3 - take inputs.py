import pandas as pd


def get_workout():
    """Find out what exercise the person has been doing"""
    print("pressups - run - situps - squats")
    workout = input("What exercise have you done today? ").lower()
    return workout

def get_ex_value():
    """get data for many how reps or kilometres they have completed"""
    print("\nReps or Kilometres")
    value = int(input("How many reps or kilometres have you done today? "))
    return value


def log_numbers(value):
    """Find out if they would like to log the exercise list, if the answer is no then the value is 0"""
    log = input("Do you wish to log your workout (y/n)? ").lower()
    if log == 'y' and workout == 'pressups':
        pressups.append(value)
    elif log == 'y' and workout == 'run':
        runs.append(value)
    elif log == 'y' and workout == 'situps':
        situps.append(value)
    elif log == 'y' and workout == 'squats':
        squats.append(value)

def table_workouts(exercise):
    """append the data from the exercise lists to the dictionary for the table"""
    exercise['Pressups'] = pressups
    exercise['Runs'] = runs
    exercise['Situps'] = situps
    exercise['Squats'] = squats

pressups = []
runs = []
situps = []
squats = []


workout = get_workout()
value = get_ex_value()
log = log_numbers(value)
table = table_workouts(exercise)

exercise = {'Pressups': [1], 'Runs': [30], 'Situps': [5], 'Squats': [40]}

#print out the data in a table
myvar = pd.DataFrame(exercise)

print(exercise)
print(workout)
print(value)
print(myvar)

"""
logging = True
while logging:
    if len(exercise['pressups']) > 5:
        print("\nPressups logged for the week")
        break
    elif len(exercise['run']) > 5:
        print("\nRuns logged for the week")
        break
    elif len(exercise['situps']) > 5:
        print("\nSitups logged for the week")
        break
    elif len(exercise['situps']) > 5:
        print("\nSitups logged for the week")
        break
    else:
        print("no activities logged")
        break
"""





#create person who is doing the exercies
#goku = []

#add data to each list
#def find_prize():
#    for value in exercise['pressups']:
#        if value < 20:
#            press_prize.append(0)
#        else:
#            press_prize.append(1)
#    for value in exercise['run']:
#        if value < 5:
#            run_prize.append(0)
#        else:
#            run_prize.append(1)
#    for value in exercise['situps']:
#        if value < 20:
#            sit_prize.append(0)
#        else:
#            sit_prize.append(1)
#    for value in exercise['squats']:
#        if value < 20:
#            squat_prize.append(0)
#        else:
#            squat_prize.append(1)
        
#print(press_prize)
#print(run_prize)
#print(sit_prize)
#print(squat_prize)

         
#check to see if goals have been hit for each day
#def give_prize():
#    for a, b, c, d in zip(press_prize, run_prize, sit_prize, squat_prize):
#        if a == 1 and b == 1 and c == 1 and d == 1:
#            goku.append("Gold medal")
#            print(goku)
#        else:
#            goku.append("poop")
#            print(goku)
        
    




