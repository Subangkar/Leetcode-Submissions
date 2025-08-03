class Node:
    def __init__(self):
        self.children = {}
        self.hasWord = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()            
            # print('->', char, node.children)
            node = node.children[char]
        node.hasWord = True
        # print('->', '', self.root.children['a'].children)
                

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                # print(char, node.children)
                return False
            else:
                node = node.children[char]

        return node.hasWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]

        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)