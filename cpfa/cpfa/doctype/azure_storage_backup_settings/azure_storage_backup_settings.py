# -*- coding: utf-8 -*-
# Copyright (c) 2018, Manqala and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import os
import os.path
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint, split_emails
from frappe.utils.background_jobs import enqueue
from azure.storage.blob import BlockBlobService
from azure.storage._error import AzureHttpError, AzureException


class AzureStorageBackupSettings(Document):
	
	def validate(self):
		block_blob_service = BlockBlobService(
			account_name=self.account_name,
			account_key=self.get_password('account_key'),
		)

		container_name = str(self.container_name)

		try:
			containers_generator = block_blob_service.list_containers()
		except (AzureHttpError,AzureException):
			frappe.throw(_("Invalid Access Key ID or Secret Access Key."))

		try:
			block_blob_service.create_container(container_name=container_name)
		except (AzureHttpError, AzureException):
			frappe.throw(_("Unable to create bucket: {0}. Change it to a more unique name.").format(container_name))


@frappe.whitelist()
def take_backup():
	"Enqueue longjob for taking backup to Azure Storage"
	enqueue("cpfa.cpfa.doctype.azure_storage_backup_settings.azure_storage_backup_settings.take_backups_azure", queue='long', timeout=1500)
	frappe.msgprint(_("Queued for backup. It may take a few minutes to an hour."))


def take_backups_daily():
	take_backups_if("Daily")


def take_backups_weekly():
	take_backups_if("Weekly")


def take_backups_monthly():
	take_backups_if("Monthly")


def take_backups_if(freq):
	if cint(frappe.db.get_value("Azure Storage Backup Settings", None, "enabled")):
		if frappe.db.get_value("Azure Storage Backup Settings", None, "frequency") == freq:
			take_backups_azure()


@frappe.whitelist()
def take_backups_azure():
	try:
		backup_to_azure()
		send_email(True, "Azure Storage Backup Settings")
	except Exception:
		error_message = frappe.get_traceback()
		frappe.errprint(error_message)
		send_email(False, "Azure Storage Backup Settings", error_message)


def send_email(success, service_name, error_status=None):
	if success:
		subject = "Backup Upload Successful"
		message = """<h3>Backup Uploaded Successfully! </h3><p>Hi there, this is just to inform you
		that your backup was successfully uploaded to your Azure Storage container. So relax!</p> """

	else:
		subject = "[Warning] Backup Upload Failed"
		message = """<h3>Backup Upload Failed! </h3><p>Oops, your automated backup to Azure Storage failed.
		</p> <p>Error message: %s</p> <p>Please contact your system manager
		for more information.</p>""" % error_status

	if not frappe.db:
		frappe.connect()

	if frappe.db.get_value("Azure Storage Backup Settings", None, "notification_email"):
		recipients = split_emails(frappe.db.get_value("Azure Storage Backup Settings", None, "notification_email"))
		frappe.sendmail(recipients=recipients, subject=subject, message=message)


def backup_to_azure():
	from frappe.utils.backups import new_backup
	from frappe.utils import get_backups_path

	doc = frappe.get_single("Azure Storage Backup Settings")
	container = doc.container_name

	block_blob_service = BlockBlobService(
			account_name=doc.account_name,
			account_key=doc.get_password('account_key'),
			)

	backup = new_backup(ignore_files=False, backup_path_db=None,
						backup_path_files=None, backup_path_private_files=None, force=True)
	db_filename = os.path.join(get_backups_path(), os.path.basename(backup.backup_path_db))
	files_filename = os.path.join(get_backups_path(), os.path.basename(backup.backup_path_files))
	private_files = os.path.join(get_backups_path(), os.path.basename(backup.backup_path_private_files))
	folder = os.path.basename(db_filename)[:15] + '/'
	# for adding datetime to folder name

	upload_file_to_azure(db_filename, folder, block_blob_service, container)
	upload_file_to_azure(private_files, folder, block_blob_service, container)
	upload_file_to_azure(files_filename, folder, block_blob_service, container)
	delete_old_backups(doc.backup_limit, container)
	if cint(doc.remove_local_backup):
		os.remove(db_filename)
		os.remove(private_files)
		os.remove(files_filename)

def upload_file_to_azure(filename, folder, block_blob_service, container):

	destpath = os.path.join(folder, os.path.basename(filename))
	try:
		print "Uploading file:", filename
		block_blob_service.create_blob_from_path(container, destpath, filename)

	except Exception as e:
		print "Error uploading: %s" % (e)


def delete_old_backups(limit, container):
	from collections import defaultdict
	
	root = 'root_dir'
	all_backups = defaultdict(set)
	doc = frappe.get_single("Azure Storage Backup Settings")
	backup_limit = int(limit)

	block_blob_service = BlockBlobService(
			account_name=doc.account_name,
			account_key=doc.get_password('account_key'),
			)
	#bucket = s3.Bucket(bucket)
	#objects = bucket.meta.client.list_objects_v2(Bucket=bucket.name, Delimiter='/')
	for blob in block_blob_service.list_blobs(doc.container_name):
		blob_name = blob.name.split('/',1)
		if len(blob_name) > 1:
			all_backups[blob_name[0]].add(blob_name[1])
			continue
		all_backups[root].add(blob_name[0])

	backup_dirs = [i for i in all_backups.keys() if i != root]
	oldest_backup = sorted(backup_dirs)[0]

	if len(backup_dirs) > backup_limit:
		print "Deleting Backup: {0}".format(oldest_backup)
		for blob in all_backups[oldest_backup]:
			# delete all keys that are inside the oldest_backup
			blob_name = '{}/{}'.format(oldest_backup, blob)
			block_blob_service.delete_blob(doc.container_name, blob_name)
