# infonomy_client.InboxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get**](InboxApi.md#read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get) | **GET** /matchers/{matcher_id}/inbox | Read Decision Contexts For Matcher
[**read_decision_contexts_for_seller_sellers_seller_id_inbox_get**](InboxApi.md#read_decision_contexts_for_seller_sellers_seller_id_inbox_get) | **GET** /sellers/{seller_id}/inbox | Read Decision Contexts For Seller


# **read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get**
> List[DecisionContextRead] read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get(matcher_id)

Read Decision Contexts For Matcher

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.decision_context_read import DecisionContextRead
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
    api_instance = infonomy_client.InboxApi(api_client)
    matcher_id = 56 # int | 

    try:
        # Read Decision Contexts For Matcher
        api_response = api_instance.read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get(matcher_id)
        print("The response of InboxApi->read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboxApi->read_decision_contexts_for_matcher_matchers_matcher_id_inbox_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matcher_id** | **int**|  | 

### Return type

[**List[DecisionContextRead]**](DecisionContextRead.md)

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

# **read_decision_contexts_for_seller_sellers_seller_id_inbox_get**
> List[DecisionContextRead] read_decision_contexts_for_seller_sellers_seller_id_inbox_get(seller_id)

Read Decision Contexts For Seller

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.decision_context_read import DecisionContextRead
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
    api_instance = infonomy_client.InboxApi(api_client)
    seller_id = 56 # int | 

    try:
        # Read Decision Contexts For Seller
        api_response = api_instance.read_decision_contexts_for_seller_sellers_seller_id_inbox_get(seller_id)
        print("The response of InboxApi->read_decision_contexts_for_seller_sellers_seller_id_inbox_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboxApi->read_decision_contexts_for_seller_sellers_seller_id_inbox_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **int**|  | 

### Return type

[**List[DecisionContextRead]**](DecisionContextRead.md)

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

