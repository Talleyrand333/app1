
$(function(){
	try {
		frappe.ui.form.States.prototype.show_actions = function(state) {
			var added = false,
				me = this;

			this.frm.page.clear_actions_menu();

			// if the loaded doc is dirty, don't show workflow buttons
			if (this.frm.doc.__unsaved===1) {
				return;
			}

			function has_approval_access(transition) {
				let approval_access = false;
				const user = frappe.session.user;
				if (user === 'Administrator'
					|| transition.allow_self_approval
					|| user !== me.frm.doc.owner) {
					approval_access = true;
				}
				return approval_access;
			}

			$.each(frappe.workflow.get_transitions(this.frm.doctype, state), function(i, d) {
				if(frappe.user_roles.includes(d.allowed) && has_approval_access(d)) {
					added = true;
					me.frm.page.add_action_item(__(d.action), function() {
						var action = d.action;
						// capture current state
						var doc_before_action = copy_dict(me.frm.doc);

						// set new state
						var next_state = frappe.workflow.get_next_state(me.frm.doctype,
								me.frm.doc[me.state_fieldname], action);
						me.frm.doc[me.state_fieldname] = next_state;
						var new_state = frappe.workflow.get_document_state(me.frm.doctype, next_state);
						var new_docstatus = cint(new_state.doc_status);


						if(new_state.update_field) {
							me.frm.set_value(new_state.update_field, new_state.update_value);
						}

						// revert state on error
						var on_error = function() {
							// reset in locals
							frappe.model.add_to_locals(doc_before_action);
							me.frm.refresh();
						}

						// success - add a comment
						var success = function() {
							me.frm.timeline.insert_comment("Workflow", next_state);
						}
						if(new_docstatus==1 && me.frm.doc.docstatus==0) {
							me.frm.savesubmit(null, success, on_error);
						} else if(new_docstatus==0 && me.frm.doc.docstatus==0) {
							me.frm.save("Save", success, null, on_error);
						} else if(new_docstatus==1 && me.frm.doc.docstatus==1) {
							me.frm.save("Update", success, null, on_error);
						} else if(new_docstatus==2 && me.frm.doc.docstatus==1) {
							me.frm.savecancel(null, success, on_error);
						} else {
							frappe.msgprint(__("Document Status transition from ") + me.frm.doc.docstatus + " "
								+ __("to") +
								new_docstatus + " " + __("is not allowed."));
							frappe.msgprint(__("Document Status transition from {0} to {1} is not allowed", [me.frm.doc.docstatus, new_docstatus]));
							return false;
						}

						return false;

					});
				}
			});

			if(added) {
				this.frm.page.btn_primary.addClass("hide");
				this.frm.toolbar.current_status = "";
				this.setup_help();
			}
		};
	} catch(e){
		console.trace('cpfa.js error')
		console.trace(e)
	}
})
