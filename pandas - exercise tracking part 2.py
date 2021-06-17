import pandas as pd



def give_medal():
    """give medal based on performance"""
    



#creating dictionary of exercises and values of each one
"""output should be bad-bad-good-bad-good"""
exercise = {
    'pressups': [30, 19, 26, 30, 20], # -20 = boo, 20+ = yay
    'run': [4, 5, 6, 0, 5],         # -4 = boo, 5+ = yay
    'situps': [19, 50, 20, 30, 21],   # -20 = boo, 20+ = yay
    'squats': [20, 35, 64, 30, 24],   # -20 = boo, 20+ = yay    
    }

#print out the data in a table
myvar = pd.DataFrame(exercise)
print(myvar)

#create empty lists to see whether the day was a successful exercise day
press_prize = []
run_prize = []
sit_prize = []
squat_prize = []

#add data to each list
for value in exercise['pressups']:
    if value < 20:
        press_prize.append(0)
    else:
        press_prize.append(1)
for value in exercise['run']:
    if value < 5:
        run_prize.append(0)
    else:
        run_prize.append(1)
for value in exercise['situps']:
    if value < 20:
        sit_prize.append(0)
    else:
        sit_prize.append(1)
for value in exercise['squats']:
    if value < 20:
        squat_prize.append(0)
    else:
        squat_prize.append(1)
        
#print(press_prize)
#print(run_prize)
#print(sit_prize)
#print(squat_prize)

         
#check to see if goals have been hit for each day
for a, b, c, d in zip(press_prize, run_prize, sit_prize, squat_prize):
    if a == 1 and b == 1 and c == 1 and d == 1:
        print("\nGood job on your exercise today.")
    else:
        print("\nTry harder next time!")
    

        


