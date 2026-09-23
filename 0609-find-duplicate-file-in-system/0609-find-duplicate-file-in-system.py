from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            
            for file_info in parts[1:]:
                # Split file name and content using '(' and ')'
                file_name, content = file_info.split('(')
                content = content[:-1] # Remove the trailing ')'
                
                full_path = f"{directory}/{file_name}"
                content_to_paths[content].append(full_path)
                
        # Filter out files that do not have duplicates (only 1 path associated with the content)
        return [paths_list for paths_list in content_to_paths.values() if len(paths_list) > 1]