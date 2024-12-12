import json
import numpy as np
from collections import defaultdict

#Парсинг#
def parsing(review_str):
    return json.loads(review_str)


def create(args):
    template = defaultdict(int)
    reviews_count = 0
    for el in json.loads(args[0]):
        if isinstance(el, list):
            for elem in el:
                template[elem] = reviews_count
                reviews_count += 1
        else:
            template[el] = reviews_count
            reviews_count += 1
    return template, reviews_count


def matrix(temp, *reviews):
    total = []
    for reviews_str in reviews:
        reviews = parsing(reviews_str)
        reviewList = [0] * len(temp)

        for i, review in enumerate(reviews):
            if isinstance(review, list):
                for elem in review:
                    reviewList[temp[elem]] = i + 1
            else:
                reviewList[temp[review]] = i + 1

        total.append(reviewList)

    return total


def calculate(matrix, reviews_count, experts_count):
    sums = np.sum(np.array(matrix), axis=0)
    D = np.var(sums) * reviews_count / (reviews_count - 1)
    D_max = experts_count ** 2 * (reviews_count ** 3 - reviews_count) / 12 / (reviews_count - 1)

    return D / D_max


def task(*args):
    template, reviews_count = create(args)
    matrix = matrix(template,  *args)
    result = calculate(matrix, reviews_count, len(args))

    return result


if __name__ == '__main__':
    one = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
    two = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
    three = '["3", ["1", "4"], "2", "6", ["5", "7", "8"], ["9", "10"]]'

    print(format(task(one, two, three), '.2f'))