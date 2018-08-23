import time
import pandas as pd
from tqdm import tqdm


@execution_time
def reader_pandas(file, chunkSize=100000, patitions=10 ** 4):
    reader = pd.read_csv(file, iterator=True)
    chunks = []
    with tqdm(range(patitions), 'Reading ...') as t:
        for _ in t:
            try:
                chunk = reader.get_chunk(chunkSize)
                chunks.append(chunk)
            except StopIteration:
                break
    return pd.concat(chunks, ignore_index=True)

