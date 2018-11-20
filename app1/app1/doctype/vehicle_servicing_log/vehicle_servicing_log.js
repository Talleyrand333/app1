// Copyright (c) 2018, frappe and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Vehicle Servicing Log","vehicle", function(frm){
// 	frappe.model.with_doc("Service Plan Template",frm.doc.vehicle,function(){
// 		var tabletransfer=frappe.model.get_doc("Service Plan Template", frm.doc.vehicle)
	// 	$.each(tabletransfer.service_plan_,function(index,row)
	// {
	// 	d=frm.add_child("Service Details")
	// 	d.service_item=row.service_item
	// 	d.type=row.doctype
	// 	cur_frm.refresh_field("service_details")
	// })

frappe.ui.form.on("Vehicle Servicing Log",{
		vehicle:function (frm) {
		var vehicle_name=cur_frm.doc.vehicle
		if(vehicle_name==" "){
		vehicle_name="blank"
	}
		frappe.call({
			args:{vehicle_name:vehicle_name},
			method:'app1.utils.hr.getServicePlan',
			callback:function(response){
					for(var o=0;o<=response.message[0].length-1;o++){
						frm.add_child("service_details")
						cur_frm.doc.service_details[o].service_item=response.message[0][o]
						cur_frm.doc.service_details[o].type=response.message[1][o]
						cur_frm.refresh_field("service_details")
						console.log(response.message[1]);
					}
			}
		})
	},
})

// frappe.ui.form.on("Vehicle Service Template", "refresh", function(frm) {
// 	frappe.ui.form.on("Service Details", {
// 			"service_item": function(frm) {
// 			frm.add_fetch("[CHILD_TABLE_LINK FIELD]", "[SOURCE_CUSTOM_FIELD2]", "[TARGET_CUSTOM_FIELD2]");
// 		}
// 	});
//
// });
