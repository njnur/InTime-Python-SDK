# InTime SDK

The objective of InTime SDK is to create, configure, and manage InTime services, such as Creating and Sending SMS's. 
The SDK provides an object-oriented API as well as low-level access to InTime services.

## Installation 

```
pip install intime-sdk
```

InTime SDK supports Python 3.6+.

## Documentation

Instantiate the Messages class to send SMS

```python
from intime_sdk import Messages


# initialize the Message class with required params
Messages(username='your-username', secret_key='your-secret-key').send_sms(
            sender_title="test-sender",
            message_body="Hello from Intime!!",
            recipients=["+123456789"],
            group_id="1",

)
```
### Parameter Definition  

**send_sms()**

```
:param sender_title: (String) Sender of the message. Use maximum 11 alphanumeric characters or 15 numeric chars.
 Allowed alphanumeric chars is aA-zZ, 0-9, space, .(dot), -(binding char), or +(plus).
 Only English characters are allowed.

:param message_body: (String) Message text.
 SMS is allowed to contain a maximum of 160 characters. Multi-SMS is allowed to contain a maximum of
 804 characters (6 SMS with 134 characters each).

:param recipients: (List) Phone number of the recipients to receive the message. At least one recipient or group
 must be addressed.

:param group_id: (String) The groups Identification number.

:param is_flash_msg: (Boolean | Default: False) If this parameter is set to True, method will send a Flash
 message (maximum 160 characters) and otherwise it will send a Normal message.

:param is_multi_sms: (Boolean | Default: False) If this parameter is set to True, method will send send up to
 six SMS or 804 characters and otherwise it will send a Normal message.

:param send_date: (Optional; String | Default: None) Date/time for scheduled sending, If the message is to be
 sent directly/right now, ignore this parameter. (Format: 2012-01-13T14:41:00)

:param status_url: (Optional; String | Default: None) URL for the server to send message status callbacks.

:param check_block_list: (Boolean | Default: False) If this parameter is set to True, method will check
 the user's block list for group mailings.

:param encrypt_msg: (Boolean | Default: False) Flag that indicates whether the message should be encrypted after
 it's sent. Sent messages cannot be read in Messenger.

:param trans_id: (Optional; String | Default: None) Value to send to the status url with the callback, this
 could be a uniq id generated for each recipient and used in callback to link the status callback.
 This is mandatory if status_url is used!    
```
