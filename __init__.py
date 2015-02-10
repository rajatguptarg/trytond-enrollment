# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.pool import Pool
from enrollment import MedicalFamilyDetails
from enrollment import Allergy, Disease
from enrollment import Occupation, Medication


def register():
    Pool.register(
        MedicalFamilyDetails,
        Allergy,
        Disease,
        Occupation,
        Medication,
        module='trytond-enrollment', type_='model'
    )
