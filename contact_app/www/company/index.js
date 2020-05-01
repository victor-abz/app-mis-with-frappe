frappe.ready(function() {
    url = window.location.params
    //   frappe.call({
    //     method:"contact_app.www.company.get_company_list",
    //     args: {
    //         doctype: 'company'
    //     },
    //     callback:function(r){
    //         console.log(r)
    //     }
    // });
    var next_start = {{ next_start or 0 }};
    var result_wrapper = $(".website-list .result");
    var data = $.extend(frappe.utils.get_query_params(), {
        doctype: "company",
        txt: "{{ txt or '' }}",
        limit_start: next_start,
        pathname: location.pathname,
    });
    $.ajax({
        url:"/api/method/frappe.www.list.get",
        data: {
            doctype: "company",
            limit_start: next_start,
        },
        statusCode: {
            200: function(data) {
                console.log('>>>>>>',data)
                var data = data.message;
                next_start = data.next_start;
                $.each(data.result, function(i, d) {
                    $(d).appendTo(result_wrapper);
                });
                toggle_more(data.show_more);
            }
        },
        dataType: "json",
        // success: function(data) {
        //     console.log('>>><<',data)
		// 	// window.render_product_list(data.message || []);
		// }
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
    // $.ajax({
	// 	method: "GET",
	// 	url: "/api/resource/company",
	// 	// data: {
	// 	// 	cmd: "erpnext.templates.pages.product_search.get_product_list",
	// 	// 	start: window.start,
	// 	// 	search: window.search,
	// 	// 	product_group: window.product_group
	// 	// },
	// 	dataType: "json",
	// 	success: function(data) {
    //         console.log('>>><<',data)
	// 		// window.render_product_list(data.message || []);
	// 	}
	// })
        
});