# 🗜️ Online File Zipping Application

A simple web application built with **Python** and **Flask** that allows users to upload a file, compress it, and download the zipped file. Perfect for DevOps engineers and developers looking to build a hands-on project for learning or portfolio purposes! 🚀

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Deployment](#deployment)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features
- **File Upload** 📁: Users can upload files for compression.
- **Automatic Zipping** 📦: Files are instantly zipped upon upload.
- **Download Link** 🔗: Users can download the zipped file.
- **Containerization Ready** 🐳: Easily deploy with Docker.
- **Cloud Ready** ☁️: Ideal for deployment on AWS, GCP, or Azure.

---

## ✅ Prerequisites
- **Python 3.7+** installed
- **Flask** and other dependencies (detailed below)
- (Optional) **Docker** for containerized deployment

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/online-file-zipper.git
   cd online-file-zipper
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Access the app**:
   - Open a web browser and navigate to `http://127.0.0.1:5000`

3. **Using the app**:
   - Upload a file through the form on the homepage.
   - After upload, the app will zip the file and provide a download link.

---

## 📁 Folder Structure

```plaintext
online-file-zipper/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── uploads/             # Folder to store uploaded files
├── zipped_files/        # Folder to store zipped files
└── templates/
    └── index.html       # HTML file for the homepage
```

---

## 🐳 Deployment with Docker

To run this application in a Docker container:

1. **Create a Dockerfile**:
   ```dockerfile
   # Use the official Python image
   FROM python:3.8-slim

   # Set the working directory
   WORKDIR /app

   # Copy the code into the container
   COPY . .

   # Install dependencies
   RUN pip install -r requirements.txt

   # Expose port 5000
   EXPOSE 5000

   # Run the application
   CMD ["python", "app.py"]
   ```

2. **Build and Run the Docker Container**:
   ```bash
   docker build -t online-file-zipper .
   docker run -p 5000:5000 online-file-zipper
   ```

---

## ☁️ Deployment on Cloud (AWS EC2)

1. Launch an **EC2 instance** with Python installed.
2. SSH into the instance and clone the repository.
3. Install dependencies and start the Flask app.
4. Configure security groups to allow inbound traffic on port 5000.

---

## 💻 Tech Stack
- **Flask**: Web framework for Python
- **Python**: Backend language
- **HTML/CSS**: Simple frontend design
- **Docker**: Containerization (optional for deployment)
- **AWS/GCP/Azure**: Cloud platforms for deployment (optional)

---

## 🤝 Contributing
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/feature-name`
3. **Commit changes**: `git commit -m 'Add feature'`
4. **Push to branch**: `git push origin feature/feature-name`
5. **Open a pull request**

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
