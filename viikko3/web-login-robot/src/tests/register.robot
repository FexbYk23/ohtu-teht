*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Delete Accounts And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
	Set Username  kalle
	Set Password  kalle123
	Set Password Confirmation  kalle123
        Click Button  Register
	Welcome Page Should Be Open

Register With Too Short Username And Valid Password
	Set Username  a
	Set Password  kalle123
	Set Password Confirmation  kalle123
	Click Button  Register
	Page Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
	Set Username  kalle
	Set Password  k
	Set Password Confirmation  k
        Click Button  Register
	Page Should Contain  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
	Set Username  kalle
	Set Password  kalle123
	Set Password Confirmation  kalle134
        Click Button  Register
	Page Should Contain  Password and confirmation don't match




*** Keywords ***
Set Username
	[Arguments]  ${username}
	Input Text  username  ${username}

Set Password
	[Arguments]  ${password}
	Input Password  password  ${password}

Set Password Confirmation
	[Arguments]  ${password}
	Input Password  password_confirmation  ${password}

Delete Accounts And Go To Register Page
	Reset Application
	Go To Register Page

