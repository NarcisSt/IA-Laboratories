from collections import Counter


def groupSort(arr):
    freq = {}
    for element in arr:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    freq2 = dict(sorted(freq.items(), key=lambda x: (-x[1], x[0])))
    table = []
    for key, value in freq2.items():
        table.append([key, value])

    print(table)


if __name__ == '__main__':
    array = [1, 1, 3, 5, 5, 4, 4, 1, 10, 10, 9, 123421, 123421]
    groupSort(array)