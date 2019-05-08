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


class SearchOrdersRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location_ids=None, cursor=None, query=None, limit=None, return_entries=None):
        """
        SearchOrdersRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'location_ids': 'list[str]',
            'cursor': 'str',
            'query': 'SearchOrdersQuery',
            'limit': 'int',
            'return_entries': 'bool'
        }

        self.attribute_map = {
            'location_ids': 'location_ids',
            'cursor': 'cursor',
            'query': 'query',
            'limit': 'limit',
            'return_entries': 'return_entries'
        }

        self._location_ids = location_ids
        self._cursor = cursor
        self._query = query
        self._limit = limit
        self._return_entries = return_entries

    @property
    def location_ids(self):
        """
        Gets the location_ids of this SearchOrdersRequest.
        The location IDs for the orders to query. The caller must have access to all provided locations.  Min: 1 `location_ids`. Max: 10 `location_ids`.

        :return: The location_ids of this SearchOrdersRequest.
        :rtype: list[str]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """
        Sets the location_ids of this SearchOrdersRequest.
        The location IDs for the orders to query. The caller must have access to all provided locations.  Min: 1 `location_ids`. Max: 10 `location_ids`.

        :param location_ids: The location_ids of this SearchOrdersRequest.
        :type: list[str]
        """

        self._location_ids = location_ids

    @property
    def cursor(self):
        """
        Gets the cursor of this SearchOrdersRequest.
        A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query. See [Pagination](/basics/api101/pagination) for more information.

        :return: The cursor of this SearchOrdersRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this SearchOrdersRequest.
        A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query. See [Pagination](/basics/api101/pagination) for more information.

        :param cursor: The cursor of this SearchOrdersRequest.
        :type: str
        """

        self._cursor = cursor

    @property
    def query(self):
        """
        Gets the query of this SearchOrdersRequest.
        Query conditions used to filter or sort the results. Note that when fetching additional pages using a `cursor`, the `query` must be equal to the `query` used to fetch the first page of results.

        :return: The query of this SearchOrdersRequest.
        :rtype: SearchOrdersQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchOrdersRequest.
        Query conditions used to filter or sort the results. Note that when fetching additional pages using a `cursor`, the `query` must be equal to the `query` used to fetch the first page of results.

        :param query: The query of this SearchOrdersRequest.
        :type: SearchOrdersQuery
        """

        self._query = query

    @property
    def limit(self):
        """
        Gets the limit of this SearchOrdersRequest.
        Number of results to be returned in a single page. SearchOrders may use a smaller limit than specified depending on server load. If the response includes a `cursor` field, you can use it to retrieve the next set of results. Default: `500`

        :return: The limit of this SearchOrdersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this SearchOrdersRequest.
        Number of results to be returned in a single page. SearchOrders may use a smaller limit than specified depending on server load. If the response includes a `cursor` field, you can use it to retrieve the next set of results. Default: `500`

        :param limit: The limit of this SearchOrdersRequest.
        :type: int
        """

        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")
        if limit < 1:
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `1`")

        self._limit = limit

    @property
    def return_entries(self):
        """
        Gets the return_entries of this SearchOrdersRequest.
         If set to `true`, SearchOrders will return [`OrderEntry`](#type-orderentry) objects instead of `Order` objects. `OrderEntry` objects are lightweight descriptions of orders that include `order_id`s.  Default: `false`.

        :return: The return_entries of this SearchOrdersRequest.
        :rtype: bool
        """
        return self._return_entries

    @return_entries.setter
    def return_entries(self, return_entries):
        """
        Sets the return_entries of this SearchOrdersRequest.
         If set to `true`, SearchOrders will return [`OrderEntry`](#type-orderentry) objects instead of `Order` objects. `OrderEntry` objects are lightweight descriptions of orders that include `order_id`s.  Default: `false`.

        :param return_entries: The return_entries of this SearchOrdersRequest.
        :type: bool
        """

        self._return_entries = return_entries

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