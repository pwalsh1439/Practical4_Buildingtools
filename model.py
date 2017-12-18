# -*- coding: utf-8 -*-
"""
Created on 06/11/2017

@author: Paul
"""

#importing standard libaries
import random, operator
#external libary
import  matplotlib.pyplot
import datetime

#Get time now in MS function
def getTimeMS():
    dt = datetime.datetime.now()
    return dt.microsecond + (dt.second * 1000000) + \
    (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)
    


#Function that works out the distance between to inputted agents
def distance_between(agent0, agent1):
    #Work out input type
    #print("here " + str(type(agent0)))
    #Pythagoris statement
    answer = (((agent0[0] - agent1[0])**2) + ((agent0[1] - agent1[1])**2))**0.5
    #Tests the previous code
    #print(answer)
    #Return the answer from the Pythagoris code 
    return answer

# Set Up Varibles
num_of_agents = 10
num_of_iterations = 100
agents = [] 


#Loop through all agents using variable then
#Randomises the y,x starting location
for i in range (num_of_agents):   
    agents.append([random.randint(0,99),random.randint(0,99)])

    print ("Start postion for agent " + str(i) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))

   
#For each step in the iteration move each agent  in a random direction.
#Loop through each step iteration 
for j in range(num_of_iterations):
    #Loop through each agent
    for i in range(num_of_agents):
        #random y Step 
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] + 1) % 100
        #random x Step
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100 
        else:
            agents[i][1] = (agents[i][1] + 1) % 100


'''
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)
'''

# Plot final postion
for i in range(num_of_agents):
    print ("End postion for agent " + str(i) + " is - y " + str(agents[i][0]) + " x " + str(agents[i][1]))
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#functions 2 answer--------
#distance = distance_between(agents[0], agents[1])
#print("Distance between Agents 1 + 2 is " + str(distance))

start = getTimeMS()
print("start time = " + str(start))

#Function 3 answer-----------
#for each agent loop trough all agents then use first and second loop postion as input for function
#Modify to find the maximum distance between agents. Add distance to List the do a min and max function.
distance_list = []
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if i != j:
            distance = distance_between(agents[i], agents[j])
            distance_list.append(distance)
            print("Distance between agent " + str(i) + " and Agent " + str(j) + " is - " + str(distance))

print("Maximum Distance between agents is " + str(max(distance_list)))
print("Minimum Distance between agents is " + str(min(distance_list)))

end = getTimeMS()
print("end time = " + str(end))


print("time taken to compare distnaces between agents = " + str(end - start))

#pulls out the higest y
#print ("The Furthest north Agent- " + str(max(agents)))

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.show()