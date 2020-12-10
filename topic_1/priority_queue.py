"""
Program: priority_queue.py
Author: Daniel Meeker
Date: 10/16/2020

This program demonstrates an implementation of priority queue
using a node class.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""

"""Exceptions"""


class PriorityException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class QueueFullException(Exception):
    pass


"""Node Class"""


class Node:

    def __init__(self, job_number, priority):
        self.job_number = job_number
        self.priority_list = ["A", "B", "C", "D", "F"]
        self.priority_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "F": 5}
        if priority.upper() in self.priority_list:
            self.priority = priority
            self.priority_value = self.priority_dict.get(priority)
        else:
            raise PriorityException("Not a valid Priority")


"""PriorityQueue Class"""


class PriorityQueue:

    def __init__(self, max_size=9):
        self.queue = []
        self.head = 0
        self.max_size = max_size

    def is_empty(self):
        """
        If there are no elements in the queue this will return true,
        otherwise it will return false
        :return: boolean
        """
        if self.size() == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        If the number of elements in the queue are equal to its self.max_size
        this will return true, otherwise it will return false.
        :return:
        """
        if self.size() == self.max_size:
            return True
        else:
            return False

    def enqueue(self, node):
        if not self.is_full():
            if self.size() == 0:
                self.queue.append(node)
            else:
                # traverse the queue to find the right place for new node
                for x in range(0, self.size()):
                    if node.priority_value >= self.queue[x].priority_value:
                        if x == (self.size() - 1):
                            self.queue.insert(x + 1, node)
                        else:
                            continue
                    else:
                        self.queue.insert(x, node)
                        return True
        else:
            raise QueueFullException("Queue is Full!")

    def dequeue(self):
        try:
            self.peek()
            job = self.queue[self.head]
            self.queue.remove(job)
            return "Job " + str(job.job_number) + " complete"
        except QueueEmptyException:
            raise QueueEmptyException("Queue is Empty!")

    def peek(self):
        if not self.is_empty():
            node_peeked = self.queue[self.head]
            node_str = str(node_peeked.job_number) + " - " + str(node_peeked.priority)
            return node_str
        else:
            raise QueueEmptyException("Queue is Empty!")

    def print_priority_queue(self):
        if not self.is_empty():
            queue_str = ""
            for x in range(self.size()):
                queue_str += (str(self.queue[x].job_number) + " - " + str(self.queue[x].priority) + "\n")
            return queue_str
        else:
            raise QueueEmptyException("Queue is Empty!")

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    pQueue = PriorityQueue()
    node1 = Node(1111, "B")
    node2 = Node(2222, "B")
    node3 = Node(3333, "B")
    node4 = Node(4444, "D")
    node5 = Node(5555, "D")
    node6 = Node(6666, "D")
    node7 = Node(7777, "D")
    node8 = Node(8888, "A")
    node9 = Node(9999, "A")

    pQueue.enqueue(node1)
    pQueue.enqueue(node2)
    pQueue.enqueue(node3)
    pQueue.enqueue(node4)
    pQueue.enqueue(node5)
    pQueue.enqueue(node6)
    pQueue.enqueue(node7)
    pQueue.enqueue(node8)
    pQueue.enqueue(node9)
    print(pQueue.print_priority_queue())
    try:
        pQueue.enqueue(node1)
    except QueueFullException as e:
        print(e)
    print("--------")
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    print(pQueue.dequeue())
    try:
        print(pQueue.dequeue())
    except QueueEmptyException as e:
        print(e)
    try:
        print(pQueue.print_priority_queue())
    except QueueEmptyException as e:
        print(e)
    try:
        print(pQueue.peek())
    except QueueEmptyException as e:
        print(e)

    pQueue.enqueue(node1)
    pQueue.enqueue(node2)
    pQueue.enqueue(node3)
    pQueue.enqueue(node4)
    pQueue.enqueue(node5)
    pQueue.enqueue(node6)
    pQueue.enqueue(node7)
    pQueue.enqueue(node8)
    pQueue.enqueue(node9)
    print(pQueue.print_priority_queue())
    print(pQueue.peek())
