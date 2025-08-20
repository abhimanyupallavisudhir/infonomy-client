# infonomy_client.InspectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_status_jobs_job_id_status_get**](InspectionApi.md#get_job_status_jobs_job_id_status_get) | **GET** /jobs/{job_id}/status | Get Job Status
[**inspect_context_questions_context_id_inspect_post**](InspectionApi.md#inspect_context_questions_context_id_inspect_post) | **POST** /questions/{context_id}/inspect | Inspect Context


# **get_job_status_jobs_job_id_status_get**
> object get_job_status_jobs_job_id_status_get(job_id)

Get Job Status

Returns the Celery task state and, if ready, the result (list of purchased IDs).

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = infonomy_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with infonomy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infonomy_client.InspectionApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get Job Status
        api_response = api_instance.get_job_status_jobs_job_id_status_get(job_id)
        print("The response of InspectionApi->get_job_status_jobs_job_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionApi->get_job_status_jobs_job_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_context_questions_context_id_inspect_post**
> object inspect_context_questions_context_id_inspect_post(context_id)

Inspect Context

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = infonomy_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with infonomy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infonomy_client.InspectionApi(api_client)
    context_id = 56 # int | 

    try:
        # Inspect Context
        api_response = api_instance.inspect_context_questions_context_id_inspect_post(context_id)
        print("The response of InspectionApi->inspect_context_questions_context_id_inspect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectionApi->inspect_context_questions_context_id_inspect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

