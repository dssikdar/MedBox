//let d = new Date();
//document.body.innerHTML = "<h1>Today's date is " + d + "</h1>"
//document.write(13);

//---------------------------------------------------------------
document.body.innerHTML = "<h1> + WELCOME TO MEDBOX + </h1>" 
document.body.innerHTML += "<h3> How can I help you? </h3>"

const button_order = document.createElement('button')
button_order.innerText = 'Order a medication'
button_order.id = 'button_order'
button_order.addEventListener('click', () => {
  //alert('Option Selected: ORDER')
  window.location.href = "order.html";
})
document.body.appendChild(button_order)
document.getElementById("button_order").style.color = "red"

const button_pickuprefill = document.createElement('button')
button_pickuprefill.innerText = 'Pick-up/Refill your medication'
button_pickuprefill.id = 'button_pickuprefill'
button_pickuprefill.addEventListener('click', () => {
  alert('Option Selected: PICK-UP/REFILL')
})
document.body.appendChild(button_pickuprefill)
document.getElementById("button_pickuprefill").style.color = "blue"




