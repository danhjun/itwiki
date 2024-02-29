function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toggleSubtopicStatus(subtopicId, isChecked) {
    const csrftoken = getCookie('csrftoken');
    fetch(`/wiki/subtopics/${subtopicId}/update_status/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ status: isChecked }),
    })
    .then(response => response.json())
    .then(data => {
        // Select the parent <li> element of the checkbox to update its class
        const listItem = document.querySelector(`#subtopic-${subtopicId}`);
        const span = listItem.querySelector('span'); // Assuming the span is directly inside the <li>
        if (data.status) {
            span.classList.add('text-success');
        } else {
            span.classList.remove('text-success');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
