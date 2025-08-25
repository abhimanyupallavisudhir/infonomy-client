# UserRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**email** | **str** |  | 
**is_active** | **bool** |  | [optional] [default to True]
**is_superuser** | **bool** |  | [optional] [default to False]
**is_verified** | **bool** |  | [optional] [default to False]
**username** | **str** |  | 
**created_at** | **datetime** |  | 
**api_keys** | **Dict[str, object]** |  | [optional] 

## Example

```python
from infonomy_client.models.user_read import UserRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserRead from a JSON string
user_read_instance = UserRead.from_json(json)
# print the JSON string representation of the object
print(UserRead.to_json())

# convert the object into a dict
user_read_dict = user_read_instance.to_dict()
# create an instance of UserRead from a dict
user_read_from_dict = UserRead.from_dict(user_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


