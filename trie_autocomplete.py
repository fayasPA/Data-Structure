class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class AutoComplete:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str):
        curr = self.root
        for chara in word:
            if chara not in curr.children:
                curr.children[chara] = TrieNode()
            curr = curr.children[chara]
        curr.endOfWord = True
    
    # def autocomplete(self,prefix: str):
    #     res = []
    #     node = self.root
    #     for chara in prefix:
    #         if chara in node.children:
    #             node = node.children[chara]
    #         return None
    #     self.helper(node, res, prefix[:-1])
    #     return res
    
    # def helper(self, node, res, prefix):
    #     if node == None:
    #         return
    #     if node.endOfWord:
    #         res.append(prefix + node.children.keys())

# Autocomplete Haseeb
    def auto_complete(self,word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return []
            current = current.children[letter]
        return self._dfs(current,word)

    def _dfs(self, node, word):
        result = []
        if node.endOfWord:
            result.append(word)
        for letter in node.children:
            result.extend(self._dfs(node.children[letter], word + letter))
        return result    

# s = 'fayas'
# print(s[:-1])

auto_complete = AutoComplete()
auto_complete.insert('fayas')
auto_complete.insert('fayman')
auto_complete.insert('fayaspa')
auto_complete.insert('fayasmuthaleef')
auto_complete.insert('faymon')
print(auto_complete.auto_complete('faym'))