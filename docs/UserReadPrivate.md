# UserReadPrivate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**email** | **str** |  | 
**is_active** | **bool** |  | [optional] [default to True]
**is_superuser** | **bool** |  | [optional] [default to False]
**is_verified** | **bool** |  | [optional] [default to False]
**username** | **str** |  | 
**created_at** | **datetime** |  | 
**last_login_date** | **datetime** |  | 
**balance** | **float** |  | 
**available_balance** | **float** |  | 
**daily_bonus_amount** | **float** |  | 
**buyer_profile** | [**HumanBuyerRead**](HumanBuyerRead.md) |  | 
**seller_profile** | [**HumanSellerRead**](HumanSellerRead.md) |  | 
**bot_sellers** | [**List[BotSellerRead]**](BotSellerRead.md) |  | 
**api_keys** | **Dict[str, object]** |  | 

## Example

```python
from infonomy_client.models.user_read_private import UserReadPrivate

# TODO update the JSON string below
json = "{}"
# create an instance of UserReadPrivate from a JSON string
user_read_private_instance = UserReadPrivate.from_json(json)
# print the JSON string representation of the object
print(UserReadPrivate.to_json())

# convert the object into a dict
user_read_private_dict = user_read_private_instance.to_dict()
# create an instance of UserReadPrivate from a dict
user_read_private_from_dict = UserReadPrivate.from_dict(user_read_private_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


