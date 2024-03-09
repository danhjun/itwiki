document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.subtopic-item input[type="checkbox"]').forEach(function(checkbox) {
        const isChecked = checkbox.checked;
        const subtopicItem = checkbox.closest('.subtopic-item');
        const codeElement = subtopicItem.querySelector('.subtopic-code');
        const nameElement = subtopicItem.querySelector('.subtopic-name');
        const descriptionElement = subtopicItem.querySelector('.subtopic-description');

        // Function to add or remove 'text-success' class based on status
        function toggleClass(element, add) {
            if (add) {
                element.classList.add('text-success');
            } else {
                element.classList.remove('text-success');
            }
        }

        // Apply the color change based on the checkbox status
        toggleClass(codeElement, isChecked);
        toggleClass(nameElement, isChecked);
        toggleClass(descriptionElement, isChecked);
    });
});

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
        // Target elements within the list item
        const subtopicItem = document.querySelector(`#subtopic-${subtopicId}`);
        const codeElement = subtopicItem.querySelector('.subtopic-code');
        const nameElement = subtopicItem.querySelector('.subtopic-name');
        const descriptionElement = subtopicItem.querySelector('.subtopic-description');

        // Function to add or remove 'text-success' class based on status
        function toggleClass(element, add) {
            if (add) {
                element.classList.add('text-success');
            } else {
                element.classList.remove('text-success');
            }
        }

        // Apply the color change based on the checkbox status
        const shouldAddClass = data.status; // This assumes `data.status` is a boolean reflecting the checkbox state
        toggleClass(codeElement, shouldAddClass);
        toggleClass(nameElement, shouldAddClass);
        toggleClass(descriptionElement, shouldAddClass);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
