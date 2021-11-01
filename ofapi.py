# -*- coding: utf-8 -*-
import base64, os, requests
import argparse
import json

email = ''
key = ''


def title():
    print("""
          ________              _____ 
_________  __/_____ ___________(_)
_  __ \_  /_ _  __ `/__  __ \_  / 
/ /_/ /  __/ / /_/ /__  /_/ /  /  
\____//_/    \__,_/ _  .___//_/   
                    /_/    
     
                            Author:JoJosec 

    """)


def helpinfo():
    print("""
usage: ofapi.py [-h] [-q QUERY] [-s SIZE] [-o OUTPUT]

python3 ofapi.py -q 'app = xxx' -s 3 -o result.txt
    """)


def getFofa(size, search, output):
    global result
    search = search.replace("'", '"')
    search = base64.b64encode(search.encode('utf-8')).decode('utf-8')
    url = "https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&size={}".format(email, key, search,
                                                                                        size)
    response = requests.get(url)

    res = json.loads((response.content).decode('utf-8'))
    try:
        with open('{}'.format(output), 'a+') as w:
            for i in range(len(res["results"])):
                url = res["results"][i][0]
                if 'http' not in url:
                    url = 'http://{}'.format(url)
                w.write('{}\n'.format(url))

        print("File save as  {}/{}".format(os.getcwd(), output))
    except Exception:
        print("语法错误！！！请检查语法后再尝试！")


if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser(description="python3 fofa.py -q 'app = xxx' -p 3 -o result.txt")
    parser.add_argument('-q', '--query', default='', help="app='xxx'")
    parser.add_argument('-s', '--size', default='', help="100")
    parser.add_argument('-o', '--output', default='result.txt', help="xxx.txt")
    args = parser.parse_args()
    query = ''
    size = ''
    output = ''
    if args.query:
        query = args.query
        if args.size:
            size = args.size
        if args.output:
            output = args.output
        getFofa(size, query, output)
    else:
        helpinfo()
