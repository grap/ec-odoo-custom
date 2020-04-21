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
        # OCA / account-financial-tools
        "account_menu",
        # OCA / account-fiscal-rule
        "account_fiscal_position_usage_group",
        "account_product_fiscal_classification",
        # OCA / reporting-engine
        "report_xlsx",
        "bi_sql_editor",
        # OCA / rest-framework
        "base_rest",
        # OCA / server-auth
        "auth_ldaps",
        # OCA / server-brand
        "disable_odoo_online",
        "remove_odoo_enterprise",
        # OCA / server-tools
        "excel_import_export",
        # OCA / server-ux
        "mass_editing",
        "base_export_manager",
        # OCA / web
        "web_responsive",
        "web_export_view",
        "web_disable_export_group",
        "web_switch_context_warning",
        "web_widget_color",
        "web_decimal_numpad_dot",
        "web_group_by_percentage",
        "web_no_bubble",
        "web_widget_image_download",
    ],
    "data": [],
    "installable": True,
}
