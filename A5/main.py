'''
Name:           Garrett Dodd
Title:          Assignment 5
Due Date:       9/7/2022
Description:    Using a dataset, made a table and made a menu to choose the function that runs. Options 
                are print data, sort, print a column, print a row, and quit

'''
import csv

rank=[]
airport=[]
code=[]
location=[]
country=[]
passengers=[]
# Rank,Airport,Code,Location,Country,Passengers

def menu():
    choice = int(input('Hello, please select an option from below: \n\t1. Print data\n\t2. Sort Data\n\t3. Print Specific Column\n\t4. Print Specific Row\n\t5. See Each Airport by Country of Choice\n\t6. Quit\n\t'))
    if choice == 1:
        printFile()
        return True
    if choice == 2:
        sortSpecific()
        return True
    if choice == 3:
        printColumn()
        return True
    if choice == 4:
        printRow()
        return True
    if choice == 5:
        perCountry()
        return True
    else:
        return False

def selectionSort(main, others):
    for ind in range(len(main)):
        min_index = ind

        for j in range(ind + 1, len(main)):
            # select the minimum element in every iteration
            if main[j] < main[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (main[ind], main[min_index]) = (main[min_index], main[ind])
        for i in range(len(others)):
            (others[i][ind], others[i][min_index]) = (others[i][min_index], others[i][ind])

def selectionSortPassengers(main, others):
    for ind in range(len(main)):
        min_index = ind

        for j in range(ind + 1, len(main)):
            # select the minimum element in every iteration
            if main[j] > main[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (main[ind], main[min_index]) = (main[min_index], main[ind])
        for i in range(len(others)):
            (others[i][ind], others[i][min_index]) = (others[i][min_index], others[i][ind])

def sortSpecific():
    arg = int(input('What would you like to sort by? \n\t1. Name\n\t2. Rank\n\t3. Location\n\t4. Country\n\t5. Code\n\t6. Passengers\n\t'))
    if arg == 1:
        selectionSort(airport, [rank, code, location, country, passengers])
    if arg == 2:
        selectionSort(rank, [airport, code, location, country, passengers])
    if arg == 3:
        selectionSort(location, [rank, code, airport, country, passengers])
    if arg == 4: 
        selectionSort(country, [rank, code, location, airport, passengers])
    if arg == 5:
        selectionSort(code, [rank, airport, location, country, passengers])
    if arg == 6:
        selectionSortPassengers(passengers, [rank, code, location, country, airport])
    arg = input('Would you like to print the sorted data? (Y/N) ')
    if arg.capitalize() == 'Y':
        printFile()
    else:
        pass

def printColumnHelper(arg):
    print('\n')
    for i in range(len(rank)):
        print(arg[i])
    print('\n')

def printColumn():
    arg = int(input('What would you like to print? \n\t1. Name\n\t2. Rank\n\t3. Location\n\t4. Country\n\t5. Code\n\t6. Passengers\n\t'))
    if arg == 1:
        printColumnHelper(airport)
    if arg == 2:
        printColumnHelper(rank)
    if arg == 3:
        printColumnHelper(location)
    if arg == 4: 
        printColumnHelper(country)
    if arg == 5:
        printColumnHelper(code)
    if arg == 6:
        printColumnHelper(passengers)

def printRow():
    i = int(input('Which row index would you like to print? '))
    print("%-50s"%'Airport', "%-5s"%'Rank ' "%-17s"%' Location', "%-20s"%'Country',  "%-3s"%'Code', "%-9s"%'Passengers')
    print('-'*111)
    print("%-50s"%airport[i], "%-5s"%rank[i], "%-17s"%location[i], "%-20s"%country[i],  "%-3s"%code[i], "%-9s"%{passengers[i]})

def parse(file):
    with open(file, 'r') as f:
        for line in f:
            x=line.split(",")
            rank.append(x[0])
            airport.append(x[1])
            code.append(x[2])
            location.append(x[3])
            country.append(x[4])
            passengers.append(int((x[5])))
                
def printFile():
    print("%-50s"%'Airport', "%-5s"%'Rank ' "%-17s"%' Location', "%-20s"%'Country',  "%-3s"%'Code', "%-9s"%'Passengers')
    print('-'*111)
    for i in range(len(rank)):
        print("%-50s"%airport[i], "%-5s"%rank[i], "%-17s"%location[i], "%-20s"%country[i],  "%-3s"%code[i], "%-9s"%{passengers[i]})

def main():
    file = 'airport.csv'
    parse(file)
    # printFile()
    x = True
    while x == True:
        x = menu()
    print('Goodbye')

def perCountry():
    arg = input('Which country would you like to see? ')
    temp=[]
    for i in range(len(airport)):
        if country[i].capitalize() == arg.capitalize():
            temp.append(i)
    if len(temp) > 0:
        print("%-50s"%'Airport', "%-5s"%'Rank ' "%-17s"%' Location', "%-20s"%'Country',  "%-3s"%'Code', "%-9s"%'Passengers')
        print('-'*111)
        for i in range(len(temp)):
            print("%-50s"%airport[temp[i]], "%-5s"%rank[temp[i]], "%-17s"%location[temp[i]], "%-20s"%country[temp[i]],  "%-3s"%code[temp[i]], "%-9s"%{passengers[temp[i]]})
    else:
        print(f'No airports in {arg}\n\n')


main()