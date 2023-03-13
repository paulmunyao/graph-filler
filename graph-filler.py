import os
from random import randint

for i in range(71):
    for j in range(0, randint(1, 2)):
        d = str(i) + "days ago"
        with open("file.txt","a") as file:
            file.write(d)
        os.system("git add .")
        os.system('git commit --date="'+ d +'" -m"First commit"')

os.system("git push origin master")        