mkdir out_test
for %%a in (testdata\*.txt) do python jsons_to_koa_csv.py %%a out_test\%%~na.csv
pause
