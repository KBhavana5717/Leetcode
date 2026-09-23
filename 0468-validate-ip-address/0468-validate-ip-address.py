class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Helper function to check IPv4
        def is_ipv4(ip: str) -> bool:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for p in parts:
                if not p.isdigit():
                    return False
                # Check for leading zeros and value range 0-255
                if (p[0] == '0' and len(p) > 1) or not (0 <= int(p) <= 255):
                    return False
            return True

        # Helper function to check IPv6
        def is_ipv6(ip: str) -> bool:
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hex_digits = set("0123456789abcdefABCDEF")
            for p in parts:
                if not (1 <= len(p) <= 4) or not all(c in hex_digits for c in p):
                    return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        elif is_ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"