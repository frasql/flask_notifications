document.addEventListener('DOMContentLoaded', init);


function init() {
    // Modal insert patient
    const edit_alert_buttons = document.querySelectorAll('.edit_alert_buttons');
    if(edit_alert_buttons) {
        edit_alert_buttons.forEach((button) => {
            const modal_edit_alert = document.querySelector('#modal_edit_alert_'+button.id);
            button.addEventListener('click', () => {
                modal_edit_alert.classList.add('is-active');
            })  
        })
    }
    
    // close update modal
    const close_edit_alert_buttons = document.querySelectorAll('.close_edit_alert_buttons');
    
    if(close_edit_alert_buttons) {
        close_edit_alert_buttons.forEach((button) => {
            const modal_edit_alert = document.querySelector('#modal_edit_alert_'+button.id);
            button.addEventListener('click', () => {
                modal_edit_alert.classList.remove('is-active');
            })
        })
    }
}