from math import sin, cos, sqrt, atan2, radians

def findfirst(point,category):
     return db.geoprog.find_one( {"$and":
                              [{ "office" :
                                 { "$near" :
                                   { "$geometry" : point,
                                         "$maxDistance" : 2000} } },
                               {"category_code":f"{category}"}]} )


def distance(lat1, lon1, lat2, lon2):  
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

distanza={}

def score(point,categories,weights):
    somma=0
    for cat in categories:
        try:
            el=findfirst(point,cat)
            lat=el["latitude"]#el["office"]["coordinates"][1]
            lon=el["longitude"]#el["office"]["coordinates"][0]
            distanza[cat]=(5000-distance(lat,lon,point["coordinates"][1],point["coordinates"][0]))*weights[cat]*0.01
            somma+=distanza[cat]
        except:
            continue
            somma+=10000000000
    return somma

#the best point is the one that minimize the score


def bestCoord1(lats,longs,categories,weights):  
    count=0
    scores=dict()
    point=dict()
    for i in range(len(lats)):      
        point["type"]="Point"
        point["coordinates"]=[longs[i],lats[i]]
        scores[count]=[score(point,categories,weights)]
        count+=1
    bestscore=min(scores.values())
    n=[]
    for key, el in scores.items():
        if el==bestscore:
            n=key
    return [ lats[n],longs[n]]

def find1(point,category):
     return db.geoprog.find( {"$and":
                              [{ "office" :
                                 { "$near" :
                                   { "$geometry" : point,
                                         "$maxDistance" : 5000} } },
                               {"category_code":f"{category}"}]} )

def nearestpleces(point,categories):
    places=[]
    for cat in categories:
        try:
            el=find1(point,cat)[0]      
            places.append(
                {"lat" :  el["office"]["coordinates"][1],
                 "lon" :  el["office"]["coordinates"][0],
                 "name":  el["name"],
                 "category": el["category_code"]})           
        except:
            try:
                el=find1(point,cat)[1]      
                places.append(
                    {"lat" :  el["office"]["coordinates"][1],
                     "lon" :  el["office"]["coordinates"][0],
                     "name":  el["name"],
                     "category": el["category_code"]})
            except:
                continue
    return places