import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


@st.cache_data
def app():

    st.header("MODEL VISUALIZATION")
    dataset=pd.read_csv("Crop_recommendation.csv")
 

    crop_dict = {
    'rice': 1,
    'maize': 2,
    'jute': 3,
    'cotton': 4,
    'coconut': 5,
    'papaya': 6,
    'orange': 7,
    'apple': 8,
    'muskmelon': 9,
    'watermelon': 10,
    'grapes': 11,
    'mango': 12,
    'banana': 13,
    'pomegranate': 14,
    'lentil': 15,
    'blackgram': 16,
    'mungbean': 17,
    'mothbeans': 18,
    'pigeonpeas': 19,
    'kidneybeans': 20,
    'chickpea': 21,
    'coffee': 22
    }
    dataset['crop_num']=dataset['label'].map(crop_dict)
    
    dataset=dataset.drop('label',axis=1)
    
    X=dataset.drop('crop_num',axis=1)
    Y=dataset['crop_num']
    
    st.subheader("Mapping names to numbers:")
    st.write(dataset.head())
    
    st.subheader("Statistic review")
    st.write(dataset.describe())

    st.subheader("Features:")
    st.write(X.head())      

    st.write("Target Variable:")
    st.write(Y.head())

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    # create instances of all models
    models = {
        'Logistic Regression': LogisticRegression(),
        'Naive Bayes': GaussianNB(),
        'Support Vector Machine': SVC(),
        'K-Nearest Neighbors': KNeighborsClassifier(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'Bagging': BaggingClassifier(),
        'AdaBoost': AdaBoostClassifier(),
        'Gradient Boosting': GradientBoostingClassifier(),
        'Extra Trees': ExtraTreeClassifier(),
    }

    # Function to train and evaluate models
    def train_and_evaluate_models(X_train, Y_train, X_test, Y_test):
        results = {}
        for name, md in models.items():
            md.fit(X_train, Y_train)
            ypred = md.predict(X_test)
            accuracy = accuracy_score(Y_test, ypred)
            precision = precision_score(Y_test, ypred, average='weighted')
            recall = recall_score(Y_test, ypred, average='weighted')
            f1 = f1_score(Y_test, ypred, average='weighted')
            results[name] = {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'F1-score': f1}
        return results

    # Training and evaluation
    evaluation_results = train_and_evaluate_models(X_train, Y_train, X_test, Y_test)

    # Convert evaluation results to DataFrame
    df_results = pd.DataFrame(evaluation_results).T

    # Displaying evaluation metrics as a table
    st.title("Model Evaluation")
    st.subheader("Evaluation Metrics:")
    st.table(df_results)

    # Assuming df_results is your DataFrame containing evaluation metrics
# Convert the DataFrame to a format suitable for plotting
    df_results_plot = df_results.reset_index().rename(columns={'index': 'Model'})

    # Bar chart for Accuracy
    st.subheader("Accuracy")
    fig_acc = go.Figure()
    fig_acc.add_trace(go.Bar(x=df_results_plot['Model'], y=df_results_plot['Accuracy'], marker_color='skyblue'))
    fig_acc.update_layout(title='Accuracy of Different Models', xaxis_title='Model', yaxis_title='Accuracy')
    st.plotly_chart(fig_acc)

    # Bar chart for Precision
    st.subheader("Precision")
    fig_prec = go.Figure()
    fig_prec.add_trace(go.Bar(x=df_results_plot['Model'], y=df_results_plot['Precision'], marker_color='salmon'))
    fig_prec.update_layout(title='Precision of Different Models', xaxis_title='Model', yaxis_title='Precision')
    st.plotly_chart(fig_prec)

    # Bar chart for Recall
    st.subheader("Recall")
    fig_recall = go.Figure()
    fig_recall.add_trace(go.Bar(x=df_results_plot['Model'], y=df_results_plot['Recall'], marker_color='lightgreen'))
    fig_recall.update_layout(title='Recall of Different Models', xaxis_title='Model', yaxis_title='Recall')
    st.plotly_chart(fig_recall)

    # Bar chart for F1-score
    st.subheader("F1-score")
    fig_f1 = go.Figure()
    fig_f1.add_trace(go.Bar(x=df_results_plot['Model'], y=df_results_plot['F1-score'], marker_color='plum'))
    fig_f1.update_layout(title='F1-score of Different Models', xaxis_title='Model', yaxis_title='F1-score')
    st.plotly_chart(fig_f1)
