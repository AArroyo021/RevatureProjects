const url = "http://127.0.0.1:5000/";
const currentEmployeeId = sessionStorage.getItem("currentId");
const reimbursementTable = document.getElementById("reimbursementTable");
const reimbursementTableBody = document.getElementById("reimbursementBody");
let negBool = false;

let button = document.getElementById("getReimbursement");
button.onclick = createAlertReload;

function logout(){
    sessionStorage.clear();
    window.location.href = "login_page.html";
}

async function employeeReimbursement(){
    let url_attach = "employee/reimbursement";

    let reasonInput = document.getElementById("reasonInput");
    let amountInput = document.getElementById("amountInput");
    negBool = false;

    console.log(url + url_attach);
    console.log(reasonInput.value + " " + amountInput.value);
    console.log(currentEmployeeId);

    if(amountInput.value <= 0){
        alert("Invalid amount entered");
        negBool = true;
    }
    else{
        let response = await fetch(url + url_attach, {
        headers: {'Content-Type': 'application/json'},
        method: "POST", 
        body: JSON.stringify({
            "claimNum": 500,
            "employeeId": currentEmployeeId,
            "claimAmount": amountInput.value,
            "claimReason": reasonInput.value,
            "claimStatus": "Some status",
            "managerValidation": "No",
            "managerReasoning": "Unlucky",
            "dateSent": "Tomorrow",
            "dateValidated": "Actually yesterday"
            })
        });

        if(response.status === 200){
            let info = await response.json();
            console.log(info);

            if(info === true)
                console.log("Made a new Reimbursement");

        }
        else{
            console.log("This ain't working");
        }
    }
}

function openTabs(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }

  async function showAllReimbursements(){
    let url_attach = "employee/reimbursements";

    let response = await fetch(url + url_attach, {
        headers: {'Content-Type': 'application/json'},
        method: "POST", 
        body: JSON.stringify({
            "employeeId": currentEmployeeId
        })
    });
    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        console.log(response);
        populateData(body);
    }
    else{
        alert("There was a problem trying to get reimbursement information");
    }
    
  }

  function populateData(responseBody){
    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.claimNum}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.claimAmount}</td><td>${reimbursement.claimReason}</td><td>${reimbursement.claimStatus}</td><td>${reimbursement.managerValidation}</td><td>${reimbursement.managerReasoning}</td><td>${reimbursement.dateSent}</td><td>${reimbursement.dateValidated}</td>`;
        reimbursementTableBody.appendChild(tableRow);
    }
}

function refresh(){

    setTimeout(function(){
        location.reload()
    }, 500);
  }
  
  function createAlertReload(){
    employeeReimbursement();
    if(negBool === false){
        alert("Reimbursement Created Successfully");
        refresh();
    }
    
  }

showAllReimbursements();