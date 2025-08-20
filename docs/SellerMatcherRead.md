# SellerMatcherRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**seller_id** | **int** |  | 
**keywords** | **List[str]** |  | 
**context_pages** | **List[str]** |  | 
**min_max_budget** | **float** |  | 
**min_inspection_rate** | **float** |  | 
**min_purchase_rate** | **float** |  | 
**min_priority** | **int** |  | 
**buyer_type** | **str** |  | 
**buyer_llm_model** | **List[str]** |  | 
**buyer_system_prompt** | **List[str]** |  | 
**age_limit** | **int** |  | 

## Example

```python
from infonomy_client.models.seller_matcher_read import SellerMatcherRead

# TODO update the JSON string below
json = "{}"
# create an instance of SellerMatcherRead from a JSON string
seller_matcher_read_instance = SellerMatcherRead.from_json(json)
# print the JSON string representation of the object
print(SellerMatcherRead.to_json())

# convert the object into a dict
seller_matcher_read_dict = seller_matcher_read_instance.to_dict()
# create an instance of SellerMatcherRead from a dict
seller_matcher_read_from_dict = SellerMatcherRead.from_dict(seller_matcher_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


