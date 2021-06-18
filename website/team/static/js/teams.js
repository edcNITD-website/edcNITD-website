function showAlumni(element){
    console.log(element.innerText);
    var year = element.innerText;
    var prev_batch = document.getElementsByClassName('batch-visible');
    prev_batch[0].classList.remove('batch-visible');
    var batch_holder = document.getElementById(year);
    batch_holder.classList.add('batch-visible')
    }