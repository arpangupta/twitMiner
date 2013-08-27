import json

trainingset= open(r'OutputTest.txt', 'r').read().splitlines()
sport = json.load(open("sportsout"))
political = json.load(open("politicalout"))
count = 0 
for line in trainingset:
	if(line.split()[1] =='Sports' and line.split()[0] in sport.keys() ):
		count = count +1
	elif(line.split()[1] =='Politics' and line.split()[0] in political.keys() ):
		count = count +1

print str(count) + " of 3916" 
print str((count/3916.0)*100.0)

