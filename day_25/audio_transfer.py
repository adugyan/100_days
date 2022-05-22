"""
    File   : quick code whip up n' things
    Authors : Kofi Adu-Gyan
    Date   : 18 May, 2022
=============================================================================

    Some laissez faire notes. Right now the script will be run manually and will take 
    the tester's name to append to the data. I don't know what system you all use for CI/CD but your Devops guy
    will know how to set up a Jenkins/Gitlab/'whatever you all use' job to run everytime a new audio data file is generated.


    Requires: Python 3.6 or later
"""
from csv import reader, writer 
from time import asctime

# Use a block like this to capture in data even if there's more than one list per .txt file
# audio_input is a short example of what I assume your .txt file is like. Yours will be named whatever you want
rows = [] 
with open('audio_input.txt', newline='') as inputfile:
    for row in reader(inputfile):
        rows.append(row)

# Add identifying positions to the row. This can be automatic, your devops guy will know what to do depending on what system you all use
tester = input('Enter the testers name here: ')


# audio_events is the excel file I'm generating. If the file name already exists it will add new information to the file
with open('audio_events.csv', 'a', newline='') as audio_file:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(audio_file)

    # storing current date and time
    current_date_time = asctime()

    # Iterating over all the data in the rows
    # variable
    for val in rows:
        # Inserting the date and time at 0th
        # index
        val.insert(0, current_date_time)
        val.insert(0, tester)

        # writing the data in csv file
        writer_object.writerow(val)


