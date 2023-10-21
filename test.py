def dijkstra(dutch):
    """

    :param dutch:
    :precondition:
    :postcondition:

    >>> test = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
    >>> dijkstra(test)
    >>> print(test)
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']

    >>> test = ['blue']
    >>> dijkstra(test)
    >>> print(test)
    ['blue']
    """
    red_list = []
    white_list = []
    blue_list = []
    for color in dutch:
        if color == 'red':
            red_list.append(color)
        elif color == 'white':
            white_list.append(color)
        else:
            blue_list.append(color)
    dutch.clear()
    dutch += (red_list + white_list + blue_list)


def main():
    dutch = ['blue', 'white', 'red']
    dijkstra(dutch)
    print(dutch)


if __name__ == "__main__":
    main()

