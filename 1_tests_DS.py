#---1.uzdevums_1-Linked_List---------------------------------------------------
class Node:
    def __init__(self, value):   #definēta klase Node, kas attēlo vienu elementu saistītā sarakstā. 
        self.value = value           #Katram mezglam ir divi atribūti: value un next - (Tas norāda uz nākamo mezglu saistītajā sarakstā.
        self.next = None                  # Sākotnēji tas ir iestatīts uz None.

class LinkedList:                       #Tas definē LinkedList klasi, kas attēlo pašu saistīto sarakstu. Tam ir šādas metodes:
    def __init__(self, value):              #__init__(): Šī ir konstruktora metode. Tas inicializē jaunu saistīto sarakstu ar vienu mezglu, 
        self.tail = new_node                      #kurā ir norādītā vērtība. Gan galvas, gan astes rādītāji ir iestatīti uz šo mezglu.
        new_node = Node(value)
        self.head = new_node

    def append(self, value):           #append(): šī metode piesaista saraksta beigām pievieno jaunu mezglu ar norādīto vērtību.
        new_node = Node(value)                 # Ja saistītais saraksts ir tukšs, tas iestata gan galvu, gan galu uz jauno mezglu.
        if self.head == None:                    # Pretējā gadījumā tas atjaunina astes rādītāju uz jauno mezglu.
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

      def find_middle_node(self):                    #find_middle_node(): šī metode atrod un atgriež saistītā saraksta vidējo mezglu. 
        if self.head is None:                                       #Tas izmanto divus rādītājus, slow_pointer un fast_pointer, kas inicializēti saistītā saraksta sākumā.
            return None                                               # Rādītājs lēnais_rādītājs pārvietojas pa vienam solim, bet ātrais_rādītājs vienlaikus pārvietojas divus soļus. 

        low_pointer = self.head                                   #Kad fast_pointer sasniedz saraksta beigas, lēnais_rādītājs atradīsies vidējā mezglā vai mezglā tieši pirms vidus, ja mezglu skaits ir pāra.
        fast_pointer = self.head

        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer if fast_pointer.next is None else slow_pointer.next

my_linked_list = LinkedList(1)      #Izveidots saistīts saraksts ar vērtībām : 1,2,3,4,5.
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )   #no šī saraksta izpildīta find_middle_node() metode un atgriezta tā vērtība.

#---1.uzdevums_2-Linked_List---------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None          
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        if self.head is None:
            return False

        slow_pointer = self.head                           #has_loop(): pārbauda, ​​vai saistītajā sarakstā ir cilpa. 
        fast_pointer = self.head                                  #Divas norādes (slow_pointer un fast_pointer) šķērso saistīto sarakstu dažādos ātrumos. 
                                                                     #Ja viņi kādā brīdī satiekas, tas norāda uz cilpas klātbūtni.
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True

        return False 

my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() )                       # Returns True

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() )               # Returns False

#-----2.uzdevums-Stack-------------------------------------------------------
class Node:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.next = None

class Stack:
    def __init__(self):
        self.top = None   #_init__(): Inicializē tukšu stack ar augšējo vērtību None un augstumu (elementu skaitu stack) uz 0.
        self.height = 0

    def is_empty(self):                 #is_empty(): pārbauda, ​​vai kaudze ir tukša, pārbaudot, vai augstums ir vienāds ar 0.
        return self.height == 0

    def push(self, value, position): 
        new_node = Node(value, position)     #push(): pievieno jaunu mezglu kaudzes augšpusē ar norādīto vērtību un pozīciju. Palielina augstumu par 1.
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.is_empty():                #pop(): noņem un atgriež mezglu kaudzes augšpusē. Samazina augstumu (elm. sk) par 1.
            return None
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp

def balancets(s):
    stack = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}     #šī funkcija ņem ievades virkni s, kurā, iespējams, ir ietverta iekavu rakstzīmju secība, un pārbauda, ​​vai iekavas ir līdzsvarotas. 
    for i, char in enumerate(s, start=1):                   #Tas atgriež vai nu “Success”, ja iekavas ir līdzsvarotas, vai arī pirmās konstatētās nelīdzsvarotās iekavas pozīciju.

        if char in '({[':
            stack.push(char, i)
        elif char in ')}]':                                                    #Tas iet cauri rakstzīmēm ievades virknē, izmantojot enumerate(), lai iegūtu gan rakstzīmi, gan tās indeksu. 
            if stack.is_empty() or stack.top.value != brackets_map[char]:            #Ja rakstzīme ir sākuma iekava ('(', '{', '['), tā nospiež to uz stack kopā ar savu pozīciju.
                return i                                                                #Ja rakstzīme ir beigu iekava tā pārbauda vei stack ir attiecīgā sākuma iekava, ja nav tad atgriež tās poz.
            else:                                                                #Pretējā gadījumā tas izceļ augšējo elementu no kaudzes.
                stack.pop()

    if stack.is_empty():
        return "Success"
    else:
        return stack.top.position
    
    

s = input("Ievadiet rindu: ")
print(balancets(s))
#--------3.uzdevums-BST--------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None         #pa kreisi: norāda uz kreiso pakārtoto mezglu. Sākotnēji iestatīts uz Nav.
        self.right = None            #pa labi: norāda uz labo pakārtoto mezglu. Sākotnēji iestatīts uz Nav.

class BinarySearchTree:                     #BinarySearchTree klase attēlo pašu bināro meklēšanas koku. Tam ir šādas metodes:
    def __init__(self):
        self.root = None                    #__init__(): Inicializē tukšu bināro meklēšanas koku, kura sakne ir iestatīta uz Nav.

    def insert(self, value):
        new_node = Node(value)       #insert(): ievieto jaunu mezglu ar norādīto vērtību binārajā meklēšanas kokā, vienlaikus saglabājot binārā meklēšanas koka rekvizītu.
        if self.root is None:          
            self.root = new_node         
            return True
        temp = self.root                              #Tas sākas no saknes mezgla un šķērso koku, lai atrastu atbilstošu ievietošanas vietu.
        while True:                                      #Ja koks ir tukšs, tas iestata jauno mezglu kā sakni.
            if new_node.value == temp.value:
                return False  # Avoids duplicate
            if new_node.value < temp.value:                   #Ja jaunā mezgla vērtība ir mazāka par pašreizējā mezgla vērtību, tas pāriet uz kreiso bērnkopu. Pretējā gadījumā tas šķērso labo bērnu.
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True                       #Kad tas atrod atbilstošo pozīciju, tas ievieto jauno mezglu kā pašreizējā mezgla atvasinājumu.
                temp = temp.right

    def tree_height(self, node):                                #tree_height(): Rekursīvi aprēķina binārā meklēšanas koka augstumu, sākot no dotā mezgla.
        if node is None:                                            #Tas izmanto mezglu kā ievadi un aprēķina apakškoka augstumu, kas sakņojas šajā mezglā.
            return 0
        else:
            left_height = self.tree_height(node.left)
            right_height = self.tree_height(node.right)

            return max(left_height, right_height) + 1

# Create a BinarySearchTree instance
my_tree = BinarySearchTree()

# Input string
input_str = input()
numbers = [int(n) for n in input_str.split()]

# Building the BST from input
for number in numbers:
    my_tree.insert(number)

# Calculating the height of the BST
height = my_tree.tree_height(my_tree.root)
print(height)
