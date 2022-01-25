import numpy as np

def sum_2_rows(M):
    return M[0::2, :] + M[1::2, :]

def sum_left_right(M):
    return M[:, :M.shape[1]//2] + M[:, M.shape[1]//2:]

def sum_upper_lower(M):
    return M[:M.shape[1]//2, :] + M[M.shape[1]//2:, :]

def sum_4_quadrants(M):
    return M[:M.shape[1]//2, :M.shape[1]//2] + M[M.shape[1]//2:, M.shape[1]//2:] + M[M.shape[1]//2:, :M.shape[1]//2] + M[:M.shape[1]//2, M.shape[1]//2:]

def sum_4_cells(M):
    return M[0::2, 0::2] + M[1::2, 0::2] + M[0::2, 1::2] + M[1::2, 1::2]

def count_leap_years(years):
    return np.sum(((years -543) % 400 == 0) | (((years -543) % 100 != 0) & ((years -543) % 4 == 0)))

exec(input().strip())