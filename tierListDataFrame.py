import csv

#create list to store csv entries with header
csvEntries = [["Name", "Watched", "Ranking", "Tier"]]

#open file for reading
dataFile = open('D:\\tierList.txt','r')

#read all of the lines into a list
lines = dataFile.readlines()

#get rid of \n
for line in lines:
    line = line[:-1]
    print(line)

#parameters for the data entries
name = ""
watched = 0
ranking = 0
tier = 8    #tier uses numerical value for z-axis to determine color in R

#for all of the lines in the list that contains the file contents
for i in range(0,len(lines)):
    
    #get the tiers based on the dashed line seperators
    if(lines[i][0] is "-"):
        tier-=1

    #get the ranks based on the first number on a line
    tempRank = "0"
    for j in range(0,len(lines[i])):
        if(lines[i][j].isdigit()):
            tempRank = tempRank + str(lines[i][j])
        else:
            ranking = -int(tempRank)    #negative integer value so higher ranked anime are higher on the y-axis
            break

    tempName = ""
    lineParition = lines[i].partition(" ")[2]   #get the string after the first space since all lines start with #. words
    for char in lineParition:
        if lineParition[0] is "-":              #skip the dashed line seperators
            break
        if(char is "("):                        #anime name will always end with (#) as the watch order
            tempName = tempName[:-1]
            break
        else:
            tempName = tempName + char
    if(tempName is not ""):                     #if not null, set the name
        name = tempName

    tempWatch = lineParition.partition("(")[2]  #get rid of the left parenthesis in the watch order
    tempWatch1 = tempWatch.partition(")")[0]    #get rid of the right parenthesis in the watch order

    if(tempWatch1.isdigit()):                   #if the number is a digit, add it to the entry
        watched = int(tempWatch1)

    if tempRank is not '0':                     #if the entry is an actualy entry (not a blank line, title, etc) add it to the entry list
        csvEntries.append([name, watched, ranking, tier])


#write the entries to a csv file
with open('D:\\tierListDataFrame.csv', mode='w', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in csvEntries:
        file_writer.writerow(item)
