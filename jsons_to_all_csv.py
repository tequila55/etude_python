# -*- coding: utf-8 -*-

import pandas
import json
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('ERROR: Input file and output file required.')
        print('       Input file must consist of one json per line.')
        exit()

    df = pandas.DataFrame()

    with open(sys.argv[1],'r', encoding="utf-8") as fin:
        for line in fin:
            try:
                data = json.loads(line)
            except json.JSONDecodeError as e:
                continue
            df2 = pandas.io.json.json_normalize(data)
            df = df.append(df2,sort=False)
            #print(df)
            #json.dump(data, sys.stdout, ensure_ascii=False, indent=4)
            #print()

    df.to_csv(sys.argv[2], encoding="utf_8_sig")
