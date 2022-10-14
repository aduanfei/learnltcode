import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordgraph=collections.defaultdict(list)

        def connected(word1,word2):
            diff=0
            for i in range(len(word1)):
                if not word1[i]==word2[i]:
                    diff+=1
            return diff==1

        for i in range(len(wordList)):
            if connected(beginWord,wordList[i]):
                wordgraph[wordList[i]].append(beginWord)
                wordgraph[beginWord].append(wordList[i])

            for j in range(i+1,len(wordList)):
                if connected(wordList[i],wordList[j]):
                    wordgraph[wordList[i]].append(wordList[j])
                    wordgraph[wordList[j]].append(wordList[i])

        depth=1
        q=collections.deque([beginWord])
        count=1
        res=[]
        path=[]
        def bfs(path,depth,count):
            if depth>len(wordList) or not q:
                return
            word=q.popleft()
            path.append(word)
            if word==endWord:
                res.append(path)
                return
            for w in wordgraph[word]:
                bfs

        while(q):
            for i in range(count):
                word=q.popleft()
                l.append(word)
                if word==endWord:
                    res.append(l)
                l.pop()

            for w in wordgraph[word]:
                    q.append(w)
            count=len(q)
            depth+=1

s=Solution()
s.findLadders("hit","cog",["hot","dot","dog","lot","log","cog"])