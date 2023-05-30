FROM python:3.11

# First try to install dependencies only
COPY requirements.txt .

# Install all dependencies
# TODO: Install only production dependencies
RUN pip install -r requirements.txt

# Copy evething that was not excluded in .dockerignore
COPY . .

EXPOSE 8000
ENTRYPOINT ["docker-files/entrypoint.sh"]
CMD ["python3", "src/cli.py"]