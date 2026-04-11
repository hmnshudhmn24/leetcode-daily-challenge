from typing import List
import collections

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_items = set()
        table_orders = collections.defaultdict(lambda: collections.defaultdict(int))
        
        for _, table, item in orders:
            food_items.add(item)
            table_orders[int(table)][item] += 1
            
        foods = sorted(list(food_items))
        res = [["Table"] + foods]
        
        for table in sorted(table_orders.keys()):
            row = [str(table)]
            for food in foods:
                row.append(str(table_orders[table][food]))
            res.append(row)
            
        return res
