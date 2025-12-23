# Sports Reference Head-to-Head Matrix Solution

## Overview
This python script takes in a JSON file containing team win-loss records, and generates a readable and formatted head to head matrix table.

## Solution Approach
The script takes nested JSON data where each team has respective win-loss records against specific opponents and creates a square matrix showing the result of the matchups.
Diagonal cells display -- (teams cannot play themselves)

## Key Features
• Identifies each team from JSON keys
• Creates a clean and readable table with proper allignment
• Handles missing matchup data with "N/A" placeholders
• Teams are sorted alphabetically

## How to run
1. Ensure Python 3.x is installed
2. Save JSON data to a file
3. Run the script:
   python head_to_head_mat.py

## Example Output
Given this JSON sample: 
data = {
    'NYY': {'BOS': {'W': 10, 'L': 9}, 'TBR': {'W': 11, 'L': 8}},
    'BOS': {'NYY': {'W': 9, 'L': 10}, 'TBR': {'W': 7, 'L': 12}},
    'TBR': {'NYY': {'W': 8, 'L': 11}, 'BOS': {'W': 12, 'L': 7}}
}
The script will generate a table like this:
   Tm   BOS   NYY   TBR
  BOS    --   9-10  7-12
  NYY  10-9    --  11-8
  TBR  12-7  8-11    --
