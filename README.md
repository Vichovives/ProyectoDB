# ProyectoDB

____
Falta excedentes (no influye en los demas solamente se relaciona con cliente)
____

## Lo que necesitamos

### Public
* Cada usuario puede contactarnos, 

### Intranet y clientes

* Cada cliente/empresa tiene uno o más usuarios, la empresa se identifica con uuid.UUID, ademas tiene una direccion compuesta por calle, comuna, region. Como tambien razon social y nombre _("Alias")_.
* Cada usuario se identifica por su mail, con el cual ingresa al sistema en conjunto con un password.
* Cada usuario ademas tiene sus datos personales como nombre, apellido, rut, telefono.
* Cada cliente tiene la opcion de ceder una o más facturas.
* Las facturas se identifican por el numero de folio, ademas estas tienen atributos, como; rut_deudor, razon_social_deudor, fecha_emision, monto, estado_sii. _(Estas facturas solo estaran en la BD de desarrollo, ya que, luego esta info se sacara del SII)_
* Al momento de que el cliente decida solicitar la cesión de una o más facturas se creará una solicitud de cesion que se identificara con un uuid.UUID, esta entidad poseera como atributos; monto_total de todas las facturas a ceder, un estado_altus (Aceptado, Pendiente, Rechazado);
* Las facturas se identificaran por su numero de folio, y tendran como atributos, rut_deudor, razon_social_deudor, fecha_emision, monto, estado_altus, estado_sii


## Modelos ER - Modelo Relacional

### Diagrama ER (Vicho)



### Diagrama Relacional (Franco)


## Script para llenar la base de datos (compañerx Jorge, compañerx Sofii)

