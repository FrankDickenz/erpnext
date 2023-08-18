from __future__ import unicode_literals
import json

import frappe
import requests

from frappe import auth, exceptions
from frappe import permissions

@frappe.whitelist(allow_guest=True)
def get_autocomplete_suggestions(pick_up,droppoff,location_type):
    suggestions = []
    api_key = 'AIzaSyALQeTzcPybl49BHvmR23_cE2PsRkcG8uw'
    url = f'https://maps.googleapis.com/maps/api/place/autocomplete/json?key={api_key}&input={pick_up}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            predictions = data['predictions']
            suggestions = [prediction['description'] for prediction in predictions]

    return suggestions