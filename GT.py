class GroceryListManager:
    def __init__(self):
        self.items = []
        self.categories = ["Fruits", "Vegetables", "Dairy", "Meat", "Other"]
    
    def display_welcome(self):
        print("\n" + "="*50)
        print("  GROCERY LIST MANAGER")
        print("="*50)
    
    def display_menu(self):
        print("\n--- MENU ---")
        print("1. Add grocery item")
        print("2. View all items")
        print("3. Calculate total cost")
        print("4. Filter items by category")
        print("5. Find most and least expensive items")
        print("6. Remove an item")
        print("7. Exit")
        print("-" * 30)
    
    def add_item(self):
        print("\n--- ADD GROCERY ITEM ---")
        name = input("Enter item name: ").strip()
        
        if not name:
            print("Error: Item name cannot be empty!")
            return
        
        try:
            price = float(input("Enter price per unit: $"))
            if price < 0:
                print("Error: Price cannot be negative!")
                return
            
            quantity = int(input("Enter quantity: "))
            if quantity < 1:
                print("Error: Quantity must be at least 1!")
                return
            
            print("\nAvailable categories:")
            for i, cat in enumerate(self.categories, 1):
                print(f"{i}. {cat}")
            
            cat_choice = int(input("Select category (1-5): "))
            if cat_choice < 1 or cat_choice > 5:
                print("Error: Invalid category selection!")
                return
            
            category = self.categories[cat_choice - 1]
            
            item = {
                'name': name,
                'price': price,
                'quantity': quantity,
                'category': category
            }
            
            self.items.append(item)
            print(f"\n✓ '{name}' added successfully!")
            
        except ValueError:
            print("Error: Invalid input! Please enter numbers for price and quantity.")
    
    def view_items(self):
        if not self.items:
            print("\nYour grocery list is empty!")
            return
        
        print("\n" + "="*80)
        print(f"{'ITEM':<20} {'PRICE/UNIT':<12} {'QUANTITY':<10} {'TOTAL':<12} {'CATEGORY':<15}")
        print("="*80)
        
        for item in self.items:
            total = item['price'] * item['quantity']
            print(f"{item['name']:<20} ${item['price']:<11.2f} {item['quantity']:<10} ${total:<11.2f} {item['category']:<15}")
        
        print("="*80)
    
    def calculate_total(self):
        if not self.items:
            print("\nYour grocery list is empty!")
            return
        
        total = sum(item['price'] * item['quantity'] for item in self.items)
        print(f"\n{'='*40}")
        print(f"TOTAL COST: ${total:.2f}")
        print(f"{'='*40}")
    
    def filter_by_category(self):
        if not self.items:
            print("\nYour grocery list is empty!")
            return
        
        print("\nAvailable categories:")
        for i, cat in enumerate(self.categories, 1):
            print(f"{i}. {cat}")
        
        try:
            cat_choice = int(input("Select category to filter (1-5): "))
            if cat_choice < 1 or cat_choice > 5:
                print("Error: Invalid category selection!")
                return
            
            category = self.categories[cat_choice - 1]
            filtered = [item for item in self.items if item['category'] == category]
            
            if not filtered:
                print(f"\nNo items found in '{category}' category.")
                return
            
            print(f"\n--- ITEMS IN '{category.upper()}' CATEGORY ---")
            print("="*80)
            print(f"{'ITEM':<20} {'PRICE/UNIT':<12} {'QUANTITY':<10} {'TOTAL':<12} {'CATEGORY':<15}")
            print("="*80)
            
            for item in filtered:
                total = item['price'] * item['quantity']
                print(f"{item['name']:<20} ${item['price']:<11.2f} {item['quantity']:<10} ${total:<11.2f} {item['category']:<15}")
            
            print("="*80)
            
        except ValueError:
            print("Error: Invalid input!")
    
    def find_extremes(self):
        if not self.items:
            print("\nYour grocery list is empty!")
            return
        
        most_expensive = max(self.items, key=lambda x: x['price'])
        least_expensive = min(self.items, key=lambda x: x['price'])
        
        print("\n" + "="*50)
        print("MOST EXPENSIVE ITEM:")
        print(f"  {most_expensive['name']} - ${most_expensive['price']:.2f} per unit")
        print(f"  Category: {most_expensive['category']}")
        print("\nLEAST EXPENSIVE ITEM:")
        print(f"  {least_expensive['name']} - ${least_expensive['price']:.2f} per unit")
        print(f"  Category: {least_expensive['category']}")
        print("="*50)
    
    def remove_item(self):
        if not self.items:
            print("\nYour grocery list is empty!")
            return
        
        print("\n--- CURRENT ITEMS ---")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item['name']} (${item['price']:.2f} x {item['quantity']}) - {item['category']}")
        
        try:
            choice = int(input("\nEnter item number to remove: "))
            if choice < 1 or choice > len(self.items):
                print("Error: Invalid item number!")
                return
            
            removed = self.items.pop(choice - 1)
            print(f"\n✓ '{removed['name']}' removed successfully!")
            
        except ValueError:
            print("Error: Invalid input!")
    
    def run(self):
        self.display_welcome()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.add_item()
                elif choice == '2':
                    self.view_items()
                elif choice == '3':
                    self.calculate_total()
                elif choice == '4':
                    self.filter_by_category()
                elif choice == '5':
                    self.find_extremes()
                elif choice == '6':
                    self.remove_item()
                elif choice == '7':
                    print("\n" + "="*50)
                    print("Thank you for using Grocery List Manager!")
                    print("Goodbye!")
                    print("="*50 + "\n")
                    break
                else:
                    print("\nError: Invalid choice! Please enter a number between 1 and 7.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Exiting gracefully...")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")


# Run the program
if __name__ == "__main__":
    manager = GroceryListManager()
    manager.run()