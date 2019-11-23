mkdir out_invest
for %%a in (testdata\*.json) do python jsons_to_all_csv.py %%a out_invest\%%~na.txt
pause
