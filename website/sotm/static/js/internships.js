document.addEventListener('input', function (event) {

	// Only run for #wizard select
    if (event.target.id == 'position-filter' || event.target.id == 'internships-order') {
        let position = document.getElementById('position-filter').value + '_' + document.getElementById('internships-order').value;
        let position_head = document.getElementById("internship-header");
        position_head = position.split("_")[0];
        document.getElementById("internship-header").innerText = position_head;
        position_head.innerText = document.getElementById('position-filter');
        let new_active_element = document.getElementById(position + '_opportunities');
        let prev_active_element = document.getElementsByClassName("active_position")[0];
        prev_active_element.classList.remove('active_position');
        new_active_element.classList.add('active_position');
        let internship_name = document.getElementById('internship-header');
        internship_name.innerText = position_head;
    }

    
}, false);