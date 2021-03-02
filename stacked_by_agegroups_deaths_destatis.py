#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Purpose: Correlations on Death data by destatis
Date: 01/2021
Version: V01
Links: https://realpython.com/numpy-scipy-pandas-correlation-python/#example-scipy-correlation-calculation
       https://stackoverflow.com/questions/24432101/correlation-coefficients-and-p-values-for-all-pairs-of-rows-of-a-matrix
"""
import numpy as np
import xlrd
import matplotlib as plt2
import matplotlib.pyplot as plt

# import dependencies (globals and functions)
import _globals_deaths_destatis_01 as hg
import _functions_deaths_destatis_01 as hf

# Todo: !! define location of excel-sheet: name and path
sheet_name_01 = "sonderauswertung-sterbefaelle.xlsx"
path_01 = "C:\\..\ToDo!!\set path of sonderauswertung-sterbefaelle.xlsx excel sheet here\\"


if __name__ == '__main__':
    ##################################################################################################
    # read in excel sheets (by XLRD)
    book = xlrd.open_workbook(
                            path_01 + sheet_name_01, 
                            on_demand=True, 
                            encoding_override = "utf-8"
                            )
    sheet_list = book.sheet_names()
    print("\nsheet_list" + ", len:", len(sheet_list))
    print(*sheet_list, sep = "\n")

    # read in data from sheets
    sheet_01 = book.sheet_by_index(4) # D_2016_2020_KW_AG_Ins
    sheet_02 = book.sheet_by_index(7) # D_2016-2020_Monate_AG_Ins

    ##################################################################################################
    # import data: only for 2020: import CW 53!!
    list_02 = hf.get_col_from_sheet(
                                    sheet_01, # sheet_object
                                    10, # set_row, like excel, start with idx one, 14-261 (see: num_rows)
                                    56, # set_col, J=10, (see: num_cols)
                                    False, # print_opt
                                    1, # step_size
                                    )
    # print(list_02)

    ##################################################################################################
    # import data: yearly cw data, deaths by age groups
    list_of_array_yr = []
    for idx_1 in range(0,len(hg.annual_header),1):
        cnt_year = idx_1 * len(hg.age_groups)
        array_yr = np.zeros(shape=(len(hg.age_groups),len(hg.cw_header))).astype(int)
        if idx_1 == 0: # special: add 2020: CW53
            array_yr = np.zeros(shape=(len(hg.age_groups),len(hg.cw_header)+1)).astype(int)
            
        for idx_2 in range(0,len(hg.age_groups),1):
            list_01 = hf.get_row_from_sheet(
                                        sheet_01, # sheet_object
                                        10 + cnt_year + idx_2, # set_row, like excel
                                        4, # set_col, e.g. J=10
                                        False, # print_opt
                                        1, # step_size
                                        )

            if idx_1 == 0: # special: add 2020: CW53
                list_01.append(list_02[idx_2])
            array_yr[idx_2,:] = np.array(list_01)

        list_of_array_yr.append(array_yr)

    # optional: print all years: cw data
    print("\nYears: " , hg.annual_header, ", len:", len(list_of_array_yr))
    print(*list_of_array_yr, sep = "\n")

    ##################################################################################################
    # visualisation with matplotlib 
    ##################################################################################################

    ##################################################################################################
    # fig: annual cw data, deaths by age groups
    # style total layout with size in lists for each plot
    widths = [1,]
    heights = [2,0]
    gs_kw = dict(width_ratios=widths, height_ratios=heights)
    fig1, ax1 = plt.subplots(nrows=2, ncols=1, figsize=(8, 8), gridspec_kw=gs_kw)

    # do not show 2nd plot
    ax1[1].axis('off')
    ax1[1].axis('tight')

    ##################################################################################################
    # create list of lists with arrays for all age groups
    list_of_list_yrs_age_groups = []
    for idx_1 in range(1,len(hg.age_groups[1:])+1,1):
        list_of_list_yrs_age_groups.append(np.empty(shape=[0], dtype=int))

    # for idx_1 in range(0,len(hg.annual_header),1):
    for idx_1 in range(len(hg.annual_header)-1,0-1,-1): # reverse 2016-2020
        for idx_2 in range(1,len(hg.age_groups[1:])+1,1):
            
            # classification: age groups, for stacked plots
            list_tmp_01 = []
            for idx_3 in range(1,idx_2+1,1):
                list_tmp_01.append(list_of_array_yr[idx_1][idx_3])
            # sum-up vertically, and stack horizontally annual data
            list_of_list_yrs_age_groups[idx_2-1] = np.append(list_of_list_yrs_age_groups[idx_2-1],\
                 np.sum(np.array(list_tmp_01), axis = 0), axis = 0)
            
    ##################################################################################################
    # plot age groups
    ax1[0].set_title("German CW Deaths stacked by Age Groups (s:destatis)", fontsize=11)
    # choose html color families:
    hmtl_colors_list = list(reversed(hg.hmtl_colors_10)) +\
                                    hg.hmtl_colors_09 +\
                                    hg.hmtl_colors_08 +\
                                    hg.hmtl_colors_06
    # set limits for axis, grid, etc. ..
    x2 = np.arange(1, 52*5+2, 1) # cws
    y_min = 0
    y_max = 35000
    yticks2 = np.arange(y_min, y_max, 5000)
    yrange2 = (yticks2[0], yticks2[-1])
    xrange2 = (x2[0], x2[-1])
    xticks2 = np.arange(1, 52*5+1, 52)

    # do manually: vertical grid (due to CW 53)
    ax1[0].grid(True, color='grey', alpha=0.5, linestyle='solid',axis='y')
    ax1[0].axvline(x=52, ymin=y_min, ymax=y_max, linewidth=1, color='grey', alpha=0.5, linestyle='solid')
    ax1[0].axvline(x=52*2, ymin=y_min, ymax=y_max, linewidth=1, color='grey', alpha=0.5, linestyle='solid')
    ax1[0].axvline(x=52*3, ymin=y_min, ymax=y_max, linewidth=1, color='grey', alpha=0.5, linestyle='solid')
    ax1[0].axvline(x=52*4, ymin=y_min, ymax=y_max, linewidth=1, color='grey', alpha=0.5, linestyle='solid')
    
    # major xticks
    x_pos = 52
    x_list_empty = [''] * len(hg.annual_header)
    x_locator = plt2.ticker.FixedLocator([x_pos*1, x_pos*2, x_pos*3, x_pos*4, x_pos*5])
    x_formatter = plt2.ticker.FixedFormatter(x_list_empty)
    ax1[0].xaxis.set_major_locator(x_locator)
    ax1[0].xaxis.set_major_formatter(x_formatter)
    ax1[0].tick_params(which='major', axis="x", direction="out", length=2, width=1, color="black")
    ax1[0].set_xlabel(' ', fontsize=9)
    
    # minor xticks
    x_pos2 = 26
    annual_header_reverse = list(reversed(hg.annual_header))
    x_locator2 = plt2.ticker.FixedLocator([x_pos2*1, x_pos2*3, x_pos2*5, x_pos2*7, x_pos2*9])
    x_formatter2 = plt2.ticker.FixedFormatter(annual_header_reverse)
    ax1[0].xaxis.set_minor_locator(x_locator2)
    ax1[0].xaxis.set_minor_formatter(x_formatter2)
    ax1[0].tick_params(which='minor', axis="x", direction="in", length=0, width=0, color="white")
    ax1[0].yaxis.set_minor_locator(plt2.ticker.MultipleLocator(1000))
    ax1[0].set_ylabel('CW Deaths', fontsize=8)
    ax1[0].set_yticks(yticks2)
    ax1[0].set_yticklabels(list(yticks2), fontsize=8)
    ax1[0].set_xlim(xrange2)
    ax1[0].set_ylim(yrange2)
    box = ax1[0].get_position() # shrink current axis by 20%
    ax1[0].set_position([box.x0, box.y0, box.width * 0.8, box.height])
    
    # plot data and legend
    for idx_1 in range(len(list_of_list_yrs_age_groups)-1,-1,-1):
        ax1[0].plot(x2, list_of_list_yrs_age_groups[idx_1],label=hg.age_groups[idx_1+1],color=hmtl_colors_list[idx_1+1])
    ax1[0].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)

    # final options
    fig1.tight_layout()
    fig1.subplots_adjust(top=0.90)
    fig1.subplots_adjust(bottom=0.1)
    fig1.subplots_adjust(right = 0.85)
    plt.show()

   

 
 

