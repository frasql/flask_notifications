from models.alert import Alert
from apputils.utils import send_mail


alerts = Alert.all()


for alert in alerts:
    if alert.notify_if_time_elapsed():
        print(alert)
    else:
      pass
    """
    html_content = f"
    <div>
      <h1>Attenzione, notifica {notification.name}</h1>
      <section>
        <h3> Ciao {notification.user_email}</h3>
        <h4> {notification.note.title} </h4>
        <h5> {notification.note.description}</h5>
      </section>
    </div>
    "
    send_mail(
        text="Alert Notification", 
        subject=f"{notification.name}",
        from_email="server address",
        to_emails=[f"{notification.user_email}"],
        html=html_content
        )
    """

if not alerts:
    print("No alert stored")