// Copyright (c) 2018, Manqala and contributors
// For license information, please see license.txt

frappe.ui.form.on('Azure Storage Backup Settings', {
	refresh: function(frm) {
		frm.clear_custom_buttons();
		frm.events.take_backup(frm);
	},

	take_backup: function(frm) {
		if (frm.doc.account_key && frm.doc.account_name && frm.doc.container_name) {
			frm.add_custom_button(__("Take Backup Now"), function(){
				frm.dashboard.set_headline_alert("Azure Storage Backup Started!");
				frappe.call({
					method: "cpfa.cpfa.doctype.azure_storage_backup_settings.azure_storage_backup_settings.take_backups_azure",
					callback: function(r) {
						if(!r.exc) {
							frappe.msgprint(__("Azure Storage Backup complete!"));
							frm.dashboard.clear_headline();
						} else {
							frm.dashboard.clear_headline();
						}
					}
				});
			}).addClass("btn-primary");
		}
	}
});
