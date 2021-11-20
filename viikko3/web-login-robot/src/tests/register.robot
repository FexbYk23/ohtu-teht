*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Delete Accounts And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
	Register As  kalle  kalle123  kalle123
	Welcome Page Should Be Open

Register With Too Short Username And Valid Password
	Register As  a  kalle123  kalle123
	Page Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
	Register As  kalle  k  k
	Page Should Contain  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
	Register As  kalle  kalle123  kalle143
	Page Should Contain  Password and confirmation don't match

Login After Successful Registration
	Register As  kalle  kalle123  kalle123
	Go To Login Page
	Login As  kalle  kalle123
	Login Should Succeed

Login After Failed Registration
	Register As  kalle  k  k
	Go To Login Page
	Login As  kalle  k
	Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Password Confirmation
	[Arguments]  ${password}
	Input Password  password_confirmation  ${password}

Delete Accounts And Go To Register Page
	Reset Application
	Go To Register Page

Register As
	[Arguments]  ${user}  ${pass}  ${confirm}
	Set Username  ${user}
	Set Password  ${pass}
	Set Password Confirmation  ${confirm}
        Click Button  Register

Login As
	[Arguments]  ${user}  ${pass}
	Set Username  ${user}
	Set Password  ${pass}
	Click Button  Login

