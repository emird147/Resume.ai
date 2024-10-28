document.addEventListener('DOMContentLoaded', () => {
    const resumeForm = document.getElementById('resumeForm');
    const resumePreview = document.getElementById('resumePreview');
    const previewContent = document.getElementById('previewContent');
    const downloadBtn = document.getElementById('downloadBtn');

    // Helper function to display an error
    const showError = (input, message) => {
        input.classList.add('is-invalid');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        errorDiv.innerText = message;
        input.parentElement.appendChild(errorDiv);
    };

    // Helper function to clear any previous errors
    const clearError = (input) => {
        input.classList.remove('is-invalid');
        const error = input.parentElement.querySelector('.invalid-feedback');
        if (error) error.remove();
    };

    // Helper function to validate email
    const isValidEmail = (email) => {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    };

    // Helper function to validate URL
    const isValidURL = (url) => {
        const regex = /^(https?:\/\/)?([\da-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/?$/;
        return regex.test(url);
    };

    // Form validation function
    const validateForm = () => {
        let isValid = true;

        // Loop through all form elements
        Array.from(resumeForm.elements).forEach((input) => {
            if (input.type !== 'submit') {
                clearError(input); // Clear previous errors

                // Check if field is required and empty
                if (input.hasAttribute('Required') && !input.value.trim()) {
                    showError(input, `Required`);
                    isValid = false;
                }

                // Validate specific field types
                if (input.type === 'email' && input.value && !isValidEmail(input.value)) {
                    showError(input, 'Please enter a valid email address.');
                    isValid = false;
                }

                if ((input.type === 'url' || input.name.includes('URL')) && input.value && !isValidURL(input.value)) {
                    showError(input, 'Please Enter a Valid URL.');
                    isValid = false;
                }
            }
        });

        return isValid;
    };

    // Handle form submission
    resumeForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevent page reload

        if (validateForm()) {
            // Generate and display the resume preview
            const formData = new FormData(resumeForm);
            let previewText = '';

            for (let [key, value] of formData.entries()) {
                if (value.trim()) {
                    previewText += `${key.replace(/([A-Z])/g, ' $1')}: ${value}\n`;
                }
            }

            previewContent.innerText = previewText;
            resumePreview.style.display = 'block';
            downloadBtn.style.display = 'inline-block';
        }
    });

    // Handle download button click
    downloadBtn.addEventListener('click', () => {
        const blob = new Blob([previewContent.innerText], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'resume.txt';
        a.click();
        URL.revokeObjectURL(url);
    });
});


