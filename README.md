# Getthelikesofconsumer
# Build a Consumer Affinity towards a entity:

 This repository contains package for calculating affinity of a consumer for a entity based on score. In this repository we are connecting with google cloud component bigquery and performing operations on user activity log to get the affinity of user towards a product.
 
------------------

## Calculating Score:

1. Scoring is  a technique to define the magnitude (affinity) for a consumer towards a entity.



-------------------


## API Specification:

Below is the API specification of this Agent.

**Request Url:**

`/entity/affinity` - `POST`

***Request body***

```json


{
         "consumerid":"consumerid",[Column name defining the id for a consumer]
        "entity":"entity",(entity for which affinity is calculated ,ex: product ,bike,car etc)
        "entityid":"entityid",(id for the entity)
        "actioncode":"actioncode",(different type of actions taken by consumer for a entity like "view","add_to_cart")
        "points":"points",(column name  from a pointstable defined on the basis of actioncode from activity log)
        "activitylog":"`table1`",(source table containig all the details for a consumer)
        "pointstable":"`table2`",(table containig points for a actioncode)
        "noofdays":180,(days for which affinity is calculated)
        "DATECOLUMN":"columnname",(column name on which the latest records to be retrieved)
        "targettable":"temptable"(destination table for saving consumer,entityid,score)

 
}



***Response***

```json
{
job success
}
```
   
## Prerequisites:

1.Python 3.7 [https://www.python.org/downloads/]
2.pip [https://pypi.org/project/pip/]
3.Ananconda/Pycharm (Python toolkit) (optional)
4.Docker
5.Gcp Storage Bucket

## Setup:

1.Create a User Service Account and download it as json with permissions to Read and write over GCS google Cloud Storage.
- Use Below url to read about creating and managing service accounts.
[https://cloud.google.com/iam/docs/creating-managing-service-accounts]
2.Copy, Paste the content of the json to credentials.json

4.requirements.txt consists of all the dependencies (along with version numbers) required for the project. pip install will install those dependencies inside your python environment (if it exists and set)
       `pip install -r requirements.txt`
 
## How to run the Agent:

**Through Postman**

Get the url if local host then http://0.0.0.0:5086/entity/affinity , run as Post Method.
for passing request json go inside Body Select Raw and editor as json and provide the request json mentioned as above Requestbody.
### *Note: by default mentioned port is 5086*.

