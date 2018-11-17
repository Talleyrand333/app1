frappe.ui.form.on("Vehicle Servicing Log",{
before_save:function(frm){
  console.log("Calculating");
    var doc_ser_det=cur_frm.doc.service_details
    var service_details_arr=Object.values(doc_ser_det)
    var sum=0;
    for(var i in service_details_arr){
      var tempsum=service_details_arr[i].expense
      sum=sum+tempsum
    }
    cur_frm.set_value("total_expenses",sum)
    console.log("Finished Calculation");
    frappe.call({
        "method": "frappe.client.set_value",
        "args": {
            "doctype": "Vehicle",
            "name": cur_frm.doc.vehicle,
            "fieldname": {
              // "last_odometer":cur_frm.doc.odometer,
              "date_of_last_service":cur_frm.doc.service_date
              //console.log(cur_frm.doc.service_date);

            }
        }
    });
    console.log("ran to the end");
    // frappe.call({
    //   "method":"frappe.client.set_value",
    //   "args":{
    //     "doctype":"Vehicle",
    //     "name":cur_frm.doc.vehicle,
    //     "fieldname":"date_of_last_service",
    //     "value":cur_frm.doc.service_date
    //   }
    // })
  }
 })
