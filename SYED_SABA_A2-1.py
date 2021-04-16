#SABA SYED
#CSIT104-04
#KATERINE G. HERBERT
#02/21/2020
#A PROGRAM TO FIND YOUR AGE ON DIFFERENT PLANETS INCLUDING DAYS AND YEARS

age = 0
age = int(input("Enter Age = "))

days_in_year = {"Mercury": 88, "Venus": 224, "Earth": 365, "Mars": 687, "Jupiter": 4307, "Saturn": 10731, "Uranus": 30660, "Neptune": 59860, "Pluto": 90520}

#days in planets
for planet in days_in_year:
    print("Days old on " + planet)
    #code for below was found on website listed in references in word doc
    print("{0}: {1}".format(planet, days_in_year[planet] * age) + " days old")

#years of age on planets
for planet in days_in_year:
    print ("Years old on " + planet)
    # code for below was found on website listed in references in word doc
    print("{0}: {1}".format(planet, age/ days_in_year[planet]) + " Earth years old")



