"""
A program that analyzes Congressional voting data to compute the fraction of 
votes that were party-line votes for each of the last 20 years (2004–2023). 
The program fetches voting data from the web, processes it, and visualizes 
the results in a line plot.

Functions:
    countPartyLine(year, maxNumber): Computes the fraction of party-line votes 
                                     for a given year.
    plotPartyLine(): Analyzes voting data from 2004 to 2023 and plots the 
                     fraction of party-line votes for each year.
    main(): Calls the plotPartyLine function to execute the analysis and plotting.

Authors: <YOUR NAMES>
Date: <DATE>
"""

# Import required functions and libraries
from utilities import isPartyLine, getVoteFileFromWeb, countVotesByParty
from matplotlib import pyplot as plt

def countPartyLine(year, maxNumber):
    """
    Calculates the fraction of votes that were party-line votes for a given year.
    
    Args:
        year (int): The year for which voting data is analyzed.
        maxNumber (int): The maximum number of roll call votes in the year.
    
    Returns:
        float: The fraction of party-line votes out of the total votes.
    """
    partylines = 0  # Initialize counter for party-line votes
    
    for num in range(1, maxNumber + 1):
        # Construct the URL for fetching voting data
        url = f"https://clerk.house.gov/cgi-bin/vote.asp?year={year}&rollnumber={num}"
        
        # Fetch voting data and process it
        line_list = getVoteFileFromWeb(url)
        count = countVotesByParty(line_list)
        
        # Check if the vote was along party lines
        if isPartyLine(count[0], count[1], count[2], count[3]):
            partylines += 1  # Increment party-line counter if true
    
    # Calculate the fraction of party-line votes
    return partylines / maxNumber

def plotPartyLine():
    """
    Analyzes Congressional voting data for the last 20 years (2004–2023) to compute 
    and plot the fraction of party-line votes for each year. Results are written 
    to a file and visualized using a line plot.
    """
    # Define the years to analyze
    year_list = list(range(2004, 2024))
    fractions = []  # List to store fractions of party-line votes
    
    # Open a file to save results
    file = open("partylines.txt", "w")
    
    # Analyze each year
    for year in year_list: 
        fraction = countPartyLine(year, 450)  # Compute the fraction for the year
        fractions.append(fraction)  # Store the result
        file.write(f"{year}: {fraction:.4f}\n")  # Write to file with 4 decimal precision
        
    # Plot the fractions as a line plot
    plt.plot(year_list, fractions, marker='o', linestyle='-', label="Fraction of Party-Line Votes")
    plt.xlabel("Year")  # X-axis label
    plt.ylabel("Fraction of Party-Line Votes")  # Y-axis label
    plt.title("Fraction of Party-Line Votes (2004-2023)")  # Plot title
    plt.grid(True)  # Enable grid
    plt.legend()  # Add legend
    
    plt.show()  # Display the plot
    
    file.close()  # Close the file

def main():
    """
    Main function to execute the analysis and plotting of party-line vote fractions.
    """
    plotPartyLine()

if __name__ == "__main__":
    main()
