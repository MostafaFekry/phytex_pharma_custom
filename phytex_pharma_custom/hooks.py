# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "phytex_pharma_custom"
app_title = "Phytex Pharma Custom"
app_publisher = "MostafaFekry"
app_description = "Phytex Pharma Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mostafa.fekry@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/phytex_pharma_custom/css/phytex_pharma_custom.css"
# app_include_js = "/assets/phytex_pharma_custom/js/phytex_pharma_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/phytex_pharma_custom/css/phytex_pharma_custom.css"
# web_include_js = "/assets/phytex_pharma_custom/js/phytex_pharma_custom.js"

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
# get_website_user_home_page = "phytex_pharma_custom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "phytex_pharma_custom.install.before_install"
# after_install = "phytex_pharma_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "phytex_pharma_custom.notifications.get_notification_config"

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
# 		"phytex_pharma_custom.tasks.all"
# 	],
# 	"daily": [
# 		"phytex_pharma_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"phytex_pharma_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"phytex_pharma_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"phytex_pharma_custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "phytex_pharma_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "phytex_pharma_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "phytex_pharma_custom.task.get_dashboard_data"
# }

