class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ret = ""
        for i in range(len(strs[0])):
            isCommon = True
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    isCommon = False
                    break
            if isCommon == False:
                break
            else:
                ret += strs[0][i]
        return ret
        