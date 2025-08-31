# BotSellerRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**matchers** | [**List[SellerMatcherRead]**](SellerMatcherRead.md) |  | 
**type** | **str** |  | 
**user_id** | **int** |  | 
**info** | **str** |  | 
**price** | **float** |  | 
**llm_model** | **str** |  | 
**llm_prompt** | **str** |  | 

## Example

```python
from infonomy_client.models.bot_seller_read import BotSellerRead

# TODO update the JSON string below
json = "{}"
# create an instance of BotSellerRead from a JSON string
bot_seller_read_instance = BotSellerRead.from_json(json)
# print the JSON string representation of the object
print(BotSellerRead.to_json())

# convert the object into a dict
bot_seller_read_dict = bot_seller_read_instance.to_dict()
# create an instance of BotSellerRead from a dict
bot_seller_read_from_dict = BotSellerRead.from_dict(bot_seller_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


