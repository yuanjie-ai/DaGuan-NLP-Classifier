import time
import pandas as pd


@execution_time
def super_pandas_reader(path, chunkSize=10000):
    reader = pd.read_csv(path, iterator=True)
    loop =True
    chunks =[]
    while loop:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop =False
            print("Reading ...\n")
    df =pd.concat(chunks, ignore_index=True)
    return df

def execution_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        tmp = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print("""Executing Time of "%s": %.3f s""" % (func.__name__, t))
        return tmp
    return wrapper