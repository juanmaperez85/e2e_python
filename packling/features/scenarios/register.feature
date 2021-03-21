Feature: Register

  Scenario: Checking the Register Page at Packlink
    When I go to "Register Page"

    Then the "email" element is displayed in "Register Page"
    And I should see the text "Introduce un correo" in the container "label_email" of the page "Register Page"

    And the "password" element is displayed in "Register Page"
    And I should see the text "Elige tu contraseña" in the container "label_password" of the page "Register Page"

    And the "shipment" element is displayed in "Register Page"
    And I should see the text "Envíos al mes" in the container "label_shipment" of the page "Register Page"

    And the "webshop" element is displayed in "Register Page"
    And I should see the text "Plataforma Webshop" in the container "label_webshop" of the page "Register Page"

    And the "marketplace" element is displayed in "Register Page"
    And I should see the text "Marketplace principal" in the container "label_marketplace" of the page "Register Page"

    And the "telephone" element is displayed in "Register Page"
    And I should see the text "Número de teléfono" in the container "label_phone" of the page "Register Page"

    And the "privacy_link" element is displayed in "Register Page"
    And the "register_button" element is displayed in "Register Page"


  Scenario: Log in for a registered user
    Given log in with the configured user
    When I go to "Dashboard Page"
    Then I should see the text "!Te damos la bienvenida a Packlink Pro" in the container "welcome_text" of the page "Dashboard Page"
