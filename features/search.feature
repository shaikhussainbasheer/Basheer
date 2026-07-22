Feature: Search Functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to Home Page
    When I enter valid product say "HP" into the search box field
    And I click on search button
    Then Valid product should get displayed in search results

  @search1818
  Scenario: Search for an invalid product
    Given I got navigated to Home Page
    When I enter invalid product say "Honda" into the search box field
    And I click on search button
    Then Proper message should be displayed in search results

  @search
  Scenario: Search without entering any  product
    Given I got navigated to Home Page
    When I dont enter anything into the search box field
    And I click on search button
    Then Proper message should be displayed in search results