class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.lower().split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            digits = "".join(filter(str.isdigit, s))
            local = f"***-***-{digits[-4:]}"
            if len(digits) == 10:
                return local
            country = "+" + "*" * (len(digits) - 10)
            return f"{country}-{local}"