# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccountAgencyFeeConfig(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountAgencyFeeConfig = True
        super(AdAccountAgencyFeeConfig, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        can_add_agency_fee_to_invoice = 'can_add_agency_fee_to_invoice'
        default_agency_fee_pct = 'default_agency_fee_pct'
        id = 'id'
        is_agency_fee_disabled = 'is_agency_fee_disabled'
        status = 'status'

    class Status:
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        draft = 'DRAFT'
        unknown = 'UNKNOWN'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountAgencyFeeConfig,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'can_add_agency_fee_to_invoice': 'bool',
        'default_agency_fee_pct': 'float',
        'id': 'string',
        'is_agency_fee_disabled': 'bool',
        'status': 'Status',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Status'] = AdAccountAgencyFeeConfig.Status.__dict__.values()
        return field_enum_info


