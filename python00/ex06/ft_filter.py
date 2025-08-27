def ft_filter(func, iterable):
    """
                                        filter(function, iterable)

        The filter() function is used to extract elements from an iterable.
        It works by applying a function to each element
        and keeping only those for which function returns True.
    """
    if not isinstance(iterable, (list, tuple, set, dict)):
        print("not iterable")
        return 1

    if func is None:
        for item in iterable:
            if item:
                yield item

    else:
        for item in iterable:
            if func(item):
                yield item
