def reducearray(array):
    while len(array) > 1:
        sum = int(abs(array[0] + array[-1]))
        x = sum % len(array)
        del array[x - 1]
    return array


if __name__ == "__main__":
    samplearray = [1, 3, 2, 4, 6]
    reduced = reducearray(samplearray)
    print(reduced)
