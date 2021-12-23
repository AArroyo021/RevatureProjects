const url = "http://127.0.0.1:5000/";
const currentManagerId = sessionStorage.getItem("currentId");
// document.getElementById("pendingTab").click(); //starts the tab clicked
const reimbursementPendingTable = document.getElementById("reimbursementPendingTable");
const reimbursementPendingTableBody = document.getElementById("reimbursementPendingBody");
const reimbursementCompletedTable = document.getElementById("reimbursementCompletedTable");
const reimbursementCompletedTableBody = document.getElementById("reimbursementCompletedBody");
const statsTable = document.getElementById("statisticsTable");
const statsTableBody = document.getElementById("statisticsBody");
//ClaimNum of Reimbursement that will be updated
let currentClaimValue = "";

let updateButton = document.getElementById("updatePending");
updateButton.onclick = updateAlertReload;


function logout(){
    sessionStorage.clear();
    window.location.href = "login_page.html";
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
  let url_attach = "manager/reimbursements/info";

  let response = await fetch(url + url_attach, {
      headers: {'Content-Type': 'application/json'},
      method: "GET"
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
    //populate pending table or completed table
    if(reimbursement['claimStatus'] === null){
      let tableRow = document.createElement("tr");
      //dynamically populating table with some important data having id's and values
      tableRow.innerHTML = `<td><button id="${'claimNum' + reimbursement.claimNum}" value="${reimbursement.claimNum}" onclick="insertManagerValidation(${'claimNum' + reimbursement.claimNum})">${reimbursement.claimNum}</button></td>
                            <td>${reimbursement.employeeId}</td>
                            <td>${reimbursement.claimAmount}</td>
                            <td>${reimbursement.claimReason}</td>
                            <td id="${'claimStatus' + reimbursement.claimNum}" value="${reimbursement.claimStatus}">${reimbursement.claimStatus}</td>
                            <td id="${'managerValidation' + reimbursement.claimNum}" value="${reimbursement.managerValidation}">${reimbursement.managerValidation}</td>
                            <td id="${'managerReasoning' + reimbursement.claimNum}" value="${reimbursement.managerReasoning}">${reimbursement.managerReasoning}</td>
                            <td>${reimbursement.dateSent}</td>
                            <td>${reimbursement.dateValidated}</td>`;
      reimbursementPendingTableBody.appendChild(tableRow);
    }
  else {
      let tableRow = document.createElement("tr");
      tableRow.innerHTML = `<td id="${'claimNum' + reimbursement.claimNum}" value="${reimbursement.claimNum}">${reimbursement.claimNum}</td>
                            <td>${reimbursement.employeeId}</td>
                            <td>${reimbursement.claimAmount}</td>
                            <td>${reimbursement.claimReason}</td>
                            <td id="${'claimStatus' + reimbursement.claimNum}" value="${reimbursement.claimStatus}">${reimbursement.claimStatus}</td>
                            <td id="${'managerValidation' + reimbursement.claimNum}" value="${reimbursement.managerValidation}">${reimbursement.managerValidation}</td>
                            <td id="${'managerReasoning' + reimbursement.claimNum}" value="${reimbursement.managerReasoning}">${reimbursement.managerReasoning}</td>
                            <td>${reimbursement.dateSent}</td>
                            <td>${reimbursement.dateValidated}</td>`;
      reimbursementCompletedTableBody.appendChild(tableRow);
    }
  }  
}

async function validateReimbursements(currentCValue, statusBool, managerBool, managerRInput){
  let url_attach = "manager/reimbursements";

  let response = await fetch(url + url_attach, {
      headers: {'Content-Type': 'application/json'},
      method: "PATCH", 
      body: JSON.stringify({
          "claimNum": currentCValue,
          "claimStatus": statusBool,
          "managerValidation": managerBool,
          "managerReasoning": managerRInput
      })
  });

  if(response.status === 200){
      let info = await response.json();
      console.log(info);

  }
  else{
      console.log("This ain't working");
  }
}

function insertManagerValidation(buttonHtml){
  currentClaimValue = buttonHtml.value;
  let claimStatusTd = document.getElementById("claimStatus" + currentClaimValue);
  let managerValidationTd = document.getElementById("managerValidation" + currentClaimValue);
  let managerReasoningTd = document.getElementById("managerReasoning" + currentClaimValue);

  //Replace Tds For Inserts
  document.getElementById(claimStatusTd.id).innerHTML = `<input type="radio" id="statusARadio" name="status" value="true" checked>
                                                         <label for="statusARadio">Approve</label>
                                                         <br>
                                                         <input type="radio" id="statusRRadio" name="status" value="false">
                                                         <label for="statusRRadio">Reject</label>`;

  document.getElementById(managerValidationTd.id).innerHTML = `<input type="radio" id="managerARadio" name="managerApproval" value="true" checked>
                                                               <label for="managerARadio">Approve</label>
                                                               <br>
                                                               <input type="radio" id="managerRRadio" name="managerApproval" value="false">
                                                               <label for="managerRRadio">Reject</label>`;

  document.getElementById(managerReasoningTd.id).innerHTML = `<input type='text' id='managerRInput' placeholder='Reasoning'>`;

}

function managerInputs(){
  let radioStatus1 = document.getElementById("statusARadio");
  let radioStatus2 = document.getElementById("statusRRadio");
  let radioManager1 = document.getElementById("managerARadio");
  let radioManager2 = document.getElementById("managerRRadio");
  let managerRInput = document.getElementById("managerRInput");
  let statusBool = "";
  let managerBool = "";

  console.log(currentClaimValue);

  if(radioStatus1.checked){
    statusBool = true;
  }
  else if(radioStatus2.checked){
    statusBool = false;
  }

  if(radioManager1.checked){
    managerBool = true;
  }
  else if(radioManager2.checked){
    managerBool = false;
  }

  validateReimbursements(currentClaimValue, statusBool, managerBool, managerRInput.value);
}

async function statisticsForManagers(){
  let url_attach = "manager/reimbursements/stats";

  let response = await fetch(url + url_attach, {
      headers: {'Content-Type': 'application/json'},
      method: "GET"
  });

  if(response.status === 200){
      let info = await response.json();
      console.log(info);
      populateStatistics(info);
  }
  else{
      console.log("This ain't working");
  }
}

function populateStatistics(responseBody){
  let maxAmount = 0;
  let minAmount = 0;
  let avgAmount = 0;
  let countStats = "";
  let leastClaimsNum = 999999999;
  let mostClaimsNum = 0;
  let leastClaimsId = 0;
  let mostClaimsId = 0;

    maxAmount = responseBody.max;
    minAmount = responseBody.min;
    avgAmount = responseBody.avg;
    countStats = responseBody.count;
    // console.log(countStats);
    // console.log(countStats[1][1]);

    for(i = 0; i < countStats.length; i++){
      if(countStats[i][1] > mostClaimsNum){
        mostClaimsNum = countStats[i][1];
        mostClaimsId = countStats[i][0];
      }
      
      if(countStats[i][1] < leastClaimsNum){
        leastClaimsNum = countStats[i][1];
        leastClaimsId = countStats[i][0];
      }
    }

  let tableRow = document.createElement("tr");
  tableRow.innerHTML = `<td>${'$' + maxAmount}</td>
                        <td>${'Employee ID:' + mostClaimsId}<br>${'Number of Claims:' + mostClaimsNum}</td>
                        <td>${'$' + avgAmount}</td>
                        <td>${'Employee ID:' + leastClaimsId}<br>${'Number of Claims:' + leastClaimsNum}</td>
                        <td>${'$' + minAmount}</td>`;
  statsTableBody.appendChild(tableRow);
}

function refresh(){

  setTimeout(function(){
      location.reload()
  }, 500);
}

function updateAlertReload(){
  managerInputs();
  alert("Updated Successfully");
  refresh();
}

showAllReimbursements();
statisticsForManagers();