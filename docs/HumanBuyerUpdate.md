# HumanBuyerUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_child_llm** | [**LLMBuyerType**](LLMBuyerType.md) |  | [optional] 

## Example

```python
from infonomy_client.models.human_buyer_update import HumanBuyerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of HumanBuyerUpdate from a JSON string
human_buyer_update_instance = HumanBuyerUpdate.from_json(json)
# print the JSON string representation of the object
print(HumanBuyerUpdate.to_json())

# convert the object into a dict
human_buyer_update_dict = human_buyer_update_instance.to_dict()
# create an instance of HumanBuyerUpdate from a dict
human_buyer_update_from_dict = HumanBuyerUpdate.from_dict(human_buyer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


