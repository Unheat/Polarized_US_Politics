"""
A collection of utility functions to analyze Congressional voting data. 
The utilities include functions to count votes by party, determine if a vote 
was a party-line vote, and fetch voting data from a web source.

Functions:
    countVotesByParty(lines): Counts "yes" and "no" votes by Democrats and Republicans.
    isPartyLine(demYes, demNo, repYes, repNo): Determines if a vote was a party-line vote.
    getVoteFileFromWeb(url): Fetches voting data from a given URL and returns the lines.

Authors: <Your Name>
Date Created: <Date>
"""

import urllib.request as web

# List of all valid state abbreviations
STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

def countVotesByParty(lines):
    """
    Counts the number of "yes" and "no" votes by Democrats and Republicans.

    Args:
        lines (list): A list of strings where each string represents a line of voting data.

    Returns:
        list: A list containing vote counts in the following order:
              [Democrats_yes, Democrats_no, Republicans_yes, Republicans_no]
    """
    Democrats_yes = 0
    Democrats_no = 0
    Republicans_yes = 0
    Republicans_no = 0

    for line in lines:
        # Count votes for Democrats
        if 'party="D"' in line:
            if "Yea" in line or "Aye" in line:
                Democrats_yes += 1
            elif "Nay" in line or "vote>No<" in line:  # Ensure it's a "No" vote, not "Not voting"
                Democrats_no += 1

        # Count votes for Republicans
        elif 'party="R"' in line:
            if "Yea" in line or "Aye" in line:
                Republicans_yes += 1
            elif "Nay" in line or "vote>No<" in line:
                Republicans_no += 1

    return [Democrats_yes, Democrats_no, Republicans_yes, Republicans_no]

def isPartyLine(demYes, demNo, repYes, repNo):
    """
    Determines whether a vote was a party-line vote.

    A vote is considered party-line if:
    - A majority of Democrats vote "yes" while a majority of Republicans vote "no".
    - OR, a majority of Democrats vote "no" while a majority of Republicans vote "yes".

    Args:
        demYes (int): Number of "yes" votes by Democrats.
        demNo (int): Number of "no" votes by Democrats.
        repYes (int): Number of "yes" votes by Republicans.
        repNo (int): Number of "no" votes by Republicans.

    Returns:
        bool: True if the vote was along party lines, False otherwise.
    """
    # Check if Democrats voted "yes" while Republicans voted "no"
    if demYes > (demYes + demNo) / 2 and repNo > (repYes + repNo) / 2:
        return True
    # Check if Democrats voted "no" while Republicans voted "yes"
    if demNo > (demYes + demNo) / 2 and repYes > (repYes + repNo) / 2:
        return True
    return False

def getVoteFileFromWeb(url):
    """
    Fetches a temporary copy of a voting record file from the given URL.

    The function downloads the file, decodes its contents, and returns a list of lines.

    Args:
        url (str): The URL from which to download the voting data. 
                   Example format: "https://clerk.house.gov/cgi-bin/vote.asp?year=<YEAR>&rollnumber=<NUMBER>"

    Returns:
        list: A list of strings, where each string represents a line of voting data.
    """
    # Open the URL to read the voting data
    webpage = web.urlopen(url)
    # Decode the lines from the response and strip unnecessary characters
    decodedLines = [line.decode('utf-8').rstrip() for line in webpage]
    webpage.close()  # Close the web resource
    return decodedLines
