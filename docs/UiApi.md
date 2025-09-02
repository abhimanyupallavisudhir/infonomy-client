# infonomy_client.UiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_answer_questions_question_id_answers_post**](UiApi.md#create_answer_questions_question_id_answers_post) | **POST** /questions/{question_id}/answers | Create Answer
[**create_bot_matcher_profile_bot_matcher_post**](UiApi.md#create_bot_matcher_profile_bot_matcher_post) | **POST** /profile/bot-matcher | Create Bot Matcher
[**create_bot_seller_profile_bot_seller_post**](UiApi.md#create_bot_seller_profile_bot_seller_post) | **POST** /profile/bot-seller | Create Bot Seller
[**create_buyer_profile_profile_buyer_post**](UiApi.md#create_buyer_profile_profile_buyer_post) | **POST** /profile/buyer | Create Buyer Profile
[**create_matcher_profile_matcher_post**](UiApi.md#create_matcher_profile_matcher_post) | **POST** /profile/matcher | Create Matcher
[**create_question_questions_post**](UiApi.md#create_question_questions_post) | **POST** /questions | Create Question
[**create_seller_profile_profile_seller_post**](UiApi.md#create_seller_profile_profile_seller_post) | **POST** /profile/seller | Create Seller Profile
[**debug_auth_debug_auth_get**](UiApi.md#debug_auth_debug_auth_get) | **GET** /debug/auth | Debug Auth
[**home_page_get**](UiApi.md#home_page_get) | **GET** / | Home Page
[**inspect_answer_inspect_question_id_answer_id_post**](UiApi.md#inspect_answer_inspect_question_id_answer_id_post) | **POST** /inspect/{question_id}/{answer_id} | Inspect Answer
[**profile_setup_page_profile_get**](UiApi.md#profile_setup_page_profile_get) | **GET** /profile | Profile Setup Page
[**question_detail_page_questions_question_id_get**](UiApi.md#question_detail_page_questions_question_id_get) | **GET** /questions/{question_id} | Question Detail Page
[**questions_page_questions_get**](UiApi.md#questions_page_questions_get) | **GET** /questions | Questions Page
[**register_page_register_get**](UiApi.md#register_page_register_get) | **GET** /register | Register Page
[**user_profile_page_users_user_id_get**](UiApi.md#user_profile_page_users_user_id_get) | **GET** /users/{user_id} | User Profile Page
[**users_page_users_get**](UiApi.md#users_page_users_get) | **GET** /users | Users Page


# **create_answer_questions_question_id_answers_post**
> str create_answer_questions_question_id_answers_post(question_id, private_info, public_info=public_info, price=price)

Create Answer

Handle new answer creation

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    question_id = 56 # int | 
    private_info = 'private_info_example' # str | 
    public_info = '' # str |  (optional) (default to '')
    price = 0.0 # float |  (optional) (default to 0.0)

    try:
        # Create Answer
        api_response = api_instance.create_answer_questions_question_id_answers_post(question_id, private_info, public_info=public_info, price=price)
        print("The response of UiApi->create_answer_questions_question_id_answers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_answer_questions_question_id_answers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**|  | 
 **private_info** | **str**|  | 
 **public_info** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **float**|  | [optional] [default to 0.0]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bot_matcher_profile_bot_matcher_post**
> str create_bot_matcher_profile_bot_matcher_post(bot_seller_id, keywords=keywords, min_max_budget=min_max_budget)

Create Bot Matcher

Create matcher for a bot seller

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    bot_seller_id = 56 # int | 
    keywords = '' # str |  (optional) (default to '')
    min_max_budget = 0.0 # float |  (optional) (default to 0.0)

    try:
        # Create Bot Matcher
        api_response = api_instance.create_bot_matcher_profile_bot_matcher_post(bot_seller_id, keywords=keywords, min_max_budget=min_max_budget)
        print("The response of UiApi->create_bot_matcher_profile_bot_matcher_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_bot_matcher_profile_bot_matcher_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_seller_id** | **int**|  | 
 **keywords** | **str**|  | [optional] [default to &#39;&#39;]
 **min_max_budget** | **float**|  | [optional] [default to 0.0]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bot_seller_profile_bot_seller_post**
> str create_bot_seller_profile_bot_seller_post(info=info, price=price, llm_model=llm_model, llm_prompt=llm_prompt)

Create Bot Seller

Create bot seller

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    info = '' # str |  (optional) (default to '')
    price = 0.0 # float |  (optional) (default to 0.0)
    llm_model = '' # str |  (optional) (default to '')
    llm_prompt = '' # str |  (optional) (default to '')

    try:
        # Create Bot Seller
        api_response = api_instance.create_bot_seller_profile_bot_seller_post(info=info, price=price, llm_model=llm_model, llm_prompt=llm_prompt)
        print("The response of UiApi->create_bot_seller_profile_bot_seller_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_bot_seller_profile_bot_seller_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info** | **str**|  | [optional] [default to &#39;&#39;]
 **price** | **float**|  | [optional] [default to 0.0]
 **llm_model** | **str**|  | [optional] [default to &#39;&#39;]
 **llm_prompt** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_profile_profile_buyer_post**
> str create_buyer_profile_profile_buyer_post(default_child_llm)

Create Buyer Profile

Create or update buyer profile

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    default_child_llm = 'default_child_llm_example' # str | 

    try:
        # Create Buyer Profile
        api_response = api_instance.create_buyer_profile_profile_buyer_post(default_child_llm)
        print("The response of UiApi->create_buyer_profile_profile_buyer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_buyer_profile_profile_buyer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_child_llm** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_matcher_profile_matcher_post**
> str create_matcher_profile_matcher_post(keywords=keywords, context_pages=context_pages, min_max_budget=min_max_budget, min_inspection_rate=min_inspection_rate, min_purchase_rate=min_purchase_rate, min_priority=min_priority, buyer_type=buyer_type, buyer_llm_model=buyer_llm_model, buyer_system_prompt=buyer_system_prompt, age_limit=age_limit)

Create Matcher

Create matcher for current user's seller profile

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    keywords = '' # str |  (optional) (default to '')
    context_pages = '' # str |  (optional) (default to '')
    min_max_budget = 0.0 # float |  (optional) (default to 0.0)
    min_inspection_rate = 0.0 # float |  (optional) (default to 0.0)
    min_purchase_rate = 0.0 # float |  (optional) (default to 0.0)
    min_priority = 0 # int |  (optional) (default to 0)
    buyer_type = '' # str |  (optional) (default to '')
    buyer_llm_model = '' # str |  (optional) (default to '')
    buyer_system_prompt = '' # str |  (optional) (default to '')
    age_limit = 0 # int |  (optional) (default to 0)

    try:
        # Create Matcher
        api_response = api_instance.create_matcher_profile_matcher_post(keywords=keywords, context_pages=context_pages, min_max_budget=min_max_budget, min_inspection_rate=min_inspection_rate, min_purchase_rate=min_purchase_rate, min_priority=min_priority, buyer_type=buyer_type, buyer_llm_model=buyer_llm_model, buyer_system_prompt=buyer_system_prompt, age_limit=age_limit)
        print("The response of UiApi->create_matcher_profile_matcher_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_matcher_profile_matcher_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | **str**|  | [optional] [default to &#39;&#39;]
 **context_pages** | **str**|  | [optional] [default to &#39;&#39;]
 **min_max_budget** | **float**|  | [optional] [default to 0.0]
 **min_inspection_rate** | **float**|  | [optional] [default to 0.0]
 **min_purchase_rate** | **float**|  | [optional] [default to 0.0]
 **min_priority** | **int**|  | [optional] [default to 0]
 **buyer_type** | **str**|  | [optional] [default to &#39;&#39;]
 **buyer_llm_model** | **str**|  | [optional] [default to &#39;&#39;]
 **buyer_system_prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **age_limit** | **int**|  | [optional] [default to 0]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question_questions_post**
> str create_question_questions_post(query, max_budget, context_pages=context_pages, priority=priority)

Create Question

Handle new question creation

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    query = 'query_example' # str | 
    max_budget = 3.4 # float | 
    context_pages = '' # str |  (optional) (default to '')
    priority = 0 # int |  (optional) (default to 0)

    try:
        # Create Question
        api_response = api_instance.create_question_questions_post(query, max_budget, context_pages=context_pages, priority=priority)
        print("The response of UiApi->create_question_questions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_question_questions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **max_budget** | **float**|  | 
 **context_pages** | **str**|  | [optional] [default to &#39;&#39;]
 **priority** | **int**|  | [optional] [default to 0]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_seller_profile_profile_seller_post**
> str create_seller_profile_profile_seller_post()

Create Seller Profile

Create seller profile

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Create Seller Profile
        api_response = api_instance.create_seller_profile_profile_seller_post()
        print("The response of UiApi->create_seller_profile_profile_seller_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->create_seller_profile_profile_seller_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_auth_debug_auth_get**
> str debug_auth_debug_auth_get()

Debug Auth

Debug endpoint to test authentication

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Debug Auth
        api_response = api_instance.debug_auth_debug_auth_get()
        print("The response of UiApi->debug_auth_debug_auth_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->debug_auth_debug_auth_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_page_get**
> str home_page_get()

Home Page

Home page with questions list and new question form

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Home Page
        api_response = api_instance.home_page_get()
        print("The response of UiApi->home_page_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->home_page_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_answer_inspect_question_id_answer_id_post**
> str inspect_answer_inspect_question_id_answer_id_post(question_id, answer_id)

Inspect Answer

Handle answer inspection

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
    api_instance = infonomy_client.UiApi(api_client)
    question_id = 56 # int | 
    answer_id = 56 # int | 

    try:
        # Inspect Answer
        api_response = api_instance.inspect_answer_inspect_question_id_answer_id_post(question_id, answer_id)
        print("The response of UiApi->inspect_answer_inspect_question_id_answer_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->inspect_answer_inspect_question_id_answer_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**|  | 
 **answer_id** | **int**|  | 

### Return type

**str**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_setup_page_profile_get**
> str profile_setup_page_profile_get()

Profile Setup Page

Profile setup page for new users

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Profile Setup Page
        api_response = api_instance.profile_setup_page_profile_get()
        print("The response of UiApi->profile_setup_page_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->profile_setup_page_profile_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **question_detail_page_questions_question_id_get**
> str question_detail_page_questions_question_id_get(question_id)

Question Detail Page

Individual question page with answers

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    question_id = 56 # int | 

    try:
        # Question Detail Page
        api_response = api_instance.question_detail_page_questions_question_id_get(question_id)
        print("The response of UiApi->question_detail_page_questions_question_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->question_detail_page_questions_question_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questions_page_questions_get**
> str questions_page_questions_get()

Questions Page

Questions listing page

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Questions Page
        api_response = api_instance.questions_page_questions_get()
        print("The response of UiApi->questions_page_questions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->questions_page_questions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_page_register_get**
> str register_page_register_get()

Register Page

User registration page

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Register Page
        api_response = api_instance.register_page_register_get()
        print("The response of UiApi->register_page_register_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->register_page_register_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_profile_page_users_user_id_get**
> str user_profile_page_users_user_id_get(user_id)

User Profile Page

Individual user profile page

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)
    user_id = 56 # int | 

    try:
        # User Profile Page
        api_response = api_instance.user_profile_page_users_user_id_get(user_id)
        print("The response of UiApi->user_profile_page_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->user_profile_page_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_page_users_get**
> str users_page_users_get()

Users Page

Users listing page

### Example


```python
import infonomy_client
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
    api_instance = infonomy_client.UiApi(api_client)

    try:
        # Users Page
        api_response = api_instance.users_page_users_get()
        print("The response of UiApi->users_page_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->users_page_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

