frappe.ready(function() {
    let labels;
    let values
    frappe.call({
        method: "contact_app.www.dashboard.get_communication_data",
        args: {
            doctype: 'Communication'
        },
        callback: function(r) {
            if (!r.exc) {
                labels = r.message.map(item => item.communication_date);
                values = r.message.map(item => item.count);
                console.log(labels, values)
            } else {
                frappe.msgprint(__("An error occurred <br /> " + r.exc));
            }
        }
    });
    $.getScript("https://cdn.jsdelivr.net/npm/frappe-charts@1.1.0/dist/frappe-charts.min.iife.js", function() {
        const data = {
            labels: labels,
            datasets: [{
                name: "Contact",
                values: values
            }],
            yMarkers: [{
                label: "Threshold",
                value: 5,
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