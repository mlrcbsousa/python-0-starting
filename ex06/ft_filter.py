def ft_filter(fn, iterable: iter) -> iter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    return [item for item in iterable if (item if fn is None else fn(item))]

# The basic syntax of a list comprehension is:
#   [expression for item in iterable if condition]
