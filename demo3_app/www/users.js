//frm.add__custom_button('submit', () => {
//    frappe.msgprint(__('You clicked!!'));
//});
function getData() {
    var value = document.getElementById('loginUser').value;
    // alert(value)


    frappe.call({
        method: 'demo3_app.www.users.get_value',
        args: {
            'value': value
        }


    }).then(r => {
        console.log(r)
    })

}