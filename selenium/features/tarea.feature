Feature: Buscar términos en Google y validar páginas universitarias
  Como usuario
  Quiero buscar universidades y términos en Google
  Para verificar que las páginas y resultados son correctos

  Scenario Outline: Buscar universidad y término en Google
    Given I am on the Google homepage
    When I search for "<universidad>"
    And I click on the first result
    Then I should be on the "<url>"
    When I search for "<termino>" in the university page
    Then I should see results related to "<termino>"

    Examples:
      | universidad       | url                | termino    |
      | ITESO            | https://www.iteso.mx | carreras   |
      | Universidad de Guadalajara | https://www.udg.mx | carreras   |
      | Universidad Anáhuac México | https://www.anahuac.mx/mexico/ | carreras   |
