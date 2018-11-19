# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cpfa"
app_title = "Total CPFA ERPNext"
app_publisher = "Manqala"
app_description = "Total E&P NIG CPFA ERPNext customization"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "dev@manqala.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cpfa/css/cpfa.css"
# app_include_js = "/assets/cpfa/js/cpfa.js"

app_include_js = "/assets/cpfa/js/cpfa.js"

# include js, css files in header of web template
# web_include_css = "/assets/cpfa/css/cpfa.css"
# web_include_js = "/assets/cpfa/js/cpfa.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cpfa.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cpfa.install.before_install"
# after_install = "cpfa.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "cpfa.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

permission_query_conditions = {
	"Workflow Notification": "cpfa.cpfa.doctype.workflow_notification.workflow_notification.get_permission_query_conditions"
}

has_permission = {
	"Workflow Notification": "cpfa.cpfa.doctype.workflow_notification.workflow_notification.has_permission",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"on_update": "cpfa.cpfa.doctype.workflow_notification.workflow_notification.process_workflow_actions",
		"on_cancel": "cpfa.cpfa.doctype.workflow_notification.workflow_notification.process_workflow_actions",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cpfa.tasks.all"
# 	],
# 	"daily": [
# 		"cpfa.tasks.daily"
# 	],
# 	"hourly": [
# 		"cpfa.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cpfa.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cpfa.tasks.monthly"
# 	]
# }

scheduler_events = {
	"daily_long": [
		"cpfa.cpfa.doctype.azure_storage_backup_settings.azure_storage_backup_settings.take_backups_daily"
	],
	"weekly_long": [
		"cpfa.cpfa.doctype.azure_storage_backup_settings.azure_storage_backup_settings.take_backups_weekly",
	],
	"monthly_long": [
		"cpfa.cpfa.doctype.azure_storage_backup_settings.azure_storage_backup_settings.take_backups_monthly"
	]
}

# Testing
# -------

# before_tests = "cpfa.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cpfa.event.get_events"
# }

fixtures = [
	{"dt":"Custom Field", "filters": [["dt", "in", ["Workflow","Workflow Transition"]]]}
]