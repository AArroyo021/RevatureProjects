Feature: A Manager should be able to log in to view the reimbursements of all Employees

  Scenario: As a Manager I want to log into the website using my Username and Password
    Given The Manager is on the login page
    When The Manager types in their correct Username and Password into the respected fields, selects Manager from the RadioButton options and then clicks Login Button
    Then The Manager should be redirected to their reimbursement viewer page

  Scenario: As a Manager I want to Approve a reimbursement request because it seems valid
    Given The Manager is on the reimbursement page
    When The Manager clicks on the Pending Button
    When The Manager clicks on the Claim Number Button
    When The Manager inputs Approve RadioButton for ClaimStatus and Manager Validation, and inputs their Manager Reasoning and proceeds to click the Update Button
    Then The Manager gets a Updated Successfully Alert and the page reloads

    Scenario: As a Manager I want to Deny a reimbursement request because it seems sketchy
    #Given The Manager is on the reimbursement page
    When The Manager clicks on the Pending Button
    When The Manager clicks on the Claim Number Button
    When The Manager inputs Deny RadioButton for ClaimStatus and Manager Validation, and inputs their Manager Reasoning and proceeds to click the Update Button
    Then The Manager gets a Updated Successfully Alert and the page reloads

  Scenario: As a Manager I want to view past reimbursements that have been Denied or Approved to check previous decisions
    #Given The Manager is on the reimbursement page
    When The Manager clicks on the Completed Button
    Then The Manager should have all the past reimbursement request decisions made with a Time stamp of the date Approved/Denied

  Scenario: As a Manager I should be able to view reimbursement statistics to better understand Employee activities
    #Given The Manager is on the reimbursement page
    When The Manager clicks on the Statistics Button
    Then The Manager should have access to the statistics involving employee reimbursements

  Scenario: As a Manager I want to log out of my account so as to protect the privacy of the reimbursement information I can view and manage
    #Given The Manager is on the Reimbursement Page
    When The Manager clicks on the logout Button
    Then The Manager should be redirected to the home page with their login information cleared
