Feature: agregar productos al carrito

  Scenario: Agregar dos productos al carrito correctamente
  Given el usuario navega a la página pagina https://www.demoblaze.com/
    When el usuario selecciona "INICIAR_SESION"
      And el usuario ingresa "JoseH" en el campo "USERNAME"
      And el usuario ingresa "Test1234*" en el campo "PASSWORD"
      And el usuario selecciona "BOTON_LOGIN"
    Then el usuario debería ver su nombre de usuario en el menú
    When el usuario selecciona "PRODUCTO1"
      And el usuario agrega el producto al "CARRITO"
      And el usuario acepta el popup de confirmación
      And el usuario selecciona "HOME_CATALOGO"
      And el usuario selecciona "PRODUCTO2"
      And el usuario agrega el producto al "CARRITO"
      And el usuario acepta el popup de confirmación
    When el usuario visualiza los productos en el "CARRITO_COMPRAS"
      And el usuario selecciona "REALIZAR_PEDIDO"
      And el usuario diligencia "Jose" en el campo "NAME"
      And el usuario diligencia "Colombia" en el campo "COUNTRY"
      And el usuario diligencia "Bogota" en el campo "CITY"
      And el usuario diligencia "10992422220" en el campo "CREDIT_CARD"
      And el usuario diligencia "OCT" en el campo "MONTH"
      And el usuario diligencia "2028" en el campo "YEAR"
    Then el usuario selecciona "COMPRAR"











