// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Money Transfere', {
    refresh: function(frm) {

    },
    to_company: function(frm) {
        if (!frm.doc.to_company) {
            frm.doc.to_account = "";

        }


    },
    from_company: function(frm) {
        if (!frm.doc.from_company) {
            frm.doc.from_account = "";
        }
    },
  
});

cur_frm.fields_dict.to_account.get_query = function() {
    if (!cur_frm.doc.to_company === "" || cur_frm.doc.to_company === undefined) {
        frappe.throw(__("please select to company"));
    } else {
        return {
            filters: [
                ["company", "=", cur_frm.doc.to_company]
            ]
        }
    }
};

cur_frm.fields_dict.from_account.get_query = function() {
    if (cur_frm.doc.from_company === "" || cur_frm.doc.from_company === undefined) {
        frappe.throw(__("please select from company"));
    } else {
        return {
            filters: [
                ["company", "=", cur_frm.doc.from_company]
            ]
        }
    }
};


// cur_frm.fields_dict.dummy_from.get_query = function() {
//     if (cur_frm.doc.from_company === "" || cur_frm.doc.from_company === undefined) {
//         frappe.throw(__("please select from company"));
//     } else {
//         return {
//             filters: [
//                 ["company", "=", cur_frm.doc.from_company],
//                 ["parent_account","=","حساب ارسال"+" - "+cur_frm.doc.abbr],
//                 ["name","=","حساب ارسال الي"+" - "+cur_frm.doc.to_company + " - "+cur_frm.doc.abbr]


//             ]
//         }
//     }
// };


// cur_frm.fields_dict.dummy_to.get_query = function() {
//     if (cur_frm.doc.from_company === "" || cur_frm.doc.from_company === undefined) {
//         frappe.throw(__("please select from company"));
//     } else {
//         return {
//             filters: [
//                 ["company", "=", cur_frm.doc.to_company],
//                 ["parent_account","=","حساب استلام من"+" - "+cur_frm.doc.abbr_to],
//                 ["name","=","حساب استلام من"+" - "+cur_frm.doc.from_company + " - "+cur_frm.doc.abbr_to]


//             ]
//         }
//     }
// };


