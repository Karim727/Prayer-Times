#!/usr/bin/env python3

import argparse

def main():
        # Create the parser  
		
    parser = argparse.ArgumentParser(description="A script that shows Prayer Times in Cairo")

	# Define options
    parser.add_argument('-a', '--all', action='store_true', help="All Prayer Times")
    parser.add_argument('-n', '--next', action='store_true', help="Next Prayer Times")
    parser.add_argument('-l', '--last', action='store_true', help="Last Prayer Times")



	# Parse the arguments
    args = parser.parse_args()

	# Access the arguments
    if args.all:
        print("all")
    if args.next:
        print("Fajr in #mintes")
    if args.last:
        print("Ishaa call was #mintes ago")
    if not args.all and not args.next and not args.last:
        print("No options Provided")
        
        
if __name__ == "__main__":
        main()
        
        
        
        
        
        #UPCOMING UPDATES: Create an option to fetch data from another city... by changing the default city -d option.