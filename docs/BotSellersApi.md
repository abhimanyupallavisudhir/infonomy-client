# infonomy_client.BotSellersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bot_seller_api_bot_sellers_post**](BotSellersApi.md#create_bot_seller_api_bot_sellers_post) | **POST** /api/bot-sellers/ | Create Bot Seller
[**create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post**](BotSellersApi.md#create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post) | **POST** /api/bot-sellers/{bot_seller_id}/matchers | Create Bot Seller Matcher
[**delete_bot_seller_api_bot_sellers_bot_seller_id_delete**](BotSellersApi.md#delete_bot_seller_api_bot_sellers_bot_seller_id_delete) | **DELETE** /api/bot-sellers/{bot_seller_id} | Delete Bot Seller
[**delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete**](BotSellersApi.md#delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete) | **DELETE** /api/bot-sellers/{bot_seller_id}/matchers/{matcher_id} | Delete Bot Seller Matcher
[**get_bot_seller_api_bot_sellers_bot_seller_id_get**](BotSellersApi.md#get_bot_seller_api_bot_sellers_bot_seller_id_get) | **GET** /api/bot-sellers/{bot_seller_id} | Get Bot Seller
[**list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get**](BotSellersApi.md#list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get) | **GET** /api/bot-sellers/{bot_seller_id}/matchers | List Bot Seller Matchers
[**list_bot_sellers_api_bot_sellers_get**](BotSellersApi.md#list_bot_sellers_api_bot_sellers_get) | **GET** /api/bot-sellers/ | List Bot Sellers
[**update_bot_seller_api_bot_sellers_bot_seller_id_put**](BotSellersApi.md#update_bot_seller_api_bot_sellers_bot_seller_id_put) | **PUT** /api/bot-sellers/{bot_seller_id} | Update Bot Seller
[**update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put**](BotSellersApi.md#update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put) | **PUT** /api/bot-sellers/{bot_seller_id}/matchers/{matcher_id} | Update Bot Seller Matcher


# **create_bot_seller_api_bot_sellers_post**
> BotSellerRead create_bot_seller_api_bot_sellers_post(bot_seller_create)

Create Bot Seller

Create a new BotSeller for the current user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.bot_seller_create import BotSellerCreate
from infonomy_client.models.bot_seller_read import BotSellerRead
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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_create = infonomy_client.BotSellerCreate() # BotSellerCreate | 

    try:
        # Create Bot Seller
        api_response = api_instance.create_bot_seller_api_bot_sellers_post(bot_seller_create)
        print("The response of BotSellersApi->create_bot_seller_api_bot_sellers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->create_bot_seller_api_bot_sellers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_create** | [**BotSellerCreate**](BotSellerCreate.md)|  | 

### Return type

[**BotSellerRead**](BotSellerRead.md)

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

# **create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post**
> SellerMatcherRead create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post(bot_seller_id, seller_matcher_create)

Create Bot Seller Matcher

Create a new matcher for a BotSeller

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.seller_matcher_create import SellerMatcherCreate
from infonomy_client.models.seller_matcher_read import SellerMatcherRead
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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 
    seller_matcher_create = infonomy_client.SellerMatcherCreate() # SellerMatcherCreate | 

    try:
        # Create Bot Seller Matcher
        api_response = api_instance.create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post(bot_seller_id, seller_matcher_create)
        print("The response of BotSellersApi->create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->create_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 
 **seller_matcher_create** | [**SellerMatcherCreate**](SellerMatcherCreate.md)|  | 

### Return type

[**SellerMatcherRead**](SellerMatcherRead.md)

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

# **delete_bot_seller_api_bot_sellers_bot_seller_id_delete**
> object delete_bot_seller_api_bot_sellers_bot_seller_id_delete(bot_seller_id)

Delete Bot Seller

Delete a BotSeller

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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 

    try:
        # Delete Bot Seller
        api_response = api_instance.delete_bot_seller_api_bot_sellers_bot_seller_id_delete(bot_seller_id)
        print("The response of BotSellersApi->delete_bot_seller_api_bot_sellers_bot_seller_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->delete_bot_seller_api_bot_sellers_bot_seller_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 

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

# **delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete**
> object delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete(bot_seller_id, matcher_id)

Delete Bot Seller Matcher

Delete a matcher for a BotSeller

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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 
    matcher_id = 56 # int | 

    try:
        # Delete Bot Seller Matcher
        api_response = api_instance.delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete(bot_seller_id, matcher_id)
        print("The response of BotSellersApi->delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->delete_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 
 **matcher_id** | **int**|  | 

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

# **get_bot_seller_api_bot_sellers_bot_seller_id_get**
> BotSellerRead get_bot_seller_api_bot_sellers_bot_seller_id_get(bot_seller_id)

Get Bot Seller

Get a specific BotSeller by ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.bot_seller_read import BotSellerRead
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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 

    try:
        # Get Bot Seller
        api_response = api_instance.get_bot_seller_api_bot_sellers_bot_seller_id_get(bot_seller_id)
        print("The response of BotSellersApi->get_bot_seller_api_bot_sellers_bot_seller_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->get_bot_seller_api_bot_sellers_bot_seller_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 

### Return type

[**BotSellerRead**](BotSellerRead.md)

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

# **list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get**
> List[SellerMatcherRead] list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get(bot_seller_id)

List Bot Seller Matchers

List all matchers for a BotSeller

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.seller_matcher_read import SellerMatcherRead
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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 

    try:
        # List Bot Seller Matchers
        api_response = api_instance.list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get(bot_seller_id)
        print("The response of BotSellersApi->list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->list_bot_seller_matchers_api_bot_sellers_bot_seller_id_matchers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 

### Return type

[**List[SellerMatcherRead]**](SellerMatcherRead.md)

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

# **list_bot_sellers_api_bot_sellers_get**
> List[BotSellerRead] list_bot_sellers_api_bot_sellers_get()

List Bot Sellers

List all BotSellers for the current user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.bot_seller_read import BotSellerRead
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
    api_instance = infonomy_client.BotSellersApi(api_client)

    try:
        # List Bot Sellers
        api_response = api_instance.list_bot_sellers_api_bot_sellers_get()
        print("The response of BotSellersApi->list_bot_sellers_api_bot_sellers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->list_bot_sellers_api_bot_sellers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BotSellerRead]**](BotSellerRead.md)

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

# **update_bot_seller_api_bot_sellers_bot_seller_id_put**
> BotSellerRead update_bot_seller_api_bot_sellers_bot_seller_id_put(bot_seller_id, bot_seller_update)

Update Bot Seller

Update a BotSeller

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.bot_seller_read import BotSellerRead
from infonomy_client.models.bot_seller_update import BotSellerUpdate
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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 
    bot_seller_update = infonomy_client.BotSellerUpdate() # BotSellerUpdate | 

    try:
        # Update Bot Seller
        api_response = api_instance.update_bot_seller_api_bot_sellers_bot_seller_id_put(bot_seller_id, bot_seller_update)
        print("The response of BotSellersApi->update_bot_seller_api_bot_sellers_bot_seller_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->update_bot_seller_api_bot_sellers_bot_seller_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 
 **bot_seller_update** | [**BotSellerUpdate**](BotSellerUpdate.md)|  | 

### Return type

[**BotSellerRead**](BotSellerRead.md)

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

# **update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put**
> SellerMatcherRead update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put(bot_seller_id, matcher_id, seller_matcher_update)

Update Bot Seller Matcher

Update a matcher for a BotSeller

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.seller_matcher_read import SellerMatcherRead
from infonomy_client.models.seller_matcher_update import SellerMatcherUpdate
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
    api_instance = infonomy_client.BotSellersApi(api_client)
    bot_seller_id = 56 # int | 
    matcher_id = 56 # int | 
    seller_matcher_update = infonomy_client.SellerMatcherUpdate() # SellerMatcherUpdate | 

    try:
        # Update Bot Seller Matcher
        api_response = api_instance.update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put(bot_seller_id, matcher_id, seller_matcher_update)
        print("The response of BotSellersApi->update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotSellersApi->update_bot_seller_matcher_api_bot_sellers_bot_seller_id_matchers_matcher_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 
 **matcher_id** | **int**|  | 
 **seller_matcher_update** | [**SellerMatcherUpdate**](SellerMatcherUpdate.md)|  | 

### Return type

[**SellerMatcherRead**](SellerMatcherRead.md)

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

