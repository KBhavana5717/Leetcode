class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        s_list = list(s)
        for i, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
            if s.startswith(src, i):
                s_list[i:i + len(src)] = list(tgt)
        return "".join(s_list)