document.getElementById('resumeForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent page reload

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const skills = document.getElementById('skills').value;
    const experience = document.getElementById('experience').value;
    const education = document.getElementById('education').value;

    const resumeContent = `
    ${name}
    Email: ${email} | Phone: ${phone}

    Experience:
    ${experience}

    Education:
    ${education}

    Skills:
    ${skills}
    `;

    const previewContent = document.getElementById('previewContent');
    previewContent.textContent = resumeContent;
    document.getElementById('resumePreview').style.display = 'block';
    document.getElementById('downloadBtn').style.display = 'inline';

    document.getElementById('downloadBtn').addEventListener('click', function () {
        const blob = new Blob([resumeContent], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${name}_resume.txt`;
        a.click();
    });
});
