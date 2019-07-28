import math

__all__ = ["p", "convert_size", "chunks"]


def p(current_value, *args):
    # p
    # isinstance(f, types.FunctionType)
    for func in args:
        current_value = func(current_value)
    return current_value


def convert_size(size):
    size_bytes = int(size)
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s%s" % (s, size_name[i])


# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks#answer-312464
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]