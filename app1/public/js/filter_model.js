frappe.ui.form.on('Vehicle',{
  vehicle_make: function(frm){
      cur_frm.fields_dict["vehicle_model"].get_query=function(doc){
        return {
          filters:{
            "vehicle_make":frm.doc.vehicle_make
        }
      }
      }
  }
})
