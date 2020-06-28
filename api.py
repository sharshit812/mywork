from google.cloud import bigquery
from google.cloud import storage

import os
from flask import Flask
from flask import request, Response
from flask_cors import CORS, cross_origin
from flask.json import jsonify
app = Flask(__name__)
api_url = "/entity"
CORS(app, support_credentials=True)
@app.route(api_url + '/affinity', methods=['GET', 'POST'])


def load1():
    if request.method == 'POST':
        data = request.get_json()  # getting data from post request
        credential_path = 'credentials.json'  #defining the credentials.json for accessing google cloud
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
        consumerid=data["consumerid"]
        entity=data["entity"]
        entityid=data["entityid"]
        actioncode=data["actioncode"]
        points=data["points"]
        activitylog=data["activitylog"]
        pointstable=data["pointstable"]
        noofdays=data["noofdays"]
        DATECOLUMN=data["DATECOLUMN"]
        targettable=data["targettable"]

        storage_client = storage.Client()

        client = bigquery.Client()    

        job_config = bigquery.QueryJobConfig(
        allow_large_results=True, destination=targettable,
        use_legacy_sql=False
        , write_disposition='WRITE_TRUNCATE')
        query = """WITH streaming_data AS (


        SELECT {0},h.{1},{2} FROM {3} ,UNNEST({4}) as h WHERE   h.{1} is not null and  DATE({5}) between date_sub(current_date(), INTERVAL {8} day) and current_date()


),

points_tables as(
 SELECT a.{0},a.{1},b.{6} FROM streaming_data a inner join {7} b on a.{2}=b.{2}),
sumofactionpointsforaconsumer  as(
 SELECT {0},sum({6}) as spoints FROM points_tables group by {0}),
 sum_of_action_points_for_a_consumer_and_recipe as (SELECT {0},{1},sum({6}) as rpoints FROM points_tables group by {0},{1})
SELECT a.{0},b.{1},(rpoints/spoints)*10 as score FROM sumofactionpointsforaconsumer a inner join sum_of_action_points_for_a_consumer_and_recipe b on a.{0}=b.{0} """.format(consumerid,entityid,actioncode,activitylog,entity,DATECOLUMN,points,pointstable,noofdays)

        query_job = client.query(query, job_config=job_config)  # Make an API request.
        query_job.result()
        return "job success"
    else:
        return "not applicable"
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5086)
