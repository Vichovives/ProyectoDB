# ProyectoDB

## LO QUE FALTA

Falta excedentes (no influye en lo demás, solamente se relaciona con cliente)

## Lo que necesitamos

### Public
* Cada usuario puede contactarnos, 

### Intranet y clientes

* Cada cliente/empresa tiene uno o más usuarios. La empresa se identifica con uuid.UUID, además tiene una dirección compuesta por calle, comuna y región. Como también razón social y nombre _("Alias")_.
* Cada usuario se identifica por su mail, con el cual ingresa al sistema en conjunto con un password.
* Cada usuario además tiene sus datos personales como nombre, apellido, rut y teléfono.
* Cada cliente tiene la opción de ceder una o más facturas.
* Las facturas se identifican por el número de folio. Además estas tienen atributos, como; rut_deudor, razon_social_deudor, fecha_emision, monto, estado_sii. _(Estas facturas sólo estarán en la BD de desarrollo, ya que, luego esta información se sacará del SII)_.
* Al momento de que el cliente decida solicitar la cesión de una o más facturas se creará una solicitud de cesión que se identificará con un uuid.UUID, esta entidad poseerá como atributos; monto_total de todas las facturas a ceder, un estado_altus (Aceptado, Pendiente, Rechazado);
* Las facturas se identificarán por su número de folio, y tendrán como atributos, rut_deudor, razon_social_deudor, fecha_emision, monto, estado_altus, estado_sii. 
* Cada cliente tiene un registro de operaciones, identificado por el ID del cliente y tiene como atributos cantidad de facturas, gasto operacional, gasto administrativo, monto, interes, mora, fecha curse, fecha vencimiento, fecha pago.
* Cada operación está asociada a un sólo cliente.

## Modelos ER - Modelo Relacional

### Diagrama Entidad-Relación (Vicho)

https://drive.google.com/drive/folders/1iw1QHyWRkIm11ruTLsB1kbqHd0ijWvnp?usp=sharing 

### Modelo Relacional (Franco)


## Script para llenar la base de datos (compañerx Jorge, compañerx Sofii)

1. Operacion: 

2. 
