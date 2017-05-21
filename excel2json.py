# -*- coding:utf-8 -*-
import xlrd;
import json;
import codecs;
import os;

workbook = xlrd.open_workbook('toJson.xls');

# sheet num
# get sheet
sheet = workbook.sheet_by_index(0);
# get key
row_0 = sheet.row(0);
nrows = sheet.nrows;
ncols = sheet.ncols;

result = {};
result['titel'] = 'toJson.xls';
result['rows'] = nrows;
result['items'] = [];

for i in range(nrows):
    if i == 0:
        continue;
    tmp = {};
    for j in range(ncols):
        title_de = str(row_0[j]).decode('unicode_escape');
        title_cn = title_de.split("'")[1];
        # traversal all the sheet table
        tmp[title_cn] = sheet.row_values(i)[j];
    result['items'].append(tmp);
json_data = json.dumps(result, indent=2, sort_keys=True).decode('unicode_escape');
print(json_data);

# save
output = codecs.open('.' + '/' + 'xls2json' + '.json', 'w', 'utf-8');
output.write(json_data);
output.close();
