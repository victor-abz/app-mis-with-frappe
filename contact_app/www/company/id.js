frappe.ready(function() {
    $('#modalClose').on("click", () => {
        window.location.reload(false);
    })
    
    // Handling Upload from form
    var $form = $("form[id='addUserForm']");

    $form.on("change", "[type='file']", function() {
      var $input = $(this);
      var input = $input.get(0);
      
      if(input.files.length) {
        input.filedata = { "files_data" : [] }; //Initialize as json array.

        window.file_reading = true;

        $.each(input.files, function(key, value) {
          setupReader(value, input);
        });

        window.file_reading = false;
      }
    });

    // Start sending data to docType
    const urlParams = new URLSearchParams(window.location.search);
    const companyId = urlParams.get('name');

    $( "form" ).submit(function( event ) {
        event.preventDefault();
      frappe.call({
        method:"contact_app.www.company.id.get_role_profile",
        args: {
            company: companyId,
            inputFirstName: document.getElementById("inputFirstName").value,
            inputLastName: document.getElementById("inputLastName").value,
            inputEmail: document.getElementById("inputEmail").value,
            inputGender: document.getElementById("inputGender").value,
            primaryCheck: document.getElementById("primaryCheck").value,
            inputPosition: document.getElementById("inputPosition").value,
            inputPhone: document.getElementById("inputPhone").value
        },
        freeze: true,
        freeze_message: __("Submitting..."),
        callback:function(r){
            if(!r.exc) {
                if($('#inputImage').prop('filedata')){
                    frappe.call({
                        method: "contact_app.www.company.id.attach_file_to_contact",
                        args: {"filedata": $('#inputImage').prop('filedata'), "contact_name": r.message.contacts[r.message.contacts.length - 1].name },
                        freeze: true,
                        freeze_message: __("Submitting......"),
                        callback: function(r){
                          if(!r.exc) {
                            $('#popMessage').text("Form submitted succesfully");
                            $('#exampleModal').modal('show'); 
                          } else {
                            frappe.msgprint(__("Image can't uploaded. <br /> " + r.exc));  
                          }
                        }
                      });
                }else{
                    $('#popMessage').text("Form submitted succesfully");
                    $('#exampleModal').modal('show'); 
                }
            } else {
                frappe.msgprint(__("An error occurred <br /> " + r.exc));
            }
        }
    });
        

      });
  });

  function setupReader(file, input) {
    console.log('herer')
    var name = file.name;
    var reader = new FileReader();  
    reader.onload = function(e) {
    input.filedata.files_data.push({
      "__file_attachment": 1,
      "filename": file.name,
      "dataurl": reader.result
    })
  }
  reader.readAsDataURL(file);
}