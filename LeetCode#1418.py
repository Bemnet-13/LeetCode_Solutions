class Solution:
    def displayTable(self, orders):
        display_table = []
        food_items = list(set([i[2] for i in orders]))
        table_no = list(set([i[1] for i in orders]))

        food_items.sort()
        print(food_items)
        table_no.sort(key = lambda k : int(k))
        food_items.insert(0, "Table")
        display_table.append(food_items)
        for i in table_no:
            display_table.append([i] + ["0" for _ in range(len(food_items) - 1)])
        print(display_table)
        # Place an order

        for customer, table, item in orders:
            idx_food = food_items.index(item)
            idx_table = table_no.index(table) + 1
            print(idx_table, idx_food)
            x = display_table[idx_table][idx_food]
            display_table[idx_table][idx_food] = str(int(x) + 1)
        
        return display_table

trial = Solution()
o = trial.displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
print(o)