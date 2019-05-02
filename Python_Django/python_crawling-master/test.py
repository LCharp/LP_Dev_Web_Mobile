from igdb_api_python.igdb import igdb as igdb

#ENTER YOUR KEY HERE
igdb = igdb("b34ee13a58748558d9f273c965c65a7f")

#RETRIEVE ONE GAME
result = igdb.games({
        'search': "mario",
        'fields' : ['name','cover','first_release_date']
})
print(result.body)
