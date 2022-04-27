import what3words


def get_what3words(c1, c2):
    geocoder = what3words.Geocoder('YB59FL4H')
    res = geocoder.convert_to_3wa(what3words.Coordinates(c1, c2)).get('words')
    return res


print(get_what3words(13.078736, 80.249492))
