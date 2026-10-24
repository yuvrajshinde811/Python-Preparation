import os

if(not os.path.exists("Test")):
    os.mkdir("Test")

for i in range(0, 5):
    os.rename(f"Test/day{i+1}", f"Test/day-{i+1}")