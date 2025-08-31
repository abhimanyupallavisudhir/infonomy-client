# SellerMatcherCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** |  | [optional] 
**context_pages** | **List[str]** |  | [optional] 
**min_max_budget** | **float** |  | [optional] [default to 0.0]
**min_inspection_rate** | **float** |  | [optional] [default to 0.0]
**min_purchase_rate** | **float** |  | [optional] [default to 0.0]
**min_priority** | **int** |  | [optional] [default to 0]
**buyer_type** | **str** |  | [optional] 
**buyer_llm_model** | **List[str]** |  | [optional] 
**buyer_system_prompt** | **List[str]** |  | [optional] 
**age_limit** | **int** |  | [optional] 

## Example

```python
from infonomy_client.models.seller_matcher_create import SellerMatcherCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMatcherCreate from a JSON string
seller_matcher_create_instance = SellerMatcherCreate.from_json(json)
# print the JSON string representation of the object
print(SellerMatcherCreate.to_json())

# convert the object into a dict
seller_matcher_create_dict = seller_matcher_create_instance.to_dict()
# create an instance of SellerMatcherCreate from a dict
seller_matcher_create_from_dict = SellerMatcherCreate.from_dict(seller_matcher_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


