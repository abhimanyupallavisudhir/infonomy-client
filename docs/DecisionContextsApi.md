# infonomy_client.DecisionContextsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_decision_context_questions_post**](DecisionContextsApi.md#create_decision_context_questions_post) | **POST** /questions | Create Decision Context
[**create_info_offer_questions_context_id_answers_post**](DecisionContextsApi.md#create_info_offer_questions_context_id_answers_post) | **POST** /questions/{context_id}/answers | Create Info Offer
[**delete_decision_context_questions_context_id_delete**](DecisionContextsApi.md#delete_decision_context_questions_context_id_delete) | **DELETE** /questions/{context_id} | Delete Decision Context
[**delete_info_offer_questions_context_id_answers_info_offer_id_delete**](DecisionContextsApi.md#delete_info_offer_questions_context_id_answers_info_offer_id_delete) | **DELETE** /questions/{context_id}/answers/{info_offer_id} | Delete Info Offer
[**list_current_user_decision_contexts_users_me_questions_get**](DecisionContextsApi.md#list_current_user_decision_contexts_users_me_questions_get) | **GET** /users/me/questions | List Current User Decision Contexts
[**list_current_user_info_offers_users_me_answers_get**](DecisionContextsApi.md#list_current_user_info_offers_users_me_answers_get) | **GET** /users/me/answers | List Current User Info Offers
[**list_decision_contexts_questions_get**](DecisionContextsApi.md#list_decision_contexts_questions_get) | **GET** /questions | List Decision Contexts
[**list_user_decision_contexts_users_user_id_questions_get**](DecisionContextsApi.md#list_user_decision_contexts_users_user_id_questions_get) | **GET** /users/{user_id}/questions | List User Decision Contexts
[**list_user_info_offers_users_user_id_answers_get**](DecisionContextsApi.md#list_user_info_offers_users_user_id_answers_get) | **GET** /users/{user_id}/answers | List User Info Offers
[**read_decision_context_questions_context_id_get**](DecisionContextsApi.md#read_decision_context_questions_context_id_get) | **GET** /questions/{context_id} | Read Decision Context
[**read_info_offer_questions_context_id_answers_info_offer_id_get**](DecisionContextsApi.md#read_info_offer_questions_context_id_answers_info_offer_id_get) | **GET** /questions/{context_id}/answers/{info_offer_id} | Read Info Offer
[**read_info_offers_for_decision_context_questions_context_id_answers_get**](DecisionContextsApi.md#read_info_offers_for_decision_context_questions_context_id_answers_get) | **GET** /questions/{context_id}/answers | Read Info Offers For Decision Context
[**update_decision_context_questions_context_id_patch**](DecisionContextsApi.md#update_decision_context_questions_context_id_patch) | **PATCH** /questions/{context_id} | Update Decision Context
[**update_info_offer_questions_context_id_answers_info_offer_id_patch**](DecisionContextsApi.md#update_info_offer_questions_context_id_answers_info_offer_id_patch) | **PATCH** /questions/{context_id}/answers/{info_offer_id} | Update Info Offer


# **create_decision_context_questions_post**
> DecisionContextRead create_decision_context_questions_post(decision_context_create_non_recursive)

Create Decision Context

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.decision_context_create_non_recursive import DecisionContextCreateNonRecursive
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    decision_context_create_non_recursive = infonomy_client.DecisionContextCreateNonRecursive() # DecisionContextCreateNonRecursive | 

    try:
        # Create Decision Context
        api_response = api_instance.create_decision_context_questions_post(decision_context_create_non_recursive)
        print("The response of DecisionContextsApi->create_decision_context_questions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->create_decision_context_questions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decision_context_create_non_recursive** | [**DecisionContextCreateNonRecursive**](DecisionContextCreateNonRecursive.md)|  | 

### Return type

[**DecisionContextRead**](DecisionContextRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_info_offer_questions_context_id_answers_post**
> InfoOfferReadPrivate create_info_offer_questions_context_id_answers_post(context_id, info_offer_create)

Create Info Offer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.info_offer_create import InfoOfferCreate
from infonomy_client.models.info_offer_read_private import InfoOfferReadPrivate
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 
    info_offer_create = infonomy_client.InfoOfferCreate() # InfoOfferCreate | 

    try:
        # Create Info Offer
        api_response = api_instance.create_info_offer_questions_context_id_answers_post(context_id, info_offer_create)
        print("The response of DecisionContextsApi->create_info_offer_questions_context_id_answers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->create_info_offer_questions_context_id_answers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 
 **info_offer_create** | [**InfoOfferCreate**](InfoOfferCreate.md)|  | 

### Return type

[**InfoOfferReadPrivate**](InfoOfferReadPrivate.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_decision_context_questions_context_id_delete**
> delete_decision_context_questions_context_id_delete(context_id)

Delete Decision Context

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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 

    try:
        # Delete Decision Context
        api_instance.delete_decision_context_questions_context_id_delete(context_id)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->delete_decision_context_questions_context_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_info_offer_questions_context_id_answers_info_offer_id_delete**
> InfoOfferReadPrivate delete_info_offer_questions_context_id_answers_info_offer_id_delete(context_id, info_offer_id)

Delete Info Offer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.info_offer_read_private import InfoOfferReadPrivate
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 
    info_offer_id = 56 # int | 

    try:
        # Delete Info Offer
        api_response = api_instance.delete_info_offer_questions_context_id_answers_info_offer_id_delete(context_id, info_offer_id)
        print("The response of DecisionContextsApi->delete_info_offer_questions_context_id_answers_info_offer_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->delete_info_offer_questions_context_id_answers_info_offer_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 
 **info_offer_id** | **int**|  | 

### Return type

[**InfoOfferReadPrivate**](InfoOfferReadPrivate.md)

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

# **list_current_user_decision_contexts_users_me_questions_get**
> List[DecisionContextRead] list_current_user_decision_contexts_users_me_questions_get(skip=skip, limit=limit)

List Current User Decision Contexts

List current user's decision contexts (including recursive ones)

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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # List Current User Decision Contexts
        api_response = api_instance.list_current_user_decision_contexts_users_me_questions_get(skip=skip, limit=limit)
        print("The response of DecisionContextsApi->list_current_user_decision_contexts_users_me_questions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->list_current_user_decision_contexts_users_me_questions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

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

# **list_current_user_info_offers_users_me_answers_get**
> List[InfoOfferReadPrivate] list_current_user_info_offers_users_me_answers_get(skip=skip, limit=limit)

List Current User Info Offers

List current user's info offers (with private info)

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.info_offer_read_private import InfoOfferReadPrivate
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # List Current User Info Offers
        api_response = api_instance.list_current_user_info_offers_users_me_answers_get(skip=skip, limit=limit)
        print("The response of DecisionContextsApi->list_current_user_info_offers_users_me_answers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->list_current_user_info_offers_users_me_answers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

### Return type

[**List[InfoOfferReadPrivate]**](InfoOfferReadPrivate.md)

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

# **list_decision_contexts_questions_get**
> List[DecisionContextRead] list_decision_contexts_questions_get(skip=skip, limit=limit)

List Decision Contexts

List all public decision contexts (excluding recursive ones)

### Example


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


# Enter a context with an instance of the API client
with infonomy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # List Decision Contexts
        api_response = api_instance.list_decision_contexts_questions_get(skip=skip, limit=limit)
        print("The response of DecisionContextsApi->list_decision_contexts_questions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->list_decision_contexts_questions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

### Return type

[**List[DecisionContextRead]**](DecisionContextRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_decision_contexts_users_user_id_questions_get**
> List[DecisionContextRead] list_user_decision_contexts_users_user_id_questions_get(user_id, skip=skip, limit=limit)

List User Decision Contexts

List decision contexts by specific user (excluding recursive ones)

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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    user_id = 56 # int | 
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # List User Decision Contexts
        api_response = api_instance.list_user_decision_contexts_users_user_id_questions_get(user_id, skip=skip, limit=limit)
        print("The response of DecisionContextsApi->list_user_decision_contexts_users_user_id_questions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->list_user_decision_contexts_users_user_id_questions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

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

# **list_user_info_offers_users_user_id_answers_get**
> List[InfoOfferReadPublic] list_user_info_offers_users_user_id_answers_get(user_id, skip=skip, limit=limit)

List User Info Offers

List info offers by specific user (public view only)

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.info_offer_read_public import InfoOfferReadPublic
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    user_id = 56 # int | 
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # List User Info Offers
        api_response = api_instance.list_user_info_offers_users_user_id_answers_get(user_id, skip=skip, limit=limit)
        print("The response of DecisionContextsApi->list_user_info_offers_users_user_id_answers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->list_user_info_offers_users_user_id_answers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

### Return type

[**List[InfoOfferReadPublic]**](InfoOfferReadPublic.md)

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

# **read_decision_context_questions_context_id_get**
> DecisionContextRead read_decision_context_questions_context_id_get(context_id)

Read Decision Context

### Example


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


# Enter a context with an instance of the API client
with infonomy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 

    try:
        # Read Decision Context
        api_response = api_instance.read_decision_context_questions_context_id_get(context_id)
        print("The response of DecisionContextsApi->read_decision_context_questions_context_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->read_decision_context_questions_context_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 

### Return type

[**DecisionContextRead**](DecisionContextRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_info_offer_questions_context_id_answers_info_offer_id_get**
> ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet read_info_offer_questions_context_id_answers_info_offer_id_get(context_id, info_offer_id)

Read Info Offer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.response_read_info_offer_questions_context_id_answers_info_offer_id_get import ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 
    info_offer_id = 56 # int | 

    try:
        # Read Info Offer
        api_response = api_instance.read_info_offer_questions_context_id_answers_info_offer_id_get(context_id, info_offer_id)
        print("The response of DecisionContextsApi->read_info_offer_questions_context_id_answers_info_offer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->read_info_offer_questions_context_id_answers_info_offer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 
 **info_offer_id** | **int**|  | 

### Return type

[**ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet**](ResponseReadInfoOfferQuestionsContextIdAnswersInfoOfferIdGet.md)

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

# **read_info_offers_for_decision_context_questions_context_id_answers_get**
> List[ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner] read_info_offers_for_decision_context_questions_context_id_answers_get(context_id)

Read Info Offers For Decision Context

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.read_info_offers_for_decision_context_questions_context_id_answers_get200_response_inner import ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 

    try:
        # Read Info Offers For Decision Context
        api_response = api_instance.read_info_offers_for_decision_context_questions_context_id_answers_get(context_id)
        print("The response of DecisionContextsApi->read_info_offers_for_decision_context_questions_context_id_answers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->read_info_offers_for_decision_context_questions_context_id_answers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 

### Return type

[**List[ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner]**](ReadInfoOffersForDecisionContextQuestionsContextIdAnswersGet200ResponseInner.md)

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

# **update_decision_context_questions_context_id_patch**
> DecisionContextRead update_decision_context_questions_context_id_patch(context_id, decision_context_update_non_recursive)

Update Decision Context

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.decision_context_read import DecisionContextRead
from infonomy_client.models.decision_context_update_non_recursive import DecisionContextUpdateNonRecursive
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 
    decision_context_update_non_recursive = infonomy_client.DecisionContextUpdateNonRecursive() # DecisionContextUpdateNonRecursive | 

    try:
        # Update Decision Context
        api_response = api_instance.update_decision_context_questions_context_id_patch(context_id, decision_context_update_non_recursive)
        print("The response of DecisionContextsApi->update_decision_context_questions_context_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->update_decision_context_questions_context_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 
 **decision_context_update_non_recursive** | [**DecisionContextUpdateNonRecursive**](DecisionContextUpdateNonRecursive.md)|  | 

### Return type

[**DecisionContextRead**](DecisionContextRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_info_offer_questions_context_id_answers_info_offer_id_patch**
> InfoOfferReadPrivate update_info_offer_questions_context_id_answers_info_offer_id_patch(context_id, info_offer_id, info_offer_update)

Update Info Offer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.info_offer_read_private import InfoOfferReadPrivate
from infonomy_client.models.info_offer_update import InfoOfferUpdate
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
    api_instance = infonomy_client.DecisionContextsApi(api_client)
    context_id = 56 # int | 
    info_offer_id = 56 # int | 
    info_offer_update = infonomy_client.InfoOfferUpdate() # InfoOfferUpdate | 

    try:
        # Update Info Offer
        api_response = api_instance.update_info_offer_questions_context_id_answers_info_offer_id_patch(context_id, info_offer_id, info_offer_update)
        print("The response of DecisionContextsApi->update_info_offer_questions_context_id_answers_info_offer_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecisionContextsApi->update_info_offer_questions_context_id_answers_info_offer_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **int**|  | 
 **info_offer_id** | **int**|  | 
 **info_offer_update** | [**InfoOfferUpdate**](InfoOfferUpdate.md)|  | 

### Return type

[**InfoOfferReadPrivate**](InfoOfferReadPrivate.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

