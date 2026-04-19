class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.word = True
    
class Solution:
    def populate_trie(self,words: List[str]):
        trie = Trie()
        for word in words:
            trie.add_word(word)
        return trie
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        trie = self.populate_trie(words)


        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] not in node.children or (r,c) in visited:
                return False
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            directions = [[1,0], [-1,0], [0,1], [0, -1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)
            
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
        
        return list(res)


        