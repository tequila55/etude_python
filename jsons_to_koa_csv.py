# -*- coding: utf-8 -*-

import json
import sys
import datetime
from pytz import timezone

def get(dct,key):
    return dct.get(key,'N/A')

def get_elem_in_array(ary,index,key):
    if len(ary) > index:
        return get(ary[index],key)
    else:
        return ''

def get_header():
    header = (
        'シリアル番号',
        '日付時刻',
        '年',
        '月',
        '日',
        '時間',
        'Twitterスクリーンネーム',
        '★TwitterURL',
        'TwitterID',
        'listID',
        '俗称･通称',
        'Tweet',
        'メンション',
        '画像URL1',
        '画像URL2',
        '画像URL3',
        '画像URL4',
        '★引用URL1',
        '★引用URL2',
        '★引用URL3',
        '★引用URL4',
        '★引用画像URL1',
        '★引用画像URL2',
        '★引用画像URL3',
        '★引用画像URL4',	
        'RT数',
        'イイネ数',
        '備考',
        '管理用情報'
    )

    s = ''
    for t in header:
        s += t + ','
    s += '\n'

    return s

def quote(word):
    return '"' + word.replace('"','""') +'"'

def get_one_line_csv(dct):

    root = dct
    user = root['user']
    entities = root['entities']

    created_at = get(root,'created_at')
    dt = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
    dt_jp = dt.astimezone(timezone('Asia/Tokyo'))

    s = ''
    s += ','                                    # シリアル番号
    s += quote(created_at) + ','                # 日付時刻
    s += quote(str(dt_jp.year)) + ','           # 年
    s += quote(str(dt_jp.month)) + ','          # 月
    s += quote(str(dt_jp.day)) + ','            # 日
    s += quote(dt_jp.strftime('%H:%M:%S')) + ','    # 時間
    s += quote(get(user,'screen_name')) + ','   # Twitterスクリーンネーム
    s += ','                                    # ★TwitterURL
    s += quote(get(root,'id_str')) + ','        # TwitteID
    s += ','                                    # listID
    s += ','                                    # 俗称･通称

    # Tweet (長い場合のみ、extended_tweetがあるようだ)
    if ( root['truncated'] == True ):
        extended_tweet = root['extended_tweet']
        s += quote(get(extended_tweet,'full_text').replace('"','""')) + ',' 
    else:
        s += quote(get(root,'text')) + ','

    # メンション
    user_mentions = entities['user_mentions']
    t = ''
    if user_mentions:
        for mention in user_mentions:
            t += '@' + get(mention,'screen_name') + ' '
    s += quote(t) + ','

    # 画像URL1-4
    # 2枚目以降は、extended_entitiesにしかない
    entities_2 = {}
    if 'extended_entities' in root:
        entities_2 = root['extended_entities']
    else:
        entities_2 = entities

    if 'media' in entities_2:
        media = entities_2['media']
        s += quote(get_elem_in_array(media,0,'media_url')) + ','
        s += quote(get_elem_in_array(media,1,'media_url')) + ','
        s += quote(get_elem_in_array(media,2,'media_url')) + ','
        s += quote(get_elem_in_array(media,3,'media_url')) + ','
    else:
        s += ',,,,'

    # ★引用URL1-4
    s += ','
    s += ','
    s += ','
    s += ','

    # ★引用画像URL1-4
    s += ','
    s += ','
    s += ','
    s += ','

    s += quote(str(get(root,'retweet_count'))) + ','    # RT数
    s += quote(str(get(root,'favorite_count'))) + ','   # イイネ数
    s += ','                                        # 備考
    s += ','                                        # 管理用情報
    s += '\n'

    return s 

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('ERROR: Input file and output file are required.')
        print('       Input file must consist of one json per line.')
        exit()

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file,'r') as f_in, open(out_file,'w') as f_out:
        f_out.write(get_header())
        for line in f_in:
            try:
                data = json.loads(line)
            except json.JSONDecodeError as e:
                continue
            f_out.write(get_one_line_csv(data))

