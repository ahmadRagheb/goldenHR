# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.data import flt, nowdate, getdate, cint

class MoneyTransfere(Document):

	def on_submit(self):
		self.validate_transfere()

	def validate_transfere(self):
		if self.from_company != self.to_company:
			# sending_account = "حساب ارسال الى " + self.to_company
			# receiving_account = "حساب استلام من " + self.from_company
			# self.add_account_for_company(sending_account, self.to_company, "Liability")
			# self.add_account_for_company(receiving_account, self.from_company, "Expense")
			self.add_payment_entry(self.from_account, "حساب ارسال الى other - اا", self.from_company)
			self.add_journal_entry(self.to_account,"حساب استقبال من Eye - o", self.to_company)
		else:
			self.add_payment_entry(self.from_account, self.to_account, self.from_company)


	def add_account_for_company(self, account, company, r_type):
		pass
		# pacc_name = ""
		# if r_type == "Expense":
		# 	pacc_name = "حساب ارسال - E"
		# elif r_type == "Liability":
		# 	pacc_name = "حساب استقبال - o"

		# # if not frappe.db.exists("Account", pacc_name):
		# # 	pacc = frappe.new_doc("Account")
		# # 	pacc.account_name = pacc_name
		# # 	pacc.root_type = r_type
		# # 	pacc.is_group = 1
		# # 	pacc.parent_account = ""
		# # 	pacc.company = company
		# # 	pacc.flags.ignore_validate = True
		# # 	pacc.insert()

		# if not frappe.db.exists("Account", account):
		# 	acc = frappe.new_doc("Account")
		# 	acc.account_name = account
		# 	acc.company = company
		# 	acc.parent_account = pacc_name
		# 	acc.is_group = 0
		# 	acc.insert()

	def add_payment_entry(self, paid_from, paid_to, company):
		pe = frappe.new_doc("Payment Entry")
		pe.payment_type = "Internal Transfer"
		pe.company = company
		pe.paid_from = paid_from
		pe.paid_to = paid_to
		pe.paid_amount = self.transfered_amount
		pe.received_amount = self.transfered_amount
		pe.posting_date = nowdate()
		pe.mode_of_payment = self.mode_of_payment

		pe.append("references", {
			"reference_doctype": "Money Transfere",
			"reference_name": self.name
		})
		pe.insert()
		pe.submit()
		# pe.setup_party_account_field()
		# pe.set_missing_values()
		# pe.set_exchange_rate()
		# pe.set_amounts()
				
		# self.assertEquals(pe.difference_amount, 500)
		
		# pe.append("deductions", {
		# 	"account": "_Test Exchange Gain/Loss - _TC",
		# 	"cost_center": "_Test Cost Center - _TC",
		# 	"amount": 500
		# })
	def add_journal_entry(self, account1, account2, company):
		jv = frappe.new_doc("Journal Entry")
		jv.posting_date = nowdate()
		jv.company = company
		jv.voucher_type = "Opening Entry"
		jv.set("accounts", [
			{
				"account": account1,
				"credit_in_account_currency": self.transfered_amount,
				"cost_center": "Main - o"
			}, {
				"account": account2,
				"debit_in_account_currency": self.transfered_amount,
				"cost_center": "Main - o"

			}
		])
		jv.insert()
		jv.submit()
		
		

