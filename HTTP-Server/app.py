import json,os,requests
from flask import Flask, redirect, url_for, request
import logging

app = Flask(__name__)

# *******************************************************************************
#           Function to get Bearer Token 
# *******************************************************************************
def getToken(clientid, clientsecret, api_url, sso_auth):
  app.logger.debug("In getToken: ", clientid, " ", clientsecret, " ", api_url)  
  try:
    headers = {
       'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = 'grant_type=client_credentials&client_id={}&client_secret={}&scope:app-engine:apps:run,automation:workflows:admin,automation:workflows:run,storage:buckets:read,storage:logs:read'.format(clientid, clientsecret)

    response = requests.post(sso_auth, headers=headers, data=data, verify=False)
    if response.status_code >= 400 and response.status_code <= 600:
      app.logger.exception("Get Token failed", str(response.status_code), response.text)

    token_data = response.json()

  except Exception as e:
    app.logger.exception("Exception encountered in rotateToken", str(e))

  finally:
    app.logger.info("Successful completion: getToken")  
    return(token_data["access_token"])

# *******************************************************************************
#           Function to trigger the workflow API 
# *******************************************************************************

def trigger_post(api_url, data, headers):
  app.logger.debug("In trigger_post")  
  response = requests.post(api_url, json=data, headers=headers)
  return response.status_code

# *******************************************************************************
#           Endpoint accessible from GITEA webhook
# *******************************************************************************
@app.route('/trigger_workflow',methods = ['POST'])
def trigger_workflow():
  try:  
    app.logger.debug("In trigger_workflow")

    payload = request.get_json()
    app.logger.debug(payload)

    if request.method == 'POST':
      clientid = os.getenv("CLIENT_ID")
      clientsecret = os.getenv("CLIENT_SECRET")
      sso_auth = os.getenv("SSO_AUTH")
      api_url=os.getenv("WORKFLOW_ENDPOINT")
      app.logger.debug("client_id=%s",clientid, " client_secret=%s", clientsecret, "api_url=%s",api_url)
      bearer = getToken(clientid,clientsecret,api_url, sso_auth)

      data = {
        "input":{     
         "commit_hash":payload["commits"][0]["id"],
         "user": payload["commits"][0]["committer"]["name"],
        }
      }
      
      headers = {
         "Authorization": f"Bearer {bearer}",
      }

      response=trigger_post(api_url, data, headers)
  except Exception as e:
    app.logger.exception("Exception encountered in trigger_builderr_workflow ", str(e))

  finally:
    app.logger.info("Successful completion: trigger_builderr_workflow")
      
    app.logger.debug("trigger_workflow response = %s", response)  
    if response >= 200 and response <= 399:
      return json.dumps({'success':True}), response, {'ContentType':'application/json'}
    else:
      return json.dumps({'success':False}), response, {'ContentType':'application/json'}

# *******************************************************************************
#           Main Function 
# *******************************************************************************
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)
