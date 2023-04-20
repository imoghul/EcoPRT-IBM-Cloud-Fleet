#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import requests
import random, string
from ibmcloudant.cloudant_v1 import Document,CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import time


key = "" # api key
url = "" # cloudant url
passcode = "ncsuECE_sdproject37"
authenticator = IAMAuthenticator(key)
service = CloudantV1(authenticator=authenticator) # get the cloudant service
service.set_service_url(url) # set the cloudant service to correct url

# stats = service.post_all_docs(db="sensor-data",include_docs=False,startkey=key).get_result() # this get information about our database

def generateUniqueID(db,id=''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=25))):
    stats = service.post_all_docs(db=db,include_docs=True,startkey='').get_result() # this gets information about our database
    documents = stats["rows"]    
    safetyCounter = len(documents)
    while True:
        found = False
        for i in documents:
            if i['doc']["_id"] ==  id:
                id = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=25))
                found = True
                break
        if not found: return id
        safetyCounter-=1
        if(safetyCounter<=0): return id
                

def main(payload):
    # error handling (very rare might remove this)
    if(type(payload)!=dict): return {"error":"not a valid input"}
    
    # extract data from payload
    try:
        if(payload["__passcode__"]!=passcode):
            return {"Error": "incorrect passcode"}
    except:return {"Error": "no passcode"}
    try: dbName = payload["__database__"]
    except: return {"Error": "no database"}
    
    # get the request id and use that as the database id because that's the best way to generate a random string
    try:docid = str(payload["__ow_headers"]["x-request-id"]) # str(has(time.time()))
    except: docid = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=25))
    docid = generateUniqueID(dbName,docid)
    
    
    data = {}
    for i in payload:
        if(i[0:2]!="__"):data[i] = payload[i]
    
    # create document with data's keys
    event_doc = Document(
        **data
    )
    # print(data)
    # store document in database
    response = service.put_document(
        db=dbName, # db name
        doc_id=str(docid),
        document=event_doc
    ).get_result()
    
    # return the data
    return data
    

