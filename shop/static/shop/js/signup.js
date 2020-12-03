let token = null


function validate(event){
    var error = document.getElementById('message')
    console.log(error)
    var message = null
    let form = event.target;
    let values = form.elements;
    token = values.csrfmiddlewaretoken.value;
    let email = values.email.value;
    let name = values.name.value;

    message = validateForm(form)
    if(message){

        error.innerHTML = message
        error.hidden = false
    }else{
        error.innerHTML = ""
        error.hidden = true

        SendEmail(name , email , token)

    }
    event.stopPropagation();

    return false


}
function validateForm(form){

    let values = form.elements;
    let name = values.name.value;
    token = values.csrfmiddlewaretoken.value;
    let message = null
    let email = values.email.value;
    let phone = values.phone.value;
    let password = values.password.value;
    let repassword = values.repassword.value;

    if(!name.trim()){

        message = "Name Is Required"
    }else if (!email.trim()){

        message = "Ëmail Is Required"
    }else if (!password.trim()){

        message = "Password Is Required"
     }else if (!repassword.trim()){

        message = "Enter Password Again"
     }else if (password.trim() != repassword.trim()){

        message = "Password Not Matched"
     }

        return message
}

function SendEmail(name , email ,token){

$.ajax({
  method: "POST",
  url: "/send-otp/",
  data: { name: name , email: email , 'csrfmiddlewaretoken' : token }
})
  .done(function( msg ) {
    ShowOtpInput()
  }).fail(function(err){
    alert(" Cant Send Email ");
  })
  }

function ShowOtpInput(){

     let input = document.getElementById('verification')
     let verifybutton = document.getElementById('verifybutton')
     let submitbutton = document.getElementById('submitbutton')

     input.hidden = false
     submitbutton.hidden = true
     verifybutton.hidden = false

}

function verifycode(){

 let codeInput = document.getElementById('code')
 let code = codeInput.value

  $.ajax({
  method: "POST",
  url: "/verify/",
  data: { 'code' : code , 'csrfmiddlewaretoken' : token }
})
  .done(function( msg ) {
    submitForm()
  }).fail(function(err){
    alert(" code invalid ");
  })
}

function submitForm(){

let form = document.getElementById('form')
let message = validateForm(form)
    try{
        if(message){

        }else{

         form.submit()
            }
    }catch(err){
    console.log(err)
    }


}