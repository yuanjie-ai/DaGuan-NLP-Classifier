import time
import pandas as pd


@execution_time
def reader_pandas_(file, chunkSize=10000):
    reader = pd.read_csv(file, iterator=True)
    chunks =[]
    while 1:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            break
    return pd.concat(chunks, ignore_index=True)


def execution_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        tmp = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print("""Executing Time of "%s": %.3f s""" % (func.__name__, t))
        return tmp
    return wrapper
