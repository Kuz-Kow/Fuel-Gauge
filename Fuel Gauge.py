def main():
    print(amount())


def ask_user():
    return input("Fraction: ").strip()

def amount():

    while True:

        fraction = ask_user()

        try:
            x = int(fraction[0])
            y = int(fraction[2])
            result = int(x/y * 100)
            if(result > 100):
                continue

            return check_result(result)

        except ValueError:
            pass

        except ZeroDivisionError:
            pass
    


        




def check_result(result):


    if not result >= 0:
        raise ValueError("Negative value")

    if(result >= 99):
        return "F"

    elif(result <= 1):
        return "E"
    else:
        return  str(result) + "%"

main()
        
    