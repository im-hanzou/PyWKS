import requests
import threading
import re
import urllib3
import signal
from queue import Queue, Empty
from colorama import init, Fore, Style

urllib3.disable_warnings()
init()

stop_event = threading.Event()

def check_word_in_website(url, keyword):
    try:
        response = requests.get(url, timeout=10, verify=False)
        if response.status_code == 200:
            content = response.text
            if keyword and re.search(re.escape(keyword), content, re.IGNORECASE):
                return url, True
        return url, False
    except requests.exceptions.Timeout:
        return url, False
    except requests.exceptions.RequestException:
        return url, False
    except Exception as e:
        return url, False

def process_queue(q, keyword):
    while not stop_event.is_set():
        try:
            url = q.get(timeout=1)
            if url is None:
                break

            result_url, found = check_word_in_website(url, keyword)
            if found:
                print(f"{result_url} {Fore.GREEN}> FOUND!{Style.RESET_ALL}")
                with open('results.txt', 'a') as result_file:
                    result_file.write(f"{result_url}\n")
            else:
                print(f"{result_url} {Fore.RED}> NOT FOUND!{Style.RESET_ALL}")

            q.task_done()
        except Empty:
            continue

def main():
    file_path = input("List: ")
    keyword = input("Insert Keyword: ")
    num_threads = input("Threads: ")

    try:
        num_threads = int(num_threads)
    except ValueError:
        print("Thread must be an integer!")
        return
    try:
        with open(file_path, 'r') as file:
            websites = file.read().splitlines()
    except FileNotFoundError:
        print("File not found!")
        return

    q = Queue()
    for url in websites:
        q.put(url)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=process_queue, args=(q, keyword))
        thread.start()
        threads.append(thread)

    try:
        signal.signal(signal.SIGINT, signal_handler)
        q.join()
    except KeyboardInterrupt:
        print("\nStopped! Result saved to results.txt")
        stop_event.set()

    for _ in range(num_threads):
        q.put(None)

    for thread in threads:
        thread.join()

def signal_handler(sig, frame):
    global stop_event
    stop_event.set()

if __name__ == "__main__":
    banner = r"""
________        ___       _______ _________
___  __ \____  ___ |     / /__  //_/_  ___/
__  /_/ /_  / / /_ | /| / /__  ,<  _____ \ 
_  ____/_  /_/ /__ |/ |/ / _  /| | ____/ / 
/_/     _\__, / ____/|__/  /_/ |_| /____/  
        /____/                             
                                            
      Mass Website Keyword Scanner
          Github : IM-Hanzou
"""

    print(Fore.CYAN + banner + Style.RESET_ALL)
    main()
