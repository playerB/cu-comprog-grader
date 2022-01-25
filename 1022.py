import numpy as np

def mult_table(nrows, ncols):
    rows = np.arange(1, nrows + 1).reshape((nrows, 1))
    cols = np.arange(1, ncols + 1).reshape((1, ncols))
    return rows.dot(cols)

exec(input().strip())