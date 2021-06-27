const form = document.getElementById("register-form")
const nameElement = document.getElementById('nameElement');
const lastname = document.getElementById('lastname');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirmpassword = document.getElementById('confirmpassword');

const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const registrations = [];

form.addEventListener("submit", event => {
  event.preventDefault()
  const formData = new FormData(form)
  const data = {}
  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    data[key] = value
    checkInputs(data);
    /* USER CODE Begin: Validate data */
  }
  if ([nameElement, lastname, username, email, password, confirmpassword].every(el => el.className == 'form-control success')) {
    // if everything is correct, then do the actual submission
    // (in this case we will put the data into an array and alert the user)
    registrations.push(data);
    console.log(registrations);
    alert('Registration completed!');
  }
  /* USER CODE Begin: What happened next after recieve form data (Optional) */

  /* USER CODE END: What happened next after recieve form data (Optional) */
})

const checkInputs = (data) => {
  const nameValue = data['name']
  const lastnameValue = data['lastname']
  const usernameValue = data['username']
  const emailValue = data['email']
  const passwordValue = data['password']
  const confirmpasswordValue = data['confirmpassword']
  if (nameValue == '') {
    displayError(nameElement, 'Name cannot be blank');
  } else {
    displaySuccess(nameElement);
  }
  if (lastnameValue == '') {
    displayError(lastname, 'Lastname cannot be blank');
  } else {
    displaySuccess(lastname);
  }
  if (usernameValue == '') {
    displayError(username, 'Username cannot be blank');
  } else {
    displaySuccess(username);
  }
  if (emailValue == '') {
    displayError(email, 'Email cannot be blank');
  } else if (!emailRegex.test(emailValue)) {
    displayError(email, 'Please enter a valid email');
  } else {
    displaySuccess(email);
  }
  if (passwordValue == '') {
    displayError(password, 'Password cannot be blank');
  } else {
    displaySuccess(password);
  }
  if (confirmpasswordValue == '') {
    displayError(confirmpassword, 'Password cannot be blank');
  } else if (confirmpasswordValue != passwordValue) {
    displayError(confirmpassword, 'Passwords do not match');
  } else {
    displaySuccess(confirmpassword);
  }
}

// create functions to change class and display error or success on specific elements
const displayError = (element, message) => {
  element.className = 'form-control error';
  const m = element.parentElement.querySelector('p');
  m.innerText = message;
}

const displaySuccess = (element) => {
  element.className = 'form-control success';
  const m = element.parentElement.querySelector('p');
  m.innerText = '';
}

// when the user inputs data, change the input styling back to normal
const inputFields = document.querySelectorAll('input');
for (let i = 0; i < inputFields.length; i++) {
  inputFields[i].addEventListener('input', () => {
    inputFields[i].className = 'form-control'
    const m = inputFields[i].parentElement.querySelector('p');
    m.innerText = '';
  })
}