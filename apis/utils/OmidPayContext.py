class OmidPayContext:
    def prepare_context(response_data):
        return {
            'expiration_date': response_data.get('ExpirationDate'),
            'token': response_data.get('Token'),
            'chanel_id': response_data.get('ChannelId'),
            'user_id': response_data.get('UserId'),
        }

    def validate_payment_data(data):
        required_fields = ['ExpirationDate', 'Token', 'ChanelId', 'UserId']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return False, f"{', '.join(missing_fields)} {'is/are'} required"
        return True, None
