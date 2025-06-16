#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import argparse
import concurrent.futures
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
        self.tools_status = {
            'theHarvester': False,
            'spiderfoot': False,
            'ghunt': False,
            'sherlock': False
        }
        
    def run_theHarvester(self, target):
        try:
            print(f"\n{Fore.YELLOW}[*] Running theHarvester...{Style.RESET_ALL}")
            harvester = TheHarvester(target)
            self.results['theHarvester'] = harvester.gather_info()
            self.tools_status['theHarvester'] = True
            print(f"{Fore.GREEN}[+] theHarvester completed successfully{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] theHarvester error: {str(e)}{Style.RESET_ALL}")
        
    def run_spiderfoot(self, target):
        try:
            print(f"\n{Fore.YELLOW}[*] Running SpiderFoot...{Style.RESET_ALL}")
            scanner = SpiderFootScanner()
            self.results['spiderfoot'] = scanner.start_scan(target)
            self.tools_status['spiderfoot'] = True
            print(f"{Fore.GREEN}[+] SpiderFoot completed successfully{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] SpiderFoot error: {str(e)}{Style.RESET_ALL}")
        
    def run_ghunt(self, target):
        try:
            print(f"\n{Fore.YELLOW}[*] Running GHunt...{Style.RESET_ALL}")
            hunter = GHunt()
            self.results['ghunt'] = hunter.search(target)
            self.tools_status['ghunt'] = True
            print(f"{Fore.GREEN}[+] GHunt completed successfully{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] GHunt error: {str(e)}{Style.RESET_ALL}")
        
    def run_sherlock(self, target):
        try:
            print(f"\n{Fore.YELLOW}[*] Running Sherlock...{Style.RESET_ALL}")
            sherlock = Sherlock()
            self.results['sherlock'] = sherlock.search(target)
            self.tools_status['sherlock'] = True
            print(f"{Fore.GREEN}[+] Sherlock completed successfully{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Sherlock error: {str(e)}{Style.RESET_ALL}")

    def run_parallel(self, target):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            tools = {
                executor.submit(self.run_theHarvester, target): 'theHarvester',
                executor.submit(self.run_spiderfoot, target): 'spiderfoot',
                executor.submit(self.run_ghunt, target): 'ghunt',
                executor.submit(self.run_sherlock, target): 'sherlock'
            }
            
            for future in concurrent.futures.as_completed(tools):
                tool = tools[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"{Fore.RED}[!] {tool} failed: {str(e)}{Style.RESET_ALL}")
        
    def save_results(self, target):
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        filename = f'sayer_results_{target}_{timestamp}.json'
        
        # Add status information to results
        self.results['status'] = self.tools_status
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4)
            
        print(f"\n{Fore.GREEN}[+] Results saved to {filename}{Style.RESET_ALL}")
        
        # Print summary
        print("\n=== Execution Summary ===")
        for tool, status in self.tools_status.items():
            status_color = Fore.GREEN if status else Fore.RED
            status_text = "Success" if status else "Failed"
            print(f"{status_color}[{status_text}] {tool}{Style.RESET_ALL}")
        
    def run_all(self, target):
        print(banner)
        print(dev_info)
        
        try:
            print(f"{Fore.CYAN}[*] Starting scan for target: {target}{Style.RESET_ALL}")
            start_time = time.time()
            
            # Run tools in parallel
            self.run_parallel(target)
            
            # Save and display results
            self.save_results(target)
            
            end_time = time.time()
            duration = end_time - start_time
            print(f"\n{Fore.CYAN}[*] Total execution time: {duration:.2f} seconds{Style.RESET_ALL}")
            
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