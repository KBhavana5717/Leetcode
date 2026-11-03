class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def get_key(log):
            _id, rest = log.split(' ', 1)
            if rest[0].isdigit():
                return (1, )
            else:
                return (0, rest, _id)
        
        return sorted(logs, key=get_key)