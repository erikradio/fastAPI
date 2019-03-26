import requests, json, csv, sys
from fuzzywuzzy import fuzz, process
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

with open('fastTest.csv','w') as outcsv, open(sys.argv[1],'r') as incsv:

    writer = csv.DictWriter(outcsv, fieldnames = ["filename", "original_term", "fast_term", "fast_id", "score"])
    writer.writeheader()

    reader = csv.DictReader(incsv)
    for row in reader:
        print(row['title'])
    # test='http://fast.oclc.org/searchfast/fastsuggest?&query=hog&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,type,raw,breaker,indicator&suggest=autoSubject&rows=10'
    #http://fast.oclc.org/searchfast/fastsuggest?query=dog&queryIndex=suggestall@queryReturn=suggestall,idroot,auth,tag,type,raw,breaker,indicator&suggest=autoSubject&rows=3&callback=testcall
    # terms=['denver']
    # for term in terms:
    #     url='http://fast.oclc.org/searchfast/fastsuggest?query='+term+'&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,type,raw,breaker,indicator&suggest=autoSubject&rows=20'
    #
    #     r = requests.get(url)
    #     res = json.loads(r.text)
    #     docs=res['response']['docs']
    #     # print(docs)
    #     for x in docs:
    #         suggest = x['suggestall'][0].lower()
    #         fastID = x['idroot']
    #
    #         score=fuzz.token_sort_ratio(term,suggest)
    #         print(score)
    #         writer.writerow({'filename': 'test', 'original_term': term, 'fast_term': suggest, 'fast_id': fastID, 'score':score})
                # print(fuzz.ratio(term,suggest))
