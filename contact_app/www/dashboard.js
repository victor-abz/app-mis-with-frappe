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
    const sidebar_menu_items = [
        `<a href="/dashboard" class="sidebar-item selected ">
					<span>Dashboard</span>
        </a>`,
        `<a href="/company" class="sidebar-item ">
					<span>Companies</span>
        </a>`,
        `<a href="/desk#List/Event/Calendar/Default" class="sidebar-item ">
					<span>Calendar</span>
        </a>`,
        `<a href="/desk#List/Appointment/List" class="sidebar-item ">
					<span>Appointments</span>
        </a>`,
        ,
        `<a href="/desk#List/Communication/List" class="sidebar-item ">
					<span>Messages</span>
		</a>`,
    ]
    sidebar_menu_items.forEach((item) =>  $( ".list-unstyled" ).append( item ))
})