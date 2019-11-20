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

def print_header():
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
    print(s)

def print_one_line_csv(dct):

    root = dct
    user = root['user']
    entities = root['entities']

    created_at = get(root,'created_at')
    dt = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
    dt_jp = dt.astimezone(timezone('Asia/Tokyo'))

    s = ''
    s += ','                                    # シリアル番号
    s += get(root,'created_at') + ','           # 日付時刻
    s += str(dt_jp.year) + ','                     # 年
    s += str(dt_jp.month) + ','                    # 月
    s += str(dt_jp.day) + ','                      # 日
    s += dt_jp.strftime('"%H:%M:%S"') + ','        # 時間
    s += get(user,'screen_name') + ','          # Twitterスクリーンネーム
    s += ','                                    # ★TwitterURL
    s += '"' + get(root,'id_str') + '",'        # TwitterID, user.id_strと間違えていたのを修正(v0.5)
    s += ','                                    # listID
    s += ','                                    # 俗称･通称

    # Tweet (長い場合のみ、extended_tweetがあるようだ)
    if ( root['truncated'] == True ):
        extended_tweet = root['extended_tweet']
        #オリジナル
        #s += '"' + get(extended_tweet,'full_text') + '",'
        # 改行を空白に置き換える場合
        #s += get(extended_tweet,'full_text').replace('\n',' ') + ','
        # csv用にカンマの置き換えが必要、全角カンマにしておく
        s += '"' + get(extended_tweet,'full_text').replace(',','，') + '",' 
    else:
        #オリジナル
        #s += '"' + get(root,'text') + '",'
        # 改行を空白に置き換える場合
        #s += get(root,'text').replace('\n',' ') + ','
        # csv用にカンマの置き換えが必要、全角カンマにしておく
        s += '"' + get(root,'text').replace(',','，') + '",'

    # メンション
    user_mentions = entities['user_mentions']
    if user_mentions:
        for mention in user_mentions:
            s += '@' + get(mention,'screen_name') + ' '
    s += ','

    # 画像URL1-4
    # 2枚目以降は、extended_entitiesにしかない
    entities_2 = {}
    if 'extended_entities' in root:
        entities_2 = root['extended_entities']
    else:
        entities_2 = entities

    if 'media' in entities_2:
        media = entities_2['media']
        s += get_elem_in_array(media,0,'media_url') + ','
        s += get_elem_in_array(media,1,'media_url') + ','
        s += get_elem_in_array(media,2,'media_url') + ','
        s += get_elem_in_array(media,3,'media_url') + ','
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

    s += str(get(root,'retweet_count')) + ','       # RT数
    s += str(get(root,'favorite_count')) + ','      # イイネ数
    s += ','                                        # 備考
    s += ','                                        # 管理用情報

    print(s)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: Input file required.')
        print('       Input file must consist of one json per line.')
        exit()

    with open(sys.argv[1],'r') as fin:
        print_header()
        for line in fin:
            try:
                data = json.loads(line)
            except json.JSONDecodeError as e:
                continue
            print_one_line_csv(data)
