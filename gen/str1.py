"""
Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        ws = paragraph.lower()
        wlist = re.split("\W+", ws)
        #print(wlist)
        ban = {}
        for w in banned:
            ban[w] = 1
        whash = {}
        rep = 0
        for w in wlist:
            if w in whash.keys():
                whash[w] = whash[w] + 1;
            else:
                whash[w] = 1;
            r = ban.get(w, None)
            if  r == None:
                if whash[w] > rep:
                    rep = whash[w]
                    word = w

        #print(whash)
        print(word)
        return word;

