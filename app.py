import pandas as pd
import numpy as np
import sys
import os
from xlrd import open_workbook,cellname
from scipy.optimize import linear_sum_assignment

def compute():

    oldcost = np.array([[35, 28, 25, 18, 15],
                        [27, 24, 17, 14,  9],
                        [33, 21, 24, 11, 16],
                        [16, 11, 27, 16, 22],
                        [14, 15, 33, 30, 23]])

    # 100 - 5-25 - 2-10 ...

    cost = np.array([[65, 72, 75, 82, 85],
                    [73, 76, 83, 86, 91],
                    [67, 79, 76, 89, 84],
                    [84, 89, 73, 84, 78],
                    [86, 85, 67, 70, 77]])

    row_ind, col_ind = linear_sum_assignment(cost)

    results = []

    # print(cost)
    # print(row_ind+1)
    # print(col_ind+1)
    #
    # print(cost[row_ind, col_ind].sum())
    #
    # for i, j in zip(row_ind, col_ind):
    #     print (i, j)
    #     results.append(j)


    cwd = os.getcwd()
    file = 'HackathonDataNEW.xlsx'

    data = pd.read_excel(file)
    df = pd.DataFrame(data, columns= ['Product'])

    book = open_workbook('HackathonDataNEW.xlsx')
    sheet0 = book.sheet_by_index(0)
    # print (sheet0.name)
    # print (sheet0.nrows)
    # print (sheet0.ncols)
    #
    # print (sheet0.row(0))
    # print('radarada')
    # print (sheet0.col(0))

    # print('People')
    people = sheet0.col_values(0,1)
    # print(people)
    # print('#1')
    teams_col1 = sheet0.col_values(1,1)
    # print(teams_col1)
    # print('#2')
    teams_col2 = sheet0.col_values(2,1)
    # print(teams_col2)
    # print('#3')
    teams_col3 = sheet0.col_values(3,1)
    # print(teams_col3)
    # print('#4')
    teams_col4 = sheet0.col_values(4,1)
    # print(teams_col4)
    # print('#5')
    teams_col5 = sheet0.col_values(5,1)
    # print(teams_col5)

    teams_lists_tmp = teams_col1 + teams_col2 + teams_col3 + teams_col4 + teams_col5
    teams_lists = [x for x in teams_lists_tmp if x]

    sheet1 = book.sheet_by_index(1)
    # print (sheet1.name)
    # print (sheet1.nrows)
    # print (sheet1.ncols)


    # print('Teams')
    teams = sheet1.col_values(0,1)
    # print(teams)
    # print('Numbers')
    numbers = sheet1.col_values(1,1)
    # print(numbers)
    # print('#1')
    names_col1 = sheet1.col_values(2,1)
    # print(names_col1)
    # print('#2')
    names_col2 = sheet1.col_values(3,1)
    # print(names_col2)
    # print('#3')
    names_col3 = sheet1.col_values(4,1)
    # print(names_col3)
    # print('#4')
    names_col4 = sheet1.col_values(5,1)
    # print(names_col4)
    # print('#5')
    names_col5 = sheet1.col_values(6,1)
    # print(names_col5)

    tuples_result = list(zip(teams, numbers))
    # print(tuples_result)

    names_list_tmp = names_col1 + names_col2 + names_col3 + names_col4 + names_col5
    names_list = [x for x in names_list_tmp if x]

    nameset = set((people))
    teamset = set((teams))
    chosen_teams = set((teams_lists))
    chosen_names = set((names_list))

    # for name in nameset:
    # print('nameset')
    # print(nameset)
    # print('teamset')
    # print(teamset)
    # print('chosen_teams')
    # print(chosen_teams)
    # print('chosen_names')
    # print(chosen_names)

    # print(teams_col1)

    bad_team = None

    for name in chosen_names:
        if (name not in nameset):
            print (name + " is not a valid input! Teams provided wrong data!")
            # names_col1.remove(name)
            bad_team = name
            # names_col2.remove(name)
            # names_col3.remove(name)
            # names_col4.remove(name)
            # names_col5.remove(name)


    for team in chosen_teams:
        if (team not in teamset):
            print (team + " is not a valid input! Grads provided wrong data!")
            # teams_col1.remove(team)
            # teams_col1[0] = ''
            # try: teams_col2.remove(team)
            # try: teams_col3.remove(team)
            # try: teams_col4.remove(team)
            # try: teams_col5.remove(team)

    # print(teams_col1)


    total_number_of_positions = 0
    for num in numbers:
        total_number_of_positions = total_number_of_positions + num

    # print(total_number_of_positions)
    # print(len(nameset))
    # print(len(teamset))

    adjusted_teams = []

    for name in tuples_result:
        # print(name[0] + " and " + str(int(name[1])))
        adjusted_teams.extend(name[0] for i in range(int(name[1])))

    # print(len(tuples_result))
    # print(len(adjusted_teams))
    #
    # print(adjusted_teams)

    lst = [[None] * int(total_number_of_positions)] * len(nameset)
    df = pd.DataFrame(100, index = people, columns = adjusted_teams)
    # print(df)
    # print('make not none')
    # df.fillna(0)

    # df.iloc[0]['Post Trading Technology'] = 100
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        # print(df)

    team_req = list(zip(teams, list(zip(names_col1, names_col2, names_col3, names_col4, names_col5))))
    # print(team_req)

    # new_team_req = filter(None, team_req)
    # print (new_team_req)
    teams_col1[0] = teams_col2[0]
    teams_col2[0] = teams_col3[0]
    teams_col3[0] = teams_col4[0]
    teams_col4[0] = teams_col5[0]
    teams_col5[0] = ''

    teams_col3[21] = teams_col4[21]
    teams_col4[21] = teams_col5[21]
    teams_col5[21] = ''

    grad_req = list(zip(people, list(zip(teams_col1, teams_col2, teams_col3, teams_col4, teams_col5))))
    # print(grad_req)
    print('He;l;p')
    # print(grad_req[0][1])
    # print(grad_req[21][1])
    # grad_req[0].remove(team)


    i = 0
    j = 5
    for entry in grad_req:
        # print(entry[0])
        for team in entry[1]:
            if (team):
                # print(team)
                tmp = j * 12
                df.iloc[i][team] = df.iloc[i][team] - tmp
                j = j - 1
            else:
                print('NO')
                j = j - 1
        j = 5
        i = i + 1

    i = 0
    j = 5
    for entry in team_req:
        # print(entry[0])
        for team in entry[1]:
            if(team):
                # print('thi siteam ' + str(team))
                tmp = j * 6
                location = int(people.index(team))
                # print('thi sis ' + str(location))
                # print('hslhashladfhljadfhlj ' + str(df.iloc[location][entry[0]]))
                # print(tmp)
                # print (df.iloc[location][entry[0]])
                df.iloc[location][entry[0]] = (df.iloc[location][entry[0]] - tmp)
                # print (df.iloc[location][entry[0]])
                j = j - 1
            else:
                print('NO ppl')
                j = j - 1
        j = 5
        i = i + 1

    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        # print(df)

    print(df["Post Trading Technology"])

    # print('team rew')
    # print(team_req)

    numpai = df.to_numpy()
    print(numpai)

    df.to_excel("output.xlsx")

    row_ind_new, col_ind_new = linear_sum_assignment(numpai)

    results_new = []

    # print(cost)
    print(row_ind_new + 1)
    print(col_ind_new + 1)

    print(numpai[row_ind_new, col_ind_new].sum())

    sum = 0
    for i, j in zip(row_ind_new, col_ind_new):
        print (i, j)
        sum = sum + j

    print (sum)

    final_teams = (adjusted_teams[team] for team in col_ind_new)
    result = list(zip(people, final_teams))

    # df2 = pd.DataFrame(result, index = people, columns = 'result')
    df2 = pd.DataFrame(result)
    df2.to_excel("output2.xlsx")


    print(result)


    # i = 0
    # j = 5
    # for entry in team_req:
    #     print(entry[0])
    #     for team in entry[1]:
    #         print(team)
    #         tmp = j * 10
    #         df.iloc[i][team] = df.iloc[i][team] - tmp
    #         j = j - 1
    #     j = 5
    #     i = i + 1

    # print(df)

    return result

compute()

# Teams
# Post Trading Technology
# Core Trading Technology
# Legal Software Architecture
# GTB: Trade Finance
# abFX Technology
# FX Risk Technology
# GTB Technology Surveillance
# Financial Spreading Automation
# Enterprise Risk Technology
# Sales, Origination & Advisory Information Technology
# Stategic Analytics
# FlowRisk
# CIB Tech: Data
# BRDS
# GTB Instant Payments
# Mercury Team
# Looking Glass
# Operations Automation
# CCNG
# DbSyndicate
# Fixed Income & Currencies Technology
# Distribution Technology
# Equity Strats
# Finance & Loan Agency
# Trade Services Technology
# Ratings Advisory Technology
# GT Production
# Test Delivery
# GTO - Data Solutions & Knowledge Visualisation
# Trade Finance Deal Management
# Cash Management Technology
# CIB Regulatory Adherence
# HR Digital Development
# Finance - GVG
# End User Production
# Vulnerability & Compliance Remediation
# Transition & Steering Office
# Enterprise Security Architecture
# Client Lifecycle Management
# End User Services
# AFC - Financial Crime Operations
# Trade Finance Operations
# Margin Loans
# Finance Control Oversight
#
#
#
# Graduates
# Danyal Schofield
# Chanel Leech
# Amy-Louise Conroy
# Syed Thompson
# Danny Connelly
# Mia Morley
# Briana Glass
# Shiv Rosas
# Melody Cook
# Willem Mcgill
# Tristan Hanna
# Annabella Crawford
# Florrie Thornton
# Yolanda Tyson
# Caitlin Browning
# Everly Holman
# Ruth Holder
# Chelsey Magana
# Karson Waller
# Arissa Mcmillan
# Marlon Osborn
# Courtnie Barker
# Mathias Becker
# Rio Wilkinson
# Vishal Logan
# Lauren Chang
# Alex Hulme
# Aiza Currie
# Maryam Lennon
# Ivan Nixon
# Lesley West
# Aida Curran
# Presley Sargent
# Anjali Bowden
# Derrick Sadler
# Nabilah Miles
# Jarod Arias
