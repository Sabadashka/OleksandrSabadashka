import random
from validation import *


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def isSorted(self):
        if self.head == None:
            sys.exit("Список пустий. Програма завершила роботу.")

        t = self.head
        while t.next != None:
            if t.data >= t.next.data:
                print("\033[93mМасив не сортований\033[0m")
                sum = 0
                l = self.head
                while l:
                    if l.data >= 0:
                        sum += l.data
                    l = l.next
                print(sum)
                return

            t = t.next
        print("\033[93mМасив сортований\033[0m")
        dob = 1
        m = self.head
        while m.next:
            d1 = m.data
            m = m.next
            d2 = m.data
            dob = dob * (d2 - d1)

        print(dob)
        return

    def push_back(self, newElement):

        newNode = Node(newElement)

        if self.head is None:
            self.head = newNode
            return
        else:

            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = newNode

    def push_at(self, newElement, position):

        try:
            int(newElement)
        except ValueError:
            return False

        newNode = Node(newElement)
        if position == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position - 1):
                if temp is not None:
                    temp = temp.next

            if temp is not None:
                newNode.next = temp.next
                temp.next = newNode
            else:

                print("\033[91m\nТакої позиції не існує.\033[0m")

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    def DeleteNode(self, position):
        if self.head is None:
            return

        temp = self.head

        if position == 1:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 2):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            print("\033[91m\nТакої позиції не існує.\033[0m")
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    def EnterFromKeyboard(self, l):

        self.head = None
        for i in range(l):
            c = input(f"\033[32mВведіть {i + 1} число: \033[0m")
            c = validation_for_a_b(c)
            self.push_back(int(c))

    def Generate(self, a, b, l):
        self.head = None
        for i in range(l):
            self.Atbegining(random.randint(a, b))

    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.data == Removekey:
                self.head = HeadVal.next
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if HeadVal is None:
            return

        prev.next = HeadVal.next
        HeadVal = None

    def LListprint(self):

        if self.head is None:
            print("\033[32mСписок пустий\033[0m")
            return True

        printval = self.head

        s = ""

        while printval:
            s = s + str(printval.data) + " "
            printval = printval.next
        print(s)
