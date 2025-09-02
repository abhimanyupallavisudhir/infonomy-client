# infonomy_client.ProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_human_buyer_api_buyers_post**](ProfilesApi.md#create_human_buyer_api_buyers_post) | **POST** /api/buyers | Create Human Buyer
[**create_human_seller_api_sellers_post**](ProfilesApi.md#create_human_seller_api_sellers_post) | **POST** /api/sellers | Create Human Seller
[**create_human_seller_matcher_api_sellers_me_matchers_post**](ProfilesApi.md#create_human_seller_matcher_api_sellers_me_matchers_post) | **POST** /api/sellers/me/matchers | Create Human Seller Matcher
[**delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete**](ProfilesApi.md#delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete) | **DELETE** /api/sellers/me/matchers/{matcher_id} | Delete Human Seller Matcher
[**get_buyer_stats_by_id_api_buyers_user_id_stats_get**](ProfilesApi.md#get_buyer_stats_by_id_api_buyers_user_id_stats_get) | **GET** /api/buyers/{user_id}/stats | Get Buyer Stats By Id
[**get_current_buyer_stats_api_buyers_me_stats_get**](ProfilesApi.md#get_current_buyer_stats_api_buyers_me_stats_get) | **GET** /api/buyers/me/stats | Get Current Buyer Stats
[**list_human_seller_matchers_api_sellers_me_matchers_get**](ProfilesApi.md#list_human_seller_matchers_api_sellers_me_matchers_get) | **GET** /api/sellers/me/matchers | List Human Seller Matchers
[**read_current_human_buyer_api_buyers_me_get**](ProfilesApi.md#read_current_human_buyer_api_buyers_me_get) | **GET** /api/buyers/me | Read Current Human Buyer
[**read_current_human_seller_api_sellers_me_get**](ProfilesApi.md#read_current_human_seller_api_sellers_me_get) | **GET** /api/sellers/me | Read Current Human Seller
[**update_current_human_buyer_api_buyers_me_put**](ProfilesApi.md#update_current_human_buyer_api_buyers_me_put) | **PUT** /api/buyers/me | Update Current Human Buyer
[**update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put**](ProfilesApi.md#update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put) | **PUT** /api/sellers/me/matchers/{matcher_id} | Update Human Seller Matcher


# **create_human_buyer_api_buyers_post**
> HumanBuyerRead create_human_buyer_api_buyers_post(human_buyer_create)

Create Human Buyer

### Example


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


# Enter a context with an instance of the API client
with infonomy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infonomy_client.ProfilesApi(api_client)
    human_buyer_create = infonomy_client.HumanBuyerCreate() # HumanBuyerCreate | 

    try:
        # Create Human Buyer
        api_response = api_instance.create_human_buyer_api_buyers_post(human_buyer_create)
        print("The response of ProfilesApi->create_human_buyer_api_buyers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_human_buyer_api_buyers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **human_buyer_create** | [**HumanBuyerCreate**](HumanBuyerCreate.md)|  | 

### Return type

[**HumanBuyerRead**](HumanBuyerRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_human_seller_api_sellers_post**
> HumanSeller create_human_seller_api_sellers_post()

Create Human Seller

### Example


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


# Enter a context with an instance of the API client
with infonomy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = infonomy_client.ProfilesApi(api_client)

    try:
        # Create Human Seller
        api_response = api_instance.create_human_seller_api_sellers_post()
        print("The response of ProfilesApi->create_human_seller_api_sellers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_human_seller_api_sellers_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HumanSeller**](HumanSeller.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_human_seller_matcher_api_sellers_me_matchers_post**
> SellerMatcherRead create_human_seller_matcher_api_sellers_me_matchers_post(seller_matcher_create)

Create Human Seller Matcher

Create a new matcher for the current user's HumanSeller profile

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
    api_instance = infonomy_client.ProfilesApi(api_client)
    seller_matcher_create = infonomy_client.SellerMatcherCreate() # SellerMatcherCreate | 

    try:
        # Create Human Seller Matcher
        api_response = api_instance.create_human_seller_matcher_api_sellers_me_matchers_post(seller_matcher_create)
        print("The response of ProfilesApi->create_human_seller_matcher_api_sellers_me_matchers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->create_human_seller_matcher_api_sellers_me_matchers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete**
> object delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete(matcher_id)

Delete Human Seller Matcher

Delete a matcher for the current user's HumanSeller profile

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
    api_instance = infonomy_client.ProfilesApi(api_client)
    matcher_id = 56 # int | 

    try:
        # Delete Human Seller Matcher
        api_response = api_instance.delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete(matcher_id)
        print("The response of ProfilesApi->delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->delete_human_seller_matcher_api_sellers_me_matchers_matcher_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_buyer_stats_by_id_api_buyers_user_id_stats_get**
> object get_buyer_stats_by_id_api_buyers_user_id_stats_get(user_id)

Get Buyer Stats By Id

Get buyer statistics for a specific user (admin access)

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
    api_instance = infonomy_client.ProfilesApi(api_client)
    user_id = 56 # int | 

    try:
        # Get Buyer Stats By Id
        api_response = api_instance.get_buyer_stats_by_id_api_buyers_user_id_stats_get(user_id)
        print("The response of ProfilesApi->get_buyer_stats_by_id_api_buyers_user_id_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_buyer_stats_by_id_api_buyers_user_id_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

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

# **get_current_buyer_stats_api_buyers_me_stats_get**
> object get_current_buyer_stats_api_buyers_me_stats_get()

Get Current Buyer Stats

Get current user's buyer statistics

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
    api_instance = infonomy_client.ProfilesApi(api_client)

    try:
        # Get Current Buyer Stats
        api_response = api_instance.get_current_buyer_stats_api_buyers_me_stats_get()
        print("The response of ProfilesApi->get_current_buyer_stats_api_buyers_me_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_current_buyer_stats_api_buyers_me_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_human_seller_matchers_api_sellers_me_matchers_get**
> List[SellerMatcherRead] list_human_seller_matchers_api_sellers_me_matchers_get()

List Human Seller Matchers

List all matchers for the current user's HumanSeller profile

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
    api_instance = infonomy_client.ProfilesApi(api_client)

    try:
        # List Human Seller Matchers
        api_response = api_instance.list_human_seller_matchers_api_sellers_me_matchers_get()
        print("The response of ProfilesApi->list_human_seller_matchers_api_sellers_me_matchers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->list_human_seller_matchers_api_sellers_me_matchers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_current_human_buyer_api_buyers_me_get**
> HumanBuyerRead read_current_human_buyer_api_buyers_me_get()

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
        api_response = api_instance.read_current_human_buyer_api_buyers_me_get()
        print("The response of ProfilesApi->read_current_human_buyer_api_buyers_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->read_current_human_buyer_api_buyers_me_get: %s\n" % e)
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

# **read_current_human_seller_api_sellers_me_get**
> HumanSellerRead read_current_human_seller_api_sellers_me_get()

Read Current Human Seller

Get current user's seller profile

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.human_seller_read import HumanSellerRead
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
        # Read Current Human Seller
        api_response = api_instance.read_current_human_seller_api_sellers_me_get()
        print("The response of ProfilesApi->read_current_human_seller_api_sellers_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->read_current_human_seller_api_sellers_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HumanSellerRead**](HumanSellerRead.md)

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

# **update_current_human_buyer_api_buyers_me_put**
> HumanBuyerRead update_current_human_buyer_api_buyers_me_put(human_buyer_update)

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
        api_response = api_instance.update_current_human_buyer_api_buyers_me_put(human_buyer_update)
        print("The response of ProfilesApi->update_current_human_buyer_api_buyers_me_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_current_human_buyer_api_buyers_me_put: %s\n" % e)
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

# **update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put**
> SellerMatcherRead update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put(matcher_id, seller_matcher_update)

Update Human Seller Matcher

Update a matcher for the current user's HumanSeller profile

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
    api_instance = infonomy_client.ProfilesApi(api_client)
    matcher_id = 56 # int | 
    seller_matcher_update = infonomy_client.SellerMatcherUpdate() # SellerMatcherUpdate | 

    try:
        # Update Human Seller Matcher
        api_response = api_instance.update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put(matcher_id, seller_matcher_update)
        print("The response of ProfilesApi->update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_human_seller_matcher_api_sellers_me_matchers_matcher_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

