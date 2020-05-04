frappe.ready(function() {
    // frappe.call({
    //     method: "contact_app.www.dashboard.get_communication_data",
    //     args: {
    //         company: 'companyId',
    //     },
    //     callback: function(r) {
    //         if (!r.exc) {

    //         } else {
    //             frappe.msgprint(__("An error occurred <br /> " + r.exc));
    //         }
    //     }
    // });
    $.getScript("https://cdn.jsdelivr.net/npm/frappe-charts@1.1.0/dist/frappe-charts.min.iife.js", function() {

        const data = {
            labels: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            datasets: [{
                name: "Contact",
                values: [18, 40, 30, 35, 8, 52, 17, 0]
            }],
            yMarkers: [{
                label: "Threshold",
                value: 20,
                options: {
                    labelPos: 'left'
                } // default: 'right'
            }]
        }

        const chart = new frappe.Chart("#chart", { // or a DOM element
            title: "My Productivity Chart",
            data: data,
            type: 'bar', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
            height: 350,
            colors: ['green'],

        })
    })
})