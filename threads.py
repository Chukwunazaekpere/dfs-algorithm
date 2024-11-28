"""
Author: Chukwunazaekpere Emmanuel Obioma
Lecture: Sorting
Nationality: Biafran
Email-1: chukwunazaekpere.obioma@ue-germany.de 
Email-2: ceo.naza.tech@gmail.com
************************************************
Implementation: to implement the sequential implementation of DFS
Course: Multi-core Programming
Written: Nov 26th 2024
Due: Nov 30th 2024
"""

from omp4py import *
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from datetime import datetime
import random
from time import time
import logging
logger = logging.getLogger(__name__)
log_date = datetime.now()
logging.basicConfig(level=logging.INFO)


def dfs_sequential(tree:dict, node:str, nodes_visited=None):
    if nodes_visited is None:
        nodes_visited = set()  # set is a non-hierarchical python data type, which does not permit repetitions
    nodes_visited.add(node)    # the root node is added into the nodes_visited nodes
    for child in tree[node]:  # Recursively implemetation for visiting un-nodes_visited nodes
        if child not in nodes_visited:
            dfs_sequential(tree, child, nodes_visited)
    return nodes_visited

# Run DFS starting from root node 'A'
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

# print("\n\t thread_two: ", thread_two)

if __name__ == "__main__":
    # print("Number of cpu :  ", multiprocessing.cpu_count())
    start_time = time()
    with ThreadPoolExecutor(max_workers=2) as threads: # the with statement creates a ThreadPoolExecutor instance and consequently clears out spawned threads upon completion.
        thread_output = threads.submit(dfs_sequential, tree=tree, node="A") # 
    # for output in concurrent.futures.as_completed(thread_output):
    print("\n\t output: ", thread_output.result())
    logging.info(msg=f"\n\t total time taken: {(time()-start_time)} secs")
