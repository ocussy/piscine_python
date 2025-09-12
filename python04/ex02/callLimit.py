def callLimit(limit: int):
    """     callLimit(limit):
    returns a decorator that limits the number
    of times a function can be called"""
    def callLimiter(function):
        """     callLimiter(function):
        decorator that wraps a function to limit its calls"""
        count = 0

        def limit_function(*args: any, **kwargs: any):
            """     limit_function(*args, **kwargs):
            wrapper function that tracks and limits function calls"""
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwargs)
            else:
                # id(function) -> adresse memoire
                # hex(num) -> hexadecimal
                print(f"Error: <function {function.__name__} at"
                      f"{hex(id(function))}> call too many times")
        return limit_function
    return callLimiter
