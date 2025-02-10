# Sample Agent for Data Transformation

## 📌 Overview
This repository provides a reference implementation for detection and/or classification tasks involving large-scale raw data transformation. The process assumes stream-based inference, handling real-time data.

### Workflow Overview

#### 1. Understanding the Data
- After collecting a sufficiently large raw dataset, we begin with Exploratory Data Analysis (EDA) and consult domain experts to gain deeper insights into the data.
- At the same time, we label a dataset, which is essential for training ML classifiers and fine-tuning AI models using a supervised learning approach. (In this sample code, the ML classifier, `anomaly_classifier`, follows an unsupervised learning approach, so the labels are used only for AI model fine-tuning.)
- Based on these insights, we define a practical approach that balances performance and cost to meet project requirements.

#### 2. Preprocessing & Data Preparation
- Once we have gathered a sufficiently large dataset, we preprocess the raw data to:
  - Prepare input data for ML/AI models.
  - Extract relevant features and calculate statistics during inference for real-time data transformation.
- For details on this process, please refer to `data_processor.ipynb`.

#### 3. Model Training & Fine-Tuning
- After preprocessing the data using `data_processor.ipynb`, we proceed with:
  - ML Model Training (e.g., anomaly detection) → `anomaly_classifier.ipynb`
  - AI Model Fine-Tuning (e.g., threat detection) → `tune_ai_model.ipynb`
- These trained models will later be used for real-time feature enrichment and detection in the data transformation process.

#### 4. Feature Enrichment for Detection
- The trained ML/AI models are applied in `cybersecurity_data_transformation.ipynb` to generate enriched feature sets, improving the detection pipeline.
- In the `cybersecurity_data_transformation` process, we apply a series of filters to bypass irrelevant raw input data, significantly reducing computational costs. However, we must perform EDA on this filtered output again to ensure that, for example, precision remains high enough to meet project requirements.
- The enriched data is then stored in a database for further analysis and related applications.
- For details on this process, please refer to `cybersecurity_data_transformation.ipynb`.

#### 5. Real-Time Detection
- The enriched dataset can be used for advanced detection tasks in `cybersecurity_detector.ipynb`.
- In this example, `cybersecurity_detector.ipynb` applies a simple prompting approach to a GenAI model for detection, demonstrating how the entire pipeline functions. (Currently, this process is identical to the threat detection feature extraction in `cybersecurity_data_transformation.ipynb`.)

This structured workflow ensures an efficient and scalable approach to (near) real-time data transformation and detection using large-scale data.

---

## 🚀 Features
Combining traditional machine learning (ML) techniques with modern Large Language Models (LLMs) enhances the detection and analysis of security threats in log data and other types of data such as:
- Network session data, connection information, traffic flow data
- Process execution metadata, registry access data, file data
- Malware signatures, exploits, attacker infrastructure (domains and IP addresses)
- Geographic locations of threat actors or incidents
- Unusual patterns in network traffic or system behavior, and more

### 1. Hybrid Approach:
- **Traditional ML Techniques:**
  - Methods like Isolation Forests, clustering algorithms, and statistical analysis identify patterns and outliers in structured data.
- **Large Language Models:**
  - Advanced LLMs (e.g., GPT-3.5 Turbo, GPT-4, or their fine-tuned versions) excel at parsing and interpreting complex log entries, generating contextual insights and responses.

### 2. Data Processing:
- **Stream-based Approach:**
  - Data is read in and processed sequentially. Our proprietary algorithm efficiently prepares aggregation features in real-time.
- **Filtering Non-Threat Data:**
  - Non-relevant data is filtered out at the beginning to reduce costs.
- **Data Augmentation:**
  - Augmentation is provided as needed for better predictive performance.

By integrating these approaches, this sample agent enhances threat detection accuracy through a combination of numerical and contextual analysis.

**Note:**
Detailed descriptions are available in the corresponding `.ipynb` files.

---

## 📦 Installation
```sh
# Clone the repository
git clone https://github.com/henrychangus/threat_dect.git
cd your-repo

# Install dependencies (if applicable)
pip install -r requirements.txt
```

---

## 🚀 Usage
Example commands to run the project:
```sh
# 1. Preprocess raw data
python -m nbconvert --to notebook --execute data_processor.ipynb

# 2. Train a ML-based classifier
python -m nbconvert --to notebook --execute anomaly_classifier.ipynb

# 3. Fine-tune an AI model
python -m nbconvert --to notebook --execute tune_ai_model.ipynb

# 4. Execute the Agent for Data Transformation
python -m nbconvert --to notebook --execute cybersecurity_data_transformation.ipynb

# 5. Detect threats using the transformed data
python -m nbconvert --to notebook --execute cybersecurity_detector.ipynb
```

### Note:
1. **Input:** Data for `data_processor.ipynb`, `anomaly_classifier.ipynb`, and `tune_ai_model.ipynb`.
2. **Output:** Data generated by `data_processor.ipynb`, `anomaly_classifier.ipynb`, `tune_ai_model.ipynb`, `cybersecurity_data_transformation.ipynb`, and `cybersecurity_detector.ipynb`.
3. **utility.py:** Contains common functions used across the project.
4. **config.json:**
   - A simple configuration file for parameters used in the `.py` and `.ipynb` files.
   - **ToDo:** Implement a sophisticated hierarchical structure for defining key-value pairs for parameters.

---

## ⚙️ Configuration
**ToDo:** Explain any necessary environment variables or configurations.

---

## 📖 Documentation
**ToDo:** Provide links or instructions for further documentation.

---

## 🛠️ Contributing
1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 📞 Contact
For questions or issues, please open an issue or contact `henry.chang.us@gmail.com`.
