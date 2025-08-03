class Node:
    def __init__(self):
        self.children = {}
        self.hasWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()            
            # print('->', char, node.children)
            node = node.children[char]
        node.hasWord = True
        # print('->', '', self.root.children['a'].children)
        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i==len(word):
                # print(word[:i+1], '->', node.children)
                return node.hasWord
            if word[i]!='.' and word[i] not in node.children:
                return False
            if word[i]=='.':
                res = False
                for childnode in node.children.values():
                    res = res or dfs(childnode, i+1)
                return res
            return dfs(node.children[word[i]], i+1)
            
        return dfs(self.root, 0)
        # return node.hasWord
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)