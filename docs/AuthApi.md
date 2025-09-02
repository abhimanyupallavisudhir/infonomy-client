# infonomy_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_jwt_login_api_auth_jwt_login_post**](AuthApi.md#auth_jwt_login_api_auth_jwt_login_post) | **POST** /api/auth/jwt/login | Auth:Jwt.Login
[**auth_jwt_logout_api_auth_jwt_logout_post**](AuthApi.md#auth_jwt_logout_api_auth_jwt_logout_post) | **POST** /api/auth/jwt/logout | Auth:Jwt.Logout
[**register_register_api_auth_register_post**](AuthApi.md#register_register_api_auth_register_post) | **POST** /api/auth/register | Register:Register
[**reset_forgot_password_api_auth_forgot_password_post**](AuthApi.md#reset_forgot_password_api_auth_forgot_password_post) | **POST** /api/auth/forgot-password | Reset:Forgot Password
[**reset_reset_password_api_auth_reset_password_post**](AuthApi.md#reset_reset_password_api_auth_reset_password_post) | **POST** /api/auth/reset-password | Reset:Reset Password
[**verify_request_token_auth_request_verify_token_post**](AuthApi.md#verify_request_token_auth_request_verify_token_post) | **POST** /auth/request-verify-token | Verify:Request-Token
[**verify_verify_auth_verify_post**](AuthApi.md#verify_verify_auth_verify_post) | **POST** /auth/verify | Verify:Verify


# **auth_jwt_login_api_auth_jwt_login_post**
> BearerResponse auth_jwt_login_api_auth_jwt_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Auth:Jwt.Login

### Example


```python
import infonomy_client
from infonomy_client.models.bearer_response import BearerResponse
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
    api_instance = infonomy_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Auth:Jwt.Login
        api_response = api_instance.auth_jwt_login_api_auth_jwt_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->auth_jwt_login_api_auth_jwt_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_jwt_login_api_auth_jwt_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**BearerResponse**](BearerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_jwt_logout_api_auth_jwt_logout_post**
> object auth_jwt_logout_api_auth_jwt_logout_post()

Auth:Jwt.Logout

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
    api_instance = infonomy_client.AuthApi(api_client)

    try:
        # Auth:Jwt.Logout
        api_response = api_instance.auth_jwt_logout_api_auth_jwt_logout_post()
        print("The response of AuthApi->auth_jwt_logout_api_auth_jwt_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_jwt_logout_api_auth_jwt_logout_post: %s\n" % e)
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
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_register_api_auth_register_post**
> UserRead register_register_api_auth_register_post(user_create)

Register:Register

### Example


```python
import infonomy_client
from infonomy_client.models.user_create import UserCreate
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
    api_instance = infonomy_client.AuthApi(api_client)
    user_create = infonomy_client.UserCreate() # UserCreate | 

    try:
        # Register:Register
        api_response = api_instance.register_register_api_auth_register_post(user_create)
        print("The response of AuthApi->register_register_api_auth_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register_register_api_auth_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_forgot_password_api_auth_forgot_password_post**
> object reset_forgot_password_api_auth_forgot_password_post(body_reset_forgot_password_api_auth_forgot_password_post)

Reset:Forgot Password

### Example


```python
import infonomy_client
from infonomy_client.models.body_reset_forgot_password_api_auth_forgot_password_post import BodyResetForgotPasswordApiAuthForgotPasswordPost
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
    api_instance = infonomy_client.AuthApi(api_client)
    body_reset_forgot_password_api_auth_forgot_password_post = infonomy_client.BodyResetForgotPasswordApiAuthForgotPasswordPost() # BodyResetForgotPasswordApiAuthForgotPasswordPost | 

    try:
        # Reset:Forgot Password
        api_response = api_instance.reset_forgot_password_api_auth_forgot_password_post(body_reset_forgot_password_api_auth_forgot_password_post)
        print("The response of AuthApi->reset_forgot_password_api_auth_forgot_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->reset_forgot_password_api_auth_forgot_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_reset_forgot_password_api_auth_forgot_password_post** | [**BodyResetForgotPasswordApiAuthForgotPasswordPost**](BodyResetForgotPasswordApiAuthForgotPasswordPost.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_reset_password_api_auth_reset_password_post**
> object reset_reset_password_api_auth_reset_password_post(body_reset_reset_password_api_auth_reset_password_post)

Reset:Reset Password

### Example


```python
import infonomy_client
from infonomy_client.models.body_reset_reset_password_api_auth_reset_password_post import BodyResetResetPasswordApiAuthResetPasswordPost
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
    api_instance = infonomy_client.AuthApi(api_client)
    body_reset_reset_password_api_auth_reset_password_post = infonomy_client.BodyResetResetPasswordApiAuthResetPasswordPost() # BodyResetResetPasswordApiAuthResetPasswordPost | 

    try:
        # Reset:Reset Password
        api_response = api_instance.reset_reset_password_api_auth_reset_password_post(body_reset_reset_password_api_auth_reset_password_post)
        print("The response of AuthApi->reset_reset_password_api_auth_reset_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->reset_reset_password_api_auth_reset_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_reset_reset_password_api_auth_reset_password_post** | [**BodyResetResetPasswordApiAuthResetPasswordPost**](BodyResetResetPasswordApiAuthResetPasswordPost.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_request_token_auth_request_verify_token_post**
> object verify_request_token_auth_request_verify_token_post(body_verify_request_token_auth_request_verify_token_post)

Verify:Request-Token

### Example


```python
import infonomy_client
from infonomy_client.models.body_verify_request_token_auth_request_verify_token_post import BodyVerifyRequestTokenAuthRequestVerifyTokenPost
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
    api_instance = infonomy_client.AuthApi(api_client)
    body_verify_request_token_auth_request_verify_token_post = infonomy_client.BodyVerifyRequestTokenAuthRequestVerifyTokenPost() # BodyVerifyRequestTokenAuthRequestVerifyTokenPost | 

    try:
        # Verify:Request-Token
        api_response = api_instance.verify_request_token_auth_request_verify_token_post(body_verify_request_token_auth_request_verify_token_post)
        print("The response of AuthApi->verify_request_token_auth_request_verify_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify_request_token_auth_request_verify_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_request_token_auth_request_verify_token_post** | [**BodyVerifyRequestTokenAuthRequestVerifyTokenPost**](BodyVerifyRequestTokenAuthRequestVerifyTokenPost.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_verify_auth_verify_post**
> UserRead verify_verify_auth_verify_post(body_verify_verify_auth_verify_post)

Verify:Verify

### Example


```python
import infonomy_client
from infonomy_client.models.body_verify_verify_auth_verify_post import BodyVerifyVerifyAuthVerifyPost
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
    api_instance = infonomy_client.AuthApi(api_client)
    body_verify_verify_auth_verify_post = infonomy_client.BodyVerifyVerifyAuthVerifyPost() # BodyVerifyVerifyAuthVerifyPost | 

    try:
        # Verify:Verify
        api_response = api_instance.verify_verify_auth_verify_post(body_verify_verify_auth_verify_post)
        print("The response of AuthApi->verify_verify_auth_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify_verify_auth_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_verify_auth_verify_post** | [**BodyVerifyVerifyAuthVerifyPost**](BodyVerifyVerifyAuthVerifyPost.md)|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

