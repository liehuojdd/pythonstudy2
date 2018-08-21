Feature: Apple site test
  some test for apple site

  Scenario: search keyword
    Given open support page
    When enter keyword "apple id"
    Then result search out
  
  Scenario: register an account
    Given open register page
    When fill the nessary register information
    Then register successful
