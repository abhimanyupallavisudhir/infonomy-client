# infonomy_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_daily_bonus_users_me_daily_bonus_post**](UsersApi.md#claim_daily_bonus_users_me_daily_bonus_post) | **POST** /users/me/daily-bonus | Claim Daily Bonus
[**get_api_keys_users_me_api_keys_get**](UsersApi.md#get_api_keys_users_me_api_keys_get) | **GET** /users/me/api-keys | Get Api Keys
[**get_current_user_api_users_me_get**](UsersApi.md#get_current_user_api_users_me_get) | **GET** /api/users/me | Get Current User
[**get_current_user_purchases_users_me_purchases_get**](UsersApi.md#get_current_user_purchases_users_me_purchases_get) | **GET** /users/me/purchases | Get Current User Purchases
[**get_current_user_sales_users_me_sales_get**](UsersApi.md#get_current_user_sales_users_me_sales_get) | **GET** /users/me/sales | Get Current User Sales
[**get_daily_bonus_status_users_me_daily_bonus_get**](UsersApi.md#get_daily_bonus_status_users_me_daily_bonus_get) | **GET** /users/me/daily-bonus | Get Daily Bonus Status
[**get_transactions_transactions_get**](UsersApi.md#get_transactions_transactions_get) | **GET** /transactions | Get Transactions
[**get_user_api_users_user_id_get**](UsersApi.md#get_user_api_users_user_id_get) | **GET** /api/users/{user_id} | Get User
[**get_users_api_users_get**](UsersApi.md#get_users_api_users_get) | **GET** /api/users/ | Get Users
[**update_api_keys_users_me_api_keys_put**](UsersApi.md#update_api_keys_users_me_api_keys_put) | **PUT** /users/me/api-keys | Update Api Keys
[**update_current_user_api_users_me_put**](UsersApi.md#update_current_user_api_users_me_put) | **PUT** /api/users/me | Update Current User
[**users_current_user_users_me_get**](UsersApi.md#users_current_user_users_me_get) | **GET** /users/me | Users:Current User
[**users_delete_user_users_id_delete**](UsersApi.md#users_delete_user_users_id_delete) | **DELETE** /users/{id} | Users:Delete User
[**users_patch_current_user_users_me_patch**](UsersApi.md#users_patch_current_user_users_me_patch) | **PATCH** /users/me | Users:Patch Current User
[**users_patch_user_users_id_patch**](UsersApi.md#users_patch_user_users_id_patch) | **PATCH** /users/{id} | Users:Patch User
[**users_user_users_id_get**](UsersApi.md#users_user_users_id_get) | **GET** /users/{id} | Users:User


# **claim_daily_bonus_users_me_daily_bonus_post**
> object claim_daily_bonus_users_me_daily_bonus_post()

Claim Daily Bonus

Manually claim daily bonus (useful if automatic login bonus didn't work)

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
    api_instance = infonomy_client.UsersApi(api_client)

    try:
        # Claim Daily Bonus
        api_response = api_instance.claim_daily_bonus_users_me_daily_bonus_post()
        print("The response of UsersApi->claim_daily_bonus_users_me_daily_bonus_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->claim_daily_bonus_users_me_daily_bonus_post: %s\n" % e)
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

# **get_api_keys_users_me_api_keys_get**
> object get_api_keys_users_me_api_keys_get()

Get Api Keys

Get current user's API keys (only key names, not values for security)

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
    api_instance = infonomy_client.UsersApi(api_client)

    try:
        # Get Api Keys
        api_response = api_instance.get_api_keys_users_me_api_keys_get()
        print("The response of UsersApi->get_api_keys_users_me_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_api_keys_users_me_api_keys_get: %s\n" % e)
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

# **get_current_user_api_users_me_get**
> UserReadPrivate get_current_user_api_users_me_get()

Get Current User

Get current user profile

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.user_read_private import UserReadPrivate
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
    api_instance = infonomy_client.UsersApi(api_client)

    try:
        # Get Current User
        api_response = api_instance.get_current_user_api_users_me_get()
        print("The response of UsersApi->get_current_user_api_users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_api_users_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserReadPrivate**](UserReadPrivate.md)

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

# **get_current_user_purchases_users_me_purchases_get**
> object get_current_user_purchases_users_me_purchases_get(skip=skip, limit=limit)

Get Current User Purchases

Get current user's purchase history

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
    api_instance = infonomy_client.UsersApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # Get Current User Purchases
        api_response = api_instance.get_current_user_purchases_users_me_purchases_get(skip=skip, limit=limit)
        print("The response of UsersApi->get_current_user_purchases_users_me_purchases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_purchases_users_me_purchases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

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

# **get_current_user_sales_users_me_sales_get**
> object get_current_user_sales_users_me_sales_get(skip=skip, limit=limit)

Get Current User Sales

Get current user's sales history

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
    api_instance = infonomy_client.UsersApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # Get Current User Sales
        api_response = api_instance.get_current_user_sales_users_me_sales_get(skip=skip, limit=limit)
        print("The response of UsersApi->get_current_user_sales_users_me_sales_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_sales_users_me_sales_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

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

# **get_daily_bonus_status_users_me_daily_bonus_get**
> object get_daily_bonus_status_users_me_daily_bonus_get()

Get Daily Bonus Status

Get current user's daily bonus status

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
    api_instance = infonomy_client.UsersApi(api_client)

    try:
        # Get Daily Bonus Status
        api_response = api_instance.get_daily_bonus_status_users_me_daily_bonus_get()
        print("The response of UsersApi->get_daily_bonus_status_users_me_daily_bonus_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_daily_bonus_status_users_me_daily_bonus_get: %s\n" % e)
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

# **get_transactions_transactions_get**
> object get_transactions_transactions_get(skip=skip, limit=limit)

Get Transactions

Get all transactions (purchases and sales) for the current user

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
    api_instance = infonomy_client.UsersApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Number of records to return (optional) (default to 100)

    try:
        # Get Transactions
        api_response = api_instance.get_transactions_transactions_get(skip=skip, limit=limit)
        print("The response of UsersApi->get_transactions_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_transactions_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Number of records to return | [optional] [default to 100]

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

# **get_user_api_users_user_id_get**
> UserRead get_user_api_users_user_id_get(user_id)

Get User

Get public user profile by ID

### Example


```python
import infonomy_client
from infonomy_client.models.user_read import UserRead
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
    api_instance = infonomy_client.UsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Get User
        api_response = api_instance.get_user_api_users_user_id_get(user_id)
        print("The response of UsersApi->get_user_api_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_api_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserRead**](UserRead.md)

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

# **get_users_api_users_get**
> List[UserRead] get_users_api_users_get()

Get Users

### Example


```python
import infonomy_client
from infonomy_client.models.user_read import UserRead
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
    api_instance = infonomy_client.UsersApi(api_client)

    try:
        # Get Users
        api_response = api_instance.get_users_api_users_get()
        print("The response of UsersApi->get_users_api_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_api_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserRead]**](UserRead.md)

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

# **update_api_keys_users_me_api_keys_put**
> object update_api_keys_users_me_api_keys_put(request_body)

Update Api Keys

Update current user's API keys for LLM services

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
    api_instance = infonomy_client.UsersApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Update Api Keys
        api_response = api_instance.update_api_keys_users_me_api_keys_put(request_body)
        print("The response of UsersApi->update_api_keys_users_me_api_keys_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_api_keys_users_me_api_keys_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**object**

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

# **update_current_user_api_users_me_put**
> UserReadPrivate update_current_user_api_users_me_put(user_update)

Update Current User

Update current user profile

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.user_read_private import UserReadPrivate
from infonomy_client.models.user_update import UserUpdate
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
    api_instance = infonomy_client.UsersApi(api_client)
    user_update = infonomy_client.UserUpdate() # UserUpdate | 

    try:
        # Update Current User
        api_response = api_instance.update_current_user_api_users_me_put(user_update)
        print("The response of UsersApi->update_current_user_api_users_me_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_current_user_api_users_me_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserReadPrivate**](UserReadPrivate.md)

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

# **users_current_user_users_me_get**
> UserRead users_current_user_users_me_get()

Users:Current User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.user_read import UserRead
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
    api_instance = infonomy_client.UsersApi(api_client)

    try:
        # Users:Current User
        api_response = api_instance.users_current_user_users_me_get()
        print("The response of UsersApi->users_current_user_users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_current_user_users_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_user_users_id_delete**
> users_delete_user_users_id_delete(id)

Users:Delete User

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
    api_instance = infonomy_client.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Users:Delete User
        api_instance.users_delete_user_users_id_delete(id)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_user_users_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_current_user_users_me_patch**
> UserRead users_patch_current_user_users_me_patch(user_update)

Users:Patch Current User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.user_read import UserRead
from infonomy_client.models.user_update import UserUpdate
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
    api_instance = infonomy_client.UsersApi(api_client)
    user_update = infonomy_client.UserUpdate() # UserUpdate | 

    try:
        # Users:Patch Current User
        api_response = api_instance.users_patch_current_user_users_me_patch(user_update)
        print("The response of UsersApi->users_patch_current_user_users_me_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_patch_current_user_users_me_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_user_users_id_patch**
> UserRead users_patch_user_users_id_patch(id, user_update)

Users:Patch User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.user_read import UserRead
from infonomy_client.models.user_update import UserUpdate
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
    api_instance = infonomy_client.UsersApi(api_client)
    id = 'id_example' # str | 
    user_update = infonomy_client.UserUpdate() # UserUpdate | 

    try:
        # Users:Patch User
        api_response = api_instance.users_patch_user_users_id_patch(id, user_update)
        print("The response of UsersApi->users_patch_user_users_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_patch_user_users_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_users_id_get**
> UserRead users_user_users_id_get(id)

Users:User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import infonomy_client
from infonomy_client.models.user_read import UserRead
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
    api_instance = infonomy_client.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Users:User
        api_response = api_instance.users_user_users_id_get(id)
        print("The response of UsersApi->users_user_users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_user_users_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Not a superuser. |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

