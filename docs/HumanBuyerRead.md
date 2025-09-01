# HumanBuyerRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**default_child_llm** | [**LLMBuyerType**](LLMBuyerType.md) |  | 
**default_max_budget** | **float** |  | 
**num_queries** | **Dict[str, int]** |  | 
**num_inspected** | **Dict[str, int]** |  | 
**num_purchased** | **Dict[str, int]** |  | 
**inspection_rate** | **Dict[str, float]** |  | 
**purchase_rate** | **Dict[str, float]** |  | 

## Example

```python
from infonomy_client.models.human_buyer_read import HumanBuyerRead

# TODO update the JSON string below
json = "{}"
# create an instance of HumanBuyerRead from a JSON string
human_buyer_read_instance = HumanBuyerRead.from_json(json)
# print the JSON string representation of the object
print(HumanBuyerRead.to_json())

# convert the object into a dict
human_buyer_read_dict = human_buyer_read_instance.to_dict()
# create an instance of HumanBuyerRead from a dict
human_buyer_read_from_dict = HumanBuyerRead.from_dict(human_buyer_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


