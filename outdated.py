def main():
    formated()

def formated():

    monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        try:
            date = input("Date: ").strip()
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if(month > 12 or day > 31):
                raise Exception()

            
            
            print(f"{year}-{month:02}-{day:02}")
            
            break

        except ValueError:
            try: 
                month, day, year = date.split(" ")
                if month in monthes and day > 31:
                    day = int(day[0])
                    year = int(year)
                    month = monthes.index(month) + 1
                    print(f"{year}-{month:02}-{day:02}")
                    break


                else:
                    raise ValueError()
                

            except ValueError:
                continue

            except Exception:
                continue

        except Exception:
            continue


main()