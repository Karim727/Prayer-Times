#!/usr/bin/env python3


#UPCOMING UPDATES: Create an option to fetch data from another city... by changing the default city -d option.

import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Fetching the Prayer times from a website.
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

    table_body = soup.find('tbody')

    # Find all rows (<tr>)
    rows = table_body.find_all('tr')
    
    return rows
        
def pp(option):
    
    
    prayer_times = fetch_Prayer_Times()
    for row in prayer_times:
            prayer_name = row.find('strong').text.strip()  # Extract the prayer name
            prayer_time_str = row.find_all('td')[1].text.strip()  # Extract the prayer time
            
            # Add one hour, because the site is an hour late due to Daylight saving time
            prayer_time = datetime.strptime(prayer_time_str, '%I:%M %p') + timedelta(hours=1)
            prayer_time_str = prayer_time.strftime('%I:%M %p')  
            
            
            #OPTION A
            if option == "a":
                if 'active' in row.get('class', []):
                    print(f"{prayer_name:<10} {prayer_time_str:<10} (ACTIVE)") 
                else:
                    print(f"{prayer_name:<10} {prayer_time_str:<10}")
                    
            #OPTION N
            if option == "n":
                #print("n")
                now = datetime.now()
                time_left = prayer_time - now
                
                if 'active' in row.get('class', []):
                    hours_left = time_left.seconds // 3600
                    minutes_left = (time_left.seconds % 3600) // 60
                    seconds_left = time_left.seconds % 60
                    print(f"{prayer_name:<10} {prayer_time_str:<10} Time left: {hours_left}h {minutes_left}m {seconds_left}s")
            #OPTION L
            if option == "l":
                return
                
                    
        

def main():
    		
    parser = argparse.ArgumentParser(description="A script that shows Prayer Times in Cairo")

	# Define options
    parser.add_argument('-a', '--all', action='store_true', help="All Prayer Times")
    parser.add_argument('-n', '--next', action='store_true', help="Next Prayer Times")
    parser.add_argument('-l', '--last', action='store_true', help="Last Prayer Times")



    args = parser.parse_args()
    
    
   
    # Options 
    if args.all:
        pp("a")
        
    if args.next:
        pp("n")
    
    if args.last:
        pp("l")
        
    if not args.all and not args.next and not args.last:
        print("No options Provided")
        
        
if __name__ == "__main__":
        main()
        
        
        
        
        