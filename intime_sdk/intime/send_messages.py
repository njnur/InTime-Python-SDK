from typing import Optional, List

from intime_sdk.core.base import APIConnector
from intime_sdk.intime import constants


class Messages(APIConnector):
    """
    Class for manipulating SMS functionalities including creating & sending SMS, removing a scheduled sms etc.
    """
    def send_sms(self, sender_title: str, message_body: str, recipients: List, group_id: str,
                 is_flash_msg: bool = False, is_multi_sms: bool = False, send_date: Optional[str] = None,
                 status_url: Optional[str] = None, check_block_list: Optional[bool] = False,
                 encrypt_msg: Optional[bool] = False, trans_id: Optional[List] = None,
                 ):
        """
        Method for crating and sending sms.

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


        :return: API response in dictionary format with a status param
         Format::: {
                "status": True/False,
                "data": "Sample Response/3545354535"
            }
        """
        recipients_list = """"""
        if status_url:
            if trans_id:
                if len(trans_id) == len(recipients):
                    for inc in range(0, len(recipients)):
                        recipients_list += constants.RECIPIENT_XML.format(
                            recipient=recipients[inc],
                            trans_id=trans_id[inc]
                        )
                else:
                    raise ValueError("Each recipients should have a trans_id for Status CallBack")
            else:
                raise ValueError("trans_id is needed for Status CallBack")
        else:
            for recipient in recipients:
                recipients_list += constants.RECIPIENT_XML.format(
                    recipient=recipient,
                    trans_id=''
                )

        xml_data = constants.SEND_SMS_XML.format(
            is_flash_msg="1" if is_flash_msg else "0",
            is_multi_sms="1" if is_multi_sms else "0",
            send_date=constants.SEND_DATE_XML.format(send_date=send_date) if send_date else '',
            sender_title=sender_title,
            message_body=message_body,
            status_url=constants.STATUS_URL_XML.format(status_url=status_url) if status_url else '',
            check_block_list="1" if check_block_list else "0",
            encrypt_msg="1" if encrypt_msg else "0",
            recipients=recipients_list,
            group_id=group_id
        )

        return self._post(api_url=constants.SEND_SMS_URI,
                          data=xml_data)
