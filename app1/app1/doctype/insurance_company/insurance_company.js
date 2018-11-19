// Copyright (c) 2018, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insurance Company', {
	refresh: function(frm) {
	//	console.log("Hello there");
			var addy=frappe.get_doc("Address","Address 2-Office")
			var temp = frappe.render_template("address__.html",data={addy:addy})
	},
	new_contact:function(frm){
	frappe.new_doc("Contact")
	},
	add_address:function(frm){
	frappe.new_doc("Address")

	}


});
