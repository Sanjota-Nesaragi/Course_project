FROM python:3.13.3
WORKDIR /app
# Copy project files
COPY . .
# Install dependencies
RUN pip install --no-cache-dir pytest
# Optional: default command
CMD ["python", "student.py"]