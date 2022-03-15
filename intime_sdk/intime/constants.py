# ==================== Send SMS ==================== #
SEND_SMS_XML = """
<?xml version="1.0" encoding="iso-8859-1"?>
<message>
       <flash>{is_flash_msg}</flash>
       <multisms>{is_multi_sms}</multisms>
       {send_date}
       <sendertitle>{sender_title}</sendertitle>
       <body>{message_body}</body>
       <statusurl>{status_url}</statusurl>
       <checknix>{check_block_list}</checknix>
       <anonymize>{encrypt_msg}</anonymize>
       <recipients>
            {recipients}
       </recipients>
       <groups>
            <group groupid="1" />
      </groups>
</message>
"""
SEND_SMS_URI = "message/create.ashx"
