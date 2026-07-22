Feature: Login Functionality

  @login18
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I Enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                          |password    |
      |amotoorisampleone@gmail.com    |secondone   |
      |amotoorisampletwo@gmail.com    |secondtwo   |
      |amotoorisamplethree@gmail.com  |secondthree |


  @login
  Scenario:  Login with invalid email and valid password
    Given I navigated to login page
    When I Enter invalid email address and valid password say "1818" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario:  Login with valid email and invalid password
    Given I navigated to login page
    When I Enter valid email address say "Virat1881@gmail.com" and invalid password say "181818" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario:  Login with invalid credentials
    Given I navigated to login page
    When I Enter invalid email address and invalid password say "18181818" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario:  Login without entering any credentials
    Given I navigated to login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message

