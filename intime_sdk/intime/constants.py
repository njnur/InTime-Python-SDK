# ==================== Send SMS ==================== #
SEND_SMS_XML = """<?xml version="1.0" encoding="iso-8859-1"?>
<message>
       <flash>{is_flash_msg}</flash>
       <multisms>{is_multi_sms}</multisms>
       {send_date}
       <sendertitle>{sender_title}</sendertitle>
       <body>{message_body}</body>
       {status_url}
       <checknix>{check_block_list}</checknix>
       <anonymize>{encrypt_msg}</anonymize>
       <recipients>
            {recipients}
       </recipients>
       <groups>
            <group groupid="{group_id}" />
      </groups>
</message>"""
SEND_SMS_URI = "message/create.ashx"
SEND_DATE_XML = """<senddate>{send_date}</senddate>"""
STATUS_URL_XML = """<statusurl>{status_url}</statusurl>"""
RECIPIENT_XML = """<recipient {trans_id}>{recipient}</recipient>"""
