class Item:
    def __init__(self, profit: float, weight: float) -> None:
        self.weight = weight
        self.profit = profit

class Knapsack:
    def __init__(self, initial_weight_limitation: float) -> None:
        self._content = []
        self._total_profit = 0.0
        self._remaining_weight = initial_weight_limitation

    def add_item(self, item: Item) -> None:
        self._content += [item]
        self._total_profit += item.profit
        self._remaining_weight -= item.weight

    # These are for outside the class and subclasses.
    # def get_total_profit(self) -> float:
    #     return self._total_profit

    # def get_remaining_weight(self) -> float:
    #     return self._remaining_weight

    def get_content(self) -> list[Item]:
        return self._content

    def optimised_collection_greedy(self, collection: list[Item]) -> float:
        sorted_collection = sort_items_in_rising_order(collection)
        for item in sorted_collection:
            remaining_weight = self._remaining_weight
            if item.weight <= remaining_weight:
                self.add_item(item)
            else:
                weight_ratio = remaining_weight/item.weight
                profit_fraction = (weight_ratio) * item.profit
                self.add_item(Item(profit_fraction, weight_ratio))
                break
        return self._total_profit
                    
        
def sort_items_in_rising_order(collection: list[Item]) -> list[Item]:
    return collection.sort(key=lambda item: (item.profit/item.weight))
    
def main() -> None:
    collection = [Item(60, 10), Item(100, 20), Item(120, 30)]
    initial_weight = 50
    knapsack = Knapsack(initial_weight)
    total_profit = knapsack.optimised_collection_greedy(collection)
    items_taken = knapsack.get_content
    print(f"\nOur total profit is: {total_profit}.\n"
            + f"Our collected items are: {items_taken}.\n")

if __name__ == "__main__":
    main()
        
        
        
        
        
        
