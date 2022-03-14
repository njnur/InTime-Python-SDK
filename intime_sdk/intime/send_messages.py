from typing import Optional, List
from datetime import datetime

from intime_sdk.core.base import APIConnector
from intime_sdk.intime import constants


class Messages(APIConnector):
    """
    Class for manipulating SMS functionalities including creating & sending SMS, removing a scheduled sms etc.
    """
    def send_sms(self, sender_title: str, message_body: str, recipients: List, groups: str, group_id: str,
                 is_flash_msg: bool = False, is_multi_sms: bool = False, send_date: Optional[datetime] = None,
                 status_url: Optional[str] = None, check_block_list: Optional[bool] = False,
                 encrypt_msg: Optional[bool] = False, trans_id: Optional[str] = None,
                 ):
        """
        Method for crating and sending sms.

        :param sender_title: (String) Sender of the message. Use maximum 11 alphanumeric characters or 15 numeric chars.
         Allowed alphanumeric chars is aA-zZ, 0-9, space, .(dot), -(binding char), or +(plus).
         Only English characters are allowed.
        :param message_body: (String) Message text.
         SMS message is allowed to contain a maximum of 160 characters. Multi-SMS is allowed to contain a maximum of
         804 characters (6 SMS with 134 characters each).
        :param recipients: (List) Phone number of the recipients to receive the message. At least one recipient or group
         must be addressed.
        :param groups: (String) Group recipients to receive the message. At least one recipient or group must be
         addressed.
        :param group_id: (String) The groups Identification number.
        :param is_flash_msg: (Boolean | Default: False) If this parameter is set to True, method will send a Flash
         message (maximum 160 characters) and otherwise it will send a Normal message.
        :param is_multi_sms: (Boolean | Default: False) If this parameter is set to True, method will send send up to
         six SMS or 804 characters and otherwise it will send a Normal message.
        :param send_date: (Optional; Boolean | Default: None) Date/time for scheduled sending, If the message is to be
         sent directly, ignore this parameter.
        :param status_url: (Optional; String | Default: None) URL for the server to send message status callbacks.
        :param check_block_list: (Boolean | Default: False) If this parameter is set to True, method will check
         the user's block list for group mailings.
        :param encrypt_msg: (Boolean | Default: False) Flag that indicates whether the message should be encrypted after
         it's sent. Sent messages cannot be read in Messenger.
        :param trans_id: (Optional; String | Default: None) Value to send to the status url with the callback, this
         could be a uniq id generated for each recipient and used in callback to link the status callback.
         This is mandatory if status_url is used!


        :return: API response in dictionary format
        """
        xml_data = constants.SEND_SMS_XML.format()
        return self._post(api_url=constants.SEND_SMS_URI,
                          data=xml_data)
