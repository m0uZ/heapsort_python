# Для реализации разворота связного списка нужно сначала определить класс узла в списке:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Затем нужно определить сам класс для связного списка:

class LinkedList:
    def __init__(self):
        self.head = None  # указатель на начальный элемент списка
 
    def push(self, new_val):  # метод добавления нового узла в начало списка
        new_node = ListNode(new_val)  # создаем новый узел
        new_node.next = self.head  # связываем новый узел со старым начальным элементом
        self.head = new_node  # устанавливаем новый узел как начальный элемент
 
    def printList(self):  # метод вывода списка на экран
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
# Теперь можно реализовать метод разворота связного списка:

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node != None:
            next_node = curr_node.next  # запоминаем следующий элемент
            curr_node.next = prev_node  # меняем ссылку на следующий элемент на ссылку на предыдущий
            prev_node = curr_node  # перемещаем указатели на текущий и предыдущий узлы
            curr_node = next_node
        self.head = prev_node  # устанавливаем новый начальный элемент


Linked_list = LinkedList()  # создание нового объекта списка
Linked_list.push(1)         # добавление узлов в список
Linked_list.push(2)
Linked_list.push(3)
Linked_list.push(4)
Linked_list.push(5)
 
Linked_list.printList()     # печать списка перед разворотом

Linked_list.reverse()       # разворот списка
 
Linked_list.printList()     # печать списка после разворота
# В результате должны получить:

# 5 4 3 2 1        # до разворота
# 1 2 3 4 5        # после разворота