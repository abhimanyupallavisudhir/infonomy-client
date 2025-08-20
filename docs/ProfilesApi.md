# infonomy_client.ProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_human_buyer_buyers_post**](ProfilesApi.md#create_human_buyer_buyers_post) | **POST** /buyers | Create Human Buyer
[**create_human_seller_sellers_post**](ProfilesApi.md#create_human_seller_sellers_post) | **POST** /sellers | Create Human Seller
[**read_current_human_buyer_buyers_me_get**](ProfilesApi.md#read_current_human_buyer_buyers_me_get) | **GET** /buyers/me | Read Current Human Buyer
[**update_current_human_buyer_buyers_me_put**](ProfilesApi.md#update_current_human_buyer_buyers_me_put) | **PUT** /buyers/me | Update Current Human Buyer


# **create_human_buyer_buyers_post**
> HumanBuyerRead create_human_buyer_buyers_post(human_buyer_create)

Create Human Buyer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.human_buyer_create import HumanBuyerCreate
from infonomy_client.models.human_buyer_read import HumanBuyerRead
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
    api_instance = infonomy_client.ProfilesApi(api_client)
    human_buyer_create = infonomy_client.HumanBuyerCreate() # HumanBuyerCreate | 

    try:
        # Create Human Buyer
        api_response = api_instance.create_human_buyer_buyers_post(human_buyer_create)
        print("The response of ProfilesApi->create_human_buyer_buyers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_human_buyer_buyers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **human_buyer_create** | [**HumanBuyerCreate**](HumanBuyerCreate.md)|  | 

### Return type

[**HumanBuyerRead**](HumanBuyerRead.md)

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

# **create_human_seller_sellers_post**
> HumanSeller create_human_seller_sellers_post()

Create Human Seller

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.human_seller import HumanSeller
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
    api_instance = infonomy_client.ProfilesApi(api_client)

    try:
        # Create Human Seller
        api_response = api_instance.create_human_seller_sellers_post()
        print("The response of ProfilesApi->create_human_seller_sellers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_human_seller_sellers_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HumanSeller**](HumanSeller.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_current_human_buyer_buyers_me_get**
> HumanBuyerRead read_current_human_buyer_buyers_me_get()

Read Current Human Buyer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.human_buyer_read import HumanBuyerRead
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
    api_instance = infonomy_client.ProfilesApi(api_client)

    try:
        # Read Current Human Buyer
        api_response = api_instance.read_current_human_buyer_buyers_me_get()
        print("The response of ProfilesApi->read_current_human_buyer_buyers_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->read_current_human_buyer_buyers_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HumanBuyerRead**](HumanBuyerRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_human_buyer_buyers_me_put**
> HumanBuyerRead update_current_human_buyer_buyers_me_put(human_buyer_update)

Update Current Human Buyer

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.human_buyer_read import HumanBuyerRead
from infonomy_client.models.human_buyer_update import HumanBuyerUpdate
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
    api_instance = infonomy_client.ProfilesApi(api_client)
    human_buyer_update = infonomy_client.HumanBuyerUpdate() # HumanBuyerUpdate | 

    try:
        # Update Current Human Buyer
        api_response = api_instance.update_current_human_buyer_buyers_me_put(human_buyer_update)
        print("The response of ProfilesApi->update_current_human_buyer_buyers_me_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_current_human_buyer_buyers_me_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **human_buyer_update** | [**HumanBuyerUpdate**](HumanBuyerUpdate.md)|  | 

### Return type

[**HumanBuyerRead**](HumanBuyerRead.md)

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

