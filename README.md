#AI-Powered Product recognition and Classification System using CNN and Computer Vision

#Project Overview:

1. GOALS: Project aims to automatise VERIFICATION and CLASSIFICATION of nictotine products throguh image analysis, classification, suggesting product labels and comparing it with Database data.

2. Technologies used:
   The project uses:

- AWS:
  - Sagemaker AI as an endpoint
  - S3 storage
  - EC2 server
- Apache airflow for orchestration
- CNN -> CLIP for image recognition and product classification
- OCR -> EasyOCR & PyTorch for text extraction
- Monitoring
- Bitbucket for CI/CD deployment and repository
- Data maching
- Data preprocessing
- Streamlit for UI
- Database: XXXX
- REST APi? (for now - wip) to connect the Database to S3

3. Architecture - Flow:

   - pictures are regulary sent to S3 storage
   - Airflow runs batch inference on SageMaker
   - CLIP classifies images, EasyOCR extracts names as a text
   - Results are being compared with data from a database
   - final reslts are being saved into the system
   - Streamlit allows for manual verification of the results

4. Installation:
   pip install -r requirements.txt
