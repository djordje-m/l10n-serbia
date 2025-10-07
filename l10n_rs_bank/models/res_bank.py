# coding: utf-8

from odoo import fields, models


class Bank(models.Model):
    _inherit = "res.bank"

    l10n_rs_rtgs_code = fields.Char(
        "RTGS Code",
        help="Three-digit code assigned by the National Bank of Serbia to identify banking "
        "institutions")

