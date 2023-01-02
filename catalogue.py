# Name: Jawaad Ahmar
# Student#: 251237757
# UWO email: jahmar@uwo.ca



# this program holds class CountryCatalogue



# import class Country, create objects in class CountryCatalogue using Country
from country import Country


# class CountryCatalogue holds information about all countries
class CountryCatalogue:
    # constructor __init__ iterates through countryFile and creates a collection of countries
    # each member is an object of the class Country
    def __init__(self, countryFile):
        self.countryCat = []
        self.countryCat_dict = {}
        self.countryName = {}

        # built in next() command skips over header line
        next(countryFile)

        # for loop iterates through countryFile and creates a collection of objects
        for record in countryFile:
            data = record.split("|")
            data[-1] = data[-1].rstrip("\n")
            name = data[0]
            continent = data[1]
            population = data[2]
            area = data[3]
            one_country = Country(name, population, area, continent)
            self.countryCat.append(one_country)
            self.countryCat_dict.update(dict({name: [continent, population, area]}))

    # setter method setPopulationOfCountry sets population given a country's name
    def setPopulationOfCountry(self,country,pop):
        success = False
        for i in range(len(self.countryCat)):
            if country == (self.countryCat[i].getName()):
                self.countryCat[i].setPopulation(pop)
                success = True
                return success

    # setter method setAreaOfCountry sets area given a country's name
    def setAreaOfCountry(self,country,area):
        success = False
        for i in range(len(self.countryCat)):
            if country == (self.countryCat[i].getName()):
                self.countryCat[i].setArea(area)
                success = True
                return success

    # setter method setContinentOfCountry sets continent given a country's name
    def setContinentOfCountry(self,country, continent):
        success = False
        for i in range(len(self.countryCat)):
            if country == (self.countryCat[i].getName()):
                self.countryCat[i].setContinent(continent)
                success = True
                return success

    # method findCountry checks if a country exists within countryCat
    def findCountry(self, country):
        for i in range(len(self.countryCat)):
            if self.countryCat[i].getName() == country:
                return self.countryCat[i]
            else:
                pass
        else:
            return None

    # method addCountry adds a country if it does not already exist
    def addCountry(self, name,pop, area, cont):
        one_country = Country(name,pop,area,cont)
        country_names = {}
        for i in range(len(self.countryCat)):
            country_names[self.countryCat[i].getName()] = self.countryCat[i].getName()

        if name in country_names:
            return False
        else:
            self.countryCat.append(one_country)
            self.countryCat_dict[name] = [cont]
            return True

    # method printCountryCatalogue
    def printCountryCatalogue(self):
        for country in self.countryCat:
            print(country)

    # method saveCountryCatalogue saves data on countries to a file
    def saveCountryCatalogue(self, fname):
        try:
           filename = open(fname, "w")
           country_list = []
           for i in range(len(self.countryCat)):
               country_list.append(self.countryCat[i].getName())
           sorted_countryCat = sorted(country_list)
           filename.write("Country|Continent|Population|Area\n")
           for i in range(len(self.countryCat)):
               for j in range(len(sorted_countryCat)):
                   if self.countryCat[j].getName() == sorted_countryCat[i]:
                        line = str(self.countryCat[j].getName()) + "|" + str(self.countryCat[j].getContinent()) + "|" + str(self.countryCat[j].getPopulation()) + "|" + str(self.countryCat[j].getArea()) + "\n"
                        filename.write(line)
        except FileNotFoundError:
            return -1