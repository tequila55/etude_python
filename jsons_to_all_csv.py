# -*- coding: utf-8 -*-

import pandas
import json
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('ERROR: Input file and output file required.')
        print('USAGE: ' + sys.argv[0] + ' <in_file> <out_file>')
        print('       in_file:  it must be one json per line.')
        print('       out_file: .csv or anything (e.g. .txt)')
        exit()

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    if out_file.endswith('.csv'):
        mode = 'csv'
    else:
        mode = 'text'

    print(mode + ' mode')

    with open(in_file, encoding="utf-8") as fin:
        if mode == 'csv':
            df = pandas.DataFrame()
            for line in fin:
                try:
                    data = json.loads(line)
                except json.JSONDecodeError as e:
                    continue
                df2 = pandas.io.json.json_normalize(data)
                df = df.append(df2,sort=False)
                #print(df)
            df.to_csv(out_file, encoding="utf_8_sig")
        else:
            with open (out_file,'w',encoding='utf_8_sig') as fout:
                for line in fin:
                    try:
                        data = json.loads(line)
                    except json.JSONDecodeError as e:
                        continue
                    json.dump(data,fout,ensure_ascii=False,indent=4)
                    fout.write('\n' + '='*60 +'\n')

