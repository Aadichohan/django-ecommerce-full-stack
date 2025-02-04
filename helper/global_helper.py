def dictArrayToDict(data):
    data       = dict(data)
    final_dict = {}
    for x in data:
        final_dict[x] = data[x][0]
    return final_dict