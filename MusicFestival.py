artists = {}


def request():
    answer = input("Enter a musician:   ").strip()
    answer = answer.lower().title()

    if answer == "Done":
        print_artists()
        return

    artists[answer] = artists.get(answer, 0) + 1
    request()


def print_artists():
    sorted_Alphabetical = dict(sorted(artists.items()))
    print("Artists and their counts:")
    for artist, count in sorted_Alphabetical.items():
        print(f"{artist}: {count}")


request()
