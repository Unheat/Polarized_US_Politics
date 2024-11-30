"""
A program that analyzes voting data for a vote of the student's choosing 
to determine if it was a party-line vote. It uses functions from `utilities.py`
to fetch, process, and analyze the voting data.

Functions:
    isMyChoicePolarized(): Fetches voting data for a specific vote, analyzes it, and determines if it was a party-line vote.
    main(): A simple test driver for isMyChoicePolarized.

Authors: <your name>
Date Created: <date>
"""

# Import required utility functions from utilities.py
from utilities import getVoteFileFromWeb, isPartyLine, countVotesByParty

def isMyChoicePolarized():
    """
    Fetches and analyzes voting data for a specific vote to determine 
    if it was a party-line vote.
    
    Steps:
    1. Fetch voting data from the web using `getVoteFileFromWeb`.
    2. Count votes by party using `countVotesByParty`.
    3. Determine party-line alignment using `isPartyLine`.

    Returns:
        bool: True if the vote was along party lines, False otherwise.
    """
    # Fetch voting data from the specified URL
    line_list = getVoteFileFromWeb("https://clerk.house.gov/cgi-bin/vote.asp?year=2024&rollnumber=473")
    # Count votes by party
    count = countVotesByParty(line_list)
    print(count)  # Print the vote count for debugging and verification.
    
    # Determine if the voting was along party lines
    return isPartyLine(count[0], count[1], count[2], count[3])

def main():
    """
    Main function for testing the isMyChoicePolarized function.
    Prints the result of whether the selected vote was a party-line vote.
    """
    print(isMyChoicePolarized())  # Test and print the result.

if __name__ == "__main__":
    main()
