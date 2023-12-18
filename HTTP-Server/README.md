**HTTP-Server Overview**  

The HTTP-Server is a Flask application designed to facilitate seamless integration within the CI/CD pipeline, specifically for relaying webhook calls to the Dynatrace workflow. This component plays a crucial role in streamlining communication and triggering automated actions.  

**Key Features**  

**Webhook Integration**  
The HTTP-Server is equipped with two robust endpoints that efficiently relay webhook calls, ensuring a smooth flow of information between different components of the CI/CD pipeline.    

**Dynatrace Workflow Connectivity**  
Through API calls, the HTTP-Server seamlessly connects with the Dynatrace workflow, enabling the automation of essential tasks and processes.  

**Environment configuration Variables**

The following environment variables can be configured:

CLIENT_ID=
(Specify the client ID for authentication purposes.)

CLIENT_SECRET=
(Provide the client secret required for secure communication.)

COMPILATION_ERROR_WORKFLOW=
(Define the workflow to handle compilation errors, ensuring a proactive response to potential issues.)

API_URL=
(Specify the API URL to establish a connection with the Dynatrace workflow.)

**Getting Started**

To effectively incorporate the HTTP-Server into your CI/CD pipeline, ensure that you configure these environment variables appropriately. This customization allows you to seamlessly integrate the HTTP-Server, enhancing the efficiency to trigger the Dynatrace-workflows on push-request.  







