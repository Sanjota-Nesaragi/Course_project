FROM python:3.13.3
WORKDIR /Course_Project
# Copy project files
COPY . .
# Install dependencies
RUN pip install --no-cache-dir pytest
# Optional: default command
CMD ["python", "student.py"]
