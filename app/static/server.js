// get the input and button elements by their ids
const serverNameInput = document.getElementById('server_name');
const createServerButton = document.getElementById('server-create-button');
const feedbackMessage = document.getElementById('feedback-message');

// set a flag to check if the user is still typing
let typingTimeout = null;

// function to disable the create button
function setCreateButtonDisabled(boolean) {
  createServerButton.disabled = boolean;
}


// function to show feedback message
function showFeedbackMessage(i) {
  if (i === 1){
    // input is valid, show green border and "Input is Valid" text
    feedbackMessage.textContent = 'You can use this server name!';
    feedbackMessage.classList.add('text-green-600');
    feedbackMessage.classList.remove('text-red-600');
  }
  else if (i === 2) {
    // input is not valid, show red border and "Input is not Valid" text
    feedbackMessage.textContent = 'Server name already exists';
    feedbackMessage.classList.add('text-red-600');
    feedbackMessage.classList.remove('text-green-600');
  }
  else if (i === 3) {
    // input is not valid, show red border and "Input is not Valid" text
    feedbackMessage.textContent = 'Server name is invalid';
    feedbackMessage.classList.add('text-red-600');
    feedbackMessage.classList.remove('text-green-600');
  }
}
function showServerNameExistMessage(){
    // input is not valid, show red border and "Input is not Valid" text
    feedbackMessage.textContent = 'Server name already exists';
    feedbackMessage.classList.add('text-red-600');
    feedbackMessage.classList.remove('text-green-600');
  }
function isUrlSafe(str) {
  console.log(str)
  var regex = /^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$/;;
  return regex.test(str);
}
// function to check if the input is valid
function validateInput() {
  const inputValue = serverNameInput.value.trim();
  let server_name = 'gb-' + inputValue
  fetch('/api/v1/server/' + server_name , { method: 'GET'})
  .then(response => response.json())
  .then(data => {
        if (data.server_name == null) { // 사용할 수 있는 이름이면
          showFeedbackMessage(1)
          setCreateButtonDisabled(false)
        }
        else{
          showFeedbackMessage(2)
          setCreateButtonDisabled(true)
        }
        
    }
  )
}

// add an event listener to the input box
serverNameInput.addEventListener('input', () => {
  // disable the create button
  setCreateButtonDisabled(true);

  // clear the typing timeout if it's already set
  if (typingTimeout) {
    clearTimeout(typingTimeout);
  }

  // set a new typing timeout to call the validation function after the user has stopped typing
  typingTimeout = setTimeout(() => {
    if (isUrlSafe(serverNameInput.value.trim())){
      validateInput();
    }
    else{
      showFeedbackMessage(3);
      setCreateButtonDisabled(true);
    }
    
  }, 1000); // adjust the timeout value as needed
});


function updateStatus(server_name) {
    let statusElement = document.getElementById("status-" + server_name);
    let deleteButton = document.getElementById("delete-" + server_name)
    let intervalId = setInterval(function() {
    fetch('/api/v1/server/' + server_name + '/status')
        .then(response => response.json())
        .then(data => {
        let status = data.status;
        
        statusElement.innerHTML = status;

        if (status === 'Running') {
            clearInterval(intervalId);
            if (deleteButton != null) {
              deleteButton.disabled = false;
            }
        }
        else if (status === 'Deleted'){
            clearInterval(intervalId);
            fetch('/api/v1/server/' + server_name, { method: 'DELETE' })
        }
        });
    }, 1000);
}


function deleteServer(btn){
    var server_name = btn.getAttribute("delete-button-for");
    btn.disabled = true
    fetch('/api/v1/server/' + server_name + '/kube', { method: 'DELETE' } )
    .then(updateStatus(server_name))
}