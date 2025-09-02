# HumanBuyerCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_child_llm** | [**LLMBuyerType**](LLMBuyerType.md) |  | [optional] 

## Example

```python
from infonomy_client.models.human_buyer_create import HumanBuyerCreate

# TODO update the JSON string below
json = "{}"
# create an instance of HumanBuyerCreate from a JSON string
human_buyer_create_instance = HumanBuyerCreate.from_json(json)
# print the JSON string representation of the object
print(HumanBuyerCreate.to_json())

# convert the object into a dict
human_buyer_create_dict = human_buyer_create_instance.to_dict()
# create an instance of HumanBuyerCreate from a dict
human_buyer_create_from_dict = HumanBuyerCreate.from_dict(human_buyer_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


