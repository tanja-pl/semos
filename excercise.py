import csv

def enter_items():
    with open('items.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        while True:
            entry = input("Vnesi produkt i cena vo csv format primer: mleko,100, da zavrsis stisni q: ").strip()
            if entry.lower() == 'q':
                break
            try:
                product, price = entry.split(',')
                writer.writerow([product.strip(), float(price.strip())])
            except ValueError:
                print("Vnesi vo format produkt, price.")

def calculate(items):
    try:
        with open('items.csv', mode='r') as file:
            reader = csv.reader(file)
            items = [(row[0], float(row[1])) for row in reader]
            if not items:
                print("Nema vneseno nisto.")
                return

            total = sum(price for _, price in items)
            average = total / len(items)
            most_expensive = max(items, key=lambda x: x[1])
            cheapest = min(items, key=lambda x: x[1])

            print("Vkupno:", total)
            print("Najskap proizvod:", most_expensive[0])
            print("Najeftin proizvod:", cheapest[0])
            print("Prosecen proizvod:", average)
    except FileNotFoundError:
        print("Datotekata ne postoi.")

def main():
    print("Odberi a za input i b za statistics:")
    print("a. input")
    print("b. statistics")

    while True:
        mode = input(">> ").strip().lower()
        if mode == 'a':
            enter_items()
        elif mode == 'b':
            calculate(None)
        else:
            print("Odberete pomegu a i b: 'a' or 'b'.")

if __name__ == "__main__":
    main()