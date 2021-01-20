# Copyright 2020 Manuel Calero - Xtendoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, models


class WizStockBarcodesRead(models.AbstractModel):
    _inherit = 'wiz.stock.barcodes.read'

    def process_barcode(self, barcode):
        """ Only has been implemented AI (01, 02, 10, 37), so is possible that
        scanner reads a barcode ok but this one is not precessed.
        """
        index = barcode.find(';')
        if index == -1:
            return super().process_barcode(barcode)
        product_barcode = barcode[:index]
        lot = barcode[index+1:]

        if not product_barcode or not lot:
            return False

        product = self.env['product.product'].search(
            [('barcode', '=', product_barcode)]
        )
        if product:
            self.action_product_scanned_post(product)
        else:
            self._set_message_error('Código de barras no encontrado')
            return False

        lines = self.line_picking_ids.filtered(
            lambda l: l.product_id == self.product_id and l.product_uom_qty >= l.quantity_done + self.product_qty
        )
        if not lines:
            self._set_message_error('No hay líneas para asignar este producto')
            return False

        if not self._is_product_lot_valid(product, lot):
            return False

        self.lot_id = lot

        self.action_done()
