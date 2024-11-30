"""
A program that analyzes and plots the number of members of the House of Representatives 
from each party (Democratic or Republican) in a given state from 2003 to 2023 (inclusive). 
The program fetches voting data, processes it, and visualizes the changes in party representation.

Functions:
    count_representative(state, line_list): Counts Democratic and Republican representatives for a state.
    stateDivide(state): Fetches and visualizes party representation data for a given state.

Authors: <your name>
Date Created: <date>
"""

# Import necessary libraries and utility functions
from matplotlib import pyplot as plt
from utilities import getVoteFileFromWeb

def count_representative(state, line_list):
    """
    Counts the number of Democratic and Republican representatives for a given state.
    
    Args:
        state (str): The two-letter abbreviation of the state.
        line_list (list): List of lines containing voting data.
    
    Returns:
        tuple: A tuple containing the count of Democratic representatives (int) 
               and Republican representatives (int).
    """
    dem = 0  # Counter for Democrats
    rep = 0  # Counter for Republicans
    
    # Iterate through each line of the voting data
    for line in line_list:
        # Check if the line corresponds to the given state
        if f'state="{state}"' in line:
            # Count Democrats
            if 'party="D"' in line:
                dem += 1
            # Count Republicans
            elif 'party="R"' in line:
                rep += 1
    return dem, rep

def stateDivide(state):
    """
    Plots the changes in Democratic and Republican representation in the House 
    of Representatives for a given state from 2003 to 2023.

    Args:
        state (str): Two-letter abbreviation of the state (e.g., "OH" for Ohio).

    Raises:
        AssertionError: If the provided state abbreviation is invalid.
    """
    # List of valid state abbreviations
    STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
              "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
              "VA", "WA", "WV", "WI", "WY"]
    assert state in STATES, f"Invalid state abbreviation: {state}"

    # Define the years for analysis
    years = range(2003, 2024)  # 2003 to 2023
    dem_counts = []  # List to store Democratic counts
    rep_counts = []  # List to store Republican counts

    # Fetch and process data for each year
    for year in years:
        # URL for the first roll call vote of the year
        url = f"https://clerk.house.gov/cgi-bin/vote.asp?year={year}&rollnumber=1"
        line_list = getVoteFileFromWeb(url)  # Fetch data
        dem, rep = count_representative(state, line_list)  # Count party representatives
        dem_counts.append(dem)
        rep_counts.append(rep)

    # Plot the data
    plt.plot(years, dem_counts, label="Democrats", marker='o', linestyle='-')
    plt.plot(years, rep_counts, label="Republicans", marker='o', linestyle='-')
    plt.title(f"Party Representation in {state} (2003–2023)")
    plt.xlabel("Year")
    plt.ylabel("Number of Representatives")
    plt.legend()
    plt.grid(True)
    plt.show()  # Display the plot

# Example function call for Ohio
stateDivide("OH")
