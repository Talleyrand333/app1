
frappe.ui.form.on('Salary Slip', {
	refresh: function(frm){
		console.log('working as expected')
	},
	employee: function(frm){
		var employee = frm.doc.employee_name
		var cal_start=frm.doc.start_date
		var cal_end=frm.doc.end_date
		/*A function that calculates the daily salary of employee and  returns the amount payable after deductions*/
		frappe.call({
				args:{employee: employee,cal_end:cal_end,cal_start:cal_start},
				method: 'app1.utils.hr.get_days_present',
				callback: function(response){
				var annual_sal=response.message[1]
				var monthly_sal=annual_sal/12
				var working_days=frm.doc.total_working_days
				var daily_equivalent=monthly_sal/working_days
				var attendance_deduc=daily_equivalent*response.message[0]
				var payment=monthly_sal-attendance_deduc
				cur_frm.set_value("number_of_days_missed",response.message[0])
				cur_frm.set_value("annual_salary",response.message[1])
				cur_frm.set_value("salary_for_month",payment)
				//console.log("number of days",response.message[1]);
			}
		})
	}
})
