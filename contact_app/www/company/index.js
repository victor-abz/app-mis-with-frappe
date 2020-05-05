frappe.ready(function() {
    url = window.location.params

    var next_start = {{ next_start or 0 }};
    var result_wrapper = $(".website-list .result");
    var data = $.extend(frappe.utils.get_query_params(), {
        doctype: "company",
        txt: "{{ txt or '' }}",
        limit_start: next_start,
        pathname: location.pathname,
    });
    $.ajax({
        url:"/api/method/frappe.www.list.get?order_by=company_name%20desc",
        data: data,
        statusCode: {
            200: function(data) {
                var data = data.message;
                next_start = data.next_start;
                $.each(data.result, function(i, d) {
                    $(d).appendTo(result_wrapper);
                });
                toggle_more(data.show_more);
            }
        },
        dataType: "json",
    })
    	var toggle_more = function(show) {
		if (!show) {
			$(".website-list .more-block").addClass("hide");
		}
	};

	if($('.navbar-header .navbar-toggle:visible').length === 1)
	{
		$('.page-head h1').addClass('list-head').click(function(){
			window.history.back();
	 	});
	}
         const sidebar_menu_items = [
        `<a href="/dashboard" class="sidebar-item ">
					<span>Dashboard</span>
        </a>`,
        `<a href="/company" class="sidebar-item selected ">
					<span>Companies</span>
        </a>`,
        `<a href="/desk#List/Event/Calendar/Default" class="sidebar-item ">
					<span>Calendar</span>
        </a>`,
        `<a href="/desk#List/Appointment/List" class="sidebar-item ">
					<span>Appointments</span>
        </a>`,
        `<a href="/desk#List/Communication/List" class="sidebar-item ">
					<span>Messages</span>
		</a>`,
    ]
    sidebar_menu_items.forEach((item) =>  $( ".list-unstyled" ).append( item ))   
});