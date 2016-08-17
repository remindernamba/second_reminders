Feature: Authorization

  Scenario: Authorization
    Open "authorization" page
    Fill "username" with "myusername"
    Fill "password" with "1234"
    Click "login button"
    See "Hello! Again..." in "status message"