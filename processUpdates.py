# Name: Jawaad Ahmar
# Student#: 251237757
# UWO email: jahmar@uwo.ca



# this program processes updates and updates data on countries



# import class CountryCatalogue
from catalogue import CountryCatalogue

# import class Country
from country import Country


# function takes 3 parameters, data.txt, upd.txt, bad updates
# function will process updates in upd.txt and update data.txt
# function will output updates records into a file called output.txt
# invalid records will be written to badUpdateFile
def processUpdates(cntryFileName, updateFileName, badUpdateFile):

    # make file names global
    # make CountryCatalogue object process_data global
    global country_FileName, update_FileName, process_data

    # make while loop booleans global
    global terminate1, terminate2


    # try and open files that are prompted for in main.py
    try:
        cntryFileName = open(cntryFileName, "r")
        terminate1 = False
        updateFileName = open(updateFileName, "r")
        terminate2 = False
    except FileNotFoundError:
        terminate1 = True
        terminate2 = True
        user_quit = input("Do you want to quit? \"Y\" (yes) or \"N\" (no): ")
        if user_quit.lower() == "n":
            pass
        elif user_quit.lower() != "n":
            outfile = open("output.txt", "w")
            outfile.write("Update Unsuccessful\n")
            exit()
            return False, None

    # if try loop above fails, this while loop is activated, prompts user until country file is valid or user quits
    while terminate1 == True:
        cntryFileName = input("Enter a valid name of a file with country data: ")
        try:
            cntryFileName = open(cntryFileName,"r")
            terminate1 = False
            break
        except FileNotFoundError:
            user_quit = input("Do you want to quit? \"Y\" (yes) or \"N\" (no): ")
            if user_quit.lower() == "n":
                continue
            elif user_quit.lower() != "n":
                outfile = open("output.txt", "w")
                outfile.write("Update Unsuccessful\n")
                exit()
                return False,None

    # if while loop above breaks, this one is is activated, prompts user until update file is valid or user quits
    while terminate2 == True:
        updateFileName = input("Enter a valid name of a file with country updates: ")
        try:
            updateFileName = open(updateFileName, "r")
            terminate2 = False
            break
        except FileNotFoundError:
            user_quit = input("Do you want to quit? \"Y\" (yes) or \"N\" (no): ")
            if user_quit.lower() == "n":
                continue
            elif user_quit.lower() != "n":
                outfile = open("output.txt", "w")
                outfile.write("Update Unsuccessful\n")
                exit()
                return False,None


    # create object of CountryCatalogue
    process_data = CountryCatalogue(cntryFileName)


    # make bad_updates dictionary global so it can be accessed within other functions
    global bad_updates
    # bad_updates dictionary holds all invalid updates
    bad_updates = {}

    # all_updates holds all updates from update file
    all_updates = {}

    # for loop iterates through update file, manipulates line and appends updates to dictionaries
    for update in updateFileName:
        update_line = update.split(";")

        update_line[-1] = update_line[-1].rstrip("\n")
        update_countryName = update_line[0]

        if len(update_countryName) == 0 or len(update_line[1:]) == 0:
            bad_updates.update(dict({update_line[0]:update_line[1:]}))

        if len(update_countryName) != 0 and len(update_line[1:]) != 0:
            all_updates.update(dict({update_countryName: update_line[1:]}))


    # population_updates holds population updates
    population_updates = {}

    # area_updates holds area updates
    area_updates = {}

    # cont_updates holds continent updates
    cont_updates = {}


    # for loop iterates through all the updates
    # filters out bad updates
    # organizes updates by type
    for name, updates in all_updates.items():

        # for loop iterates through individual updates
        for update in updates:

            # if statements updates population updates
            if "P=" in update:
                P_pos = update.find("P=")
                new_pop = (update[P_pos+2:])
                if validPopulation(new_pop) == True:
                    if name in population_updates:
                        population_updates.pop(name,update)
                        bad_updates.update(dict({name: updates}))
                    if name in bad_updates:
                        population_updates.pop(name, update)
                        bad_updates.update(dict({name: updates}))
                    else:
                        population_updates.update(dict({name: new_pop}))
                else:
                    bad_updates.update(dict({name: updates}))

            # if statements updates area updates
            if "A=" in update:
                A_pos = update.find("A=")
                new_area = (update[A_pos+2:])
                if validArea(new_area) == True:
                    if name in area_updates:
                        area_updates.pop(name,update)
                        bad_updates.update(dict({name: updates}))
                    # start here, append if in bad updates
                    if name in bad_updates:
                        area_updates.pop(name,update)
                        bad_updates.update(dict({name: updates}))
                    else:
                        area_updates.update(dict({name: new_area}))
                else:
                    bad_updates.update(dict({name: updates}))

            # if statements updates continent updates
            if "C=" in update:
                C_pos = update.find("C=")
                new_cont = (update[C_pos+2:])
                if validContinent(new_cont) == True:
                    if name in cont_updates:
                        cont_updates.pop(name,update)
                        bad_updates.update(dict({name: updates}))
                    if name in bad_updates:
                        cont_updates.pop(name,update)
                        bad_updates.update(dict({name: updates}))
                    else:
                        cont_updates.update(dict({name: new_cont}))
                else:
                    bad_updates.update(dict({name: updates}))

            # if statement updates bad updates, if there are no updates
            if "P=" not in update and "A=" not in update and "C=" not in update:
                bad_updates.update(dict({name: updates}))


    # pass update dictionaries through remove_space function
    # removes unnecessary spaces
    population_updates = remove_spaces(population_updates)
    area_updates = remove_spaces(area_updates)
    cont_updates = remove_spaces(cont_updates)

    # pass update dictionaries through validCountry function
    # to check if country name is valid
    population_updates = validCountry(population_updates)
    area_updates = validCountry(area_updates)
    cont_updates = validCountry(cont_updates)


    # merge together all dictionaries so we can use addCountry method from CountryCatalogue

    # allValid_updates holds all valid updates
    allValid_updates = {}

    # for loop iterates through population_updates
    # appends update to allValid_updates
    for name,update in population_updates.items():
        if name in allValid_updates:
            allValid_updates[name][0] = update
        else:
            allValid_updates[name] = [update,None,None]

    # for loop iterates through area_updates
    # appends update to allValid_updates
    for name,update in area_updates.items():
        if name in allValid_updates:
            allValid_updates[name][1] = update
        else:
            allValid_updates[name] = [None,update,None]

    # for loop iterates through cont_updates
    # appends update to allValid_updates
    for name,update in cont_updates.items():
        if name in allValid_updates:
            allValid_updates[name][2] = update
        else:
            allValid_updates[name] = [None,None,update]


    # for loop iterates through population_updates
    # updates population if country exists
    for name,update in population_updates.items():
        if process_data.findCountry(name) != None:
            process_data.setPopulationOfCountry(name,update)

    # for loop iterates through area_updates
    # updates area if country exists
    for name,update in area_updates.items():
        if process_data.findCountry(name) != None:
            process_data.setAreaOfCountry(name,update)

    # for loop iterates through cont_updates
    # updates continent if country exists
    for name,update in cont_updates.items():
        if process_data.findCountry(name) != None:
            process_data.setContinentOfCountry(name,update)

    # for loop iterates through allValid_updates
    # adds new country with updates if it does not exist
    for country,values in allValid_updates.items():
        if process_data.findCountry(country) == None:
            process_data.addCountry(country,values[0],values[1],values[2])


    # object process_data uses method saveCountryCatalogue from class CountryCatalogue
    # saves data on updated countries to output.txt
    process_data.saveCountryCatalogue("output.txt")


    # opens badUpdate_File from main.py
    badUpdate_FileName = open(badUpdateFile, "w")

    # for loop iterates through bad_updates dictionary
    # writes bad updates to badUpdate_FileName file
    for country, badUpdate in bad_updates.items():
        line = str(country) + "|" + str(badUpdate) + "\n"
        badUpdate_FileName.write(line)



    # processUpdates function returns True, with object process_data
    return True, process_data




# function validContintent checks if continent is valid
def validContinent(cont):
    continents = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]
    if type(cont) == str:
        if cont in continents:
            return True
        else:
            return False
    else:
        return False


# function validCountry checks if country name is valid
def validCountry(update_type):
    new_update_type = {}
    for name, update in update_type.items():
        if type(name) == str:
            if "=" in str(name) or " " in str(name):
                bad_updates.update(dict({name: update}))
            else:
                if str(name[0]) != str(name[0]).upper():
                    bad_updates.update(dict({name: update}))

                Name_pos = name.find("_")
                if "_" in str(name):
                    if str(name[Name_pos+1]) != str(name[Name_pos+1]).upper():
                        bad_updates.update(dict({name: update}))

                if len(name) == 0:
                    bad_updates.update(dict({name: update}))
                else:
                    new_update_type.update(dict({name: update}))
        else:
            bad_updates.update(dict({name: update}))

    return new_update_type


# function validPopulation checks if population is valid
def validPopulation(pop):
    if type(pop) == str:
        components = pop.split(",")
        for i in components:
            if len(i) == 1 or len(i) == 2 or len(i) == 3:
                return True
            else:

                return False
    else:
        return False


# function validArea checks if area is valid
def validArea(area):
    if type(area) == str:
        components = area.split(",")
        for i in components:
            if len(i) == 1 or len(i) == 2 or len(i) == 3:
                return True
            elif len(i) > 3:
                return False
            else:
                return False
    else:
        return False


# function remove_spaces removes spaces from updates
def remove_spaces(update_type):
    update_type = {key.strip(): item.strip() for key, item in update_type.items()}
    return update_type