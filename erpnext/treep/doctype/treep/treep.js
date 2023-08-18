// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Treep', {	
	refresh: function(frm) {
		// Attach event listeners to the pickup and dropoff input fields
		frm.fields_dict.pick_up.$input.on('keyup', function() {
				// Create an Autocomplete object for the pickup input field
				var autocomplete = new google.maps.places.Autocomplete(this);
				frm.set_value('pick_up', autocomplete);
		});

		frm.fields_dict.dropoff.$input.on('keyup', function() {
				// Create an Autocomplete object for the dropoff input field
				var autocomplete = new google.maps.places.Autocomplete(this);
				frm.set_df_property('dropoff', 'options', autocomplete);
		});

}
});