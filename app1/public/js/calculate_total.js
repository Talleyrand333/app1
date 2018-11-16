frappe.ui.form.on("Vehicle Servicing Log",{
before_save:function(frm){
    var doc_ser_det=cur_frm.doc.service_details
    var service_details_arr=Object.values(doc_ser_det)
    var sum=0;
    for(var i in service_details_arr){
      var tempsum=service_details_arr[i].expense
      sum=sum+tempsum
    }
    cur_frm.set_value("total_expenses",sum)

  },
  validate: function(frm) {
      console.log("Hello");
        frappe.call({
            "method": "frappe.client.set_value",
            "args": {
                "doctype": "Vehicle",
                "name": frm.doc.vehicle,
                "fieldname": "odometer_2",
                "value": frm.doc.odometer
            }
        });
    }
})
