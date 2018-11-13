frappe.ui.form.on('Vehicle Model',{
  refresh:function(frm){
    console.log("Working")
  },
cur_frm.on_save:function(frm){
    var make_=frm.doc.vehicle_make
    var name_=frm.doc.name1
    var year_=frm.doc.model_year.toString()
    var uniqueID=make_.substring(0,3)+name_.substring(0,3)+year_.substring(0,2)
    cur_frm.set_value("vmn",uniqueID)
  }
})
