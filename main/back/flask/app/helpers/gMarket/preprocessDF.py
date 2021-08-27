from app.helpers.gMarket.objToDF import objToDF
from app.helpers.gMarket.trimBed import trimBed


def preprocessDF(objects):

    # turn a list of objects into a df

    rawDF = objToDF(objects)

    # bed

    intermedBed = trimBed(rawDF)

    # mattress

    intermedMatt = trimMatt(rawDF)

    # preprocess bed

    finalBed = preprocessBed(intermedBed)

    # preprocess Mattress

    finalMatt = preprocessMatt(intermedMatt)

    # upload them to database

    upsertToDB(finalBed)

    upsertToDB(finalMatt)
