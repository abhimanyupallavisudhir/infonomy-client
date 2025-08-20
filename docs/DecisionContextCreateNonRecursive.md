# DecisionContextCreateNonRecursive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**context_pages** | **List[str]** |  | [optional] 
**max_budget** | **float** |  | 
**seller_ids** | **List[int]** |  | [optional] 
**priority** | **int** |  | [optional] [default to 0]

## Example

```python
from infonomy_client.models.decision_context_create_non_recursive import DecisionContextCreateNonRecursive

# TODO update the JSON string below
json = "{}"
# create an instance of DecisionContextCreateNonRecursive from a JSON string
decision_context_create_non_recursive_instance = DecisionContextCreateNonRecursive.from_json(json)
# print the JSON string representation of the object
print(DecisionContextCreateNonRecursive.to_json())

# convert the object into a dict
decision_context_create_non_recursive_dict = decision_context_create_non_recursive_instance.to_dict()
# create an instance of DecisionContextCreateNonRecursive from a dict
decision_context_create_non_recursive_from_dict = DecisionContextCreateNonRecursive.from_dict(decision_context_create_non_recursive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


