*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User  test  12345678

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User  testi  12345678
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User  test  salasana1
    Output Should Contain  User with username test already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  a  12345678
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input New Command And Create User  testi  salass1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  testi  salasana
    Output Should Contain  Password must not consist of only characters a-z

