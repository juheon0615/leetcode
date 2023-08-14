class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        let ss = s.trimmingCharacters(in: .whitespacesAndNewlines)
        var lastWhiteSpace = 0
        for (i,ch) in ss.enumerated() {
            if !ch.isLetter {
                lastWhiteSpace = i
            }
        }

        let startOffset = lastWhiteSpace == 0 ? 0 : lastWhiteSpace + 1
        let start = ss.index(ss.startIndex, offsetBy: startOffset)
        let end = ss.endIndex

        let ret = ss[start ..< end]
        
        return ret.count
    }
}