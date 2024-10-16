import requests
from django.conf import settings
from django.urls import reverse
import logging
logger = logging.getLogger(__name__)


class OmidPayAPI:

    @staticmethod
    def get_omidpay_token(amount):

        omid_pay_data = settings.OMIDPAYDATA
        url = omid_pay_data['GENERATE_TOKEN_URL']
        payload = {
            "WSContext": {
                "UserId": omid_pay_data['USERNAME'],
                "Password": omid_pay_data['PASSWORD']
            },
            "TransType": "EN_GOODS",
            "ReserveNum": "123456",
            "MerchantId": omid_pay_data['MERCHANT_ID'],
            "Amount": amount,
            "RedirectUrl": f"{settings.BASE_URL}{reverse('payment_success_callback')}"
        }
        headers = {
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            if data.get('Result') == 'erSucceed':
                return {'status': 'success', 'data': data}
            else:
                return {'status': 'error', 'message': "Could not retrieve token"}
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred while getting the token: {e.response}")
            return {'status': 'error', 'message': 'An error occurred while getting the token'}

    @staticmethod
    def verify_omidpay_transaction(ref_num, token):
        omid_pay_data = settings.OMIDPAYDATA
        payload = {
            "WSContext": {
                "UserId": omid_pay_data['USERNAME'],
                "Password": omid_pay_data['PASSWORD']
            },
            "Token": token,
            "RefNum": ref_num,
        }
        verify_url =omid_pay_data['VERIFY_URL']

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(verify_url, json=payload, headers=headers)
            response.raise_for_status()
            verify_response = response.json()
            if verify_response.get('Result') == 'erSucceed':
                return {'status': 'success', 'verify_response': verify_response}
            else:
                return {'status': 'error', 'message': 'Verification failed'}
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred during verification: {e}")
            return {'status': 'error', 'message': 'An error occurred during verification'}
