# Name: Jawaad Ahmar
# Student#: 251237757
# UWO email: jahmar@uwo.ca



# this program holds class Country



# class Country - holds the information about a single country
class Country:
    # constructor __init__ takes 4 parameters on data of a single country
    def __init__(self, name, pop, area, cont):
        self.name = name
        self.population = pop
        if self.population == None:
            self.population = ""
        self.area = area
        if self.area == None:
            self.area = ""
        self.continent = cont
        if self.continent == None:
            self.continent = ""

    # getter method getName returns name of a country
    def getName(self):
        return self.name

    # getter method getPopulation returns population of a country
    def getPopulation(self):
        return self.population

    # getter method getArea returns area of a country
    def getArea(self):
        return self.area

    # getter method getContinent returns continent of a country
    def getContinent(self):
        return self.continent

    # setter method setName sets the name of a country
    def setName(self,name):
        self.name = name

    # setter method setPopulation sets the population of a country
    def setPopulation(self,pop):
        self.population = pop

    # setter method setArea sets the area of a country
    def setArea(self, area):
        self.area = area

    # setter method setContinent sets continent of a country
    def setContinent(self, cont):
        self.continent = cont

    # special method __repr__ generates string representation of objects
    def __repr__(self):
        return str(self.name) + " (pop: " + str(self.population) + ", size: " + str(self.area) + ") in " + str(self.continent)





