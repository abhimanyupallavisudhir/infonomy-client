# DecisionContextRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**query** | **str** |  | 
**context_pages** | **List[str]** |  | 
**buyer_id** | **int** |  | 
**max_budget** | **float** |  | 
**seller_ids** | **List[int]** |  | 
**priority** | **int** |  | 
**created_at** | **datetime** |  | 
**parent** | [**DecisionContextRead**](DecisionContextRead.md) |  | 

## Example

```python
from infonomy_client.models.decision_context_read import DecisionContextRead

# TODO update the JSON string below
json = "{}"
# create an instance of DecisionContextRead from a JSON string
decision_context_read_instance = DecisionContextRead.from_json(json)
# print the JSON string representation of the object
print(DecisionContextRead.to_json())

# convert the object into a dict
decision_context_read_dict = decision_context_read_instance.to_dict()
# create an instance of DecisionContextRead from a dict
decision_context_read_from_dict = DecisionContextRead.from_dict(decision_context_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


