# SellerMatcherUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** |  | [optional] 
**context_pages** | **List[str]** |  | [optional] 
**min_max_budget** | **float** |  | [optional] 
**min_inspection_rate** | **float** |  | [optional] 
**min_purchase_rate** | **float** |  | [optional] 
**min_priority** | **int** |  | [optional] 
**buyer_type** | **str** |  | [optional] 
**buyer_llm_model** | **List[str]** |  | [optional] 
**buyer_system_prompt** | **List[str]** |  | [optional] 
**age_limit** | **int** |  | [optional] 

## Example

```python
from infonomy_client.models.seller_matcher_update import SellerMatcherUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMatcherUpdate from a JSON string
seller_matcher_update_instance = SellerMatcherUpdate.from_json(json)
# print the JSON string representation of the object
print(SellerMatcherUpdate.to_json())

# convert the object into a dict
seller_matcher_update_dict = seller_matcher_update_instance.to_dict()
# create an instance of SellerMatcherUpdate from a dict
seller_matcher_update_from_dict = SellerMatcherUpdate.from_dict(seller_matcher_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


