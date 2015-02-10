# -*- coding: utf-8 -*-
"""
    enrollment.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['MedicalFamilyDetails', 'Allergy', 'Disease', 'Occupation', 'Mediaction']
__metaclass__ = PoolMeta


STATES = {
    'readonly': ~Eval('active')
}

DEPENDS = ['active']


class Allergy(ModelSQL, ModelView):
    '''
    Adding allergies and their types
    '''
    __name__ = "party.allergy"

    allergy_name = fields.Char(
        "Type", states=STATES, depends=DEPENDS
    )


class Disease(ModelSQL, ModelView):
    '''
    Types of Diseases
    '''
    __name__ = "party.disease"

    disease_name = fields.Char(
        "Disease", states=STATES, depends=DEPENDS
    )


class Occupation(ModelSQL, ModelView):
    '''
    Types of Occupations
    '''
    __name__ = "party.occupation"

    occupation_name = fields.Char(
        "Occupation", states=STATES, depends=DEPENDS
    )


class Medication(ModelSQL, ModelView):
    '''
    Types of Mediactions
    '''

    __name__ = "party.medication"

    medication_name = fields.Char(
        "Mediaction", states=STATES, depends=DEPENDS
    )


class Party:
    "Party"
    __name__ = "party.party"

    familydetail = fields.One2Many(
        "party.familydetail", "party",
        "Family Details", states=STATES, depends=DEPENDS
    )
    medicaldetail = fields.One2Many(
        "party.medicaldetail", "party",
        "Medical Details", states=STATES, depends=DEPENDS
    )


class FamilyDetails(ModelSQL, ModelView):
    '''
    Adding Family Deatils to Party Module
    '''
    __name__ = "party.familydetail"

    party = fields.Many2One(
        "party.party", "Party",
        required=True, select=True
    )
    father_name = fields.Char(
        "Father's Name", states=STATES, depends=DEPENDS
    )
    father_occupation = fields.Many2One(
        "company.occupation", "Father's Occupation",
        states=STATES, depends=DEPENDS
    )
    mother_name = fields.Char(
        "Mother's Name", states=STATES, depends=DEPENDS
    )
    mother_occupation = fields.Many2One(
        "company.occupation", "Mother's Occupation",
        states=STATES, depends=DEPENDS
    )
    parent_contact = fields.Many2One(
        "party.contact_mechanism", "Parent's Contact",
        states=STATES, depends=DEPENDS
    )


class MedicalDetails(ModelSQL, ModelSQL):
    '''
    Adding Medical Issues to Party Module
    '''
    __name__ = "party.medicaldetail"

    party = fields.Many2One(
        "party.party", "Party",
        required=True, select=True
    )
    blood_group = fields.Selection(
        [
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
        ],
        "Blood Group", states=STATES, depends=DEPENDS
    )
    doctor_name = fields.Char(
        "Doctor's Name", states=STATES, depends=DEPENDS
    )
    doctor_contact = fields.Many2One(
        "party.contact_mechanism", "Doctor's Contact",
        states=STATES, depends=DEPENDS
    )
    allergies = fields.Many2One(
        "company.allergy", "Allergy",
        states=STATES, depends=DEPENDS
    )
    past_diseases = fields.Many2One(
        "company.disease", "Past Allergy",
        states=STATES, depends=DEPENDS
    )
    current_diseases = fields.Many2One(
        "company.disease", "Current Allergy",
        states=STATES, depends=DEPENDS
    )
    medications = fields.Many2One(
        "company.medication", "Mediactions",
        states=STATES, depends=DEPENDS
    )

    @staticmethod
    def default_blood_group():
        return 'A+'
