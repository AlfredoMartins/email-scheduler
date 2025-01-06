
# Email Scheduler

This project automates the process of sending scheduled emails using a Python script. The email content and attachments are sent from a Gmail account to a specified receiver every day at scheduled times. The script checks if the current day is a weekday and runs the scheduled email jobs accordingly.

## Features

- Sends automated emails at 08:30, 13:45, and 19:00 every weekday.
- Reads email content from a CSV file and attaches images.
- Sends the email to a receiver and BCC to another email address.
- Uses environment variables to securely handle Gmail credentials.

## Prerequisites

Before running the application, make sure the following are installed:

- Python 3.x
- Docker (if running in a containerized environment)

### Python Libraries

- `schedule`: To manage the scheduling of the emails.
- `smtplib`: To send emails.
- `email.message`: To construct email messages.
- `dotenv`: To load environment variables from a `.env` file.
- `os`: To access environment variables and handle file paths.
- `csv`: To read email content from a CSV file.
- `random`: For generating random numbers used in email subjects.
- `datetime`: To handle date and time operations.

Use the `requirements.txt` to install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file at the root of the project to store your Gmail credentials and other sensitive information:

```
GMAIL_USERNAME=your_email@gmail.com
GMAIL_PASSWORD=your_password
```

Ensure the CSV file `content.csv` exists in the project directory and contains the content to be included in the email body.

The images `passport.png` and `visa.png` should also be placed in the `./files/` directory for attachment.

## How It Works

### Main Script (`app.py`)

1. **Imports necessary libraries**: `send_email`, `schedule`, `time`, and `datetime`.
2. **Job function**: Calls `send_email()` function to send the email.
3. **Scheduler Setup**: The `run_scheduler()` function schedules the job to run three times daily at 08:30, 13:45, and 19:00. It ensures that the script only runs on weekdays (Monday to Friday).
4. **Main function**: Checks if today is a weekend (Saturday or Sunday) and exits the script if it is. Otherwise, it starts the scheduler.

### Email Sending Logic (`send.py`)

1. **Reset Function**: The `reset()` function creates an email message with a randomly generated subject and reads email content from `content.csv`. It also attaches `passport.png` and `visa.png` from the `./files/` directory.
2. **Send Email**: The `send_email()` function logs into Gmail via SMTP, sends the email message, and prints "Sent..." when successful.

### Docker Setup

If you want to run the application in a Docker container, use the following commands:

1. Build the Docker image:

   ```bash
   docker build --no-cache -t email-scheduler .
   ```

2. Run the container with the following command:

   ```bash
   docker run -d --restart always email-scheduler
   ```

### Dockerfile

The `Dockerfile` defines the steps to build the Docker image for this project:

```dockerfile
FROM python:3.11-bullseye

RUN apt-get update     && apt-get install -y --no-install-recommends --no-install-suggests     build-essential     && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

CMD [ "python3", "./app.py"]
```

## Running the Application

### Using Python

1. Set up your environment variables in `.env`.
2. Ensure the CSV file and image files are in place.
3. Run the application:

   ```bash
   python3 app.py
   ```

### Using Docker

1. Build and run the Docker container as described above.

The scheduler will start running and will send emails at the defined times during weekdays.

## Troubleshooting

- **Email not sent**: Make sure the Gmail username and password are correct in the `.env` file. If you're using 2FA for Gmail, you may need to create an app-specific password.
- **Missing Files**: Ensure that `content.csv` and the image files (`passport.png`, `visa.png`) are present in the correct directories (`./files/` for images).
- **Scheduling issues**: Check if your system time is synchronized properly. You can also log the times the script runs for debugging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.