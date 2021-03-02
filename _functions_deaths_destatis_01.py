#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.special import betainc

# various helper functions
def corrcoef(matrix):
    ''' 
    r: Pearson Correlation Coefficients
    p: PValues
    r,p returned as 2D Matrices
    dependencies: numpy, scipy.special (betainc)
    '''
    r = np.corrcoef(matrix)
    rf = r[np.triu_indices(r.shape[0], 1)]
    df = matrix.shape[1] - 2
    ts = rf * rf * (df / (1 - rf * rf))
    pf = betainc(0.5 * df, 0.5, df / (df + ts))
    p = np.zeros(shape=r.shape)
    p[np.triu_indices(p.shape[0], 1)] = pf
    p[np.tril_indices(p.shape[0], -1)] = p.T[np.tril_indices(p.shape[0], -1)]
    p[np.diag_indices(p.shape[0])] = np.ones(p.shape[0])
    return r, p
  
def get_row_from_sheet(
                        sheet_object,
                        set_row, 
                        set_col,
                        print_opt,
                        step_size, 
                        ):
    ''' 
    get a row from excel sheet
    dependencies: xlrd
    '''
    list_row = []
    num_cols = sheet_object.ncols   # Number of columns
    # print("\nCols: Outputs") 
    for idx_1 in range(set_col,num_cols,step_size):
        list_row.append(sheet_object.cell_value(set_row-1, idx_1-1))
        if print_opt:
            print(sheet_object.cell_type(set_row-1, idx_1-1)) # type: 1 = text, type: 0 = empty, row, col
            print(sheet_object.cell_value(set_row-1, idx_1-1)) # row, col
    return list_row

def get_col_from_sheet(
                        sheet_object,
                        set_row, 
                        set_col,
                        print_opt,
                        step_size, 
                        ):
    ''' 
    get a col from excel sheet
    dependencies: xlrd
    '''
    list_col = []
    num_rows = sheet_object.nrows   # Number of columns
    # print("\nCols: Outputs") 
    for idx_1 in range(set_row,num_rows+1,step_size):
        list_col.append(sheet_object.cell_value(idx_1-1, set_col-1))
        if print_opt:
            print(sheet_object.cell_type(idx_1-1, set_col-1)) # type: 1 = text, type: 0 = empty, row, col
            print(sheet_object.cell_value(idx_1-1, set_col-1)) # row, col
    return list_col
   

 

   

 
 

