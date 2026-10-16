class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i

        # Initialize DSU and mappings
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)
                
        # Group emails by their root parent
        from collections import defaultdict
        components = defaultdict(list)
        for email in parent:
            root = find(email)
            components[root].append(email)
            
        # Format the results
        res = []
        for root, emails in components.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))
            
        return res