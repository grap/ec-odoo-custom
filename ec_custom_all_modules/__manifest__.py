# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "EC - All modules",
    "summary": "Install all modules required for EC",
    "version": "12.0.1.0.1",
    "category": "EC Custom",
    "author": "GRAP",
    "license": "AGPL-3",
    "depends": [
        # OCA / account-budgeting
        "account_budget_oca",
        # OCA / account-financial-reporting
        "account_financial_report",
        "account_tax_balance",
        "mis_builder_cash_flow",
        "partner_statement",
        # OCA / account-financial-tools
        "account_asset_management",
        "account_balance_line",
        "account_check_deposit",
        "account_move_budget",
        "account_menu",
        "account_netting",
        "account_partner_required",
        "account_payment_netting",
        "account_spread_cost_revenue",
        # OCA / account-fiscal-rule
        "account_fiscal_position_usage_group",
        "account_product_fiscal_classification",
        # OCA / account-invoicing
        "account_invoice_refund_link",
        "account_invoice_fiscal_position_update",
        "account_invoice_pricelist",
        "account_invoice_refund_link",
        "account_invoice_refund_reason",
        "account_invoice_supplierinfo_update",
        "account_invoice_view_payment",
        # OCA / account-payment
        "account_payment_widget_amount",
        "account_payment_show_invoice",
        "account_due_list",
        "account_due_list_days_overdue",
        # OCA / l10n-france
        "l10n_fr_siret",
        "l10n_fr_state",
        "l10n_fr_department",
        "l10n_fr_department_oversea",
        "l10n_fr_fec_oca",
        "l10n_fr_mis_reports",
        # OCA / mis-builder
        "mis_builder",
        "mis_builder_budget",
        "mis_builder_demo",  # ATTENTION : Just for test
        # # OCA / web
        "web_responsive",
        "web_export_view",
        "web_disable_export_group",
        "web_switch_context_warning",
        "web_widget_color",
        "web_decimal_numpad_dot",
        "web_group_by_percentage",
        "web_no_bubble",
        "web_widget_image_download",
        # OCA / account-closing
        # TODO
        # OCA / account-reconcile
        # TODO
        # OCA / account-invoice-reporting
        # TODO
        # # OCA / reporting-engine
        # "report_xlsx",
        # "bi_sql_editor",
        # # OCA / rest-framework
        # "base_rest",
        # # OCA / server-auth
        # "auth_ldaps",
        # # OCA / server-brand
        # "disable_odoo_online",
        # "remove_odoo_enterprise",
        # # OCA / server-tools
        # "excel_import_export",
        # # OCA / server-ux
        # "mass_editing",
        # "base_export_manager",
    ],
    "data": [],
    "installable": True,
}
