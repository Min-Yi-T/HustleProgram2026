# Min Yi Truong/Lab3/Hustle

#Ticket 1
username = "Yuu"
#PERDICT : 2
print(len(username))
# Len did count every single letter but not symbols like "" though.


#Ticket 2
print(username[0]) #Y
print(username[2]) #u

# The reason why the last letter (aka the second letter u) is one numeber less is because the first letter is counted as 0.


#Ticket 3
print(f"Welcome to Loop, @{username}!")
starting = "Welcome to Loop, @"
print(starting + username + "!")

#PERDICT : I think the two lines would look the same or very simlar.
# Method 1 the one where you use f is easier for me because it's just quicker to remember since I learned it just recently.


#Ticket 4
# username[0] = "X"

#PERDICT : I perdict that it will run the red purple line ERROR thing. (The Error that showed up for me is down below)

# Traceback (most recent call last):
#   File "/Users/yu/Desktop/HustleProgram2026/lab3_minyi.py", line 22, in <module>
#     username[0] = "X"

# The thing that the string was not able to change was the first latter of the user name to X.


#Ticket 5
feed = ["Drawing", "Sleeping", "Writing"]
#PERDICT : I think Drawing will be printed out first and that it will count 6 letters.
print(len(feed[0]))
# I used index 0 to get the first string.

#Ticket 6
feed.append("Water")
print(feed)
#Perdict : I decided to put water so I think the next thing added will be water but IDK.
# My 4th post does not sit at index three so i'm not really sure what you mean.

#Ticket 7