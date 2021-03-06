# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "app1"
app_title = "App1"
app_publisher = "frappe"
app_description = "Test App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ebukaakeru@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/app1/css/app1.css"
# app_include_js = "/assets/app1/js/app1.js"

# include js, css files in header of web template
# web_include_css = "/assets/app1/css/app1.css"
# web_include_js = "/assets/app1/js/app1.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {
"Salary Slip" : "public/js/custom_hr.js",
}
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
# get_website_user_home_page = "app1.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "app1.install.before_install"
# after_install = "app1.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "app1.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Salary Slip": {
        "validate": "app1.utils.hr.calculate_base_amount"
    },
    "Vehicle Model": {
        "before_save":"app1.utils.hr.change_auto_name"
     }
    }



# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"app1.tasks.all"
# 	],
# 	"daily": [
# 		"app1.tasks.daily"
# 	],
# 	"hourly": [
# 		"app1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"app1.tasks.weekly"
# 	]
# 	"monthly": [
# 		"app1.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "app1.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "app1.event.get_events"
# }
