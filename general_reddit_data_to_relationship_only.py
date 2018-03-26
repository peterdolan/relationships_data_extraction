import json

def json_readr(file):
    for line in open(file, mode="r"):
            yield json.loads(line)

f=open("relationships_11", "a+")
total = 0

generator = json_readr('RS_2017-11')
for object in generator:
    if ('subreddit' in object and object['subreddit'] == 'relationships'):
        #f.write(object['subreddit'] + ' ' + object['title'] + '\n')
        total += 1
        if (total%100 == 0):
            print (total)
        f.write(json.dumps(object))
