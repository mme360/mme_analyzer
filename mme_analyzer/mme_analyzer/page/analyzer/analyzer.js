frappe.pages['analyzer'].on_page_load = function (wrapper) {
    frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Analyzer',
        single_column: true,
    });
};

frappe.pages['analyzer'].on_page_show = function () {
    frappe.set_route('List', 'Analyzer');
};
