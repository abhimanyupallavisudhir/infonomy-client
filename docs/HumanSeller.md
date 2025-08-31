# HumanSeller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user_id** | **int** |  | 
**type** | **str** |  | [optional] [default to 'human_seller']

## Example

```python
from infonomy_client.models.human_seller import HumanSeller

# TODO update the JSON string below
json = "{}"
# create an instance of HumanSeller from a JSON string
human_seller_instance = HumanSeller.from_json(json)
# print the JSON string representation of the object
print(HumanSeller.to_json())

# convert the object into a dict
human_seller_dict = human_seller_instance.to_dict()
# create an instance of HumanSeller from a dict
human_seller_from_dict = HumanSeller.from_dict(human_seller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


