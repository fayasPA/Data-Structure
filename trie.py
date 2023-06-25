class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word: str):
        """ Insert a word into trie """
        cur = self.root

        for chara in word:
            if chara not in cur.children:
                cur.children[chara] = TrieNode()
            cur = cur.children[chara]
            print("current",cur.children)
        cur.endOfWord = True

    def search(self, word: str):
        cur = self.root
        for chara in word:
            if chara not in cur.children:
                return False
            cur = cur.children[chara]
        return cur.endOfWord
    
    def startsWith(self, prefix: str):
        cur = self.root
        for chara in prefix:
            if chara not in cur.children:
                return False
            cur = cur.children[chara]
        return True
    
_trie = Trie()
_trie.insert("fayas")
# print(_trie.startsWith("a"))
