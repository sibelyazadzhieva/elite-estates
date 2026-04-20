from celery import shared_task
import logging
import time

logger = logging.getLogger(__name__)


@shared_task
def send_appointment_confirmation_email(appointment_id):
    logger.info(f"Starting email dispatch for appointment ID: {appointment_id}...")

    time.sleep(3)

    logger.info(f"Successfully sent confirmation email for appointment {appointment_id}.")

    return f"Email sent for Appointment {appointment_id}"