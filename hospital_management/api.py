import frappe
from frappe.query_builder import DocType


@frappe.whitelist()
def appointment_api_demo():
    # Define DocTypes
    Patient = DocType("patient")
    Appointment = DocType("Hospital Appointment")

    # -------------------------------
    # Query Builder
    # Join Hospital Appointment with Patient
    # -------------------------------
    results = (
        frappe.qb.from_(Appointment)
        .join(Patient)
        .on(Appointment.patient == Patient.name)
        .select(
            Appointment.name,
            Appointment.appointment_id,
            Appointment.status,
            Patient.patient_id,
            Patient.last_name
        )
        .limit(5)
        .run(as_dict=True)
    )

    # -------------------------------
    # Document API
    # Fetch one record, update it, and save
    # -------------------------------
    if results:
        appointment = frappe.get_doc(
            "Hospital Appointment",
            results[0]["name"]
        )

        # Valid value from your Select field
        appointment.status = "completed"
        appointment.save()

    # -------------------------------
    # Database API
    # Bulk update all queried records
    # -------------------------------
    for row in results:
        frappe.db.set_value(
            "Hospital Appointment",
            row["name"],
            "status",
            "completed",
            update_modified=False
        )

    return {
        "message": "API executed successfully",
        "count": len(results),
        "data": results
    }
