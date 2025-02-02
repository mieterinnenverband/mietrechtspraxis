# -*- coding: utf-8 -*-
# Copyright (c) 2021, libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ArbitrationAuthority(Document):
    pass


def _get_sb(**kwargs):
    '''
    call on [IP]/api/method/mietrechtspraxis.api.get_sb
    Mandatory Parameter:
        - token
        - plz
    '''
    
    # check that token is present
    try:
        token = kwargs['token']
    except:
        # 400 Bad Request (Missing Token)
        return raise_4xx(400, 'Bad Request', 'Token Required')
        
    # check that token is correct
    if not token == frappe.db.get_single_value('mietrechtspraxis API', 'token'):
        # 401 Unauthorized (Invalid Token)
        return raise_4xx(401, 'Unauthorized', 'Invalid Token')
    
    # check that plz_city is present
    try:
        plz_city = kwargs['plz_city']
    except:
        # 400 Bad Request (Missing PLZ/City)
        return raise_4xx(400, 'Bad Request', 'PLZ/City Required')
        
    answer = []
    
    # lookup for plz
    city_results = frappe.db.sql("""
                                    SELECT
                                        `city`,
                                        `municipality`,
                                        `district`,
                                        `canton`
                                    FROM `tabPincode`
                                    WHERE `pincode` = '{plz_city}'
                                    ORDER BY `city` ASC
                                    """.format(plz_city=plz_city), as_dict=True)
    if len(city_results) < 1:
        # lookup for city
        city_results = frappe.db.sql("""
                                        SELECT
                                            `city`,
                                            `municipality`,
                                            `district`,
                                            `canton`
                                        FROM `tabPincode`
                                        WHERE `city` LIKE '%{plz_city}%'
                                        ORDER BY `city` ASC
                                        """.format(plz_city=plz_city), as_dict=True)
                            
    if len(city_results) > 0:
        for city in city_results:
            data = {}
            data['plz'] = city.plz
            data['ort'] = city.city
            data['gemeinde'] = city.municipality
            data['bezirk'] = city.district
            data['kanton'] = city.canton
            data['allgemein'] = get_informations(city.canton)
            data['schlichtungsbehoerde'] = frappe.db.sql("""
                                                                SELECT
                                                                    `schlichtungsbehoerde`.`titel` AS `Titel`,
                                                                    `schlichtungsbehoerde`.`telefon` AS `Telefon`,
                                                                    `schlichtungsbehoerde`.`kuendigungstermine` AS `Kündigungstermine`,
                                                                    `schlichtungsbehoerde`.`pauschalen` AS `Pauschalen`,
                                                                    `schlichtungsbehoerde`.`rechtsberatung` AS `Rechtsberatung`,
                                                                    `schlichtungsbehoerde`.`elektronische_eingaben` AS `elektronische Eingaben`,
                                                                    `schlichtungsbehoerde`.`homepage` AS `Homepage`
                                                                FROM `tabArbitration Authority` AS `schlichtungsbehoerde`
                                                                LEFT JOIN `tabMunicipality Table` AS `geminendentbl` ON `schlichtungsbehoerde`.`name`=`geminendentbl`.`parent`
                                                                WHERE `geminendentbl`.`municipality` = '{municipality}'
                                                                """.format(municipality=city.municipality), as_dict=True)
            answer.append(data)
            
        if len(answer) > 0:
            return raise_200(answer)
        else:
            # 404 Not Found
            return raise_4xx(404, 'Not Found', 'No results')
    else:
        # 404 Not Found
        return raise_4xx(404, 'Not Found', 'No results')
        
def get_informations(kanton):
    search = frappe.db.sql("""
                            SELECT
                                `informationen`,
                                `homepage`,
                                `gesetzessammlung`,
                                `formulare`
                            FROM `tabKantonsinformationen`
                            WHERE `kanton` = '{kanton}'
                            """.format(kanton=kanton), as_dict=True)
    if len(search) > 0:
        result = search[0]
    else:
        result = {}
    return result
        
def raise_4xx(code, title, message):
    # 4xx Bad Request / Unauthorized / Not Found
    return ['{code} {title}'.format(code=code, title=title), {
        "error": {
            "code": code,
            "message": "{message}".format(message=message)
        }
    }]
    
def raise_200(answer):
    return ['200 OK', answer]
