class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and uppercase everything
        cleaned = s.replace("-", "").upper()

        # Length of the first (possibly shorter) group
        first_group_len = len(cleaned) % k
        if first_group_len == 0 and cleaned:
            first_group_len = k

        groups = []
        if first_group_len:
            groups.append(cleaned[:first_group_len])

        # Remaining characters split into groups of exactly k
        for i in range(first_group_len, len(cleaned), k):
            groups.append(cleaned[i:i + k])

        return "-".join(groups)