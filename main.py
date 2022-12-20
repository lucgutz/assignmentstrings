# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
#1
player_goal_one = "Ruud Gullit"
player_goal_two = "Marco van Basten"

#2
goal_0 = 32
goal_1 = 54

#3
scorers = player_goal_one + " " + str(goal_0) + ", " + player_goal_two + " " + str(goal_1)
print(scorers)

scorers_fstring = f"{player_goal_one} {goal_0}, {player_goal_two} {goal_1}"
print(scorers_fstring)

#4
report = f"{player_goal_one} scored in the {goal_0}nd minute\n{player_goal_two} scored in the {goal_1}th minute"
print(report)

#part 2
#1
player = "Hans van Breukelen"

#2
find_space = player.find(" ")
first_name = player[:find_space]
print(first_name)

#3
#find option is: valuable.find(value, start, end)
find_start = player.find("v")
last_name = player[find_start:]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

#4
name_short = player.replace("Hans","H.")
print(name_short)

#5
first_name_len = len(first_name)
chant = f"{first_name}! " *first_name_len 
chant = chant[:-1]
print(chant)

#6
last_character = chant[-1]
good_chant = last_character != " "
print(good_chant)

#extra
if chant[-1] != " ":
  print("The last character of chant is NOT a space")

if chant[-1] == " ":
  print("The last character of chant IS a space")

