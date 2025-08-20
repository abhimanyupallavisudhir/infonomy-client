# LLMBuyerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**model** | **str** |  | [optional] [default to 'openrouter/openai/chatgpt-4o-latest']
**custom_prompt** | **str** |  | [optional] 
**max_budget** | **float** |  | [optional] [default to 50.0]

## Example

```python
from infonomy_client.models.llm_buyer_type import LLMBuyerType

# TODO update the JSON string below
json = "{}"
# create an instance of LLMBuyerType from a JSON string
llm_buyer_type_instance = LLMBuyerType.from_json(json)
# print the JSON string representation of the object
print(LLMBuyerType.to_json())

# convert the object into a dict
llm_buyer_type_dict = llm_buyer_type_instance.to_dict()
# create an instance of LLMBuyerType from a dict
llm_buyer_type_from_dict = LLMBuyerType.from_dict(llm_buyer_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


