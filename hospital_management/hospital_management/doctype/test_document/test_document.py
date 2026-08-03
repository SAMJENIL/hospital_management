from frappe.model.document import Document


class TestDocument(Document):

    def before_save(self):
        if not self.description:
            self.description = "Default Description"