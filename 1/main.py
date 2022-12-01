import os

file = "1/calories.txt"

#check if file is present
if os.path.isfile(file):
    #open text file in read mode
    text_file = open(file, "r")
 
    #read whole file to a string
    data = text_file.read()
 
    #close file
    text_file.close()
 
    new = data.split("\n\n")
    sums = []
    for l in new:
        nums = l.split("\n")
        sum = 0
        for n in nums:
            sum = sum + int(n)
        print("sum:", sum)
        sums.append(sum)
    
    sums = sorted(sums)
    len = len(sums)
    print(sums[len -1] + sums[len -2] + sums[len -3])