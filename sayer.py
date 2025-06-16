#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import argparse
from colorama import init, Fore, Style
from theHarvester.theHarvester import TheHarvester
from spiderfoot import SpiderFootScanner
from ghunt import GHunt
from sherlock import Sherlock

# Initialize colorama
init()

# ASCII Art Banner in blue
banner = f'''{Fore.BLUE}
   _____ _____     _______ _____  
  / ____|  __ \   |__   __|  __ \ 
 | (___ | |__) |     | |  | |__) |
  \___ \|  _  /      | |  |  _  / 
  ____) | | \ \     | |  | | \ \ 
 |_____/|_|  \_\    |_|  |_|  \_\
{Style.RESET_ALL}'''

# Developer info in blue
dev_info = f'''{Fore.BLUE}
Developer: SaudiLinux
Email: SaudiCrackers@gmail.com{Style.RESET_ALL}
'''

class Sayer:
    def __init__(self):
        self.results = {
            'theHarvester': [],
            'spiderfoot': [],
            'ghunt': [],
            'sherlock': []
        }
        
    def run_theHarvester(self, target):
        print(f"\n{Fore.YELLOW}[*] Running theHarvester...{Style.RESET_ALL}")
        harvester = TheHarvester(target)
        self.results['theHarvester'] = harvester.gather_info()
        
    def run_spiderfoot(self, target):
        print(f"\n{Fore.YELLOW}[*] Running SpiderFoot...{Style.RESET_ALL}")
        scanner = SpiderFootScanner()
        self.results['spiderfoot'] = scanner.start_scan(target)
        
    def run_ghunt(self, target):
        print(f"\n{Fore.YELLOW}[*] Running GHunt...{Style.RESET_ALL}")
        hunter = GHunt()
        self.results['ghunt'] = hunter.search(target)
        
    def run_sherlock(self, target):
        print(f"\n{Fore.YELLOW}[*] Running Sherlock...{Style.RESET_ALL}")
        sherlock = Sherlock()
        self.results['sherlock'] = sherlock.search(target)
        
    def save_results(self, target):
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        filename = f'sayer_results_{target}_{timestamp}.json'
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4)
            
        print(f"\n{Fore.GREEN}[+] Results saved to {filename}{Style.RESET_ALL}")
        
    def run_all(self, target):
        print(banner)
        print(dev_info)
        
        try:
            self.run_theHarvester(target)
            self.run_spiderfoot(target)
            self.run_ghunt(target)
            self.run_sherlock(target)
            self.save_results(target)
            
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Search interrupted by user{Style.RESET_ALL}")
            sys.exit(1)
            
        except Exception as e:
            print(f"\n{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Sayer - OSINT Tool Integration')
    parser.add_argument('target', help='Target to search (domain, email, username, etc.)')
    args = parser.parse_args()
    
    sayer = Sayer()
    sayer.run_all(args.target)

if __name__ == '__main__':
    main()