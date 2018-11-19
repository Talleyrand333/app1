frappe.ui.form.on('Vehicle',{
  vehicle_make: function(frm){
    //console.log("At the beginning")
      cur_frm.fields_dict["vehicle_model"].get_query=function(doc){
        return {
          filters:{
            "vehicle_make":frm.doc.vehicle_make,
            //console.log("Finished")
        }
      }
      }
  },
  refresh: function(frm){
		var name__=cur_frm.doc.name
cur_frm.add_custom_button(("Vehicle Servicing Log"),function(ev){
	frappe.set_route("List","Vehicle Servicing Log",{"vehicle":name__})
},("Show"))
cur_frm.add_custom_button(("Vehicle Trip Log"),function(ev){
	frappe.set_route("List","Vehicle Trip Log",{"vehicle":name__})
},("Show"))
cur_frm.add_custom_button(("Vehicle Servicing Log"),function(ev){
	frappe.new_doc("Vehicle Servicing Log")
},("Create"))
cur_frm.add_custom_button(("Vehicle Trip Log"),function(ev){
doc=frappe.new_doc("Vehicle Trip Log")
},("Create"))

}
})
