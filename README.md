[![PyPI version](https://badge.fury.io/py/pickrr.svg)](https://badge.fury.io/py/pickrr)
[![Build Status](https://api.travis-ci.org/harishbisht/pickrr.svg?branch=master)](https://api.travis-ci.org/harishbisht/pickrr.svg?branch=master)


# Pickrr Python API
### Installation


```sh
$ pip install pickrr
```

### How to use

First setup the auth-token

```sh
$ from pickrr.session import Session
$ Session.setup("auth-token")
```

EXAMPLE:

```sh
$ from pickrr.session import Session
$ Session.setup("94539823sd342d5453224")
```


For placing order:

```sh
$ from pickrr.placeorder import PlaceOrder
$ PlaceOrder.placeorder(item_name,from_name,from_phone_number,from_pincode,from_address,to_name,to_phone_number,to_pincode,to_address,cod_amount,client_order_id,client_other_id)
```
for prepaid pass cod_amount=0.0, and order_id and client_other_id are optional

EXAMPLE:
```sh
$ from pickrr.placeorder import PlaceOrder
$ PlaceOrder.placeorder(item_name = "ITEM NAME",from_name = "NAME",from_phone_number = "9999999999",from_pincode = "110023",from_address= "FULL ADDRESS",to_name = "TO NAME",to_phone_number ="9898989898",to_pincode = "110045",to_address = "TO ADDRESS",cod_amount = "123",client_order_id = "345345",client_other_id = "32")
```
RETURN:

```
{"pickrr_phone_number": "+91-9818197991", "err": null, "order_id": "109124", "to_notify": false, "order_from_city": "NEW DELHI", "item_name": "test", "user_email": "harish@pickrr.com", "tracking_id": "90410810064184", "pickrr_name": "Sahil Goyal", "order_pk": 108100, "order_service_used": "Standard", "order_to_city": "NEW DELHI"}
```

For Cancel the order:

```sh
$ from pickrr.cancelorder import CancelOrder
$ CancelOrder.cancelorder(order_id)
```
EXAMPLE:

```sh
$ from pickrr.cancelorder import CancelOrder
$ CancelOrder.cancelorder(order_id="109124")
```

RETURN:

```sh
$ {"err": null}
```

For order tracking:

```sh
$ from pickrr.trackorder import TrackOrder
$ TrackOrder.trackorder(tracking_id)
```

EXAMPLE:

```sh
$ from pickrr.trackorder import TrackOrder
$ TrackOrder.trackorder(tracking_id="45323232342")
```


