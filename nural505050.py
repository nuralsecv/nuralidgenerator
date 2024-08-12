#### LIBS ######
import os
import time
import random

##### APP TOOLS ####

def nural_system(cmd):
    os.system(cmd)
    
def nural_clear():
    os.system("cls" if os.name == "nt" else "clear")

#### Settings #####

nuralapp_title = "nural0"

##### Title ######

os.system("title " + nuralapp_title)

###### Clear Screen ######

nural_clear()

########## Data ############

Countrys = ["MA", "US"]

Females_US = ["Ju", "Jesika", "Ashely", "Angel", "Loria"]
Males_US = ["John", "Michael", "David", "Chris", "James"]

Females_MA = ["Aicha", "Hiba", "Samira", "Najia", "Ahlam", "Khnata"]
Males_MA = ["Youssef", "Ahmed", "Mohamed", "Rachid", "Hassan"]

####### Gender Select ####

nuralgender = input("Select a GENDER (M,F)     : ").upper()

if nuralgender == "M":
    print("> Gender : M")
    print("> Wait..... ")
    time.sleep(2)
elif nuralgender == "F":
    print("> Gender : F")
    print("> Wait..... ")
    time.sleep(2)
else:
    print("Invalid gender selected.")
    exit()

######## Select Country ##########

print("""Countries :
-MA -US
         
""")

nuralask = input("Select Your Country : ").upper()

########## Print Results #########

nural_clear()

print("> Waiting ..")
time.sleep(1.5)
nural_clear()
print("> Waiting ....")
time.sleep(1)
nural_clear()

###### API #######

if nuralask == "MA":
    if nuralgender == "M":
        Youssef = random.choice(Males_MA)
    elif nuralgender == "F":
        Youssef = random.choice(Females_MA)
elif nuralask == "US":
    if nuralgender == "M":
        Youssef = random.choice(Males_US)
    elif nuralgender == "F":
        Youssef = random.choice(Females_US)
else:
    print("Country not recognized.")
    exit()

## Results
print(f"""
> Results :
 - Gender :  {nuralgender} 
 - Country: {nuralask}
 - Name : {Youssef}  """)
