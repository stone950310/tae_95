# Taehyun Seok(110701372)
# AMS 380 quiz 2
# 1 (1) winning chance with staying is that first choice door is car : 1/3
# 1	(2) winning chance with switching is that first choice door is goat : 2/3
# 2
import random
n = 1000
win_stay_counts = 0
win_switch_counts = 0
for i in range(n):
	car_door = random.randint(1, 3)
	first_choice_door = random.randint(1, 3)
	if first_choice_door == car_door:
		win_stay_counts = win_stay_counts + 1
	if first_choice_door != car_door:
		win_switch_counts = win_switch_counts + 1
print(win_stay_counts / n)  # winning chance with staying
print(win_switch_counts / n)  # winning chance with switching
