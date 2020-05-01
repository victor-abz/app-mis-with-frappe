// Copyright (c) 2020, Abizeyimana Victor and contributors
// For license information, please see license.txt

frappe.ui.form.on('company', {
    on_submit: function(frm) {
		change_route(frm);
	},
	after_save: function(frm) {
		change_route(frm);
	}
});

var change_route = function() {
	window.location.href = "/company"
}