mkdir out_test
for %%a in (testdata\*.json) do python jsons_to_koa_csv.py %%a out_test\%%~na.csv
pause
