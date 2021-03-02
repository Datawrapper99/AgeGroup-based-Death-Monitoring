#!/usr/bin/env python
# -*- coding: utf-8 -*-


# define globals
age_groups = [
"Total",
"00-29",
"30-34",
"35-39",
"40-44",
"45-49",
"50-54",
"55-59",
"60-64",
"65-69",
"70-74",
"75-79",
"80-84",
"85-89",
"90-94",
"95+",
]

annual_header = [
"2020", # with 29.02, 53CWs
"2019",
"2018",
"2017",
"2016", # with 29.02
]

cw_header = [
"01",
"02",
"03",
"04",
"05",
"06",
"07",
"08",
"09",
"10",
"11",
"12",
"13",
"14",
"15",
"16",
"17",
"18",
"19",
"20",
"21",
"22",
"23",
"24",
"25",
"26",
"27",
"28",
"29",
"30",
"31",
"32",
"33",
"34",
"35",
"36",
"37",
"38",
"39",
"40",
"41",
"42",
"43",
"44",
"45",
"46",
"47",
"48",
"49",
"50",
"51",
"52",
]

# get some html colors:
# https://www.htmlcsscolor.com/hex/5733FF

# Tints of ForestGreen
hmtl_colors_01 = [
                    "#228B22", 
                    "#4EA24E",
                    "#71B571",
                    "#8DC48D",
                    "#A4D0A4",
                    "#B6D9B6",
                    "#C5E1C5",
                    "#D1E7D1",
                    "#DAECDA",
                    "#E1F0E1",
                    ]
# Tints of Sea Green
hmtl_colors_02 = [
                    "#228B56", 
                    "#4EA278",
                    "#71B593",
                    "#8DC4A9",
                    "#A4D0BA",
                    "#B6D9C8",
                    "#C5E1D3",
                    "#D1E7DC",
                    "#DAECE3",
                    "#E1F0E9",
                    ]

# Tints of Outrageous Orange
hmtl_colors_03 = [
                "#FF5733",
                "#FF795C",
                "#FF947D",
                "#FFA997",
                "#FFBAAC",
                "#FFC8BD",
                "#FFD3CA",
                "#FFDCD5",
                "#FFE3DD",
                "#FFE9E4",
                ]

# Tints of Han Purple
hmtl_colors_04 = [
                "#5733FF",
                "#795CFF",
                "#947DFF",
                "#A997FF",
                "#BAACFF",
                "#C8BDFF",
                "#D3CAFF",
                "#DCD5FF",
                "#E3DDFF",
                "#E9E4FF",
                ]

# https://www.htmlcsscolor.com/hex/33FF66

# Monochromatic: Outrageous Orange
hmtl_colors_05 = [
# "#FED9CC", # rgb(254,217,204)
"#FFB39A", # rgb(255,179,154)
"#BF8673", # rgb(191,134,115)
"#BF4C26", # rgb(191,76,38)
"#7F331A", # rgb(127,51,26)
"#5F2613", # rgb(95,38,19)
]

# Monochromatic: Screamin' Green
hmtl_colors_06 = [
# "#CCFED9", # rgb(204,254,217)
# "#9AFFB3", # rgb(154,255,179)
"#73BF86", # rgb(115,191,134)
"#26BF4C", # rgb(38,191,76)
"#1A7F33", # rgb(26,127,51)
# "#135F26", # rgb(19,95,38)
]


# Monochromatic: Shades of Deep Fir Green
hmtl_colors_07 = [
# "#C3D0C6", # rgb(195,208,198)
"#87A18E", # rgb(135,161,142)
"#65786A", # rgb(101,120,106)
"#0A3114", # rgb(10,49,20)
"#07210E", # rgb(7,33,14)
# "#05180A", # rgb(5,24,10)
]

# Monochromatic: Shades of Fruit Salad Green
hmtl_colors_08 = [
# "#CEE9D0", # rgb(206,233,208)
# "#9DD4A1", # rgb(157,212,161)
"#759F78", # rgb(117,159,120)
"#2A7E31", # rgb(42,126,49)
"#1D5421", # rgb(29,84,33)
"#153F18", # rgb(21,63,24)
]


# Monochromatic: Shades of Apple Green
hmtl_colors_09 = [
# "#D9E9CE", # rgb(217,233,206)
# "#B4D49D", # rgb(180,212,157)
"#879F75", # rgb(135,159,117)
"#4E7E2A", # rgb(78,126,42)
"#34541D", # rgb(52,84,29)
"#273F15", # rgb(39,63,21)
]


# Monochromatic: red
hmtl_colors_10 = [
# "#FEBFBF", # rgb(254,191,191)
"#FF8080", # rgb(255,128,128)
"#BF6060", # rgb(191,96,96)
"#BF0000", # rgb(191,0,0)
"#7F0000", # rgb(127,0,0)
"#5F0000", # rgb(95,0,0)
]

# non-seasonal age bands summed up manually, todo: sum up by numpy
#2020-2016 
death_percentage_5sig = [
    "5.1%",
    "5.4%",
    "2.1%",
    "5.8%",
    "6.2%",
]






   

 
 

