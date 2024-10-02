#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def fetch_Prayer_Times():
    url = "https://timesprayer.com/en/prayer-times-in-cairo.html"
    try:
            response = requests.get(url)
            response.raise_for_status() #Raises an error for bad responses (4xx & 5xx)
    except requests.exceptions.RequestException as e:
            print(f"Error Fetching Data: {e}")
            return None
            
    soup = BeautifulSoup(response.text, 'html.parser')
    #print (soup)
    #Prayers = soup.findAll("tr", attrs={"class":"active"})

    table_body = soup.find('tbody')

    # Find all rows (<tr>)
    rows = table_body.find_all('tr')
    
    return rows
        
    

def main():
        # Create the parser  
		
    parser = argparse.ArgumentParser(description="A script that shows Prayer Times in Cairo")

	# Define options
    parser.add_argument('-a', '--all', action='store_true', help="All Prayer Times")
    parser.add_argument('-n', '--next', action='store_true', help="Next Prayer Times")
    parser.add_argument('-l', '--last', action='store_true', help="Last Prayer Times")



    args = parser.parse_args()
    
    prayer_times = fetch_Prayer_Times()
    
    if prayer_times is None:
        return

    if args.all:
        for row in prayer_times:
            prayer_name = row.find('strong').text.strip()  # Extract the prayer name
            prayer_time_str = row.find_all('td')[1].text.strip()  # Extract the prayer time
            
            # Parse the prayer time and add one hour
            prayer_time = datetime.strptime(prayer_time_str, '%I:%M %p') + timedelta(hours=1)
            prayer_time_str = prayer_time.strftime('%I:%M %p')  # Convert back to string
            
            # Check if the row has the 'active' class
            if 'active' in row.get('class', []):
                print(f"{prayer_name:<10} {prayer_time_str:<10} (ACTIVE)")  # Print active prayer with formatting
            else:
                print(f"{prayer_name:<10} {prayer_time_str:<10}")  # Print normal prayer with formatting

        
    if args.next:
        print("Fajr in #mintes")
    if args.last:
        print("Ishaa call was #mintes ago")
    if not args.all and not args.next and not args.last:
        print("No options Provided")
        
        
if __name__ == "__main__":
        main()
        
        
        
        
        
        #UPCOMING UPDATES: Create an option to fetch data from another city... by changing the default city -d option.