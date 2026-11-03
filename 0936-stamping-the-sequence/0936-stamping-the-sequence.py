class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        m, n = len(stamp), len(target)
        t_list = list(target)
        s_list = ['?'] * n
        res = []
        
        def can_stamp(i):
            changed = False
            for j in range(m):
                if t_list[i + j] == '?':
                    continue
                if t_list[i + j] != stamp[j]:
                    return False
                changed = True
            return changed

        def do_stamp(i):
            count = 0
            for j in range(m):
                if t_list[i + j] != '?':
                    t_list[i + j] = '?'
                    count += 1
            return count

        changed = True
        total_changed = 0
        while changed:
            changed = False
            for i in range(n - m + 1):
                if can_stamp(i):
                    matched_chars = do_stamp(i)
                    total_changed += matched_chars
                    res.append(i)
                    changed = True
                    if total_changed == n:
                        return res[::-1]
                        
        return [] if total_changed != n else res[::-1]