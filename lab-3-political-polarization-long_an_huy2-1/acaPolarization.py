"""
A program that analyzes voting data to determine whether the Affordable Care Act (ACA)
was a party-line vote or not. It utilizes functions from `utilities.py` to process 
voting data and compute party alignment.

Functions:
    isACAPolarized(filename): Reads and returns the lines from a voting data file.
    main(): Coordinates the process to analyze voting data for party-line behavior.

Authors: <An_Long_Huy>
"""

# Import required utility functions from utilities.py
from utilities import countVotesByParty, isPartyLine

def isACAPolarized(filename):
    """
    Reads the voting data file and returns the list of lines.
    
    Args:
        filename (str): The name of the file containing voting data.
    
    Returns:
        list: A list of lines from the file.
    """
    file = open(filename, "r")  # Open the file in read mode.
    lines = file.readlines()  # Read all lines from the file.
    file.close()  # Close the file after reading.
    return lines

def main():
    """
    Main function to analyze whether the Affordable Care Act was a party-line vote.
    It reads voting data, counts votes by party, and checks party-line alignment.
    
    Process:
    1. Reads the voting data from the ACA file.
    2. Counts votes for and against by party using `countVotesByParty`.
    3. Determines if the voting was along party lines using `isPartyLine`.
    4. Prints the results.
    """
    lines_list = isACAPolarized("aca.xml")  # Read the voting data file.
    a = countVotesByParty(lines_list)  # Count votes by party.
    print(a)  # Print the vote counts.
    print(isPartyLine(a[0], a[1], a[2], a[3]))  # Check and print if voting was along party lines.

if __name__ == "__main__":
    main()
