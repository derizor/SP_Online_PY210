#!/usr/bin/env python

"""
The Mailroom assignment part 2.

Part 1 info:
The data is a global list.
Appending donations was repetitive, so was made into its own function 'add_donations()'
A separate data structure (a list of lists) was built from the original data (a list of \
tuples, which contain strings and lists) to facilitate report writing.

Part 2 info:
The original data was converted to a dict, with the strings now as keys and the lists now as \
values.
The separate data structure was converted to a list of dicts, with each dict corresponding to \
a donor.
The letter template already used .format().  Now it pulls data from the dict.
"""

import sys

# This was originally a list of lists.  I changed it based on the recommendation in the notes.
data = dict([('Bob', [17.56]), ('Billy', [500.00, 1000.00]), ('Joe Schmoe', [2.00, 0.03, 45.00]), ('This Guy', [1.00, 100000]), ('That Gal', [9876.54])])

prompt = """\nPlease choose between the following option numbers:
(enter the digit only)
'1' - Send a Thank You
'2' - Create a Report
'3' - Quit
: """

# This was originally a single function called 'Part1()' which called another function to add
# donations.  It worked, but I restructured it based on the recommendation in the notes.
def main():
    while True:
        action = input(prompt)
        if action == '1':
            Send_Thank_You(data)
        elif action == '2':
            Create_a_Report(data)
        elif action == '3':
            Quit_Program()


def Send_Thank_You(data):
    Full_Name = 'list'
    while Full_Name == 'list':  # loop if 'list' is provided
        Full_Name = input("""Please provide a full name (case sensitive).
                          'list will show the list of donor names.
                          'quit' exits script.
                          : """)
        if Full_Name == 'quit':  # exit option, break while loop
            Quit_Program()
        if Full_Name == 'list':
            print('\n\n')
            for name in data:
                print(name)
    if Full_Name not in data:
        data[Full_Name] = []  # Add name to original data, and empty donation list
        data, don_sum = add_donations(Full_Name, data)  # call function to add donation info
    elif Full_Name in data:  # Select name already on list
        data, don_sum = add_donations(Full_Name, data)  # call function to add donation info
    print("\n\nHi {},\n\nThank you for your total donation of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555".format(Full_Name, don_sum))


def Create_a_Report(data):
    key1 = 'Donor Name'
    key2 = '# Gifts'
    key3 = 'Total Given($)'
    key4 = 'Average Gift'
    Report_List = []  # create empty dataset of for reporting, to be populated by dicts
    # start populating dataset in accordance with the original data
    for i, name in enumerate(data):
        num_don = len(data[name])  # number of donations
        Report_List.append({key1: name, key2: num_don})
        sum_individual = 0
        for j in range(len(data[name])):
            sum_individual += data[name][j]  # build sum of donations per individual
        Report_List[i][key3] = sum_individual
        if num_don != 0:
            # determine average donation
            Report_List[i][key4] = sum_individual / num_don
        else:
            Report_List[i][key4] = sum_individual  # prevent division by zero

    def sort_total(val):  # define key for sorting
        return val[key3]
    Report_List.sort(key=sort_total, reverse=True)  # sort by descending sum of donations
    print("\n\n {:^28}|{:^18s}|{:^7s}|{:^18s}".format(key1, key3, key2, key4))
    print("-" * 75)
    for j in range(len(Report_List)):
        print(" {:28s}|{:17,.2f} |{:6d} |{:>18,.2f}".format(Report_List[j][key1], Report_List[j][key3], Report_List[j][key2], Report_List[j][key4]))


def Quit_Program():
    print('\n\ngoodbye\n\n')
    sys.exit()


def add_donations(A_Full_Name, A_data):  # function that adds donation info
    A_donation = ''
    A_don_sum = 0
    while A_donation != 'none':
        # query for amount, with option for no donation or exit parent function
        A_donation = input("""Please provide the donation amount
***(enter 'none' for no additional donation, 'quit' to exit script): """)
        if A_donation == 'quit':
            Quit_Program()
        if A_donation != 'none':
            # add individual donation to original
            A_data[A_Full_Name].append(float(A_donation))
            A_don_sum += float(A_donation)  # keep sum of donations
    return A_data, A_don_sum  # return the updated original data and the sum of donations


if __name__ == "__main__":
    main()


