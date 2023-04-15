if __name__ == '__main__':
    items = {}
    best_item = None
    best_ratio = 0

    while True:
        item_name = input("\nEnter name of item ['done' to exit]: ")
        if item_name.lower() == "done":
            break
        item_price = float(input(f"Enter price of {item_name}\t: RM "))
        item_quantity = float(input(f"Enter quantity of {item_name}\t: "))
        items[item_name] = {"price": item_price, "quantity\t": item_quantity}
        item_ratio = item_price / item_quantity
        print(f"Price to quantity ratio of {item_name}\t: RM{item_ratio:.2f} per unit")

        if item_ratio < best_ratio or len(list(items.keys())) == 1:
            best_ratio = item_ratio
            best_item = item_name
        print(f"\n=============================================================\nCurrent best\t: {best_item} (RM{best_ratio:.2f} per unit)\n=============================================================")

    if best_item:
        print(f"\nThe best item is {best_item}\t: RM{best_ratio:.2f} per unit")
    else:
        print("You did not enter any items.")
