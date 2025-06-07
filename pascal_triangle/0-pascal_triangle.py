#!/usr/bin/python3
"""
0-pascal-triangle: a function that generate pascal
triangle
"""


def generate_new_pascal_row(rowNumber, previousRow):
    """
    function that return new pascal row
        args:
            rowNumber: the current row to be generated
            previousRow: the previous generated row

        return: new generated row
    """
    newList = []

    if (rowNumber == 1):
        return [1]

    if ((rowNumber > 1) and (len(previousRow) == rowNumber - 1)):
        for i in range(rowNumber):
            if (i == 0):
                newList.append(1)
                continue
            elif (i == rowNumber - 1):
                newList.append(1)
                continue
            else:
                newList.append(previousRow[i] + previousRow[i - 1])
                continue

    return newList


def pascal_triangle(n):
    """
    function to return pascal triangle
        n: triangle number of rows
    """
    pascalTriangleList = []

    if (n > 0):
        for i in range(n):
            if (len(pascalTriangleList) == 0):
                previousRow = []
            else:
                previousRow = pascalTriangleList[i - 1]

            pascalTriangleList.append(
                generate_new_pascal_row(
                    rowNumber=i + 1, previousRow=previousRow
                )
            )
        return pascalTriangleList
    else:
        return []
