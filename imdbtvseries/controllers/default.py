# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():

    return locals()

def search():
    import json, urllib
    # corename = "imdbSeries"
    # data = json.loads('[{"name": "The Walking Dead", "image": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMDk1NDYyMV5BMl5BanBnXkFtZTgwNjE1NDU4MDI@._V1_UX182_CR0,0,182,268_AL_.jpg", "summary": "Sheriff Deputy Rick Grimes wakes up from a coma, to learn the world is in ruins, and must lead a group of survivors to stay alive.", "genre": ["Drama", "Horror", "Thriller"], "rate": "9.7", "year": "2010", "vote": "680,928"}]')
    # search_url = "http://localhost:8983/solr/imdbSeries/select?indent=on&q=*:*&wt=json"
    # search_resp = urllib.urlopen(search_url)
    # data = json.loads(search_resp.read())

    # search_query = request.vars.searchQuery.replace(' ', '+')
    # if not request.vars.prevQuery:
    #     request.vars.prevQuery = request.vars.searchQuery
    # if request.vars.prevQuery != request.vars.searchQuery:
    #     search_query = request.vars.prevQuery + "+AND+" + search_query
    # page = request.args(0, cast=int) or 0
    # category = request.vars.cat or "*"
    # date = request.vars.date or "*"
    # search_result_url = "http://localhost:8983/solr/Mashable/select?q=category:{0}+AND+date:{3}+AND+{1}&start={2}&wt=json&indent=true&facet=true&facet.field=category".format(category, search_query, (page-1)*10, date)
    # # return search_result_url
    # search_response = urllib.urlopen(search_result_url)
    # search_result = json.loads(search_response.read())
    return locals()

def details():
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
