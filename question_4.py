from __future__ import print_function

import math

from cubes import Workspace, Cell, PointCut
import time


# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="mysql://root@localhost/olapdb")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("london12")

# 3. Play with aggregates
result = browser.aggregate()

sport = []
agegroup = []
continent = []
gender = []
# all queries
query = []

# question 6_a
cv =[]
queries_a = []
def cv_function(result_a, query_a):
    global cv
    global queries_a
    medals = []
    substract = []
    sum_pow = 0
    variance = 0
    deviation_standard = 0
    medals_sum=0
    record_num = 0
    average = 0
    for record in result_a:
        medals.append(record["gold_sum"] + record["silver_sum"] + record["bronze_sum"])
        record_num = record_num + record["record_count"]
    for x in medals:
        medals_sum = medals_sum + x
    if record_num >= 100 and medals_sum >= 20:
        average = medals_sum / len(medals)
        for x in medals:
            substract.append(x - average)
        for x in substract:
            sum_pow = sum_pow + math.pow(x, 2)
        variance = sum_pow/len(substract)
        deviation_standard = math.sqrt(variance)
        cv.append(float(deviation_standard) / float(average))
        queries_a.append(query_a)


# question 6_b
queries_b = []
medals_records_ratio = []

def ratio_b(result,query_b):
    global medals_records_ratio
    global queries_b
    medals_num = 0
    record_num = 0
    for record in result:
        medals_num = record["gold_sum"] + record["silver_sum"] + record["bronze_sum"] + medals_num
        record_num = record_num + record["record_count"]
    if record_num >= 10:
        medals_records_ratio.append(medals_num / record_num)
        queries_b.append(query_b)

# question 6_c
total_medals= []
queries_c = []

def ratio_c(result_c,query_c):
    global total_medals
    global queries_c
    medals_num = 0
    silver_bronze_num = 0
    for record in result_c:
        medals_num = record["gold_sum"] + record["silver_sum"] + record["bronze_sum"] + medals_num
        silver_bronze_num = silver_bronze_num + record["silver_sum"] + record["bronze_sum"]
    if medals_num != 0 and silver_bronze_num/medals_num >= 0.9:
        total_medals.append(medals_num)
        queries_c.append(query_c)

# question 6_d
total_medals_2= []
queries_d = []

def ratio_d(result_d,query_d):
    global total_medals_2
    global queries_d
    medals_num = 0
    gold_num = 0
    for record in result_d:
        medals_num = record["gold_sum"] + record["silver_sum"] + record["bronze_sum"] + medals_num
        gold_num = gold_num + record["gold_sum"]
    if medals_num != 0 and gold_num/medals_num >= 0.5:
        total_medals_2.append(medals_num)
        queries_d.append(query_d)


result = browser.aggregate()
query1 = "'SELECT * FROM london12'"
query.append(query1)


result = browser.aggregate(drilldown=["sport"])
result1 = browser.aggregate(drilldown=["sport"])
result2 = browser.aggregate(drilldown=["sport"])
result3 = browser.aggregate(drilldown=["sport"])
query1="Drilldown='sport'"
query.append(query1)
for record in result:
    sport.append(record["sport.sport"])
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=["agegroup"])
result1 = browser.aggregate(drilldown=["agegroup"])
result2 = browser.aggregate(drilldown=["agegroup"])
result3 = browser.aggregate(drilldown=["agegroup"])
query1="Drilldown='agegroup'"
query.append(query1)
for record in result:
    agegroup.append(record["agegroup.agegroup"])
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=["location"])
result1 = browser.aggregate(drilldown=["location"])
result2 = browser.aggregate(drilldown=["location"])
result3 = browser.aggregate(drilldown=["location"])
query1="Drilldown='continent'"
query.append(query1)
for record in result:
    continent.append(record["location.continent"])
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=["gender"])
result1 = browser.aggregate(drilldown=["gender"])
result2 = browser.aggregate(drilldown=["gender"])
result3 = browser.aggregate(drilldown=["gender"])
query1="Drilldown='gender'"
query.append(query1)
for record in result:
    gender.append(record["gender.gender"])
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("agegroup", None, "agegroup"), ("sport", None, "sport")])
result1 = browser.aggregate(drilldown=[("agegroup", None, "agegroup"), ("sport", None, "sport")])
result2 = browser.aggregate(drilldown=[("agegroup", None, "agegroup"), ("sport", None, "sport")])
result3 = browser.aggregate(drilldown=[("agegroup", None, "agegroup"), ("sport", None, "sport")])
query1="Drilldown='sport , agegroup'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("location", None, "continent"), ("sport", None, "sport")])
result1 = browser.aggregate(drilldown=[("location", None, "continent"), ("sport", None, "sport")])
result2 = browser.aggregate(drilldown=[("location", None, "continent"), ("sport", None, "sport")])
result3 = browser.aggregate(drilldown=[("location", None, "continent"), ("sport", None, "sport")])
query1="Drilldown='sport , continent'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("gender", None, "gender"), ("sport", None, "sport")])
result1 = browser.aggregate(drilldown=[("gender", None, "gender"), ("sport", None, "sport")])
result2 = browser.aggregate(drilldown=[("gender", None, "gender"), ("sport", None, "sport")])
result3 = browser.aggregate(drilldown=[("gender", None, "gender"), ("sport", None, "sport")])
query1="Drilldown='sport , gender'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("location", None, "continent"), ("agegroup", None, "agegroup")])
result1 = browser.aggregate(drilldown=[("location", None, "continent"), ("agegroup", None, "agegroup")])
result2 = browser.aggregate(drilldown=[("location", None, "continent"), ("agegroup", None, "agegroup")])
result3 = browser.aggregate(drilldown=[("location", None, "continent"), ("agegroup", None, "agegroup")])
query1="Drilldown='agegroup , continent'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
result1 = browser.aggregate(drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
result2 = browser.aggregate(drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
result3 = browser.aggregate(drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
query1="Drilldown='agegroup , gender'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("gender", None, "gender"), ("location", None, "continent")])
result1 = browser.aggregate(drilldown=[("gender", None, "gender"), ("location", None, "continent")])
result2 = browser.aggregate(drilldown=[("gender", None, "gender"), ("location", None, "continent")])
result3 = browser.aggregate(drilldown=[("gender", None, "gender"), ("location", None, "continent")])
query1="Drilldown='continent , gender'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("location", None, "continent")])
result1 = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("location", None, "continent")])
result2 = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("location", None, "continent")])
result3 = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("location", None, "continent")])
query1="Drilldown='sport , agegroup ,continent'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
result1 = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
result2 = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
result3 = browser.aggregate(drilldown=[("sport",None,"sport"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
query1="Drilldown='sport , agegroup ,gender'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("location",None,"continent"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
result1 = browser.aggregate(drilldown=[("location",None,"continent"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
result2 = browser.aggregate(drilldown=[("location",None,"continent"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
result3 = browser.aggregate(drilldown=[("location",None,"continent"),("agegroup", None, "agegroup"), ("gender", None, "gender")])
query1="Drilldown=' agegroup , continent ,gender'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender")])
result1 = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender")])
result2 = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender")])
result3 = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender")])
query1="Drilldown=' sport, continent ,gender'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)

result = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender"),("agegroup", None, "agegroup")])
result1 = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender"),("agegroup", None, "agegroup")])
result2 = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender"),("agegroup", None, "agegroup")])
result3 = browser.aggregate(drilldown=[("location",None,"continent"),("sport", None, "sport"), ("gender", None, "gender"),("agegroup", None, "agegroup")])
query1="Drilldown=' sport, continent ,gender , agegroup'"
query.append(query1)
cv_function(result1,query1)
ratio_b(result,query1)
ratio_c(result2,query1)
ratio_d(result3,query1)





for item in sport:

    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["sport"])
    result1 = browser.aggregate(cell, drilldown=["sport"])
    result2 = browser.aggregate(cell, drilldown=["sport"])
    result3 = browser.aggregate(cell, drilldown=["sport"])
    query1 = "Slice='sport =%s'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("sport",[item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell,drilldown=["agegroup"])
    result1 = browser.aggregate(cell,drilldown=["agegroup"])
    result2 = browser.aggregate(cell,drilldown=["agegroup"])
    result3 = browser.aggregate(cell,drilldown=["agegroup"])
    query1 = "Slice='sport =%s' Drilldown='agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["location"])
    result1 = browser.aggregate(cell, drilldown=["location"])
    result2 = browser.aggregate(cell, drilldown=["location"])
    result3 = browser.aggregate(cell, drilldown=["location"])
    query1 = "Slice='sport =%s' Drilldown='continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["gender"])
    result1 = browser.aggregate(cell, drilldown=["gender"])
    result2 = browser.aggregate(cell, drilldown=["gender"])
    result3 = browser.aggregate(cell, drilldown=["gender"])
    query1 = "Slice='sport =%s' Drilldown='gender'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    query1 = "Slice='sport =%s' Drilldown='agegroup , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
    result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
    result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
    result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
    query1 = "Slice='sport =%s' Drilldown='agegroup , gender'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    query1 = "Slice='sport =%s' Drilldown='gender , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("sport", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
    result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
    result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
    result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
    query1 = "Slice='sport =%s' Drilldown='agegroup , gender , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

for item in agegroup:

    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["agegroup"])
    result1 = browser.aggregate(cell, drilldown=["agegroup"])
    result2 = browser.aggregate(cell, drilldown=["agegroup"])
    result3 = browser.aggregate(cell, drilldown=["agegroup"])
    query1 = "Slice='agegroup =%s'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("agegroup",[item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell,drilldown=["sport"])
    result1 = browser.aggregate(cell,drilldown=["sport"])
    result2 = browser.aggregate(cell,drilldown=["sport"])
    result3 = browser.aggregate(cell,drilldown=["sport"])
    query1 = "Slice='agegroup =%s' Drilldown='sport'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["location"])
    result1 = browser.aggregate(cell, drilldown=["location"])
    result2 = browser.aggregate(cell, drilldown=["location"])
    result3 = browser.aggregate(cell, drilldown=["location"])
    query1 = "Slice='agegroup =%s' Drilldown='continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["gender"])
    result1 = browser.aggregate(cell, drilldown=["gender"])
    result2 = browser.aggregate(cell, drilldown=["gender"])
    result3 = browser.aggregate(cell, drilldown=["gender"])
    query1 = "Slice='agegroup =%s' Drilldown='gender'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    query1 = "Slice='agegroup =%s' Drilldown='sport , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    query1 = "Slice='agegroup =%s' Drilldown='sport , gender'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
    query1 = "Slice='agegroup =%s' Drilldown='gender , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("agegroup", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
    result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
    result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
    result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
    query1 = "Slice='agegroup =%s' Drilldown='sport , gender , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

for item in continent:

    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["location"])
    result1 = browser.aggregate(cell, drilldown=["location"])
    result2 = browser.aggregate(cell, drilldown=["location"])
    result3 = browser.aggregate(cell, drilldown=["location"])
    query1 = "Slice='continent =%s'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("location",[item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell,drilldown=["sport"])
    result1 = browser.aggregate(cell,drilldown=["sport"])
    result2 = browser.aggregate(cell,drilldown=["sport"])
    result3 = browser.aggregate(cell,drilldown=["sport"])
    query1 ="Slice='continent =%s' Drilldown='sport'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["agegroup"])
    result1 = browser.aggregate(cell, drilldown=["agegroup"])
    result2 = browser.aggregate(cell, drilldown=["agegroup"])
    result3 = browser.aggregate(cell, drilldown=["agegroup"])
    query1 = "Slice='continent =%s' Drilldown='agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["gender"])
    result1 = browser.aggregate(cell, drilldown=["gender"])
    result2 = browser.aggregate(cell, drilldown=["gender"])
    result3 = browser.aggregate(cell, drilldown=["gender"])
    query1 = "Slice='continent =%s' Drilldown='gender'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    query1 = "Slice='continent =%s' Drilldown='sport , agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
    query1 = "Slice='continent =%s' Drilldown='sport , gender'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
    result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
    result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
    result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup")])
    query1 = "Slice='continent =%s' Drilldown='gender , agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("location", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
    result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
    result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
    result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
    query1 = "Slice='continent =%s' Drilldown='sport , gender , agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

for item in gender:

    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["gender"])
    result1 = browser.aggregate(cell, drilldown=["gender"])
    result2 = browser.aggregate(cell, drilldown=["gender"])
    result3 = browser.aggregate(cell, drilldown=["gender"])
    query1 = "Slice='gender =%s'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("gender",[item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell,drilldown=["sport"])
    result1 = browser.aggregate(cell,drilldown=["sport"])
    result2 = browser.aggregate(cell,drilldown=["sport"])
    result3 = browser.aggregate(cell,drilldown=["sport"])
    query1 = "Slice='gender =%s' Drilldown='sport'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["location"])
    result1 = browser.aggregate(cell, drilldown=["location"])
    result2 = browser.aggregate(cell, drilldown=["location"])
    result3 = browser.aggregate(cell, drilldown=["location"])
    query1 = "Slice='gender =%s' Drilldown='continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=["agegroup"])
    result1 = browser.aggregate(cell, drilldown=["agegroup"])
    result2 = browser.aggregate(cell, drilldown=["agegroup"])
    result3 = browser.aggregate(cell, drilldown=["agegroup"])
    query1 = "Slice='gender =%s' Drilldown='agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
    query1 ="Slice='gender =%s' Drilldown='sport , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
    query1 = "Slice='gender =%s' Drilldown='sport , agegroup'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)

    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
    query1 = "Slice='gender =%s' Drilldown='agegroup , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


    cut = PointCut("gender", [item])
    cell = Cell(browser.cube, cuts=[cut])
    result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
    result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
    result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
    result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
    query1 = "Slice='gender =%s' Drilldown='sport , agegroup , continent'" % (item)
    query.append(query1)
    cv_function(result1, query1)
    ratio_b(result, query1)
    ratio_c(result2, query1)
    ratio_d(result3, query1)


for item in sport:
    for item2 in agegroup:

        cut = PointCut("sport", [item])
        cut2 = PointCut("agegroup", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("sport", None, "sport")])
        result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("sport", None, "sport")])
        result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("sport", None, "sport")])
        result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("sport", None, "sport")])
        query1 = "Slice='sport = %s , agegroup = %s'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("agegroup",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["location"])
        result1 = browser.aggregate(cell, drilldown=["location"])
        result2 = browser.aggregate(cell, drilldown=["location"])
        result3 = browser.aggregate(cell, drilldown=["location"])
        query1 = "Slice='sport = %s , agegroup = %s' Drilldown='location'" % (item,item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("agegroup",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["gender"])
        result1 = browser.aggregate(cell, drilldown=["gender"])
        result2 = browser.aggregate(cell, drilldown=["gender"])
        result3 = browser.aggregate(cell, drilldown=["gender"])
        query1 = "Slice='sport = %s , agegroup = %s' Drilldown='gender'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("agegroup", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        query1 = "Slice='sport = %s , agegroup = %s' Drilldown='continent,gender'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

for item in sport:
    for item2 in gender:

        cut = PointCut("sport", [item])
        cut2 = PointCut("gender", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("sport", None, "sport"),("gender", None, "gender")])
        result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"),("gender", None, "gender")])
        result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"),("gender", None, "gender")])
        result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"),("gender", None, "gender")])
        query1 = "Slice='sport = %s , gender = %s'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("gender",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["location"])
        result1 = browser.aggregate(cell, drilldown=["location"])
        result2 = browser.aggregate(cell, drilldown=["location"])
        result3 = browser.aggregate(cell, drilldown=["location"])
        query1 = "Slice='sport = %s , gender = %s' Drilldown='location'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("gender",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["agegroup"])
        result1 = browser.aggregate(cell, drilldown=["agegroup"])
        result2 = browser.aggregate(cell, drilldown=["agegroup"])
        result3 = browser.aggregate(cell, drilldown=["agegroup"])
        query1 = "Slice='sport = %s , gender = %s' Drilldown='agegroup'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("gender", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        query1 = "Slice='sport = %s , gender = %s' Drilldown='agegroup , continent'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

for item in sport:
    for item2 in continent:

        cut = PointCut("sport", [item])
        cut2 = PointCut("location", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("location", None, "continent"),("sport", None, "sport")])
        result1 = browser.aggregate(cell, drilldown=[("location", None, "continent"),("sport", None, "sport")])
        result2 = browser.aggregate(cell, drilldown=[("location", None, "continent"),("sport", None, "sport")])
        result3 = browser.aggregate(cell, drilldown=[("location", None, "continent"),("sport", None, "sport")])
        query1 = "Slice='sport = %s , continent = %s'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("location",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["agegroup"])
        result1 = browser.aggregate(cell, drilldown=["agegroup"])
        result2 = browser.aggregate(cell, drilldown=["agegroup"])
        result3 = browser.aggregate(cell, drilldown=["agegroup"])
        query1 = "Slice='sport = %s , continent = %s' Drilldown='agegroup'" % (item,item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("location",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["gender"])
        result1 = browser.aggregate(cell, drilldown=["gender"])
        result2 = browser.aggregate(cell, drilldown=["gender"])
        result3 = browser.aggregate(cell, drilldown=["gender"])
        query1 = "Slice='sport = %s , continent = %s' Drilldown='gender'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("sport", [item])
        cut2 = PointCut("location", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
        result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
        result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
        result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("gender", None, "gender")])
        query1 = "Slice='sport = %s , continent = %s' Drilldown='agegroup,gender'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

for item in agegroup:
    for item2 in gender:

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("gender", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("gender", None, "gender")])
        result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("gender", None, "gender")])
        result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("gender", None, "gender")])
        result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"),("gender", None, "gender")])
        query1 = "Slice='agegroup = %s , gender = %s'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("gender",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["sport"])
        result1 = browser.aggregate(cell, drilldown=["sport"])
        result2 = browser.aggregate(cell, drilldown=["sport"])
        result3 = browser.aggregate(cell, drilldown=["sport"])
        query1 = "Slice='agegroup = %s , gender = %s' Drilldown='sport'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("gender",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["location"])
        result1 = browser.aggregate(cell, drilldown=["location"])
        result2 = browser.aggregate(cell, drilldown=["location"])
        result3 = browser.aggregate(cell, drilldown=["location"])
        query1 = "Slice='agegroup = %s , gender = %s' Drilldown='continent'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("gender", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
        result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
        result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
        result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("location", None, "continent")])
        query1 = "Slice='agegroup = %s , gender = %s' Drilldown='sport , continent'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)


for item in agegroup:
    for item2 in continent:

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("location", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent")])
        query1 = "Slice='agegroup = %s , continent = %s'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("location",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["sport"])
        result1 = browser.aggregate(cell, drilldown=["sport"])
        result2 = browser.aggregate(cell, drilldown=["sport"])
        result3 = browser.aggregate(cell, drilldown=["sport"])
        query1 = "Slice='agegroup = %s , continent = %s' Drilldown='sport'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("location",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["gender"])
        result1 = browser.aggregate(cell, drilldown=["gender"])
        result2 = browser.aggregate(cell, drilldown=["gender"])
        result3 = browser.aggregate(cell, drilldown=["gender"])
        query1 = "Slice='agegroup = %s , continent = %s' Drilldown='gender'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("agegroup", [item])
        cut2 = PointCut("location", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
        result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
        result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
        result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("gender", None, "gender")])
        query1 = "Slice='agegroup = %s , continent = %s' Drilldown='sport , gender'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

for item in gender:
    for item2 in continent:
        cut = PointCut("gender", [item])
        cut2 = PointCut("location", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent")])
        query1 = "Slice='gender = %s , continent = %s'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("gender", [item])
        cut2 = PointCut("location",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["sport"])
        result1 = browser.aggregate(cell, drilldown=["sport"])
        result2 = browser.aggregate(cell, drilldown=["sport"])
        result3 = browser.aggregate(cell, drilldown=["sport"])
        query1 = "Slice='gender = %s , continent = %s' Drilldown='sport'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("gender", [item])
        cut2 = PointCut("location",[item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=["agegroup"])
        result1 = browser.aggregate(cell, drilldown=["agegroup"])
        result2 = browser.aggregate(cell, drilldown=["agegroup"])
        result3 = browser.aggregate(cell, drilldown=["agegroup"])
        query1 = "Slice='gender = %s , continent = %s' Drilldown='agegroup'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

        cut = PointCut("gender", [item])
        cut2 = PointCut("location", [item2])
        cell = Cell(browser.cube, cuts=[cut, cut2])
        result = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
        result1 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
        result2 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
        result3 = browser.aggregate(cell, drilldown=[("sport", None, "sport"), ("agegroup", None, "agegroup")])
        query1 = "Slice='gender = %s , continent = %s' Drilldown='sport,agegroup'" % (item, item2)
        query.append(query1)
        cv_function(result1, query1)
        ratio_b(result, query1)
        ratio_c(result2, query1)
        ratio_d(result3, query1)

for item in sport:
    for item2 in agegroup:
        for item3 in gender:
            cut = PointCut("sport", [item])
            cut2 = PointCut("agegroup", [item2])
            cut3 = PointCut("gender", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
            result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
            result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
            result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("agegroup", None, "agegroup"),("sport", None, "sport")])
            query1 = "Slice='sport = %s , agegroup = %s , gender = %s'" % (item, item2, item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

            cut = PointCut("sport", [item])
            cut2 = PointCut("agegroup", [item2])
            cut3 = PointCut("gender", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=["location"])
            result1 = browser.aggregate(cell, drilldown=["location"])
            result2 = browser.aggregate(cell, drilldown=["location"])
            result3 = browser.aggregate(cell, drilldown=["location"])
            query1 = "Slice='sport = %s , agegroup = %s , gender = %s' Drilldown='continent'" % (item, item2,item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

for item in sport:
    for item2 in agegroup:
        for item3 in continent:
            cut = PointCut("sport", [item])
            cut2 = PointCut("agegroup", [item2])
            cut3 = PointCut("location", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
            result1 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
            result2 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
            result3 = browser.aggregate(cell, drilldown=[("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
            query1 = "Slice='sport = %s , agegroup = %s , continent = %s'" % (item, item2, item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

            cut = PointCut("sport", [item])
            cut2 = PointCut("agegroup", [item2])
            cut3 = PointCut("location", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=["gender"])
            result1 = browser.aggregate(cell, drilldown=["gender"])
            result2 = browser.aggregate(cell, drilldown=["gender"])
            result3 = browser.aggregate(cell, drilldown=["gender"])
            query1 = "Slice='sport = %s , agegroup = %s , continent = %s' Drilldown='gender'" % (item, item2,item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

for item in agegroup:
    for item2 in gender:
        for item3 in continent:
            cut = PointCut("agegroup", [item])
            cut2 = PointCut("gender", [item2])
            cut3 = PointCut("location", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
            result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
            result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
            result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("agegroup", None, "agegroup")])
            query1 = "Slice='agegroup = %s , gender = %s , continent = %s'" % (item, item2, item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

            cut = PointCut("agegroup", [item])
            cut2 = PointCut("gender", [item2])
            cut3 = PointCut("location", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=["sport"])
            result1 = browser.aggregate(cell, drilldown=["sport"])
            result2 = browser.aggregate(cell, drilldown=["sport"])
            result3 = browser.aggregate(cell, drilldown=["sport"])
            query1 = "Slice='agegroup = %s , gender = %s , continent = %s' Drilldown='sport'" % (item, item2,item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

for item in sport:
    for item2 in gender:
        for item3 in continent:
            cut = PointCut("sport", [item])
            cut2 = PointCut("gender", [item2])
            cut3 = PointCut("location", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
            result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
            result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
            result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"), ("location", None, "continent"),("sport", None, "sport")])
            query1 = "Slice='sport = %s , gender = %s , continent = %s'" % (item, item2, item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

            cut = PointCut("sport", [item])
            cut2 = PointCut("gender", [item2])
            cut3 = PointCut("location", [item3])
            cell = Cell(browser.cube, cuts=[cut, cut2, cut3])
            result = browser.aggregate(cell, drilldown=["agegroup"])
            result1 = browser.aggregate(cell, drilldown=["agegroup"])
            result2 = browser.aggregate(cell, drilldown=["agegroup"])
            result3 = browser.aggregate(cell, drilldown=["agegroup"])
            query1 = "Slice='sport = %s , gender = %s , continent = %s' Drilldown='agegroup'" % (item, item2,item3)
            query.append(query1)
            cv_function(result1, query1)
            ratio_b(result, query1)
            ratio_c(result2, query1)
            ratio_d(result3, query1)

for item in sport:
    for item2 in agegroup:
        for item3 in continent:
            for item4 in gender:
                cut = PointCut("sport", [item])
                cut2 = PointCut("agegroup", [item2])
                cut3 = PointCut("location", [item3])
                cut4 = PointCut("gender", [item4])
                cell = Cell(browser.cube, cuts=[cut, cut2, cut3, cut4])
                result = browser.aggregate(cell, drilldown=[("gender", None, "gender"),("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
                result1 = browser.aggregate(cell, drilldown=[("gender", None, "gender"),("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
                result2 = browser.aggregate(cell, drilldown=[("gender", None, "gender"),("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
                result3 = browser.aggregate(cell, drilldown=[("gender", None, "gender"),("agegroup", None, "agegroup"), ("location", None, "continent"),("sport", None, "sport")])
                query1 = "Slice='sport = %s , agegroup = %s , continent = %s , gender = %s'" % (item, item2, item3 , item4)
                query.append(query1)
                cv_function(result1, query1)
                ratio_b(result, query1)
                ratio_c(result2, query1)
                ratio_d(result3, query1)

print("number of values in sport list: %d"%(len(sport)))
print("sport values:")
for x in sport:
    print(x)
print("number of values in agegroup list: %d"%(len(agegroup)))
print("agegroup value:")
for x in agegroup:
    print(x)
print("number of values in continent list: %d"%(len(continent)))
print("continent values:")
for x in continent:
    print(x)
print("number of values in gender list: %d"%(len(gender)))
print("gender values:")
for x in gender:
    print(x)
print("all queries are:")
for row in query:
    print(row)
print("number of queries: %d"%(len(query)))

# question 6_a
print("A query that results in a class of values that has the highest relative standard deviation for the number of medals obtained.(question 6_a)")
index = cv.index(max(cv))
print(queries_a[index])

# question 6_b
print("A query that specifies the highest ratio of total medals obtained to the total number of records:(quetion6_b)")
index = medals_records_ratio.index(max(medals_records_ratio))
print(queries_b[index])

# question 6_c
print("Query showing the most evolving sub-cube:(question6_c)")
index = total_medals.index(max(total_medals))
print(queries_c[index])


# question 6_d
print("A query that shows the most developed sub-cube:(question6_d)")
index = total_medals_2.index(max(total_medals_2))
print(queries_d[index])

