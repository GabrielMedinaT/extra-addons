# Importa las clases necesarias de Odoo
from odoo import models, fields, api
import base64  # Para la codificación de archivos en base64
###################SUCURSALES#############################
# Modelo para gestionar sucursales
class SucursalesSucursales(models.Model):
    _name = "sucursales.sucursales"  # Nombre técnico del modelo
    _description = "Sucursales"  # Descripción del modelo

    # Campos de la sucursal
    name = fields.Char(string="Número de sucursal", required=True)  # Nombre de la sucursal
    encargado = fields.Many2one('hr.employee', string="Encargado", required=True)  # Relación con empleados

    # Relación con otros modelos
    empleados = fields.One2many('hr.employee', 'sucursal_id', string="Empleados")  # Empleados de la sucursal
    cajeros = fields.One2many('sucursales.cajeros', 'sucursal_id', string="Cajeros")  # Cajeros de la sucursal

    # Campo computado para contar el número de cajeros en la sucursal
    num_caj = fields.Integer(string="Número de cajeros", compute="_compute_num_caj", store=True)

    @api.depends('cajeros')
    def _compute_num_caj(self):
        """ Calcula el número de cajeros en la sucursal """
        for record in self:
            record.num_caj = len(record.cajeros)  # Cuenta el número de cajeros
############CAJERO################
# Modelo para gestionar cajeros automáticos dentro de las sucursales
class SucursalesCajeros(models.Model):
    _name = "sucursales.cajeros"
    _description = "Cajeros de sucursales"

    # Campos de los cajeros
    name = fields.Char(string="Código de cajero", required=True)  # Identificador del cajero
    direccion = fields.Char(string="Dirección")  # Ubicación del cajero

    # Estado del cajero
    estado = fields.Selection(
        [
            ('operativo', 'Operativo'),
            ('pendiente', 'Pendiente actualización'),
            ('inhabilitado', 'Inhabilitado'),
            ('averiado', 'Pendiente de reparación')
        ],
        string="Estado",
        default='operativo'  # Estado por defecto
    )

    # Relación con sucursales y reparaciones
    sucursal_id = fields.Many2one(#Relación con sucursales
        "sucursales.sucursales", string="Sucursal", ondelete="cascade"#Si se elimina la sucursal se eliminan los cajeros por eso delete cascade
    )
    rep_id = fields.Many2one(#Relación con reparaciones
        "sucursales.reparaciones", string="Reparador", ondelete="cascade"#Si se elimina la reparación se eliminan los cajeros por eso delete cascade
    )

    # Campo computado para mostrar si se debe mostrar el reparador
    mostrar_reparador = fields.Boolean(
        string="Mostrar Reparador",
        compute="_compute_mostrar_reparador",
        store=False  # No se almacena en la base de datos
    )

    @api.depends()
    def _compute_mostrar_reparador(self):
        """ Determina si se debe mostrar el campo de reparador según la configuración """
        param = self.env['ir.config_parameter'].sudo().get_param('sucursales.mostrar_historial_averias', default=False)
        for record in self:
            record.mostrar_reparador = param == 'True'  # Se muestra solo si el parámetro está activado

# Modelo para gestionar reparaciones en las sucursales
class SucursalesReparaciones(models.Model):
    _name = "sucursales.reparaciones"
    _description = "Reparaciones en sucursales"

    # Campos de la reparación
    name = fields.Char(string="Código de reparación", required=True)  # Identificador de la reparación
    fecha = fields.Date(string="Fecha de reparación")  # Fecha en la que se realizó la reparación
    descripcion = fields.Text(string="Descripción")  # Descripción de la reparación
    empleado = fields.Many2one('hr.employee', string="Empleado Responsable")  # Empleado responsable de la reparación
    cliente = fields.Many2one('res.partner', string="Cliente")  # Cliente asociado a la reparación

    # Firma digital
    digital_signature = fields.Binary(string="Firma Digital")  # Campo para almacenar la firma digital
    cajeros = fields.One2many('sucursales.cajeros', 'rep_id', string="Cajeros")  # Cajeros asociados a la reparación

    # Campo computado para determinar si se debe mostrar la firma digital
    mostrar_firma = fields.Boolean(
        string="Mostrar Firma",
        compute="_compute_mostrar_firma",
        store=False
    )

    def get_base64_signature(self):
        """ Convierte la firma digital a formato base64 para su almacenamiento o transmisión """
        return base64.b64encode(self.digital_signature).decode('utf-8') if self.digital_signature else ''

    @api.depends('digital_signature')
    def _compute_mostrar_firma(self):
        """ Determina si se debe mostrar la firma digital según la configuración """
        firma_type = self.env['ir.config_parameter'].sudo().get_param('sucursales_reparaciones.firma_type', 'con_firma')
        for record in self:
            record.mostrar_firma = firma_type == 'con_firma'  # Se muestra si la configuración lo permite

# Configuración de parámetros del módulo en la interfaz de administración
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'  # Hereda de la configuración de Odoo
    
    firma_type = fields.Selection(
        [('con_firma', 'Firmar'), ('sin_firma', 'No Firmar')],
        string="Firmar por las averías",
        config_parameter='sucursales_reparaciones.firma_type',  # Configuración global en el sistema
    )

    mostrar_reparador = fields.Boolean(
        string="Mostrar Reparador en Cajeros",
        config_parameter="sucursales.mostrar_historial_averias",  # Configuración global
    )

# Extensión del modelo res.partner (contactos) para incluir la relación con reparaciones
class ResPartner(models.Model):
    _inherit = 'res.partner'

    reparaciones = fields.One2many('sucursales.reparaciones', 'cliente', string="Reparaciones")  # Relación con reparaciones

# Extensión del modelo hr.employee (empleados) para asociarlos a sucursales
class HrEmployee(models.Model):
    _inherit = "hr.employee"

    sucursal_id = fields.Many2one(
        "sucursales.sucursales", string="Sucursal", ondelete="set null"
    )  # Relación del empleado con una sucursal

# Extensión del modelo de sucursales para incluir la firma digital
class sucursales_firma(models.Model):
    _inherit = "sucursales.sucursales"

    digital_signature = fields.Binary(string="Signature")  # Firma digital para las sucursales
