from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Subscription"),
            "icon": "fa fa-money",
            "items": [
                   {
                       "type": "doctype",
                       "name": "mp Abo",
                       "label": _("mp Abo"),
                       "description": _("mp Abo")
                   },
                   {
                       "type": "doctype",
                       "name": "mp Abo Settings",
                       "label": _("mp Abo Settings"),
                       "description": _("mp Abo Settings")
                   }
            ]
        },
        {
            "label": _("Tools"),
            "icon": "fa fa-money",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Customers Search Mask",
                       "label": _("Customers Search Mask"),
                       "description": _("Customers Search Mask")
                   },
                   {
                       "type": "page",
                       "name": "invoice_and_print",
                       "label": _("Invoice run and collective printing"),
                       "description": _("Invoice run and collective printing")
                   }
            ]
        },
        {
            "label": _("Master Data"),
            "icon": "fa fa-money",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Customer",
                       "label": _("Customer"),
                       "description": _("Customer")
                   },
                   {
                       "type": "doctype",
                       "name": "Contact",
                       "label": _("Contact"),
                       "description": _("Contact")
                   },
                   {
                       "type": "doctype",
                       "name": "Address",
                       "label": _("Address"),
                       "description": _("Address")
                   },
                   {
                       "type": "doctype",
                       "name": "Sales Invoice",
                       "label": _("Sales Invoice"),
                       "description": _("Sales Invoice")
                   },
                   {
                       "type": "doctype",
                       "name": "Payment Entry",
                       "label": _("Payment Entry"),
                       "description": _("Payment Entry")
                   }
            ]
        },
        {
            "label": _("Schlichtungsbehörden"),
            "icon": "fa fa-money",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Arbitration Authority",
                       "label": _("Schlichtungsbehörden"),
                       "description": _("Schlichtungsbehörden")
                   },
                   {
                       "type": "doctype",
                       "name": "Kantonsinformationen",
                       "label": _("Kantonsinformationen"),
                       "description": _("Kantonsinformationen")
                   }
            ]
        },
        {
            "label": _("API"),
            "icon": "fa fa-money",
            "items": [
                   {
                       "type": "doctype",
                       "name": "mietrechtspraxis API",
                       "label": _("API Einstellungen"),
                       "description": _("API Einstellungen")
                   }
            ]
        }
]
