class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.root = None
        self.nodes = {}

    def add_rule(self, a, b):
        if self.nodes.get(a):
            if self.nodes.get(b):
                self.nodes[a].next = self.nodes[b]
            else:
                no = Node()
                no.data = b
                self.nodes[b] = no
                self.nodes[a].next = no
        else:
            a_no = Node()
            a_no.data = a
            if not self.nodes.get(b):
                b_no = Node()
                b_no.data = b
                self.nodes[b] = b_no
            else:
                b_no = self.nodes[b]
            a_no.next = b_no
            self.nodes[a] = a_no

    def set_root(self):
        nexts = []
        for i in self.nodes:
            nexts.append(self.nodes[i].next.data) if self.nodes[i].next else None
        self.root = list(set(self.nodes.keys()).difference(set(nexts)))[0]
        # print(self.root)

    def print(self):
        node = self.nodes[self.root]
        while(node):
            print(node.data, end='')
            node = node.next
        print('')


def driver(arr):
    lis = LinkedList()
    for j in arr:
        lis.add_rule(j[0], j[2])
    lis.set_root()
    lis.print()
driver(["P>E","E>R","R>U"])
driver(["I>N","A>I","P>A","S>P"]) # SPAIN
driver(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) #HUNGARY
driver(["I>F", "W>I", "S>W", "F>T"]) # SWIFT
driver(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]) # PORTUGAL
driver(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]) # SWITZERLAND

# print(lis.nodes)