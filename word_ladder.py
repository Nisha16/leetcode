class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        result = []
        wordlist.add(beginWord)
        wordlist.add(endWord)
        
        cur = [beginWord]
        visited = set([beginWord])
        found = False
        trace = {word: [] for word in wordlist}
        
        while cur and not found:
            for word in cur:
                visited.add(word)
                
            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in wordlist:
                            if candidate == endWord:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next
        if found:
            self.backtrack(result, trace, [], endWord)
        
        return result
        
    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)