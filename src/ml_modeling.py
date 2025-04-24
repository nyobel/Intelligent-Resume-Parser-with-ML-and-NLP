import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics.pairwise import cosine_similarity

# Load the cleaned aggregated data
agg_df = pd.read_csv("src/clean_resume_data.csv")

# Encode skills with MultiLabelBinarizer
mlb = MultiLabelBinarizer()
skill_matrix = mlb.fit_transform(agg_df['skill_name'].apply(eval))  # eval to convert string to list
skill_df = pd.DataFrame(skill_matrix, columns=mlb.classes_)

# Merge with main dataset
data_encoded = pd.concat([agg_df.drop(columns=['skill_name']), skill_df], axis=1)

# Export encoded data to CSV
data_encoded.to_csv("encoded_resume_data.csv", index=False)

# Preview encoded data
print(data_encoded.head())

# ----------------------------
# Supervised ML: Predict current_title
# ----------------------------

# Prepare features and target
X = skill_df
y = data_encoded['current_title']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("\n Classification Report:")
print(classification_report(y_test, y_pred))

# ----------------------------
# Similarity Matching by Skill Profile
# ----------------------------

# Use cosine similarity to find similar candidates to index 0
base_candidate_idx = 0
base_vector = skill_df.iloc[[base_candidate_idx]]

# Compute cosine similarity
similarities = cosine_similarity(base_vector, skill_df)[0]
data_encoded["similarity"] = similarities

# Show top matches
matches = data_encoded.drop(index=base_candidate_idx).sort_values("similarity", ascending=False)
print("\n🔍 Top Similar Candidates:")
print(matches[["full_name", "current_title", "similarity"]].head(5))
