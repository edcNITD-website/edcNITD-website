function showAlumni(element){
    var year = element.innerText;
    var prev_batch = document.getElementsByClassName('batch-visible');
    prev_batch[0].classList.remove('batch-visible');
    var batch_holder = document.getElementById(year);
    batch_holder.classList.add('batch-visible');
    var prev_year_btn = document.getElementsByClassName('active_year');
    prev_year_btn[0].classList.remove('active_year');
    var current_year_btn = document.getElementById(year+'-year');
    current_year_btn.classList.add('active_year');
    }