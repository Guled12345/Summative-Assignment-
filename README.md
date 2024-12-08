# Education Access Web Application
Enhancing Access to Education in Somalia with Predictive Tools

The Education Access Web Application is an innovative platform aimed at improving education accessibility in Somalia. It offers users the ability to generate predictions, retrain machine learning models with updated data, and gain insights through data visualization.

# 🔗 Project Links
Live Application: https://educationaccess5.streamlit.app/ 
Backend API: View the API
The backend API runs via the main.py file located in the src folder. This file includes key functions and scripts for processing and predictions.
Demo Walkthrough: Video Demonstration
Sample Data:
For testing: Test Dataset
Original training dataset: Training Dataset
Docker Deployment: Docker image available under education-access-app. Pull it using:
bash
Copy code
docker pull username/education-access-app
Load Testing Results: See performance metrics and response times under various conditions: Test Results.
 # About the Project
The Education Access Web Application uses machine learning to analyze and address educational challenges in Somalia. It offers tools to predict dropout risks and other trends that affect accessibility, enabling better decision-making.

Core Features
Prediction: Upload individual data points or bulk datasets for predictions.
Model Retraining: Retrain machine learning models using new datasets directly from the platform.
Visualization: Explore insights with interactive charts that highlight patterns and trends in education data.
# Getting Started
Prerequisites
To set up the project, ensure the following are installed:

Python (version 3.9 or higher)
Streamlit (for building the user interface)
Docker (for containerizing the application)
Locust (for testing application performance under load)
1. Clone the Project
Download the project repository:

bash
Copy code
git clone https://github.com/your-username/education-access-app.git
cd education-access-app
2. Install Required Libraries
Install all dependencies using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
3. Run the Web Application
Start the application with Streamlit:

bash
Copy code
streamlit run app.py
4. Launch the Backend API
Navigate to the src folder and start the backend API:

bash
Copy code
python main.py
5. Deploy Using Docker
Build the Docker image and run the container:

bash
Copy code
docker build -t education-access-app .
docker run -p 8501:8501 education-access-app
6. Conduct Performance Tests
Use Locust to simulate concurrent user requests and evaluate performance:

bash
Copy code
locust -f locustfile.py

📁 Project Structure
arduino
Copy code
education-access-app/
│
├── README.md  
│
├── data/  
│   ├── train/  
│   └── test/  
│
├── models/  
│   ├── model.pkl  
│   └── model.tf  
│
├── src/  
│   ├── preprocessing.py  
│   ├── model.py  
│   └── prediction.py  
│
├── app.py  
├── home.py  
├── prediction.py  
├── retrain_model.py  
└── requirements.txt  
# Highlights and Results
Load Testing: Performance results under various user loads, showing system robustness, are documented here.
Model Evaluation: Detailed metrics and insights are included in the Notebook.
