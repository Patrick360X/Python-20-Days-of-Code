'''
# Day - 17:
'''

# Hybrid Inheritance : Combination of single and multiple inheritance

class BaseClass:
    pass

class Derived1(BaseClass):  # Single inheritance between first 2 classes
    pass

class Derived2(BaseClass):     
    pass

class Derived3(Derived1,Derived2):   # Multiple inheritance can be observed between derived1, derived2 as multiple base classes for derived3 
    pass

# Hierarchical Inheritance : Single base class acts as parent for multiple subclasses

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):     
    pass

class Derived3(Derived1):
    pass

class Derived4(Derived2):
    pass

# Time Module : 


# 1. time.time() : return total seconds taken to perform an operation in python
import time

# def usingwhile():
#     i = 0
#     while (i<50000):
#         i = i+1
#         print(i)

# def usingfor():
#     for i in range(1,50000):
#         print(i)

# start = time.time()
# usingwhile()
# t1 = time.time() - start
# start = time.time()
# usingfor()
# t2 = time.time() - start
# print(f'Time taken to complete for loop : {t2}')
# print(f'Time taken to complete while loop : {t1}')

# if(t1>t2):
#     print('For loop is faster')
# else:
#     print("While loop is faster")

#2. sleep()

# print("My name is pradyumna")
# time.sleep(5)
# print("I was resting from past 5 seconds")

# 3. Strftime() 

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S %p",t)

print(formatted_time)

print('\n')

# Command line utilities

import argparse
import requests

def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename
  
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)