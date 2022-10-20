
// Dashboard Header Script






//SideBar Script
// show side bar in mobile view
const showSideBar = document.getElementById('show-sidebar');
const sideBar = document.querySelector('.aside');
const closeAside = document.querySelector('.close');

showSideBar.addEventListener('click',function(e){
sideBar.classList.toggle('show-aside');
closeAside.classList.toggle('close-aside');

})

closeAside.addEventListener('click',function(e){
closeAside.classList.toggle('close-aside');
sideBar.classList.remove('show-aside');
})





//Security Sections Script
const profileWrapper = document.querySelectorAll(".profile-wrapper");
// console.log(profileWrapper)

for(let prop of profileWrapper){
prop.addEventListener("click",function(e){
const hiddenSecuritySection = document.querySelectorAll(".security-section");
const verificationSection = document.querySelectorAll(".verification-section");

hiddenSecuritySection.forEach(hiddenItem =>{
(e.target.id === hiddenItem.id) ? hiddenItem.classList.add("active-security") :hiddenItem.classList.remove("active-security");
})

verificationSection.forEach(hiddenItem =>{
(e.target.id === hiddenItem.id) ? hiddenItem.classList.add("active-verification") :hiddenItem.classList.remove("active-verification");
})

})

}




// Verification Section Script || show password when eye-check is toggled
const eyeCheckIcon  = document.querySelectorAll(".eye-check-icon");
for(let eyeIcon of eyeCheckIcon){
// console.log(eyeIcon)
eyeIcon.addEventListener('click',function(e){
const enteredPassword = document.querySelectorAll('.password');
enteredPassword.forEach(password => {
console.log(password)
let a = false;
if(password.value == ""){
a = true;
}
a ? password.type = 'password' : password.type = 'text';
})
})
}
