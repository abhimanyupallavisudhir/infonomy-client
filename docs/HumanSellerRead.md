# HumanSellerRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**matchers** | [**List[SellerMatcherRead]**](SellerMatcherRead.md) |  | 
**info_offers** | [**List[InfoOfferReadPublic]**](InfoOfferReadPublic.md) |  | 

## Example

```python
from infonomy_client.models.human_seller_read import HumanSellerRead

# TODO update the JSON string below
json = "{}"
# create an instance of HumanSellerRead from a JSON string
human_seller_read_instance = HumanSellerRead.from_json(json)
# print the JSON string representation of the object
print(HumanSellerRead.to_json())

# convert the object into a dict
human_seller_read_dict = human_seller_read_instance.to_dict()
# create an instance of HumanSellerRead from a dict
human_seller_read_from_dict = HumanSellerRead.from_dict(human_seller_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


