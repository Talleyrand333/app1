frappe.listview_settings['Workflow Notification'] = {
	get_form_link: (doc) => {
		let doctype = '';
		let docname = '';
		if(doc.status === 'Open') {
			doctype = doc.reference_doctype;
			docname = doc.reference_name;
		} else {
			doctype = 'Workflow Notification';
			docname = doc.name;
		}
		docname = docname.match(/[%'"]/)
			? encodeURIComponent(docname)
			: docname;

		const link = '#Form/' + doctype + '/' + docname;
		return link;
	}
};