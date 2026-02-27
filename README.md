# CodeAlpha Task 3: Jenkins Remoting & Distributed Infrastructure

## 🚀 Project Overview
This project demonstrates a professional CI/CD setup using **Jenkins Remoting**. I have configured a distributed system where a local Jenkins Controller manages builds on a remote Azure Cloud Agent.

## 🏗️ Architecture
- **Controller (The Brain):** Jenkins running in Docker on a Windows 11 host (`localhost:8080`).
- **Agent (The Muscle):** Ubuntu 24.04 LTS Virtual Machine hosted on Microsoft Azure.
- **Connection:** Secure SSH-based Jenkins Remoting.

## 🔐 Security Features
- **Node Isolation:** The "Built-In" node on the laptop has **0 executors**, ensuring no code runs on the controller.
- **Distributed Load:** All Python Flask builds and tests are offloaded to the remote Azure environment.
- **Credential Management:** Used SSH Private Keys for secure agent-to-controller communication.

## 🛠️ Tech Stack
- **CI/CD:** Jenkins (Pipeline as Code)
- **Cloud:** Microsoft Azure (VM)
- **App:** Python Flask with Unit Testing
- **Environment:** Docker, Linux (Ubuntu), PowerShell

## 🚦 How to Run
1. Ensure the Azure Agent is online in Jenkins Nodes.
2. Run the Pipeline: `CodeAlpha_Flask-Remote-Build`.
3. Access the live app at: `http://52.141.17.215:5000`
