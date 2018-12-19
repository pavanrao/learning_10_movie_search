import movie_svc
import requests

def print_header():
    print('----------------------------------------------------')
    print('                 Movie Service App                   ')
    print('----------------------------------------------------')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input("Which movie do you want to search? (x to exit)")
            if search != "x":
                results = movie_svc.find_mpovies(search)
                results.sort(key = lambda md : -md.year)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print("{} == {}".format(r.year, r.title))
                print()
        except requests.exceptions.ConnectionError as ce:
            print("Error: You network is down: {}".format(ce))
        except ValueError as x:
            print("Error: Search text is required")
        except Exception as e:
            print("Oh snap! something is broken :(")
            print("error: "+ type(e))

        print("exiting...")


def main():
    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()
