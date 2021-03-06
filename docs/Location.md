# Location
> squareconnect.models.location

### Description

Represents one of a business's locations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The location&#39;s unique ID. | [optional] 
**name** | **str** | The location&#39;s name. Location names are set by the account owner and displayed in the dashboard as the location&#39;s nickname | [optional] 
**address** | [**Address**](Address.md) | The location&#39;s physical address. | [optional] 
**timezone** | **str** | The [IANA Timezone Database](https://www.iana.org/time-zones) identifier for the location&#39;s timezone. | [optional] 
**capabilities** | **list[str]** | Indicates which Square features are enabled for the location. See [LocationCapability](#type-locationcapability) for possible values | [optional] 
**status** | **str** | The location&#39;s status See [LocationStatus](#type-locationstatus) for possible values | [optional] 
**created_at** | **str** | The time when the location was created, in RFC 3339 format. | [optional] 
**merchant_id** | **str** | The identifier of the merchant that owns the location. | [optional] 
**country** | **str** | The location&#39;s country, in ISO 3166-1-alpha-2 format. See [Country](#type-country) for possible values | [optional] 
**language_code** | **str** | The language associated with the location in [BCP 47 format](https://tools.ietf.org/html/bcp47#appendix-A). | [optional] 
**currency** | **str** | The currency used for all transactions at this location, specified in __ISO 4217 format__. For example, the currency for a location processing transactions in the United States is &#39;USD&#39;. See [Currency](#type-currency) for possible values | [optional] 
**phone_number** | **str** | The location&#39;s phone_number. | [optional] 
**business_name** | **str** | The location&#39;s business_name which is shown to its customers. For example, this is the name printed on its customer&#39;s receipts. | [optional] 
**type** | **str** | The location&#39;s type, as set by the account owner in the Square dashboard. Typically used to indicate whether or not the location object represents a physical space like a building or mall space. See [LocationType](#type-locationtype) for possible values | [optional] 
**website_url** | **str** | The location&#39;s website, as set by the account owner in the Square dashboard.  Default: none; only exists if explicitly set. | [optional] 
**business_hours** | [**BusinessHours**](BusinessHours.md) |   The hours of operation for a business location.  Default: none; only exists if explicitly set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


