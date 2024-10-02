#!/usr/bin/env python3


# UPCOMING UPDATES: Create an option to fetch data from another city... by changing the default city -d option.
# Convert this code into a cpp code.
# Some Code improvement

import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from colorama import Fore


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
    #print(prayer_times)

    for row in prayer_times:
            #print(prayer_times[5])
            prayer_name = row.find('strong').text.strip()  # Extract the prayer name
            prayer_time_str = row.find_all('td')[1].text.strip()  # Extract the prayer time
            
            # Add one hour, because the site is an hour late due to Daylight saving time
            prayer_time = datetime.strptime(prayer_time_str, '%I:%M %p') + timedelta(hours=1)
            prayer_time_str = prayer_time.strftime('%I:%M %p')  
            
            #condition for option l
            last_prayer = 'Fajr'
            
            #OPTION a
            if option == "a":
                if 'active' in row.get('class', []):
                    print(f"{prayer_name:<10} {Fore.GREEN}{prayer_time_str:<10}{Fore.WHITE} {Fore.RED}(ACTIVE){Fore.WHITE}") 
                else:
                    print(f"{prayer_name:<10} {Fore.GREEN}{prayer_time_str:<10}{Fore.WHITE}")
                    
            #OPTION n
            if option == "n":
                #print("n")
                now = datetime.now()
                time_left = prayer_time - now
                
                if 'active' in row.get('class', []):
                    hours_left = time_left.seconds // 3600
                    minutes_left = (time_left.seconds % 3600) // 60
                    seconds_left = time_left.seconds % 60
                    print(f"{prayer_name:<10} {Fore.GREEN}{prayer_time_str:<10}{Fore.WHITE} Time left: {Fore.YELLOW}{hours_left}h {minutes_left}m {seconds_left}s{Fore.WHITE}")
                    
            #OPTION l
            if option == "l":
            
                if last_prayer == 'Fajr' and 'active' in row.get('class',[]):
                    prayer_name = prayer_times[5].find('strong').text.strip()  # Extract the prayer name
                    prayer_time_str = prayer_times[5].find_all('td')[1].text.strip()  # Extract the prayer time
                    
                    # Add one hour, because the site is an hour late due to Daylight saving time
                    prayer_time = datetime.strptime(prayer_time_str, '%I:%M %p') + timedelta(hours=1)
                    prayer_time_str = prayer_time.strftime('%I:%M %p')  
                    
                    now = datetime.now()
                    time_ellapsed = now - prayer_time
                    hours_ellapsed = time_ellapsed.seconds // 3600
                    minutes_ellapsed = (time_ellapsed.seconds % 3600) // 60
                    seconds_ellapsed = time_ellapsed.seconds % 60
                    print(f"{prayer_name} was {Fore.YELLOW}{hours_ellapsed}h {minutes_ellapsed}m {seconds_ellapsed}s{Fore.WHITE} ago")
                    
                    break
                            
                             
                elif 'active' in row.get('class', []):
                    now = datetime.now()
                    time_ellapsed = now - last_time
                    hours_ellapsed = time_ellapsed.seconds // 3600
                    minutes_ellapsed = (time_ellapsed.seconds % 3600) // 60
                    seconds_ellapsed = time_ellapsed.seconds % 60
                    print(f"{last_prayer} was {Fore.YELLOW}{hours_ellapsed}h {minutes_ellapsed}m {seconds_ellapsed}s{Fore.WHITE} ago")
                    
                    #print("pass")
                last_prayer = prayer_name
                last_time = prayer_time
                


                
                    
                    
            
def main():
    		
    parser = argparse.ArgumentParser(description="A script that shows Prayer Times in Cairo")

	# Define options
    parser.add_argument('-a', '--all', action='store_true', help="All Prayer Times Data")
    parser.add_argument('-n', '--next', action='store_true', help="Next Prayer Times")
    parser.add_argument('-l', '--last', action='store_true', help="Last Prayer Times")



    args = parser.parse_args()
    
    
   
    # Options 
    if args.all:
        pp("a")
        print('-----------------')
        pp("n")
        print('-----------------')
        pp("l")
        
    if args.next:
        pp("n")
    
    if args.last:
        pp("l")
        
    if not args.all and not args.next and not args.last:
        pp("a")
        
        
if __name__ == "__main__":
        main()
        
        
        
        
        