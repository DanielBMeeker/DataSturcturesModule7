"""
Program: priority_queue_application.py
Author: Daniel Meeker
Date: 10/16/2020

This program demonstrates using a priority queue
with the heapq library.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""
import heapq
import random

NUMBER_OF_CUSTOMERS = 100
customer_list = []  # a list of lists where each inner list contains the priority, the order the customer joined
# the line, and the customer name
priority_queue = []
count = 1
PRIORITY_MIN = 1
PRIORITY_MAX = 5
for i in range(NUMBER_OF_CUSTOMERS):
    customer_priority = random.randint(PRIORITY_MIN, PRIORITY_MAX)
    customer_list.append(
        [customer_priority, count, "Customer " + str(i + 1)])  # count keeps track of when the customer gets in line
    count += 1
for i in range(NUMBER_OF_CUSTOMERS):
    heapq.heappush(priority_queue, customer_list[i])
priority_queue = sorted(
    priority_queue)  # have to sort the queue so that the priority stays in the right order where customers that have
# the same priority are organized by order added to list.
if __name__ == '__main__':
    print(customer_list)
    print(priority_queue)
