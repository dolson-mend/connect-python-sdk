# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class ChargeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, idempotency_key=None, amount_money=None, card_nonce=None, customer_card_id=None, delay_capture=None, reference_id=None, note=None, customer_id=None, billing_address=None, shipping_address=None, buyer_email_address=None, order_id=None, additional_recipients=None):
        """
        ChargeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'idempotency_key': 'str',
            'amount_money': 'Money',
            'card_nonce': 'str',
            'customer_card_id': 'str',
            'delay_capture': 'bool',
            'reference_id': 'str',
            'note': 'str',
            'customer_id': 'str',
            'billing_address': 'Address',
            'shipping_address': 'Address',
            'buyer_email_address': 'str',
            'order_id': 'str',
            'additional_recipients': 'list[AdditionalRecipient]'
        }

        self.attribute_map = {
            'idempotency_key': 'idempotency_key',
            'amount_money': 'amount_money',
            'card_nonce': 'card_nonce',
            'customer_card_id': 'customer_card_id',
            'delay_capture': 'delay_capture',
            'reference_id': 'reference_id',
            'note': 'note',
            'customer_id': 'customer_id',
            'billing_address': 'billing_address',
            'shipping_address': 'shipping_address',
            'buyer_email_address': 'buyer_email_address',
            'order_id': 'order_id',
            'additional_recipients': 'additional_recipients'
        }

        self._idempotency_key = idempotency_key
        self._amount_money = amount_money
        self._card_nonce = card_nonce
        self._customer_card_id = customer_card_id
        self._delay_capture = delay_capture
        self._reference_id = reference_id
        self._note = note
        self._customer_id = customer_id
        self._billing_address = billing_address
        self._shipping_address = shipping_address
        self._buyer_email_address = buyer_email_address
        self._order_id = order_id
        self._additional_recipients = additional_recipients

    @property
    def idempotency_key(self):
        """
        Gets the idempotency_key of this ChargeRequest.
        A value you specify that uniquely identifies this transaction among transactions you've created.  If you're unsure whether a particular transaction succeeded, you can reattempt it with the same idempotency key without worrying about double-charging the buyer.  See [Idempotency](/basics/api101/idempotency) for more information.

        :return: The idempotency_key of this ChargeRequest.
        :rtype: str
        """
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, idempotency_key):
        """
        Sets the idempotency_key of this ChargeRequest.
        A value you specify that uniquely identifies this transaction among transactions you've created.  If you're unsure whether a particular transaction succeeded, you can reattempt it with the same idempotency key without worrying about double-charging the buyer.  See [Idempotency](/basics/api101/idempotency) for more information.

        :param idempotency_key: The idempotency_key of this ChargeRequest.
        :type: str
        """

        if idempotency_key is None:
            raise ValueError("Invalid value for `idempotency_key`, must not be `None`")
        if len(idempotency_key) > 192:
            raise ValueError("Invalid value for `idempotency_key`, length must be less than `192`")
        if len(idempotency_key) < 1:
            raise ValueError("Invalid value for `idempotency_key`, length must be greater than or equal to `1`")

        self._idempotency_key = idempotency_key

    @property
    def amount_money(self):
        """
        Gets the amount_money of this ChargeRequest.
        The amount of money to charge.  Note that you specify the amount in the __smallest denomination of the applicable currency__. For example, US dollar amounts are specified in cents. See [Working with monetary amounts](#workingwithmonetaryamounts) for details.  The value of `currency` must match the currency associated with the business that is charging the card.

        :return: The amount_money of this ChargeRequest.
        :rtype: Money
        """
        return self._amount_money

    @amount_money.setter
    def amount_money(self, amount_money):
        """
        Sets the amount_money of this ChargeRequest.
        The amount of money to charge.  Note that you specify the amount in the __smallest denomination of the applicable currency__. For example, US dollar amounts are specified in cents. See [Working with monetary amounts](#workingwithmonetaryamounts) for details.  The value of `currency` must match the currency associated with the business that is charging the card.

        :param amount_money: The amount_money of this ChargeRequest.
        :type: Money
        """

        self._amount_money = amount_money

    @property
    def card_nonce(self):
        """
        Gets the card_nonce of this ChargeRequest.
        A nonce generated from the `SqPaymentForm` that represents the card to charge.  The application that provides a nonce to this endpoint must be the _same application_ that generated the nonce with the `SqPaymentForm`. Otherwise, the nonce is invalid.  Do not provide a value for this field if you provide a value for `customer_card_id`.

        :return: The card_nonce of this ChargeRequest.
        :rtype: str
        """
        return self._card_nonce

    @card_nonce.setter
    def card_nonce(self, card_nonce):
        """
        Sets the card_nonce of this ChargeRequest.
        A nonce generated from the `SqPaymentForm` that represents the card to charge.  The application that provides a nonce to this endpoint must be the _same application_ that generated the nonce with the `SqPaymentForm`. Otherwise, the nonce is invalid.  Do not provide a value for this field if you provide a value for `customer_card_id`.

        :param card_nonce: The card_nonce of this ChargeRequest.
        :type: str
        """

        if card_nonce is None:
            raise ValueError("Invalid value for `card_nonce`, must not be `None`")
        if len(card_nonce) > 192:
            raise ValueError("Invalid value for `card_nonce`, length must be less than `192`")

        self._card_nonce = card_nonce

    @property
    def customer_card_id(self):
        """
        Gets the customer_card_id of this ChargeRequest.
        The ID of the customer card on file to charge. Do not provide a value for this field if you provide a value for `card_nonce`.  If you provide this value, you _must_ also provide a value for `customer_id`.

        :return: The customer_card_id of this ChargeRequest.
        :rtype: str
        """
        return self._customer_card_id

    @customer_card_id.setter
    def customer_card_id(self, customer_card_id):
        """
        Sets the customer_card_id of this ChargeRequest.
        The ID of the customer card on file to charge. Do not provide a value for this field if you provide a value for `card_nonce`.  If you provide this value, you _must_ also provide a value for `customer_id`.

        :param customer_card_id: The customer_card_id of this ChargeRequest.
        :type: str
        """

        if customer_card_id is None:
            raise ValueError("Invalid value for `customer_card_id`, must not be `None`")
        if len(customer_card_id) > 192:
            raise ValueError("Invalid value for `customer_card_id`, length must be less than `192`")

        self._customer_card_id = customer_card_id

    @property
    def delay_capture(self):
        """
        Gets the delay_capture of this ChargeRequest.
        If `true`, the request will only perform an Auth on the provided card. You can then later perform either a Capture (with the [CaptureTransaction](#endpoint-capturetransaction) endpoint) or a Void (with the [VoidTransaction](#endpoint-voidtransaction) endpoint).  Default value: `false`

        :return: The delay_capture of this ChargeRequest.
        :rtype: bool
        """
        return self._delay_capture

    @delay_capture.setter
    def delay_capture(self, delay_capture):
        """
        Sets the delay_capture of this ChargeRequest.
        If `true`, the request will only perform an Auth on the provided card. You can then later perform either a Capture (with the [CaptureTransaction](#endpoint-capturetransaction) endpoint) or a Void (with the [VoidTransaction](#endpoint-voidtransaction) endpoint).  Default value: `false`

        :param delay_capture: The delay_capture of this ChargeRequest.
        :type: bool
        """

        self._delay_capture = delay_capture

    @property
    def reference_id(self):
        """
        Gets the reference_id of this ChargeRequest.
        An optional ID you can associate with the transaction for your own purposes (such as to associate the transaction with an entity ID in your own database).  This value cannot exceed 40 characters.

        :return: The reference_id of this ChargeRequest.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this ChargeRequest.
        An optional ID you can associate with the transaction for your own purposes (such as to associate the transaction with an entity ID in your own database).  This value cannot exceed 40 characters.

        :param reference_id: The reference_id of this ChargeRequest.
        :type: str
        """

        if reference_id is None:
            raise ValueError("Invalid value for `reference_id`, must not be `None`")
        if len(reference_id) > 40:
            raise ValueError("Invalid value for `reference_id`, length must be less than `40`")

        self._reference_id = reference_id

    @property
    def note(self):
        """
        Gets the note of this ChargeRequest.
        An optional note to associate with the transaction.  This value cannot exceed 60 characters.

        :return: The note of this ChargeRequest.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this ChargeRequest.
        An optional note to associate with the transaction.  This value cannot exceed 60 characters.

        :param note: The note of this ChargeRequest.
        :type: str
        """

        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")
        if len(note) > 60:
            raise ValueError("Invalid value for `note`, length must be less than `60`")

        self._note = note

    @property
    def customer_id(self):
        """
        Gets the customer_id of this ChargeRequest.
        The ID of the customer to associate this transaction with. This field is required if you provide a value for `customer_card_id`, and optional otherwise.

        :return: The customer_id of this ChargeRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this ChargeRequest.
        The ID of the customer to associate this transaction with. This field is required if you provide a value for `customer_card_id`, and optional otherwise.

        :param customer_id: The customer_id of this ChargeRequest.
        :type: str
        """

        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")
        if len(customer_id) > 50:
            raise ValueError("Invalid value for `customer_id`, length must be less than `50`")

        self._customer_id = customer_id

    @property
    def billing_address(self):
        """
        Gets the billing_address of this ChargeRequest.
        The buyer's billing address.

        :return: The billing_address of this ChargeRequest.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this ChargeRequest.
        The buyer's billing address.

        :param billing_address: The billing_address of this ChargeRequest.
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this ChargeRequest.
        The buyer's shipping address, if available.

        :return: The shipping_address of this ChargeRequest.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this ChargeRequest.
        The buyer's shipping address, if available.

        :param shipping_address: The shipping_address of this ChargeRequest.
        :type: Address
        """

        self._shipping_address = shipping_address

    @property
    def buyer_email_address(self):
        """
        Gets the buyer_email_address of this ChargeRequest.
        The buyer's email address, if available.

        :return: The buyer_email_address of this ChargeRequest.
        :rtype: str
        """
        return self._buyer_email_address

    @buyer_email_address.setter
    def buyer_email_address(self, buyer_email_address):
        """
        Sets the buyer_email_address of this ChargeRequest.
        The buyer's email address, if available.

        :param buyer_email_address: The buyer_email_address of this ChargeRequest.
        :type: str
        """

        self._buyer_email_address = buyer_email_address

    @property
    def order_id(self):
        """
        Gets the order_id of this ChargeRequest.
        The ID of the order to associate with this transaction.  If you provide this value, the `amount_money` value of your request must __exactly match__ the value of the order's `total_money` field.

        :return: The order_id of this ChargeRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this ChargeRequest.
        The ID of the order to associate with this transaction.  If you provide this value, the `amount_money` value of your request must __exactly match__ the value of the order's `total_money` field.

        :param order_id: The order_id of this ChargeRequest.
        :type: str
        """

        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")
        if len(order_id) > 192:
            raise ValueError("Invalid value for `order_id`, length must be less than `192`")

        self._order_id = order_id

    @property
    def additional_recipients(self):
        """
        Gets the additional_recipients of this ChargeRequest.
        The basic primitive of multi-party transaction. The value is optional. The transaction facilitated by you can be split from here.  If you provide this value, the `amount_money` value in your additional_recipients must not be more than 90% of the `amount_money` value in the charge request. The `location_id` must be the valid location of the app owner merchant.  This field requires the `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.  This field is currently not supported in sandbox.

        :return: The additional_recipients of this ChargeRequest.
        :rtype: list[AdditionalRecipient]
        """
        return self._additional_recipients

    @additional_recipients.setter
    def additional_recipients(self, additional_recipients):
        """
        Sets the additional_recipients of this ChargeRequest.
        The basic primitive of multi-party transaction. The value is optional. The transaction facilitated by you can be split from here.  If you provide this value, the `amount_money` value in your additional_recipients must not be more than 90% of the `amount_money` value in the charge request. The `location_id` must be the valid location of the app owner merchant.  This field requires the `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.  This field is currently not supported in sandbox.

        :param additional_recipients: The additional_recipients of this ChargeRequest.
        :type: list[AdditionalRecipient]
        """

        self._additional_recipients = additional_recipients

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
