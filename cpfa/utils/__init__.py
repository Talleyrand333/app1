

def get_pdf_link(doctype, docname, print_format='Standard', no_letterhead=0):
	return '/api/method/frappe.utils.print_format.download_pdf?doctype={doctype}&name={docname}&format={print_format}&no_letterhead={no_letterhead}'.format(
		doctype = doctype,
		docname = docname,
		print_format = print_format,
		no_letterhead = no_letterhead
	)