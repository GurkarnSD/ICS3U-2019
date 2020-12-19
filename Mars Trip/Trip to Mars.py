import time
from random import randint

energyPods = {"pod1":1000, "pod2":1000, "pod3":1000, "pod4":1000, "pod5":1000, "pod6":1000, "pod7":1000, "pod8":1000, "pod9":1000, "pod10":1000}
energyUsage = {"Engine":60, "Guide":3, "EnvironSys":5, "onboardPC":2, "sciApparatus":randint(5,15), "Crew":4}
energyUsed = {"Engine":0, "Guide":0, "EnvironSys":0, "onboardPC":0, "sciApparatus":0, "Crew":0}
day = 0
commands = 0
daysToMars = 50
daysToEarth = 50
researchGathered = 0

print("Welcome to the BFR! Prepare for the trip to mars!")

def podSelect(component):
    pod = int(input("Which pod would you like to use for the "+component+": \n"))
    print("pod"+str(pod)+" has been selected for the "+component+"\n")
    return("pod"+str(pod))

def statusReport(position):
    print("----------------------------------------\nDay "+str(day)+" - "+position+": All Systems are up and running.")
    print("Status Report:\n>Engine Status\nPower remaining in "+str(Engine)+" is "+str(energyPods[Engine])+" MegaUnits\n")
    print(">Guide Status\nPower remaining in "+str(Guide)+" is "+str(energyPods[Guide])+" MegaUnits\n")
    print(">Environment System Status\nPower remaining in "+str(EnvironSys)+" is "+str(energyPods[EnvironSys])+" MegaUnits\n")
    print(">on-board PC Status\nPower remaining in "+str(onboardPC)+" is "+str(energyPods[onboardPC])+" MegaUnits\n")
    print(">Scientific Apparatus Power Status\nPower remaining in "+str(sciApparatus)+" is "+str(energyPods[sciApparatus])+" MegaUnits\n")
    print(">Crew Power Status\nPower remaining in "+str(Crew)+" is "+str(energyPods[Crew])+" MegaUnits\n")
    

def podSwitcher(component,compName):
    print("The "+str(compName)+" has lost power!")
    print(component+" has reached an energy level of 0!")
    diffInPower = energyPods[component]
    energyPods[component] = 0
    compName = podSelect("Engine")
    energyPods[compName] += diffInPower
    return compName

Engine = podSelect("Engine")
Guide = podSelect("Guide")
EnvironSys = podSelect("EnvironSys")
onboardPC = podSelect("onboardPC")
sciApparatus = podSelect("sciApparatus")
Crew = podSelect("Crew")
travelSpeed = int(input("Engine Speed:\nPress [1] for Full Power\nPress [2] for Half Power(60% Speed)\n"))

if travelSpeed == 2:
    energyUsage["Engine"] = 30
    daysToMars = 80

if 1 == int(input("Press 1 to begin launch: ")):
    cVar = 10
    while(cVar > 0):
        print(cVar)
        cVar -= 1
        time.sleep(0)

print("We have take off!\n")

while day < daysToMars:
    energyPods[Engine] -= energyUsage["Engine"]
    energyPods[Guide] -= energyUsage["Guide"]
    energyPods[EnvironSys] -= energyUsage["EnvironSys"]
    energyPods[onboardPC] -= energyUsage["onboardPC"]
    energyPods[Crew] -= energyUsage["Crew"]
    
    if energyPods[Engine] <= 0:
        Engine = podSwitcher(Engine, "Engine")

    if energyPods[Guide] <= 0:
        Guide = podSwitcher(Guide, "Guide")

    if energyPods[EnvironSys] <= 0:
        EnvironSys = podSwitcher(EnvironSys, "Environment System")

    if energyPods[onboardPC] <= 0:
        onboardPC = podSwitcher(onboardPC, "on-board PC")

    if energyPods[Crew] <= 0:
        Crew = podSwitcher(Crew, "Crew")

    day += 1
    statusReport("On Course for Mars")
   

    time.sleep(0)


print("We have arrived at Mars!\n\nBeginning Desecent....We have landed on Mars!\n")

command = int(input("What would you like to do next\nPress [1] to Start Gathering Research\nPress [2] to View Power Levels\nPress [3] to Return Home\n"))
while command == 1 or command == 2:

    if command == 2:
        print(energyPods)
        command = int(input("What would you like to do next\nPress [1] to Start Gathering Research\nPress [3] to Return Home\n"))
        
    if command == 1:
        command = int(input("Press [1] to Begin Research\nPress [2] to Cancel Research\nPress [3] to Return to Home\n"))

        while command == 1 or command == 2:
            energyPods[EnvironSys] -= energyUsage["EnvironSys"]
            energyPods[onboardPC] -= energyUsage["onboardPC"]
            energyPods[Crew] -= energyUsage["Crew"]

            if command == 1:
                energyPods[sciApparatus] -= randint(5,15) #energyUsage["sciApparatus"] this verison only runs randint once in the dictionary and the value does not change every time. This version complies with the different research power bonus question
                researchGathered += 1

            if energyPods[sciApparatus] <= 0:
                sciApparatus = podSwitcher(sciApparatus, "Scientific Apparatus")

            if energyPods[EnvironSys] <= 0:
                EnvironSys = podSwitcher(EnvironSys, "Environment System")

            if energyPods[onboardPC] <= 0:
                onboardPC = podSwitcher(onboardPC, "on-board PC")

            if energyPods[Crew] <= 0:
                Crew = podSwitcher(Crew, "Crew")

            day += 1
            statusReport("On Mars")
            command = int(input("Press [1] to Continue Research\nPress [2] to Cancel Research\nPress [3] to Return to Home\n"))

            if command == 3:
                print("Prepare for Launch!\nAll Systems Ready!\n")
        

        
    
daysToEarth = day + 50

if command == 3:
    travelSpeed = int(input("Engine Speed:\nPress [1] for Full Power\nPress [2] for Half Power(60% Speed)\n"))

    energyUsage["Engine"] = 60

    if travelSpeed == 2:
        energyUsage["Engine"] = 30
        daysToEarth = day + 80
        
    
    while day < daysToEarth:
        energyPods[Engine] -= energyUsage["Engine"]
        energyPods[Guide] -= energyUsage["Guide"]
        energyPods[EnvironSys] -= energyUsage["EnvironSys"]
        energyPods[onboardPC] -= energyUsage["onboardPC"]
        energyPods[Crew] -= energyUsage["Crew"]

        if energyPods[Engine] <= 0:
            Engine = podSwitcher(Engine, "Engine")

        if energyPods[Guide] <= 0:
            Guide = podSwitcher(Guide, "Guide")

        if energyPods[EnvironSys] <= 0:
            EnvironSys = podSwitcher(EnvironSys, "Environment System")

        if energyPods[onboardPC] <= 0:
            onboardPC = podSwitcher(onboardPC, "on-board PC")

        if energyPods[Crew] <= 0:
            Crew = podSwitcher(Crew, "Crew")
            
        day += 1
        statusReport("Returning Home")
        time.sleep(0)

    print("You Have Returned to Earth!\nBeginning Descent....Welcome Back to Earth")
    print(energyPods)
    print(researchGathered)





