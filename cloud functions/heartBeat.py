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
from math import radians, cos, sin, asin, sqrt


key = "" # api key
url = "" # cloudant url
passcode = "ncsuECE_sdproject37"
authenticator = IAMAuthenticator(key)
service = CloudantV1(authenticator=authenticator) # get the cloudant service
service.set_service_url(url) # set the cloudant service to correct url

def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # 6371 Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

def main(payload):
    holder = []
    invalidDocuments = []
    
    stats = service.post_all_docs(db="sensor-data",include_docs=True,startkey='').get_result() # this gets information about our database
    
    try: 
        payload["distance"]
        long = payload["longitude"]
        latt = payload["latitude"]
    except:
        return { "body":{'error': "Invalid payload"} }
    
    documents = stats["rows"]
    for i in documents:
        try:
            dist = distance(latt, i["doc"]["latitude"], long, i["doc"]["longitude"])
        except:
            invalidDocuments.append(i["doc"])
            continue
        #print(dist)
        if (dist < payload["distance"]):
            holder.append(i["doc"])
    
    returnMessage = {}

    # if (len(holder) > 0):
    #     returnMessage['Scores In Range'] = holder
    # else:
    #     returnMessage['Scores In Range'] = "No valid road quality scores in range."

    returnMessage['Scores In Range'] = holder

    return {"body":returnMessage}
    
