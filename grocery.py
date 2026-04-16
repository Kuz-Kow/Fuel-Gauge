def main():
    grocerys()


def grocerys():
    item_list = {}
    while True:

        try:

            item = input("").title()

            if item in item_list:
                item_list[item] = item_list[item] + 1

            else:
                item_list[item] = 1
            
        except EOFError:
            show_list(item_list)
            break

        except KeyError:
            continue

def show_list(item_list):
    sorted(item_list)
    for item_name in item_list:
        print(f"{item_list[item_name]} {item_name}")




main()