himachal = ['great himalayan','inderkilla','khirganga','pin valley','col. sherjung','simbalbara']
ladakh = ['hemis']
uk = ['corbett','gangotri','govind','nanda devi','rajaji','valley of flowers']
jammu = ['city forest','salim ali','dachigam','kazinag','kishtwar high altitude']
haryana = ['kalesar','sultanpur']
rajasthan = ['desert np','keoladeo ghana','mukundra hills','ranthambhore','sariska']
jharkhand = ['betla']
up = ['dudhwa']
bihar = ['valmiki']
sikkim = ['khangchendzonga']
assam = ['dibru-saikhowa','kaziranga','manas','nameri','orang','raimona','dihang patkai']
arunachal = ['mouling','namdhapha']
nagaland = ['intanki']
manipur = ['keibul-lamjao','shiroi']
mizoram = ['murlen','phawngpui','blue mountain']
tripura = ['clouded leapard','bison','rajbari']
meghalaya = ['balphakram','nokrek ridge']
bengal = ['bux','gorumara','jaldapara','neora vally','singalila','sunderban']
goa = ['mollem']
karnataka = ['anshi','bandipur','bannerghatta','kudermukh','nagarahole','rajiv gandhi']
kerala = ['anamudi shola','eravikulam','mathikettan shola','pambadum shola','periyar','silent valley']
tamil = ['guindy','gulf of mannar','indira gandhi','annamalai','mudumalai','mukurthi']
full = ['great himalayan','inderkilla','khirganga','pin valley','col. sherjung','simbalbara',
        'hemis','corbett','gangotri','govind','nanda devi','rajaji','valley of flowers',
        'city forest','salim ali','dachigam','kazinag','kishtwar high altitude'
        ,'kalesar','sultanpur','desert np','keoladeo ghana','mukundra hills','ranthambhore','sariska',
        'betla','dudhwa','khangchendzonga','dibru-saikhowa','kaziranga','manas',
        'nameri','orang','raimona','dihang patkai','mouling','namdhapha','intanki',
        'keibul-lamjao','shiroi','murlen','phawngpui','blue mountain','clouded leapard','bison','rajbari',
        'balphakram','nokrek ridge','bux','gorumara','jaldapara','neora vally','singalila','sunderban',
        'mollem','anshi','bandipur','bannerghatta','kudermukh','nagarahole','rajiv gandhi',
        'anamudi shola','eravikulam','mathikettan shola','pambadum shola','periyar','silent valley',
        'guindy','gulf of mannar','indira gandhi','annamalai','mudumalai','mukurthi']
state = [tamil,kerala,karnataka,goa,bengal,meghalaya,tripura,mizoram,manipur,
         nagaland,arunachal,assam,sikkim,up,jharkhand,rajasthan,haryana,jammu,uk,ladakh,himachal]

import random

print('''CODE - STATE\n
HP - HIMACHAL PRADESH
LD - LADAKH
UK - UTRAKHAND
JK - JAMMU AND KASHMIR
HR - HARYANA
RJ - RAJASTHAN
JH - JHARKHAND
UP - UTTAR PRADESH
BR - BIHAR
SK - SIKKIM
AS - ASSAM
AP - ARUNACHAL PRADESH
NL - NAGALAND
MN - MANIPUR
MZ - MIZORAM
TR - TRIPURA
ML - MEGHALAYA
WB - WEST BENGAL
GA - GOA
KA - KARNATAKA
KL - KERALA
TN - TAMIL NADU''')

score = 0
x = 0
while x < 10:
    q=random.choice(full)
    print(q)
    ans=input("Enter the CODE: ")
    if ans.lower().strip() == 'hp':
        if q in himachal:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")
            
    if ans.lower().strip() == 'ld':
        if q in ladakh:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'uk':
        if q in uk:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'jk':
        if q in jammu:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'hr':
        if q in haryana:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'rj':
        if q in rajasthan:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'jh':
        if q in jharkhand:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'up':
        if q in up:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'br':
        if q in bihar:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'sk':
        if q in sikkim:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'as':
        if q in assam:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'ap':
        if q in arunachal:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'nl':
        if q in nagaland:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")
    if ans.lower().strip() == 'mn':
        if q in manipur:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'mz':
        if q in mizoram:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'tr':
        if q in tripura:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'ml':
        if q in meghalaya:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'wb':
        if q in bengal:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'ga':
        if q in goa:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'ka':
        if q in karnataka:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'kl':
        if q in kerala:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    if ans.lower().strip() == 'tn':
        if q in tamil:
            score += 1
            print("CORRECT")
        else:
            print("WRONG")

    x += 1
print('\n'f"TOTAL SCORE --> {score} OUT OF 10")










