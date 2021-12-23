Feature: An Employee should be able to log in to view their reimbursements, create a new reimbursement and logout

  Scenario: As an Employee I want to log into the website using my Username and Password
    Given The Employee is on the login page
    When The Employee types in their correct Username and Password into the respected fields and clicks Login Button
    Then The Employee should be redirected to their reimbursements page

  Scenario: As an Employee I want to submit a new reimbursement request to get money back
    Given The Employee is on the Reimbursement Page
    When The Employee clicks on the Create A Reimbursement Button
    When The Employee inputs their reasoning for a reimbursement and a valid claim amount and clicks Create Button
    Then The Employee gets a Reimbursement Created Alert

  Scenario: As an Employee I want to view the past reimbursement requests I created to view if they've been accepted or not
    #Given The Employee is on the Reimbursement Page
    When The Employee clicks on the Completed Reimbursements Button
    Then The Employee should have all their past reimbursement request with all the information pertaining them appear

  Scenario: As an Employee I want to log out of my account so as to protect the privacy of my reimbursement request
    #Given The Employee is on the Reimbursement Page
    When The Employee clicks on the logout Button
    Then The Employee should be redirected to the home page with their login information cleared

