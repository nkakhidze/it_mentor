import time


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, value):
        """
        Добавление элемента в конец связанного списка.
        """
        new_node = Node(value)

        # Если список пустой, новый узел становится головой списка
        if self.head is None:
            self.head = new_node
            return

        # Иначе идём до последнего узла
        current = self.head

        while current.next is not None:
            current = current.next

        # Последний узел теперь ссылается на новый узел
        current.next = new_node

    def add_first(self, value):
        """
        Добавление элемента в начало связанного списка.
        """
        new_node = Node(value)

        # Новый узел должен ссылаться на старую голову
        new_node.next = self.head

        # Теперь голова списка — новый узел
        self.head = new_node

    def delete_element(self, value):
        """
        Удаление первого найденного элемента по значению.
        Возвращает True, если элемент был удалён.
        Возвращает False, если элемент не найден.
        """

        # Если список пустой
        if self.head is None:
            return False

        # Если удаляем голову списка
        if self.head.value == value:
            self.head = self.head.next
            return True

        # Иначе ищем элемент дальше
        previous = self.head
        current = self.head.next

        while current is not None:
            if current.value == value:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def find_element(self, value):
        """
        Поиск элемента по значению.
        Возвращает True, если элемент найден.
        Возвращает False, если элемент не найден.
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True

            current = current.next

        return False

    def show_linked_list(self):
        """
        Вывод связанного списка в консоль.
        """
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    def to_list(self):
        """
        Преобразование связанного списка в обычный Python list.
        Это удобно для проверки.
        """
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result





linked_list = LinkedList()
linked_list.show_linked_list()

linked_list.add_element(10)
linked_list.add_element(20)
linked_list.add_element(30)

linked_list.show_linked_list()