function toggleAnswer(element){
    let id = element.id;
    let answer_element = document.getElementById(id+'-answer');
    let question_element = document.getElementById(id+'-question');
    let faq_element = document.getElementById(id + '-faq');
    if (element.innerHTML == '+') {
        element.innerHTML = '-';
    } else {
        element.innerHTML = '+';
    }
    answer_element.classList.toggle('active');
    question_element.classList.toggle('active');
    faq_element.classList.toggle('active');
}