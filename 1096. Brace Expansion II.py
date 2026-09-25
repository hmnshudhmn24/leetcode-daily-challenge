class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        groups = [[]]
        level = 0
        for i, char in enumerate(expression):
            if char == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif char == '}':
                level -= 1
                if level == 0:
                    sub_result = self.braceExpansionII(expression[start:i])
                    groups[-1].append(sub_result)
            elif char == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([char])
        final_set = set()
        for group in groups:
            current_group_set = {""}
            for item in group:
                temp_set = set()
                for prefix in current_group_set:
                    for suffix in item:
                        temp_set.add(prefix + suffix)
                current_group_set = temp_set
            final_set.update(current_group_set)
        return sorted(list(final_set))
