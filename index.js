let submitBtn = document.getElementById("submitBtn")
let name_input = document.getElementById("name_input")
let message =  document.getElementById('message')

name_input.value = ''
submitBtn.addEventListener("click", (e) =>{
if (name_input.value == '') {
    message.innerHTML='Please Enter Name'
} else {
    alert('success')
}
})