import axios from "./node_modules/axios"

window.onload=function(){
    const form=document.getElementById("authform")
    form.addEventListener("submit",authorize)
    window.location.href="index.html"
}

async function authorize(){
   const formData={}
     let email=document.getElementById("emailInput").value
     let password=document.getElementById("passwordInput").value
    formData.email=email
     formData.password=password
     const response= await fetch('http://127.0.0.1:8000/api/login', formData,{'content-type': 'multipart/form-data'})
     console.log(1)
    return response
}