
# U.S. House of Representatives Polarization Analysis

## Project Overview

This project is a data analysis project for CS109 that explores political polarization in the U.S. House of Representatives by analyzing roll call votes from 2004 to 2023. The goal is to computationally investigate how party-line voting has changed over time and understand political divisions across different states.

## Learning Objectives

- Read and parse XML data from roll call votes
- Use string manipulation and conditional logic to analyze voting patterns
- Visualize political trends using Python data analysis and plotting libraries
- Critically examine political polarization through a data-driven approach

## Key Components

### Part 1: Party Line Vote Analysis
- Develop functions to:
  - Count votes by party from XML vote records
  - Determine if a vote is a "party-line" vote
  - Analyze the Affordable Care Act vote
  - Explore polarization trends across 20 years (2004-2023)

### Part 2: State Representative Distribution
- Create a function to visualize the number of Democratic and Republican representatives in a specific state over time

## Key Functions

1. `countVotesByParty(lines)`: Counts votes by party from XML vote data
2. `isPartyLine(demYes, demNo, repYes, repNo)`: Determines if a vote follows party lines
3. `countPartyLine(year, maxNumber)`: Calculates the fraction of party-line votes in a given year
4. `plotPartyLine()`: Generates a plot showing party-line voting trends
5. `stateDivide(state)`: Plots representative party distribution for a specific state

## Project Requirements

### Data Sources
- Roll call vote data from: https://clerk.house.gov/Votes
- Congress vote records: https://www.congress.gov/roll-call-votes

### Technical Requirements
- Python programming
- XML parsing
- Data visualization
- Web data retrieval

## Deliverables

- Comprehensive Python scripts
- Visualization plots
- Detailed project writeup including:
  - Analysis of findings
  - Ethical reflections
  - Personal project insights
  - Contribution statements

## Ethical Considerations

The project encourages students to reflect on:
- Potential positive and negative uses of political data analysis
- Responsible data interpretation
- Media representation of political polarization

## Getting Started

1. Clone the repository
2. Install required Python libraries
3. Run individual analysis scripts
4. Generate visualizations and reports


