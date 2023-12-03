```go
type Factura struct {
	Factura_rut_receptor  string    `gorm:"type:varchar(20);not null" json:"factura_rut_receptor"`
	Factura_razon_social  string    `gorm:"type:varchar(120);not null" json:"factura_razon_social"`
	Factura_folio         int       `gorm:"primaryKey;unique;type:integer;not null" json:"factura_folio"`
	Factura_fecha_emision time.Time `gorm:"not null" json:"factura_fecha_emision"`
	Factura_monto         int       `gorm:"type:bigint;not null" json:"factura_monto"`
	Factura_estado_sii    string    `gorm:"type:varchar(40);not null" json:"factura_estado_sii"`
}
```

```go
type Cobranza struct {
	Cobranza_deudor               string    `gorm:"type:varchar(120);not null" json:"cobranza_deudor"`
	Cobranza_numero_operacion     int       `gorm:"type:integer;not null" json:"cobranza_numero_operacion"`
	Cobranza_fecha_curse          time.Time `gorm:"not null" json:"cobranza_fecha_curse"`
	Cobranza_numero_dcto          int       `gorm:"primaryKey;unique;type:integer;not null" json:"cobranza_numero_dcto"`
	Cobranza_fecha_emision        time.Time `gorm:"not null" json:"cobranza_fecha_emision"`
	Cobranza_vencimiento_original time.Time `gorm:"not null" json:"cobranza_vencimiento_original"`
	Cobranza_vencimiento          time.Time `gorm:"not null" json:"cobranza_numero_vencimiento"`
	Cobranza_estado_dcto          string    `gorm:"type:varchar(40);not null" json:"cobranza_estado_dcto"`
	Cobranza_numero_dias          int       `gorm:"type:smallint;not null" json:"cobranza_numero_dias"`
	Cobranza_valor_dcto           int       `gorm:"type:bigint;not null" json:"cobranza_valor_dcto"`
	Cobranza_valor_anticipo       int       `gorm:"type:bigint;not null" json:"cobranza_valor_anticipo"`
	Cobranza_saldo_dcto           int       `gorm:"type:bigint;not null" json:"cobranza_saldo_dcto"`
	Cobranza_estado_cobranza      string    `gorm:"type:varchar(40);default:'Dcto Nuevo'" json:"cobranza_estado_cobranza"`
	Cobranza_proximo_llamado      time.Time `json:"cobranza_proximo_llamado"`
	Cobranza_fecha_pago           time.Time `json:"cobranza_fecha_pago"`
	Cobranza_ultima_gestion       time.Time `json:"cobranza_ultima_gestion"`
	//FK
	Cobranza_evento_fk []Cobranza_evento `gorm:"foreignKey:Cobranza_evento_dcto"`
}
```

```go
type Cobranza_evento struct {
	Cobranza_evento_dcto        int       `json:"cobranza_id"`
	Cobranza_evento_estado      string    `gorm:"type:varchar(30);not null" json:"cobranza_evento_estado"`
	Cobranza_evento_fecha_pago  time.Time `json:"cobranza_evento_fecha_pago"`
	Cobranza_evento_observacion string    `gorm:"type:varchar(200)" json:"cobranza_evento_observacion"`
}
```

```go
type Excedente_por_liquidar struct {
	Excedente_por_liquidar_deudor             string    `gorm:"type:varchar(120)" json:"excedente_por_liquidar_deudor"`
	Excedente_por_liquidar_numero_dcto        int       `gorm:"primaryKey;unique;not null;type:integer" json:"excedente_por_liquidar_numero_dcto"`
	Excedente_por_liquidar_valor_dcto         int       `gorm:"type:bigint" json:"excedente_por_liquidar_valor_dcto"`
	Excedente_por_liquidar_valor_cancelado    int       `gorm:"type:bigint" json:"excedente_por_liquidar_valor_cancelado"`
	Excedente_por_liquidar_fecha_vencimiento  time.Time `json:"excedente_por_liquidar_fecha_vencimiento"`
	Excedente_por_liquidar_fecha_pago         time.Time `json:"excedente_por_liquidar_fecha_pago"`
	Excedente_por_liquidar_excedente          int       `gorm:"type:bigint" json:"excedente_por_liquidar_excedente"`
	Excedente_por_liquidar_diferencia_precio  int       `gorm:"type:bigint" json:"excedente_por_liquidar_diferencia_precio"`
	Excedente_por_liquidar_gasto              int       `gorm:"type:bigint" json:"excedente_por_liquidar_gasto"`
	Excedente_por_liquidar_devolucion_cliente int       `gorm:"type:bigint" json:"excedente_por_liquidar_devolucion_cliente"`
}
```

```go
type Excedente_por_pagar struct {
	Excedente_por_pagar_deudor              string    `gorm:"type:varchar(120)" json:"excedente_por_pagar_deudor"`
	Excedente_por_pagar_numero_dcto         int       `gorm:"primaryKey;unique;not null;type:integer" json:"excedente_por_pagar_numero_dcto"`
	Excedente_por_pagar_fecha_vencimiento   time.Time `json:"excedente_por_pagar_fecha_vencimiento"`
	Excedente_por_pagar_valor_dcto          int       `gorm:"type:bigint" json:"excedente_por_pagar_valor_dcto"`
	Excedente_por_pagar_intereses_mora      int       `gorm:"type:bigint" json:"excedente_por_pagar_intereses_mora"`
	Excedente_por_pagar_gastos              int       `gorm:"type:bigint" json:"excedente_por_pagar_gastos"`
	Excedente_por_pagar_saldo_x_pagar       int       `gorm:"type:bigint" json:"excedente_por_pagar_saldo_x_pagar"`
	Excedente_por_pagar_porcentaje_anticipo float32   `gorm:"type:real" json:"excedente_por_pagar_porcentaje_anticipo"`
	Excedente_por_pagar_monto_anticipo      int       `gorm:"type:bigint" json:"excedente_por_pagar_monto_anticipo"`
}
```

```go
type Operacion struct {
	Operacion_cliente              int       `gorm:"type:smallint"`
	Operacion_cantidad_facturas    int       `gorm:"type:smallint;not null" json:"operacion_cantidad_facturas"`
	Operacion_gasto_operacional    int       `gorm:"type:bigint;not null" json:"operacion_gasto_operacional"`
	Operacion_gasto_administrativo int       `gorm:"type:bigint;not null" json:"operacion_gasto_administrativo"`
	Operacion_monto                int       `gorm:"type:bigint;not null" json:"operacion_monto"`
	Operacion_interes              float32   `gorm:"type:real;not null" json:"operacion_interes"`
	Operacion_mora                 int       `gorm:"type:bigint;not null" json:"operacion_mora"`
	Operacion_fecha_curse          time.Time `gorm:"type:timestamp;not null" json:"operacion_fecha_curse"`
	Operacion_fecha_vencimiento    time.Time `gorm:"type:timestamp;not null" json:"operacion_fecha_vencimiento"`
	Operacion_fecha_pago           time.Time `gorm:"type:timestamp" json:"operacion_fecha_pago,omitempty"`
}
```

Crear dataset en csv de nombres de personas (nombre y apellido); crear empresas (rut y su razon social);
