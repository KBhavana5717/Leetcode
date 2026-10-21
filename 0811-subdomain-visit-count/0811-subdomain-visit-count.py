class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        from collections import defaultdict
        
        counts = defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            
            fragments = domain.split('.')
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                counts[subdomain] += count
                
        return [f"{count} {domain}" for domain, count in counts.items()]