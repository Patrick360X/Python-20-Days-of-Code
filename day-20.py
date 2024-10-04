'''
# Day - 20:
'''

# Async IO : is a programming pattern that allows for high performance I/O 
# operations in concurrent and non-blocking manner.

import time
import asyncio
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

async def func1():
    URL = "https://www.pexels.com/photo/mountain-at-night-under-a-starry-sky-1624496/"
    response = requests.get(URL)
    open("pngimages/img1.jpeg","wb").write(response.content)
    await asyncio.sleep(1)
    print("My Friend's")

async def func2():
    URL = "https://www.pexels.com/photo/photography-of-mountains-under-cloudy-sky-1183099/"
    response = requests.get(URL)
    open("pngimages/img2.jpeg", "wb").write(response.content)
    await asyncio.sleep(1)
    print("name is")
    
async def func3():
    URL = "https://www.pexels.com/photo/blue-sea-under-clear-blue-sky-50594/"
    response = requests.get(URL)
    open("pngimages/img3.jpeg","wb").write(response.content)
    await asyncio.sleep(1)
    print("Pradyumna")

async def main():
    task = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print(task)

# asyncio.run(main()) ## Uncomment this


# Multithreading : allows multiple threads of execution to run concurrently within a single process 

def fun(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1 = time.perf_counter()
    # Normal code execution
    # fun(4)
    # fun(2)    
    # fun(1)    
    # time2 = time.perf_counter()
    # print(time2 - time1)

    #Using multithreading concept

    thread1 = threading.Thread(target=fun,args=[4])
    thread2 = threading.Thread(target=fun,args=[2])
    thread3 = threading.Thread(target=fun,args=[1])

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()

    thread2.join()

    thread3.join()

    time2 = time.perf_counter()
    print(time2 - time1)

# main() ## Uncomment this

# Using threadpool for parellel execution

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # here we're submitting our function to the executor and it executes it parallely 

        # future1 = executor.submit(fun, 3)
        # future2 = executor.submit(fun, 4)
        # future3 = executor.submit(fun, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        # here we'll use map functionality to handover list element to executor parallely
        list1 = [1,5,3,2,6]
        results = executor.map(fun, list1)

        for result in results:
            print(result)

# poolingDemo() ## Uncomment this

# Multiprocessing
import multiprocessing

def DownloadFiles(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"pngimages/urlgenerated/{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/3200/2400"

    # processes = []

    # for i in range(5):
    #     # DownloadFiles(url,i)
    #     process = multiprocessing.Process(target=DownloadFiles,args=[url,i])

    #     process.start()
    #     processes.append(process)

    # for process in processes:
    #     process.join()

    # here we'll use map functionality 

    with ProcessPoolExecutor() as executor:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]

        results = executor.map(DownloadFiles, l1, l2)

        for result in results:
            print(result)