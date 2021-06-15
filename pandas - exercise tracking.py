import pandas as pd

exercise = {
    'pressups': [30, 19, 26], # -20 = boo, 20+ = yay
    'run': [4, 5, 6],         # -4 = boo, 5+ = yay
    'situps': [19, 50, 20],   # -20 = boo, 20+ = yay
    'squats': [20, 35, 64],   # -20 = boo, 20+ = yay    
    }

myvar = pd.DataFrame(exercise)

print(myvar)

press_prize = []
run_prize = []
sit_prize = []
squat_prize = []

for value in exercise['pressups']:
    if value < 20:
        press_prize.append("Boo")
    else:
        press_prize.append("Yay")
for value in exercise['run']:
    if value < 5:
        run_prize.append("Boo")
    else:
        run_prize.append("Yay")
for value in exercise['situps']:
    if value < 20:
        sit_prize.append("Boo")
    else:
        sit_prize.append("Yay")
for value in exercise['squats']:
    if value < 20:
        squat_prize.append("Boo")
    else:
        squat_prize.append("Yay")
#print(press_prize)
#print(run_prize)
#print(sit_prize)
#print(squat_prize)
         

if press_prize[0] == 'Yay' and run_prize[0] == 'Yay' and sit_prize[0] == 'Yay' and squat_prize[0] == 'Yay':
    print("Day 1 = yay")
else:
    print("Day 1 = boo")
if press_prize[1] == 'Yay' and run_prize[1] == 'Yay' and sit_prize[1] == 'Yay' and squat_prize[1] == 'Yay':
    print("Day 2 = yay")
else:
    print("Day 2 = boo")    
if press_prize[2] == 'Yay' and run_prize[2] == 'Yay' and sit_prize[2] == 'Yay' and squat_prize[2]== 'Yay':
    print("Day 3 = yay")
else:
    print("Day 3 = boo")    