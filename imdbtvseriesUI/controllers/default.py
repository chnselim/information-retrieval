# -*- coding: utf-8 -*-

def index():
    """ removing item from solr """
    #http://localhost:8983/solr/imdb/update?stream.body=%3Cdelete%3E%3Cquery%3Eid:03109f46-3938-402f-94e9-4ae006466525%3C/query%3E%3C/delete%3E&commit=true
    """ search field is exist in solr """
    #-field:[* *]

    return locals()

def search():
    import json, urllib
    search_query = request.vars.q.replace(' ', '+')

    genre = request.vars.catQuery or "*"
    year = request.vars.yearQuery or "*"
    rate = request.vars.rateQuery or "*"

    page = request.args(0) or 1
    search_result_url = "http://127.0.0.1:8983/solr/imdb/select?indent=on&q={1}&fq=genre:{0}&fq=year:{3}&fq=rate:{4}&rows=12&facet=true&facet.field=genre&facet.field=year&start={2}&wt=json".format(genre, search_query, (int(page)-1)*12, year, rate)
    search_response = urllib.urlopen(search_result_url)
    search_result = json.loads(search_response.read())
    print(search_result['facet_counts']['facet_fields'])
    return locals()

def details():
    import urllib
    import json
    id = request.args(0)
    search_result_url = "http://127.0.0.1:8983/solr/imdb/select?indent=on&q={}&df=id&wt=json".format(id)
    search_response = urllib.urlopen(search_result_url)
    search_result = json.loads(search_response.read())
    return locals()

def user():
    return dict(form=auth())

@cache.action()
def download():
    return response.download(request, db)

def call():
    return service()