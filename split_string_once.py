def split_once(mystr, separators=None):
    splitted_result = list()
    if separators is None:
        splitted_result = mystr.split()
    else:
        for separator in separators:
            _, mystr = mystr.split(sep=separator, maxsplit=1)
            splitted_result.append(_)
        splitted_result.append(mystr)
    # print(mystr)
    print(splitted_result)
