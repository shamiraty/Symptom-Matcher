## Symptom-Matcher AI - Intelligent Patient Similarity & Treatment Suggestion

<img src="https://github.com/user-attachments/assets/90e6bb44-455c-4079-9a4d-59feadce6fdb" alt="logo7" width="100" height="100" />

- **Location**: Dodoma, Tanzania
- **Email**: [sashashamsia@gmail.com](mailto:sashashamsia@gmail.com)
- **WhatsApp**: [+255675839840](https://wa.me/255675839840)
- **Demo**: [Online](https://clinicaltreatment.pythonanywhere.com/)
  <!--- **Youtube**: [Videos](https://www.youtube.com/channel/UCjepDdFYKzVHFiOhsiVVffQ)-->

| Icon | Rank | Professional Target Audience                                |
|------|------|------------------------------------------------------------|
| 🔬  | 1    | Healthcare Researchers (Epidemiologists, Clinical Researchers) |
| 🩺  | 2    | Physicians (General Practitioners and Specialists)            |
| 🏛️  | 3    | Public Health Officials (Health Department Personnel, Policy Makers) |
| 🏢  | 4    | Hospital Administrators                                      |
| 👩‍⚕️ | 5    | Nurses                                                     |
| 📊  | 6    | Data Analysts in Healthcare                                   |
| 👨‍💼 | 7    | Medical Directors                                          |
| 💊  | 8    | Pharmacists                                                 |
| 🏥  | 9    | Clinic Administrators                                        |
| 🎓  | 10   | Medical Educators (Professors of medicine)                   |

## Disclaimer

> The patient records used to train and test the **Symptom-Matcher AI** model are **not real patient data**. They are **fictitious data** that have been generated for educational purposes only. These records have no connection to any actual individuals or real-life medical conditions. 

> The diseases and symptoms displayed in the application are **for learning and demonstration purposes**. They do not represent actual medical diagnoses and should not be interpreted as such. The use of these simulated cases is intended solely for academic and training purposes.

> This application and its content are not intended to diminish or disrespect the real-world medical field, institutions, or individuals. The information presented is purely hypothetical and should not be used for making medical decisions. The primary goal of this project is to provide a platform for learning and development in the field of machine learning and healthcare technology.

## 1. INTRODUCTION

In healthcare, a **health record** refers to the documentation of a patient’s medical history, treatment details, symptoms, diagnoses, and doctor’s comments each time they visit a healthcare facility. This data is crucial for tracking the health progress of patients, providing personalized treatments, and preventing recurring issues.

Each time a patient visits a healthcare center, their symptoms, disease, treatment, and doctor’s comments are recorded. These records are maintained to offer a comprehensive history of the patient’s health, which can guide doctors in making informed decisions.

**Machine Learning (ML)** models in this system aim to optimize the process by identifying patterns in patient symptoms and doctor’s comments. The system helps match new patients to those with similar symptoms and treatments, offering both doctors and patients valuable insights. It is particularly beneficial for:

- **Doctors**: Helping them recall previous patient treatments and solutions that might be applicable for current patients with similar symptoms.
- **Healthcare Providers**: Facilitating quicker diagnosis by finding patterns across numerous patient records.
- **Patients**: Offering better treatment consistency and personalized recommendations based on prior cases.

The **Symptom-Matcher AI** system applies machine learning techniques to solve the challenge of grouping and matching patients with similar conditions and treatments.

---

## 2. PROBLEM

In healthcare, it is common for patients to present similar symptoms and diseases, especially for recurring conditions. However, managing such large datasets manually becomes challenging. Typically, when a new patient visits a healthcare center, their symptoms might resemble those of a patient who has been treated previously. The challenge arises in efficiently grouping these patients or recalling their doctor’s comments.

- **Issue 1**: Traditional systems like Excel are not capable of grouping patients with similar symptoms or diseases based on structured data alone.
- **Issue 2**: Even if doctor comments are recorded, it is difficult to assess whether they are related to similar symptoms or diseases by just reading them manually. The vast amounts of text data make it nearly impossible to analyze without using intelligent algorithms.

By using machine learning, this system provides a solution to:
- Automatically group patients with similar symptoms.
- Match doctor’s comments with similar treatments to ensure the best possible diagnosis for new patients.
  
The core problem is to **automatically categorize and group patients based on their symptoms and treatment history** using advanced machine learning models.

---

## 3. IMPORTANCE OF THIS APP

The **Symptom-Matcher AI** app plays a significant role in the healthcare industry by offering the following benefits:

1. **Enhanced Patient Diagnosis**: The system helps doctors identify patients with similar symptoms, allowing them to review previous treatments and doctor comments for faster and more accurate diagnoses.
  
2. **Improved Treatment Consistency**: By recommending similar treatments based on historical data, the system ensures that patients with similar conditions receive consistent and effective care.
  
3. **Efficient Healthcare Operations**: The AI model improves the overall workflow in healthcare centers by categorizing patients based on symptoms and doctor comments, eliminating the need for manual data entry and review.
  
4. **Data-Driven Insights**: Healthcare providers can analyze trends in diseases, symptoms, and treatments over time, improving the general understanding of common conditions.
  
5. **Cost and Time Saving**: By reducing the time spent manually reviewing patient records, healthcare providers can focus on delivering better patient care, improving the overall efficiency of the healthcare system.

6. **Accurate Predictive Models**: The ML model can identify patterns and trends from large datasets, leading to more reliable predictive analytics for future patient visits.

---

## 4. MAIN PURPOSE

The primary purpose of **Symptom-Matcher AI** is to streamline the process of diagnosing patients and providing treatment suggestions based on historical data. Specifically, the system aims to:

1. **Match Patients with Similar Symptoms**: When a new patient arrives, the system will use their symptoms and medical history to find similar patients from the past and recommend the most suitable treatment based on previous doctor comments and diagnoses.
  
2. **Categorize Doctor’s Comments**: The system categorizes doctor’s comments to group patients with the same or similar conditions, enabling doctors to recall prior cases and treatments effectively.
  
3. **Offer Treatment Recommendations**: By analyzing past treatments and diseases, the system provides insights into which treatments might be effective for a new patient with similar conditions.
  
Ultimately, the goal is to use machine learning to **enhance the decision-making process for healthcare providers**, improve patient outcomes, and save time and resources in the healthcare system.

---

## 5. METHODOLOGY

The **Symptom-Matcher AI** system leverages various machine learning (ML) techniques to recommend similar patients and categorize them based on their conditions and doctor comments. Below is a breakdown of the methodology used in the development of this system.

### Technologies Used:

- **Flask**: A lightweight Python web framework used to build the web application.
- **Pandas**: A powerful library for data manipulation and analysis, used to load and handle patient data.
- **NumPy**: A core library for numerical computations, used in various mathematical operations.
- **Scikit-learn**: A machine learning library, used for text vectorization and similarity computation.
- **Gensim**: A library for topic modeling, used here for categorizing patients based on doctor comments.

### Key Components:

1. **Data Preparation**:
   - Patient data is loaded from a **CSV file** (or MySQL database in production) containing information on diseases, symptoms, and doctor comments.
   - The patient data is then processed to extract relevant information for model input.

2. **Patient Recommendation**:
   - **Text Vectorization**: Using **TF-IDF (Term Frequency-Inverse Document Frequency)**, the disease and symptom fields are converted into a numerical matrix. This matrix represents the importance of terms in the text.
   - **Cosine Similarity**: The similarity between the selected patient and all other patients is calculated using the **cosine similarity** metric. This helps identify patients with similar conditions.
   - **Top-N Recommendation**: The function `recommend_patients()` returns the top N patients (7 by default) with the highest similarity to the selected patient.

3. **Patient Categorization**:
   - **Text Preprocessing**: Doctor comments are split into individual words and converted into a **bag-of-words** representation.
   - **LDA (Latent Dirichlet Allocation)**: This technique is used to categorize patients based on the topics in their doctor comments. The LDA model identifies **10 topics**, assigning each patient to the most relevant category.
   - **Topic Assignment**: After running the LDA model, each patient is assigned a category based on the dominant topic in their doctor comment. This category is then added to the patient data.

4. **Web Application**:
   - **Flask Routes**:
     - The **`/` route** renders the main page, displaying patient data and their corresponding categories.
     - The **`/recommend/<int:patient_id>` route** returns a JSON response with recommended patients based on similarity, as well as patients in the same category as the selected patient.

5. **User Interface**:
   - **Flask Framework**: The backend is built using Flask, a Python web framework that allows easy integration of machine learning models with the frontend.
   - **Frontend (HTML/CSS/JavaScript)**: The user interface is designed using modern frontend technologies like HTML, CSS, and JavaScript to present patient records, doctor comments, and recommendations in a user-friendly manner.
   - **AJAX**: Used for fetching and updating patient data dynamically without reloading the page, making the user experience smooth.


### Code Flow:

1. **Recommendation Process**:
   - The `recommend_patients()` function calculates similarities between the selected patient's symptoms and diseases and the rest of the patients.
   - The results are sorted and the top N similar patients are returned.

2. **Categorization Process**:
   - The `categorize_patients()` function processes doctor comments, splits them into words, and uses **LDA** to categorize the patients.
   - Each patient is assigned to a topic, represented by a category number.

3. **Web Display**:
   - The data is displayed on the web page using **Flask templates** (`index.html`), showing patients along with their recommended matches and assigned categories.

### Advantages of the Methodology:
- **Scalability**: The system can be easily scaled to handle larger datasets (e.g., through integration with MySQL).
- **Dynamic Categorization**: Patients can be dynamically categorized based on their doctor comments, making the system adaptive to new cases.
- **Efficient Recommendation**: The use of **TF-IDF** and **cosine similarity** ensures that the recommendations are based on meaningful textual analysis of symptoms and diseases, making them accurate and relevant.

### Potential Improvements:
- Integrating additional patient features (e.g., age, gender) for a more comprehensive recommendation system.
- Implementing more advanced models like **BERT** or **transformers** for a deeper understanding of patient text data.

---


## 6. PATIENT RECORDS INTERPRETATION

The following tables represent the **patient records**, **recommended patients**, and **patient categorization** as part of the **Symptom-Matcher AI** system. These interpretations help in understanding how patient data is organized and matched based on symptoms and treatments.

---

## 1. Patient Records

| ID  | Age | Disease      | Symptoms                     | Doctor Comment                       | Actions |
| --- | --- | ------------ | ---------------------------- | ------------------------------------ | ------- |
| 1   | 45  | Diabetes     | Fatigue, thirst               | Monitor blood sugar regularly        |         |
| 2   | 50  | Hypertension | Headache, dizziness           | Reduce salt intake                   |         |
| 3   | 46  | Diabetes     | Blurred vision, thirst        | Increase water intake                |         |
| 4   | 30  | Asthma       | Shortness of breath           | Use inhaler regularly                |         |
| 5   | 48  | Diabetes     | Fatigue, slow healing wounds  | Exercise regularly                   |         |
| 6   | 60  | Hypertension | Chest pain, dizziness         | Avoid stress and monitor blood pressure |       |
| 7   | 35  | Asthma       | Wheezing, coughing            | Avoid triggers, use inhaler as needed |         |
| 8   | 55  | Diabetes     | Frequent urination, fatigue  | Check blood sugar levels regularly   |         |
| 9   | 40  | Hypertension | Headache, blurred vision      | Take prescribed medication and reduce salt intake |   |
| 10  | 62  | Heart Disease| Chest pain, shortness of breath | Avoid physical strain, follow medication plan |  |

Showing **1 to 10 of 100 entries**  
[Previous] [1] [2] [3] [4] [5] … [10] [Next]

---

## 2. Recommended Patients

These are patients with similar symptoms to a selected patient, aiding in identifying the most relevant cases based on shared conditions and treatment strategies:

| ID  | Disease     | Symptoms                        |
| --- | ----------- | ------------------------------- |
| 42  | Diabetes    | Increased thirst, slow healing wounds |
| 1   | Diabetes    | Fatigue, thirst                  |
| 38  | Diabetes    | Thirst, fatigue                  |
| 46  | Diabetes    | Thirst, fatigue                  |
| 26  | Diabetes    | Blurred vision, fatigue          |
| 30  | Diabetes    | Fatigue, blurred vision          |
| 52  | Diabetes    | Fatigue, blurred vision          |

---

## 3. Patients in Same Category

This section groups patients who fall under the same treatment or symptom category. By categorizing patients based on their doctor comments and treatment plans, the system enables more accurate treatment suggestions:

| Category | ID  | Doctor Comment                                 |
| -------- | --- | ---------------------------------------------- |
| Category 5 | 5   | Exercise regularly                             |
| Category 5 | 15  | Avoid cold air and use inhaler regularly       |
| Category 5 | 16  | Maintain healthy diet and exercise routine     |
| Category 5 | 37  | Follow a heart-healthy diet and exercise plan  |
| Category 5 | 55  | Follow a low-sodium diet and take medication   |
| Category 5 | 59  | Follow a healthy diet and exercise regularly   |
| Category 5 | 65  | Maintain a healthy diet and exercise regularly |
| Category 5 | 67  | Avoid cold air and use inhaler regularly       |
| Category 5 | 80  | Follow a healthy heart plan and monitor symptoms |
| Category 5 | 88  | Follow a heart-healthy diet and exercise regularly |
| Category 5 | 92  | Follow a healthy heart care plan               |
| Category 5 | 94  | Exercise and monitor blood pressure regularly  |
| Category 5 | 99  | Follow a heart-healthy diet and exercise regularly |

---

## 4. Patient Categorization

This table shows the categorization of patient records based on the **doctor’s comment** and the corresponding **category**. The category number indicates the type of treatment or recommendation given to the patient, providing a structured approach to patient management:

| ID  | Doctor Comment                              | Category |
| --- | ------------------------------------------- | -------- |
| 1   | Monitor blood sugar regularly               | Category 1 |
| 2   | Reduce salt intake                          | Category 9 |
| 3   | Increase water intake                       | Category 9 |
| 4   | Use inhaler regularly                       | Category 8 |
| 5   | Exercise regularly                          | Category 5 |
| 6   | Avoid stress and monitor blood pressure     | Category 2 |
| 7   | Avoid triggers, use inhaler as needed       | Category 6 |
| 8   | Check blood sugar levels regularly          | Category 8 |
| 9   | Take prescribed medication and reduce salt intake | Category 9 |
| 10  | Avoid physical strain, follow medication plan | Category 7 |




## 7. CONCLUSION

The **Symptom-Matcher AI** system leverages cutting-edge machine learning algorithms to solve real-world healthcare problems related to patient similarity and treatment suggestions. By intelligently grouping patients based on symptoms and doctor’s comments, this system not only improves diagnostic accuracy but also enhances healthcare operations and patient care.

With the growing importance of data-driven decision-making in healthcare, the **Symptom-Matcher AI** application represents a valuable tool for doctors and healthcare providers in delivering better, more consistent care to patients.
